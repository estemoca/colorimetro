# MEMORIA TÉCNICA

## Registro de Derechos de Autor — Software

### Colorímetro de Mango — Análisis de Maduración con IA

---

| | |
|---|---|
| **Título de la obra** | Colorímetro de Mango |
| **Tipo de obra** | Programa de computador / Software |
| **Versión registrada** | 1.1.0 |
| **Fecha de creación** | Marzo 2026 - Mayo 2026 |
| **Autores** | [Por definir] |
| **Titular** | [Por definir] |
| **Fecha del documento** | Mayo 2026 |

---

## DECLARACIÓN DE AUTORÍA

Los abajo firmantes declaramos que el contenido intelectual del software **Colorímetro de Mango**, incluyendo la lógica de negocio, diseño de arquitectura, estructura de datos, algoritmos de clasificación y dirección del desarrollo, fue realizado por personas naturales identificadas.

Las herramientas de inteligencia artificial fueron utilizadas exclusivamente como instrumentos auxiliares bajo nuestra supervisión y dirección humana permanente.

---

## TABLA DE CONTENIDO

1. [Identificación de la Obra](#1-identificación-de-la-obra)
2. [Identificación de los Autores](#2-identificación-de-los-autores)
3. [Origen y Motivación del Desarrollo](#3-origen-y-motivación-del-desarrollo)
4. [Proceso Creativo e Intelectual](#4-proceso-creativo-e-intelectual)
5. [Uso de Inteligencia Artificial como Herramienta Auxiliar](#5-uso-de-inteligencia-artificial-como-herramienta-auxiliar)
6. [Descripción Técnica Resumida](#6-descripción-técnica-resumida)
7. [Originalidad y Diferenciación](#7-originalidad-y-diferenciación)
8. [Licencias de Terceros Incorporadas](#8-licencias-de-terceros-incorporadas)
9. [Derechos Patrimoniales y Morales](#9-derechos-patrimoniales-y-morales)
10. [Declaraciones Finales](#10-declaraciones-finales)

---

## 1. IDENTIFICACIÓN DE LA OBRA

### 1.1 Nombre del Software

**Colorímetro de Mango — Análisis de Maduración con IA**

### 1.2 Descripción General

Aplicación web desarrollada en Flask (Python) y JavaScript que permite detectar automáticamente mangos en tiempo real mediante técnicas de visión por computadora e inteligencia artificial, analizarlos para determinar su grado de madurez (escala 0-5) y estimar valores bioquímicos como grados Brix y acidez titulable.

### 1.3 Tipo y Naturaleza de la Obra

- **Tipo**: Programa de computador
- **Naturaleza**: Original
- **Versión objeto del registro**: 1.1.0

### 1.4 Lenguajes de Programación

| Lenguaje | Propósito |
|----------|-----------|
| Python 3.8+ | Backend (Flask, OpenCV, NumPy) |
| HTML5 | Estructura de interfaz |
| CSS3 | Estilos visuales |
| JavaScript (ES6+) | Lógica frontend, TensorFlow.js |

### 1.5 Plataforma / Entorno de Ejecución

- **Backend**: Windows, macOS, Linux con Python 3.8+
- **Frontend**: Navegadores modernos (Chrome, Firefox, Edge, Safari)
- **Puerto por defecto**: 5002

### 1.6 Versión Objeto del Registro

Versión 1.1.0 (Mayo 2026)

---

## 2. IDENTIFICACIÓN DE LOS AUTORES

### 2.1 Datos de los Autores

| # | Nombre | Identificación | Rol | Contribución |
|---|--------|-----------------|-----|---------------|
| 1 | [Por definir] | [Por definir] | Desarrollador Principal | Arquitectura, backend, algoritmos |
| 2 | [Por define] | [Por definir] | Desarrollador Frontend | UI, JavaScript, detección IA |

### 2.2 Relación con el Titular

[Por definir: Relación laboral / contrato de prestación de servicios / asociación]

---

## 3. ORIGEN Y MOTIVACIÓN DEL DESARROLLO

### 3.1 Problema que Resuelve el Software

La determinación del grado de madurez del mango es crucial para la postcosecha, ya que define el momento óptimo de consumo, venta y exportación. Los métodos tradicionales requieren equipos costosos y personal especializado. Este software ofrece una solución accesible, económica y automatizada.

### 3.2 Necesidad u Oportunidad

- Democratizar el acceso a tecnología de análisis de maduración
- Reducir costos en operaciones de postcosecha
- Apoyar investigaciones académicas en fruticultura

### 3.3 Contexto Organizacional

Desarrollo realizado en el marco de proyectos de investigación de la **Universidad Minuto de Dios**, orientado a soluciones tecnológicas para el sector agrícola colombiano.

### 3.4 Fecha de Inicio y Duración

- **Inicio**: Marzo 2026
- **Duración**: 2 meses (en desarrollo activo)
- **Estado**: Operativo / Beta

---

## 4. PROCESO CREATIVO E INTELECTUAL

### 4.1 Metodología de Desarrollo

Metodología ágil simplificada con las siguientes fases:

1. **Análisis de requisitos** - Definición de funcionalidades
2. **Diseño de arquitectura** - Estructura MVC
3. **Diseño de interfaz** - Layout Grid 2x2
4. **Codificación** - Implementación de módulos
5. **Pruebas** - Validación de detección y análisis
6. **Despliegue** - Publicación local

### 4.2 Fases del Desarrollo y Decisiones Clave

| Fase | Decisiones Tomadas por Ingenieros |
|------|-----------------------------------|
| Análisis | Definición de 6 grados de madurez, selección de modelo COCO-SSD |
| Arquitectura | Diseño Cliente-Servidor con Flask, streaming MJPEG |
| Base de datos | Definición de tabla de referencias RGB para clasificación |
| Interfaz | Layout Grid 2x2 con 4 paneles: cámara, muestra, resultados, gráfica |
| Codificación | Implementación de algoritmos de clasificación con distancia euclidiana |
| Pruebas | Validación con mangos reales, ajustes de umbrales |

### 4.3 Originalidad de la Solución

Elementos originales del software:

- **Algoritmo de clasificación por distancia euclidiana** con interpolación basada en canal rojo
- **Estimación bioquímica** mediante regresión lineal (Brix y Acidez)
- **Integración de TensorFlow.js + OpenCV** en arquitectura híbrida cliente-servidor

### 4.4 Problemas Técnicos Resueltos

| Problema | Solución Ingenieril |
|----------|---------------------|
| COCO-SSD no detecta específicamente "mango" | Uso de objetos similares (food, banana, orange) como fallback |
| Ruido en detección de contornos | Aplicación de desenfoque gaussiano y umbral adaptativo |
| Variación en iluminación | Normalización de valores RGB con interpolación |

---

## 5. USO DE INTELIGENCIA ARTIFICIAL COMO HERRAMIENTA AUXILIAR

### 5.1 Declaración sobre el Uso de IA

Se utilizado herramientas de **inteligencia artificial generativa** (ChatGPT, GitHub Copilot, Claude) durante el proceso de desarrollo, exclusivamente como herramientas de asistencia bajo la dirección y supervisión de los ingenieros autores.

### 5.2 Rol de la IA en el Proyecto

La IA **NO** realizó las siguientes actividades:

- ❌ No tomó decisiones de diseño
- ❌ No definió la arquitectura
- ❌ No determinó la lógica de negocio
- ❌ No estableció los criterios de clasificación

La IA fue utilizada para:

- ✅ Sugerencia de fragmentos de código bajo especificación humana
- ✅ Autocompletado de patrones repetitivos
- ✅ Generación de código boilerplate a partir de instrucciones precisas
- ✅ Asistencia en documentación y estilos CSS

### 5.3 Control Humano Ejercido sobre la IA

| Control | Descripción |
|---------|-------------|
| Prompts redactados por ingenieros | Todos los prompts fueron diseñados y formulados por personas |
| Output revisado manualmente | Todo código generado fue revisado, comprendido y validado |
| Modificaciones realizadas | El código fue adaptado, mejorado y corregido antes de integración |
| Decisiones de integración | Qué generar, cómo integrarlo y qué descartar fue siempre humano |

### 5.4 Inventario de Módulos con Asistencia de IA

| Módulo / Archivo | Herramienta IA | Prompt / Descripción | Modificaciones Realizadas | Estimación IA/Humano |
|------------------|----------------|----------------------|---------------------------|----------------------|
| `main.js` | ChatGPT/Copilot | "Crear función de detección con COCO-SSD" | Adaptado el flujo de detección, modificado manejo de canvas | 30% IA / 70% Humano |
| `style.css` | ChatGPT | "Estilos para aplicación de análisis de fruta" | Personalizado el tema oscuro con gradientes verdes | 40% IA / 60% Humano |
| `app.py` | ChatGPT | "Estructura Flask con OpenCV" | Completamente reescrito por el autor | 20% IA / 80% Humano |

### 5.5 Evidencia de Autoría Humana

- Repositorio Git con historial de commits
- Documentos de diseño (SPEC.md, derechosautor.md)
- Actas de reuniones de decisiones de arquitectura
- Prompts documentados utilizados con IA
- Código fuente con comentarios y estructura coherente

---

## 6. DESCRIPCIÓN TÉCNICA RESUMIDA

### 6.1 Arquitectura en Términos No Técnicos

El sistema funciona como una aplicación web donde:
1. La cámara muestra video en tiempo real
2. Un modelo de inteligencia artificial dibuja un recuadro sobre la fruta detectada
3. El usuario presiona "analizar"
4. El servidor procesa la imagen y calcula el color promedio
5. El sistema compara el color con una tabla de referencia y determina la madurez

### 6.2 Funcionalidades Principales

| Funcionalidad | Descripción |
|---------------|-------------|
| Video en vivo | Streaming de cámara web |
| Detección IA | Identificación de objetos con COCO-SSD |
| Recorte automático | Aislamiento del área detectada |
| Análisis de color | Cálculo de RGB promedio con máscara de contorno |
| Clasificación | Determinación de grado de madurez (0-5) |
| Estimación bioquímica | Cálculo de Brix y Acidez |
| Firma espectral | Gráfica de barras RGB |

### 6.3 Flujo General del Sistema

```
Usuario → Navegador → Video Stream (MJPEG)
                         ↓
                 TensorFlow.js (IA)
                         ↓
                 Recuadroverde (detección)
                         ↓
                 Botón "Analizar"
                         ↓
                 /analyze (POST con imagen)
                         ↓
                 OpenCV (procesamiento)
                         ↓
                 Clasificación RGB
                         ↓
                 Resultado JSON → UI
```

### 6.4 Datos que Procesa y Produce

| Tipo | Descripción |
|------|-------------|
| Entrada | Imagen JPEG de la cámara (640x480) |
| Procesamiento | Análisis de contornos, cálculo de color promedio |
| Salida | RGB, Grado de madurez, Brix, Acidez, Imagen recortada |

### 6.5 Integraciones con Otros Sistemas

- **TensorFlow.js**: Detección de objetos en navegador
- **Plotly.js**: Generación de gráficas
- **OpenCV**: Procesamiento de imagen en servidor

---

## 7. ORIGINALIDAD Y DIFERENCIACIÓN

### 7.1 Diferenciación de Soluciones Existentes

| Característica | Soluciones Existentes | Colorímetro de Mango |
|----------------|----------------------|---------------------|
| Costo | Equipos profesionales ($1000+) | Software gratuito |
| Portabilidad | Dispositivo físico | Navegador web |
| Detección | Manual | Automática con IA |
| Salida | Solo color | RGB + Brix + Acidez + Gráfica |

### 7.2 Elementos Creativos y Originales

- **Sistema híbrido cliente-servidor** con streaming de video
- **Algoritmo de clasificación** con interpolación basada en distancia euclidiana
- **Estimación bioquímica** mediante fórmulas de regresión lineal
- **Interfaz Grid 2x2** con visualización en tiempo real

### 7.3 Algoritmos o Lógicas Propias

```python
# Algoritmo de clasificación (desarrollado por autores)
distancias = [np.linalg.norm(promedio_rgb - np.array(ref)) for ref in referencias_rgb]
grado_base = np.argmin(distancias)
r_norm = np.clip((promedio_rgb[0] - 58) / (255 - 58) * 4, 0, 5)
grado_final = (grado_base + r_norm) / 2
```

### 7.4 Declaración de No Reproducción

Declaramos que el software no reproduce código de terceros sin licencia. Todas las librerías utilizadas son de código abierto con licencias compatibles.

---

## 8. LICENCIAS DE TERCEROS INCORPORADAS

### 8.1 Tabla de Componentes

| Biblioteca / Componente | Versión | Licencia | Uso |
|------------------------|---------|----------|-----|
| Flask | 2.0+ | BSD | Servidor web |
| OpenCV | 4.5+ | Apache 2.0 | Procesamiento de imagen |
| NumPy | 1.20+ | BSD | Cálculos numéricos |
| TensorFlow.js | Latest | Apache 2.0 | IA en navegador |
| COCO-SSD | Latest | Apache 2.0 | Detección de objetos |
| Plotly.js | 2.12.1 | MIT | Gráficas |

### 8.2 Declaración de Cumplimiento

Todos los componentes de terceros se utilizan de acuerdo con sus licencias originales. El código fuente del proyecto se distribuye bajo licencia [Por definir -建议: MIT].

---

## 9. DERECHOS PATRIMONIALES Y MORALES

### 9.1 Derechos Patrimoniales

| Aspecto | Definición |
|---------|------------|
| Titular de derechos patrimoniales | [Por definir] |
| Forma de explotación | Uso académico, investigación |
| Licencia de distribución | [Por definir] |

### 9.2 Derechos Morales

Los autores conservan sus derechos morales irrenunciables:
- Derecho a la paternidad de la obra
- Derecho a la integridad de la obra
- Derecho a modificar la obra

### 9.3 Términos de Uso

[Por definir según políticas de la institución]

---

## 10. DECLARACIONES FINALES

Los abajo firmantes declaramos bajo juramento que:

- ✅ La obra es original y de nuestra autoría
- ✅ No se vulnera derechos de terceros
- ✅ El contenido creativo fue desarrollado por personas naturales
- ✅ Las herramientas de IA fueron usadas exclusivamente como instrumentos auxiliares
- ✅ La información proporcionada es veraz

---

## ANEXOS

### Anexo 1 — Extracto del Código Fuente

Ver archivos del proyecto:
- `app.py` (líneas 1-150)
- `main.js` (líneas 1-348)
- `static/style.css` (líneas 1-263)

### Anexo 2 — Diagrama de Arquitectura

Incluido en MANUAL_TECNICO.md

### Anexo 3 — Historial de Commits

[Por obtener del repositorio Git]

### Anexo 4 — Prompts Utilizados con IA

[Por documentar]

### Anexo 5 — Contratos Laborales

[Por incluir]

### Anexo 6 — Capturas de Pantalla

[Por incluir]

---

## FIRMAS

| Autor | Nombre | Fecha | Firma |
|-------|--------|-------|-------|
| 1 | [Por definir] | Mayo 2026 | _________________ |
| 2 | [Por definir] | Mayo 2026 | _________________ |

---

*Documento elaborado para registro ante la Dirección Nacional de Derechos de Autor (DNDA).*
*Colorímetro de Mango — Universidad Minuto de Dios*
*Mayo 2026*