# Colorímetro de Mango - Especificación del Software

## 📋 Información General

| Campo | Descripción |
|-------|-------------|
| **Nombre** | Colorímetro de Mango - Análisis de Maduración con IA |
| **Versión** | 1.1.0 |
| **Fecha de creación** | 2026-03-31 |
| **Última actualización** | 2026-03-31 |

---

## 🎯 Objetivo del Proyecto

Aplicación web Flask para detectar el grado de madurez de mangos mediante análisis de color usando:
- **TensorFlow.js + COCO-SSD** para detección de objetos por IA
- **OpenCV** para procesamiento de imagen en servidor
- **Análisis RGB** para determinar madurez (Grados 0-5)

---

## 🏗️ Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                      NAVEGADOR WEB                          │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │  index.html │  │  style.css  │  │      main.js        │ │
│  │  (Grid 2x2) │  │  (UI/Mód.)  │  │ (TensorFlow + IA)   │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
│         │                │                    │               │
│         └────────────────┴────────────────────┘               │
│                          │                                   │
│              ┌───────────┴───────────┐                      │
│              │   video_feed (MJPEG)  │                      │
│              └───────────┬───────────┘                      │
│                          │ HTTP POST                         │
└──────────────────────────┼───────────────────────────────────┘
                           │
┌──────────────────────────┼───────────────────────────────────┐
│                    SERVIDOR FLASK                            │
├──────────────────────────┼───────────────────────────────────┤
│              ┌───────────┴───────────┐                      │
│              │      app.py (Flask)    │                      │
│              │  ┌─────────────────┐  │                      │
│              │  │  / (index)      │  │                      │
│              │  │  /video_feed    │  │                      │
│              │  │  /analyze       │  │                      │
│              │  └─────────────────┘  │                      │
│              │           │            │                      │
│              │  ┌────────┴────────┐   │                      │
│              │  │  OpenCV (CV2)   │   │                      │
│              │  │  - Detección    │   │                      │
│              │  │  - Análisis RGB │   │                      │
│              │  │  - Clasificación│   │                      │
│              │  └─────────────────┘   │                      │
│              └────────────────────────┘                      │
└──────────────────────────────────────────────────────────────┘
```

---

## 📁 Estructura de Archivos

```
Colorimetro mango comun/
├── app.py                          # Servidor Flask (Backend)
├── ProgramaCamaraAvanzado.py       # Versión standalone de referencia
├── templates/
│   └── index.html                  # Interfaz principal (Grid 2x2)
├── static/
│   ├── main.js                     # Lógica frontend (IA + UI)
│   └── style.css                   # Estilos CSS
├── SPEC.md                         # Este archivo
└── .vscode/
    └── settings.json
```

---

## 🔧 Dependencias

### Python (Backend)
```
flask>=2.0
opencv-python>=4.5
numpy>=1.20
```

### JavaScript (Frontend - CDN)
```
- TensorFlow.js: https://cdn.jsdelivr.net/npm/@tensorflow/tfjs
- COCO-SSD: https://cdn.jsdelivr.net/npm/@tensorflow-models/coco-ssd
- Plotly.js: https://cdn.plot.ly/plotly-2.12.1.min.js
```

---

## 🎨 Interfaz de Usuario

### Layout Grid 2x2

```
┌─────────────────────┬─────────────────────┐
│   📷 CÁMARA EN VIVO │  🔍 MUESTRA         │
│                     │   DETECTADA         │
│   [Video stream]    │   [Canvas recorte]  │
│   [Overlay canvas]  │   Área: --          │
│                     │   Confianza: --     │
│   [Recuadro verde]  │                     │
├─────────────────────┼─────────────────────┤
│   📊 RESULTADOS     │  📈 FIRMA ESPECTRAL │
│                     │                     │
│   Estado: --        │   [Gráfica RGB]     │
│   Color RGB: --     │                     │
│   Brix: --          │                     │
│   Acidez: --        │                     │
└─────────────────────┴─────────────────────┘

[ 🔬 ANALIZAR FRUTA ]
[████████░░░░░░░░░░░░] 50%

Modo: IA lista        Detección: IA ✓
```

### Elementos UI

| Elemento | ID | Descripción |
|----------|-----|-------------|
| Video stream | `#video-stream` | Feed de cámara en vivo |
| Overlay canvas | `#overlay-canvas` | Canvas superpuesto para dibujar recuadros |
| Detection box | `#detection-box` | HTML overlay para etiqueta de detección |
| Cropped canvas | `#cropped-canvas` | Muestra recortada de la fruta |
| Results div | `#results` | Panel de resultados |
| Plot container | `#plot-container` | Gráfica Plotly |
| Analyze button | `#analyze-btn` | Botón de análisis |
| Progress bar | `#progress-fill` | Barra de progreso (0-100%) |

---

## 🤖 Detección con IA

### Modelo COCO-SSD

- **Modelo**: cocoSsd.load()
- **Detección**: Cada 500ms
- **Objetos detectados**: banana, orange, apple, food, broccoli, pizza, cake, donut, hot dog

### Lógica de Detección

