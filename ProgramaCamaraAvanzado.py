import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AnalizadorMangoMaestro:
    def __init__(self, window):
        self.window = window
        self.window.title("Analizador Multiespectral de Maduración")
        self.window.geometry("1400x850")
        self.window.configure(bg="#121212")

        # --- BASE DE DATOS DE COLORES (Tu tabla) ---
        self.referencias_rgb = [
            (58, 95, 11),   # Grado 0
            (107, 142, 35),  # Grado 1
            (189, 183, 107), # Grado 2
            (255, 215, 0),   # Grado 3
            (255, 165, 0),   # Grado 4
            (204, 119, 34)   # Grado 5
        ]

        # --- LAYOUT ---
        self.frame_cam = tk.Frame(window, bg="#121212")
        self.frame_cam.pack(side=tk.LEFT, padx=20)

        self.frame_info = tk.Frame(window, bg="#1e1e1e", padx=20, pady=20)
        self.frame_info.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Video
        self.canvas_cam = tk.Canvas(self.frame_cam, width=640, height=480, bg="black", highlightthickness=0)
        self.canvas_cam.pack(pady=10)

        self.btn_capturar = tk.Button(self.frame_cam, text="ANALIZAR FRUTA", command=self.analizar_completo,
                                     bg="#0078d7", fg="white", font=("Segoe UI", 12, "bold"), height=2)
        self.btn_capturar.pack(fill=tk.X)

        self.btn_live = tk.Button(self.frame_cam, text="VISTA EN VIVO", command=self.activar_video, bg="#333", fg="white")
        self.btn_live.pack(fill=tk.X, pady=5)

        # Resultados Bioquímicos
        tk.Label(self.frame_info, text="INDICADORES BIOQUÍMICOS", font=("Segoe UI", 16, "bold"), fg="#0078d7", bg="#1e1e1e").pack()
        
        self.lbl_datos = tk.Label(self.frame_info, text="Coloque el mango frente a la cámara", font=("Consolas", 12),
                                 fg="#00ff00", bg="#000", justify=tk.LEFT, padx=15, pady=15, width=50)
        self.lbl_datos.pack(pady=20)

        # Barra de Maduración Profesional
        tk.Label(self.frame_info, text="LÍNEA DE TIEMPO DE MADURACIÓN (Grados 0-5)", fg="white", bg="#1e1e1e").pack()
        self.barra_madurez = ttk.Progressbar(self.frame_info, orient=tk.HORIZONTAL, length=500, mode='determinate', maximum=5)
        self.barra_madurez.pack(pady=10)

        # Gráfica de comparación RGB
        self.fig, self.ax = plt.subplots(figsize=(5, 3))
        self.fig.patch.set_facecolor('#1e1e1e')
        self.canvas_plot = FigureCanvasTkAgg(self.fig, master=self.frame_info)
        self.canvas_plot.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.cap = cv2.VideoCapture(0)
        self.pausar = False
        self.actualizar_frame()

    def actualizar_frame(self):
        if not self.pausar:
            ret, frame = self.cap.read()
            if ret:
                self.frame_actual = frame
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img_tk = ImageTk.PhotoImage(image=Image.fromarray(img))
                self.canvas_cam.create_image(0, 0, anchor=tk.NW, image=img_tk)
                self.canvas_cam.image = img_tk
        self.window.after(15, self.actualizar_frame)

    def analizar_completo(self):
        if not hasattr(self, 'frame_actual'): return
        
        frame = self.frame_actual.copy()
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gris, (7, 7), 0)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        
        contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if contornos:
            cnt = max(contornos, key=cv2.contourArea)
            mask = np.zeros_like(gris)
            cv2.drawContours(mask, [cnt], -1, 255, -1)
            
            # Recorte sin fondo
            recorte_bgr = cv2.bitwise_and(frame, frame, mask=mask)
            recorte_rgb = cv2.cvtColor(recorte_bgr, cv2.COLOR_BGR2RGB)
            self.pausar = True
            
            # Mostrar solo el mango en la cámara
            img_pil = Image.fromarray(recorte_rgb)
            img_tk = ImageTk.PhotoImage(image=img_pil)
            self.canvas_cam.create_image(0, 0, anchor=tk.NW, image=img_tk)
            self.canvas_cam.image = img_tk

            # --- CÁLCULO MULTI-COLOR (RGB) ---
            pixeles = recorte_rgb[mask > 0]
            promedio_rgb = np.mean(pixeles, axis=0) # [R, G, B] actuales

            # Encontrar el grado más cercano usando distancia Euclidiana
            distancias = [np.linalg.norm(promedio_rgb - np.array(ref)) for ref in self.referencias_rgb]
            grado_base = np.argmin(distancias)
            
            # Refinamiento (interpolación suave entre grados)
            # Usamos el canal rojo como guía de progresión lineal para el ajuste fino
            r_norm = np.clip((promedio_rgb[0] - 58) / (255 - 58) * 4, 0, 5)
            grado_final = (grado_base + r_norm) / 2 # Promediamos cercanía de vector y progresión de rojo

            # --- ECUACIONES DE MÍNIMOS CUADRADOS ---
            # Basado en los rangos: Brix (7 a 18) | Acidez (3 a 0.2)
            brix_est = 2.41 * grado_final + 7.15
            acidez_est = max(0.1, -0.65 * grado_final + 3.12)

            # --- ACTUALIZAR UI ---
            self.barra_madurez['value'] = grado_final
            txt = (f"RESULTADOS DEL ESCANEO:\n"
                   f"{'-'*30}\n"
                   f"Estado: Grado {int(grado_final)}\n"
                   f"Color Promedio: R:{int(promedio_rgb[0])} G:{int(promedio_rgb[1])} B:{int(promedio_rgb[2])}\n"
                   f"{'-'*30}\n"
                   f"Grados Brix: {brix_est:.2f} °Bx\n"
                   f"Acidez Titulable: {acidez_est:.2f} %\n"
                   f"Confianza: {100 - min(distancias):.1f}%")
            
            self.lbl_datos.config(text=txt)

            # Gráfica comparativa
            self.ax.clear()
            x_labs = ['R', 'G', 'B']
            self.ax.bar(x_labs, promedio_rgb, color=['red', 'green', 'blue'], alpha=0.8, label='Detectado')
            self.ax.set_ylim([0, 255])
            self.ax.set_title("Firma Espectral del Mango", color="white")
            self.ax.tick_params(colors='white')
            self.canvas_plot.draw()

    def activar_video(self):
        self.pausar = False
        self.lbl_datos.config(text="Buscando muestra...")

    def terminar(self):
        self.cap.release()
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalizadorMangoMaestro(root)
    root.mainloop()