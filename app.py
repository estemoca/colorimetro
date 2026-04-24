from flask import Flask, render_template, Response, request, jsonify, send_from_directory
import cv2
import numpy as np
import base64

app = Flask(__name__)

camera = None

def get_camera():
    global camera
    if camera is None or not camera.isOpened():
        camera = cv2.VideoCapture(0)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    return camera

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename, cache_timeout=0)

# --- BASE DE DATOS DE COLORES (Tu tabla) ---
referencias_rgb = [
    (58, 95, 11),   # Grado 0
    (107, 142, 35),  # Grado 1
    (189, 183, 107), # Grado 2
    (255, 215, 0),   # Grado 3
    (255, 165, 0),   # Grado 4
    (204, 119, 34)   # Grado 5
]

def generate_frames():
    cap = get_camera()
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    image_data = data['image'].split(',')[1]
    decoded_image = base64.b64decode(image_data)
    np_arr = np.frombuffer(decoded_image, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Convertir a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplicar desenfoque gaussiano
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Umbral adaptativo
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Encontrar contornos
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cropped_image_base64 = None
    mean_color = (0, 0, 0)

    if contours:
        # Encontrar el contorno más grande
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Solo procesar si el contorno es suficientemente grande
        if cv2.contourArea(largest_contour) > 1000: # Umbral de área
            x, y, w, h = cv2.boundingRect(largest_contour)

            # Crear una máscara para el contorno más grande
            mask = np.zeros_like(gray)
            cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)

            # Aplicar la máscara a la imagen original
            masked_image = cv2.bitwise_and(image, image, mask=mask)
            
            # Recortar la imagen enmascarada para visualización
            cropped_for_display = masked_image[y:y+h, x:x+w]
            
            # Codificar la imagen recortada a base64
            _, buffer = cv2.imencode('.jpg', cropped_for_display)
            cropped_image_base64 = base64.b64encode(buffer).decode('utf-8')

            # Calcular el color promedio del área enmascarada
            mean_color = cv2.mean(image, mask=mask)[:3]
        else:
            # Si el contorno más grande es muy pequeño, usar el promedio de toda la imagen
            mean_color = cv2.mean(image)[:3]
    else:
        # Si no se encuentran contornos, usar el color promedio de toda la imagen
        mean_color = cv2.mean(image)[:3]


    # Convertir BGR a RGB
    r, g, b = int(mean_color[2]), int(mean_color[1]), int(mean_color[0])
    
    # --- Lógica de clasificación ---
    promedio_rgb = np.array([r, g, b])
    distancias = [np.linalg.norm(promedio_rgb - np.array(ref)) for ref in referencias_rgb]
    grado_base = np.argmin(distancias)
    
    # Interpolación para un grado más continuo
    r_norm = np.clip((promedio_rgb[0] - 58) / (255 - 58) * 4, 0, 5)
    grado_final = (grado_base + r_norm) / 2

    # Mapeo a nombres de madurez
    if grado_final < 0.5: madurez = "Grado 0: Verde"
    elif grado_final < 1.5: madurez = "Grado 1: Pintón"
    elif grado_final < 2.5: madurez = "Grado 2: Ligeramente Maduro"
    elif grado_final < 3.5: madurez = "Grado 3: Maduro"
    elif grado_final < 4.5: madurez = "Grado 4: Muy Maduro"
    else: madurez = "Grado 5: Sobre Maduro"

    # Estimación de Brix y Acidez
    brix = round(2.41 * grado_final + 7.15, 2)
    acidez = round(max(0.1, -0.65 * grado_final + 3.12), 2)

    # Devolver resultados, incluida la imagen recortada
    return jsonify({
        'r': r,
        'g': g,
        'b': b,
        'madurez': madurez,
        'brix': brix,
        'acidez': acidez,
        'cropped_image': cropped_image_base64
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