```javascript
// Pseudocódigo
1. Si modelo IA cargado:
   - Detectar objetos cada 500ms
   - Si objeto es fruta/comida:
     - Dibujar recuadro verde
     - Guardar bbox para análisis
   - Sino:
     - Usar fallback por color

2. Si modelo NO cargado:
   - Usar solo detección por color
```

### Recuadro de Detección

- **Color borde**: Verde (#4CAF50)
- **Grosor**: 3px
- **Relleno**: rgba(76, 175, 80, 0.3)
- **Etiqueta**: `{clase} {confianza}%`

---

## 📊 Análisis de Color (Backend)

### Base de Datos de Referencias RGB

| Grado | Nombre | RGB | Descripción |
|-------|--------|-----|-------------|
| 0 | Verde | (58, 95, 11) | Sin madurar |
| 1 | Pintón | (107, 142, 35) | Iniciando maduración |
| 2 | Ligeramente Maduro | (189, 183, 107) | En proceso |
| 3 | Maduro | (255, 215, 0) | Listo para consumo |
| 4 | Muy Maduro | (255, 165, 0) | Sobre madurando |
| 5 | Sobre Maduro | (204, 119, 34) | Muy maduro |

### Algoritmo de Clasificación

```python
# 1. Detectar contornos en imagen
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(...)

# 2. Encontrar contorno más grande
contours, _ = cv2.findContours(thresh, ...)
largest = max(contours, key=cv2.contourArea)

# 3. Crear máscara y calcular color promedio
mask = np.zeros_like(gray)
cv2.drawContours(mask, [largest], -1, 255, -1)
mean_color = cv2.mean(image, mask=mask)

# 4. Clasificar por distancia euclidiana
distancias = [dist(color_promedio, ref) for ref in referencias_rgb]
grado_base = argmin(distancias)

# 5. Refinamiento con interpolación
r_norm = clip((r - 58) / (255 - 58) * 4, 0, 5)
grado_final = (grado_base + r_norm) / 2
```

### Estimación Bioquímica

```python
# Basado en regresión lineal
brix = 2.41 * grado_final + 7.15      # °Bx (7-18)
acidez = max(0.1, -0.65 * grado_final + 3.12)  # % (3-0.1)
```

---

## 🔌 Endpoints API

### `GET /`

- **Descripción**: Página principal
- **Respuesta**: Renderiza `index.html`

### `GET /video_feed`

- **Descripción**: Stream de video MJPEG
- **MIME Type**: `multipart/x-mixed-replace; boundary=frame`
- **Fuente**: Cámara web (OpenCV)

### `POST /analyze`

- **Descripción**: Analiza imagen y devuelve resultados
- **Body**: `{ "image": "data:image/jpeg;base64,..." }`
- **Respuesta**:

```json
{
  "r": 180,
  "g": 150,
  "b": 80,
  "madurez": "Grado 3: Maduro",
  "brix": 14.38,
  "acidez": 1.17,
  "cropped_image": "base64_encoded_jpeg..."
}
```

---

## ⚙️ Configuración

### Puertos

| Servicio | Puerto | Descripción |
|----------|--------|-------------|
| Flask | 5001 | Servidor principal |
| Camera | 0 | Webcam por defecto |

### Canvas

| Canvas | Dimensiones | Propósito |
|--------|-------------|-----------|
| Overlay | 100% video | Dibujar recuadros IA |
| Cropped | 320x240 | Mostrar muestra recortada |
| Capture | 640x480 | Captura para análisis |

### Caché

```python
# Headers para evitar caché
Cache-Control: no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0
Pragma: no-cache
Expires: 0
```

---

## 🐛 Problemas Conocidos

1. **Navegador cachea archivos CSS/JS**
   - Solución: Ctrl+Shift+R o borrar caché

2. **COCO-SSD no detecta específicamente "mango"**
   - Solución: Usar objetos similares (food, banana, orange)

3. **Puerto 5000 puede estar ocupado en macOS**
   - Solución: Usar puerto 5001

---

## 📝 Historial de Cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-03-31 | 1.0.0 | Versión inicial con IA (TensorFlow.js + COCO-SSD) |
| 2026-03-31 | 0.9.0 | Versión básica con análisis por color |

---

## 🚀 Para Ejecutar

```bash
# 1. Instalar dependencias
pip install flask opencv-python numpy

# 2. Ejecutar servidor
cd "/Users/esteban/Documents/uniminuto/Proyectos investigacion/Colorimetro mango comun"
python app.py

# 3. Abrir navegador
http://localhost:5001
```

---

## ✅ Checklist de Verificación

- [ ] Servidor Flask inicia sin errores
- [ ] Cámara muestra video en vivo
- [ ] Modelo COCO-SSD carga correctamente
- [ ] Recuadro verde aparece sobre objetos detectados
- [ ] Botón "Analizar Fruta" funciona
- [ ] Resultados muestran RGB, Brix, Acidez
- [ ] Gráfica RGB se actualiza
- [ ] Muestra recortada aparece en canvas
- [ ] Barra de progreso muestra grado de madurez
- [ ] No hay "temblor" en el diseño

---

*Documento creado para referencia y mantenimiento del proyecto.*
