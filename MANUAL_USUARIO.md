# MANUAL DE USUARIO

## Colorímetro de Mango — Análisis de Maduración con IA

| | |
|---|---|
| **Versión** | 1.1.0 |
| **Fecha** | Mayo 2026 |
| **Registro DNDA** | [Pendiente] |

---

## TABLA DE CONTENIDO

1. [Introducción](#1-introducción)
2. [Requisitos del Sistema](#2-requisitos-del-sistema)
3. [Instalación y Configuración](#3-instalación-y-configuración)
4. [Interfaz de Usuario](#4-interfaz-de-usuario)
5. [Funcionalidades Principales](#5-funcionalidades-principales)
6. [Resolución de Problemas](#6-resolución-de-problemas)
7. [Soporte Técnico](#7-soporte-técnico)

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento

Este manual describe cómo instalar, configurar y utilizar el **Colorímetro de Mango**, una aplicación web para analizar el grado de madurez de mangos mediante técnicas de visión por computadora e inteligencia artificial.

### 1.2 Alcance

El documento cubre desde la instalación del software hasta el uso diario de todas las funcionalidades del sistema.

### 1.3 Público Objetivo

- Técnicos agrícolas
- Investigadores de postcosecha
- Productores de mango
- Estudiantes de agronomía

### 1.4 Descripción General del Software

El Colorímetro de Mango es una aplicación web que:

- **Detecta automáticamente** la fruta en tiempo real usando inteligencia artificial
- **Analiza el color** promedio de la superficie del mango
- **Clasifica la madurez** en una escala de 0 a 5 grados
- **Estima valores bioquímicos** como grados Brix y acidez titulable
- **Muestra una gráfica** de la firma espectral RGB

### 1.5 Glosario de Términos

| Término | Definición |
|---------|------------|
| **Grados Brix** | Medida de dulzura del fruto (escala 7-18 °Bx) |
| **Acidez Titulable** | Porcentaje de ácido en el fruto (escala 0.1-3%) |
| **IA** | Inteligencia Artificial |
| **RGB** | Modelo de color Rojo-Verde-Azul |
| **OpenCV** | Biblioteca de visión por computadora |

---

## 2. REQUISITOS DEL SISTEMA

### 2.1 Requisitos de Hardware

| Tipo | Mínimo | Recomendado |
|------|--------|-------------|
| Procesador | Dual Core 1.5 GHz | Quad Core 2.0 GHz |
| RAM | 2 GB | 4 GB |
| Almacenamiento | 500 MB | 1 GB |
| Cámara Web | USB 2.0 | USB 3.0 |

### 2.2 Sistemas Operativos

- Windows 10/11
- macOS 11 (Big Sur) o superior
- Linux (Ubuntu 20.04+)

### 2.3 Software Prerrequisito

| Software | Versión | Propósito |
|----------|---------|------------|
| Python | 3.8+ | Runtime del servidor |
| Navegador Web | Moderno | Chrome, Firefox, Edge, Safari |
| pip | Latest | Gestor de paquetes Python |

### 2.4 Conexión a Internet

**Requerida** para cargar el modelo de IA (TensorFlow.js) y las librerías CDN.

---

## 3. INSTALACIÓN Y CONFIGURACIÓN

### 3.1 Descarga del Software

```bash
# Clonar o descargar el proyecto
cd "/Users/esteban/Documents/uniminuto/Proyectos investigacion/Colorimetro mango comun"
```

### 3.2 Instalación de Dependencias

```bash
# Instalar dependencias Python
pip install flask opencv-python numpy
```

### 3.3 Ejecución del Servidor

```bash
# Ejecutar la aplicación
python app.py
```

El servidor iniciara en: **http://localhost:5002**

### 3.4 Primer Acceso

1. Abra un navegador web (Chrome recomendado)
2. Ingrese la URL: `http://localhost:5002`
3. Espere a que cargue el modelo de IA (indicador en la parte inferior)

---

## 4. INTERFAZ DE USUARIO

### 4.1 Layout General

La interfaz presenta un diseño de cuadrícula 2x2:

```
┌─────────────────────┬─────────────────────┐
│   CÁMARA EN VIVO    │  MUESTRA DETECTADA  │
│   [Video stream]    │  [Canvas recorte]   │
│   [Overlay canvas]  │  Área: --           │
├─────────────────────┼─────────────────────┤
│   RESULTADOS        │  FIRMA ESPECTRAL    │
│   Estado: --        │  [Gráfica RGB]      │
│   Brix: --          │                     │
└─────────────────────┴─────────────────────┘
```

### 4.2 Elementos de la Interfaz

| Elemento | Descripción |
|----------|-------------|
| **Cámara en Vivo** | Muestra el feed de la webcam |
| **Muestra Detectada** | Visualiza el mango recortado detectado |
| **Resultados** | Muestra madurez, RGB, Brix, Acidez |
| **Firma Espectral** | Gráfica de barras RGB |
| **Botón Analizar** | Inicia el análisis de la fruta |

### 4.3 Indicadores de Estado

| Indicador | Significado |
|-----------|--------------|
| Modo: IA lista | Modelo de IA cargado correctamente |
| Modo: Cargando modelo... |正在 Cargando modelo |
| Detección: IA ✓ | Fruit detected por IA |
| Detección: Color | Usando detección por color |

---

## 5. FUNCIONALIDADES PRINCIPALES

### 5.1 Visualización en Vivo

La cámara muestra el video en tiempo real. Cuando se detecta una fruta, aparece un recuadro verde con la etiqueta de confianza.

**Pasos:**
1. Permita el acceso a la cámara cuando el navegador lo solicite
2. Coloque un mango frente a la cámara
3. Espere a que aparezca el recuadro de detección

### 5.2 Análisis de Madurez

**Pasos para analizar:**

1. Asegúrese de que el mango esté visible y bien iluminado
2. Espere a que el sistema detecte el mango (recuadro verde)
3. Haga clic en el botón **"🔬 ANALIZAR FRUTA"**
4. Espere a que completes el análisis
5. Revise los resultados en el panel inferior

### 5.3 Interpretación de Resultados

| Grado | Nombre | Descripción |
|-------|--------|-------------|
| 0 | Verde | Sin madurar - No apropiado para consumo |
| 1 | Pintón | Iniciando maduración |
| 2 | Ligeramente Maduro | En proceso de maduración |
| 3 | Maduro | Listo para consumo |
| 4 | Muy Maduro | Sobre madurando |
| 5 | Sobre Maduro | Muy maduro - consumo inmediato |

**Valores Bioquímicos Estimados:**

- **Grados Brix**: Indica dulzura (7-18 °Bx)
- **Acidez**: Indica aciditud (0.1-3%)

### 5.4 Firma Espectral

La gráfica muestra los valores RGB promedio detectados del mango, permitiendo visualizar el perfil de color de la muestra analizada.

---

## 6. RESOLUCIÓN DE PROBLEMAS

### 6.1 Problemas Frecuentes

| Problema | Solución |
|----------|----------|
| La cámara no se muestra | Verifique que la cámara esté conectada y tenga permisos |
| El modelo de IA no carga | Verifique conexión a internet y actualice la página |
| No detecta el mango | Asegúrese de que el mango esté bien iluminado |
| Los resultados no aparecen | Presione el botón de analizar de nuevo |

### 6.2 Mensajes de Error

| Mensaje | Significado | Acción |
|---------|--------------|--------|
| "Modo: Sin IA (fallback color)" | Modelo no cargo, usando color | Verificar conexión a internet |
| "Error en análisis" | Fallo en el servidor | Verificar que Python esté corriendo |
| "Sin fecha" | Cámara no disponible | Conectar cámara y refrescar |

### 6.3 Cómo Reportar un Error

Envíe un correo con:
- Descripción del problema
- Sistema operativo y navegador
- Captura de pantalla del error
- Pasos para reproducir

---

## 7. SOPORTE TÉCNICO

### 7.1 Canales de Soporte

- **Correo**: [Por definir]
- **Documentación**: Este manual y SPEC.md

### 7.2 Información para Soporte

Al contactar soporte, proporcione:

1. Versión del software (1.1.0)
2. Sistema operativo
3. Navegador utilizado
4. Descripción del problema

### 7.3 Horarios de Atención

Por definir según institución.

---

## APÉNDICES

### Apéndice A — Atajos de Teclas

| Atajo | Función |
|-------|---------|
| F5 | Actualizar página |
| Ctrl+Shift+R | Forzar caché limpio |

### Apéndice B — Historial de Versiones

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0.0 | Marzo 2026 | Versión inicial con IA |
| 1.1.0 | Mayo 2026 | Mejoras en detección y análisis |

---

*Documento elaborado para el registro de derechos de autor.*
*Colorímetro de Mango — Universidad Minuto de Dios*