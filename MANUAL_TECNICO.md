# MANUAL TÉCNICO

## Colorímetro de Mango — Análisis de Maduración con IA

| | |
|---|---|
| **Versión** | 1.1.0 |
| **Clasificación** | USO INTERNO |
| **Fecha** | Mayo 2026 |
| **Registro DNDA** | [Pendiente] |

---

## TABLA DE CONTENIDO

1. [Introducción](#1-introducción)
2. [Visión General del Sistema](#2-visión-general-del-sistema)
3. [Arquitectura del Sistema](#3-arquitectura-del-sistema)
4. [Estructura del Proyecto](#4-estructura-del-proyecto)
5. [APIs e Integraciones](#5-apis-e-integraciones)
6. [Instalación y Despliegue](#6-instalación-y-despliegue)
7. [Seguridad](#7-seguridad)
8. [Rendimiento](#8-rendimiento)

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento

Documento técnico completo que describe la arquitectura, instalación, operación y mantenimiento del Colorímetro de Mango.

### 1.2 Alcance Técnico

- Backend: Servidor Flask + OpenCV
- Frontend: HTML5/JavaScript + TensorFlow.js
- Detección: COCO-SSD (IA)
- Análisis: Procesamiento de imagen Python

### 1.3 Audiencia Objetivo

- Desarrolladores
- Administradores de sistemas
- Investigadores técnicos

---

## 2. VISIÓN GENERAL DEL SISTEMA

### 2.1 Descripción de la Solución

Aplicación web Flask para detectar el grado de madurez de mangos mediante análisis de color usando:
- **TensorFlow.js + COCO-SSD** para detección de objetos por IA
- **OpenCV** para procesamiento de imagen en servidor
- **Análisis RGB** para determinar madurez (Grados 0-5)

### 2.2 Objetivos del Sistema

| Objetivo | Descripción |
|----------|-------------|
| Detección automática | Identificar mango en tiempo real |
| Clasificación de madurez | Clasificar en grados 0-5 |
| Estimación bioquímica | Calcular Brix y Acidez |
| Interfaz visual | Mostrar resultados y gráfica espectral |

### 2.3 Diagrama de Contexto

```
┌─────────────┐     HTTP      ┌─────────────┐
│  Navegador  │◄─────────────►│   Flask     │
│   (Client)  │               │  (Server)   │
└──────┬──────┘               └──────┬──────┘
       │                                │
       │MJPEG                    OpenCV │
       ▼                                ▼
┌─────────────┐               ┌─────────────┐
│   Camera    │               │   Python    │
│   (Webcam)  │               │  (Analysis) │
└─────────────┘               └─────────────┘
```

---

## 3. ARQUITECTURA DEL SISTEMA

### 3.1 Patrón Arquitectónico

**Modelo-Vista-Controlador (MVC) Simplificado**

| Capa | Componente | Tecnología |
|------|------------|------------|
| Vista | Frontend | HTML5 + CSS3 + JS |
| Controlador | Flask Routes | Python/Flask |
| Modelo | OpenCV + TensorFlow.js | Python/JS |

### 3.2 Componentes Principales

| Componente | Responsabilidad |
|------------|-----------------|
| `app.py` | Servidor Flask, rutas, análisis |
| `index.html` | Interfaz de usuario |
| `main.js` | Lógica frontend, detección IA |
| `style.css` | Estilos visuales |

### 3.3 Stack Tecnológico

| Capa | Tecnología | Versión |
|------|------------|---------|
| Backend | Flask | 2.0+ |
| Procesamiento | OpenCV | 4.5+ |
| Numérico | NumPy | 1.20+ |
| Frontend JS | TensorFlow.js | Latest |
| Detección IA | COCO-SSD | Latest |
| Gráficas | Plotly.js | 2.12.1 |

### 3.4 Tabla de Dependencias

| Componente | Tecnología | Licencia |
|------------|------------|----------|
| Flask | Python | BSD |
| OpenCV | C++/Python | Apache 2.0 |
| TensorFlow.js | JS | Apache 2.0 |
| COCO-SSD | TensorFlow | Apache 2.0 |
| Plotly.js | JS | MIT |

---

## 4. ESTRUCTURA DEL PROYECTO

### 4.1 Organización de Directorios

```
Colorimetro mango comun/
├── app.py                          # Servidor Flask (Backend)
├── ProgramaCamaraAvanzado.py       # Standalone Tkinter (referencia)
├── templates/
│   └── index.html                  # Interfaz principal
├── static/
│   ├── main.js                     # Lógica frontend (IA)
│   └── style.css                   # Estilos CSS
├── SPEC.md                         # Especificación del proyecto
├── MANUAL_USUARIO.md               # Manual de usuario
├── MANUAL_TECNICO.md               # Este archivo
├── MEMORIA_TECNICA.md              # Memoria para DNDA
└── .vscode/
    └── settings.json               # Configuración VSCode
```

### 4.2 Módulos y Responsabilidades

| Archivo | Responsabilidad |
|---------|-----------------|
| `app.py` | Servidor, video stream, análisis de imagen |
| `main.js` | Detección IA, UI, comunicación con servidor |
| `style.css` | Estilos, tema oscuro verde |

### 4.3 Módulos con Asistencia de IA

| Módulo | Herramienta IA | Propósito |
|--------|---------------|-----------|
| `main.js` | GitHub Copilot/ChatGPT | Detección y renderizado |
| `style.css` | GitHub Copilot | Estilos UI |

---

## 5. APIs E INTEGRACIONES

### 5.1 APIs Internas

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/` | GET | Página principal |
| `/video_feed` | GET | Stream MJPEG de cámara |
| `/analyze` | POST | Analizar imagen |
| `/static/<filename>` | GET | Archivos estáticos |

### 5.2 Endpoint: `/analyze`

**Request:**
```json
{
  "image": "data:image/jpeg;base64,..."
}
```

**Response:**
```json
{
  "r": 180,
  "g": 150,
  "b": 80,
  "madurez": "Grado 3: Maduro",
  "brix": 14.38,
  "acidez": 1.17,
  "cropped_image": "base64..."
}
```

### 5.3 Formatos de Intercambio

- **HTTP**: JSON sobre HTTPS
- **Imágenes**: Base64 encode (JPEG)
- **Video**: MJPEG stream

### 5.4 Autenticación

No requiere autenticación (uso local).

---

## 6. INSTALACIÓN Y DESPLIEGUE

### 6.1 Requisitos de Infraestructura

| Recurso | Mínimo | Recomendado |
|---------|--------|-------------|
| CPU | 2 cores | 4 cores |
| RAM | 2 GB | 4 GB |
| Almacenamiento | 500 MB | 1 GB |

### 6.2 Prerrequisitos de Software

```bash
# Python 3.8+
python --version

# Instalar dependencias
pip install flask>=2.0 opencv-python>=4.5 numpy>=1.20
```

### 6.3 Variables de Entorno

| Variable | Valor por defecto | Descripción |
|----------|-------------------|-------------|
| `FLASK_ENV` | development | Entorno Flask |
| `PORT` | 5002 | Puerto del servidor |
| `CAMERA_INDEX` | 0 | Índice de cámara |

### 6.4 Proceso de Despliegue

```bash
# 1. Navegar al directorio del proyecto
cd "/Users/esteban/Documents/uniminuto/Proyectos investigacion/Colorimetro mango comun"

# 2. Instalar dependencias
pip install flask opencv-python numpy

# 3. Ejecutar servidor
python app.py

# 4. Verificar en navegador
http://localhost:5002
```

### 6.5 Configuración de Cámara

```python
# Configuración de cámara en app.py
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
```

---

## 7. SEGURIDAD

### 7.1 Medidas Implementadas

| Medida | Descripción |
|--------|-------------|
| Cache-Control | Encabezados para evitar caché |
| CORS | Restricciones por defecto Flask |
| Puerto local | Solo acceso localhost |

### 7.2 Encabezados de Seguridad

```python
response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0'
response.headers['Pragma'] = 'no-cache'
response.headers['Expires'] = '0'
```

### 7.3 Consideraciones OWASP

- No hay exposición de archivos sensibles
- No hay entrada de usuario persistida
- No hay credenciales almacenadas

---

## 8. RENDIMIENTO

### 8.1 Métricas Objetivo

| Métrica | Valor |
|---------|-------|
| Tiempo de carga página | < 3 seg |
| Tiempo análisis imagen | < 2 seg |
| FPS video stream | 15-30 fps |

### 8.2 Detección IA

| Parámetro | Valor |
|-----------|-------|
| Intervalo de detección | 150 ms |
| Modelo | lite_mobilenet_v2 |
| Intervalo mínimo | 100 ms |

---

## APÉNDICES

### Apéndice A — Diagrama de Arquitectura

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
├──────────────────────────────────────────────────────────────┤
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

### Apéndice B — Base de Datos de Referencias RGB

| Grado | Nombre | RGB |
|-------|--------|-----|
| 0 | Verde | (58, 95, 11) |
| 1 | Pintón | (107, 142, 35) |
| 2 | Ligeramente Maduro | (189, 183, 107) |
| 3 | Maduro | (255, 215, 0) |
| 4 | Muy Maduro | (255, 165, 0) |
| 5 | Sobre Maduro | (204, 119, 34) |

### Apéndice C — Glosario Técnico

| Término | Definición |
|---------|------------|
| MJPEG | Motion JPEG - formato de streaming |
| COCO-SSD | Modelo de detección de objetos |
| TensorFlow.js | Biblioteca TF en JavaScript |
| OpenCV | Biblioteca de visión por computadora |
| Brix | Medida de sólidos solubles |
| DNDA | Dirección Nacional de Derechos de Autor |

---

*Documento técnico elaborado para registro de derechos de autor.*
*Colorímetro de Mango — Universidad Minuto de Dios*