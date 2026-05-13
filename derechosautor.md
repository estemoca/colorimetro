# Plan de Registro de Derechos de Autor — Software con Componente de IA
> **Versión:** 1.0 | **Fecha:** Mayo 2026  
> **Contexto:** Software cuya lógica, arquitectura y prompts fueron diseñados por ingenieros humanos, con asistencia de herramientas de IA generativa en la generación de fragmentos de código.

---

## Índice General

1. [Marco Legal y Posición Jurídica](#1-marco-legal-y-posición-jurídica)
2. [Estrategia de Titularidad](#2-estrategia-de-titularidad)
3. [Documentación Requerida para el Registro](#3-documentación-requerida-para-el-registro)
4. [Estructura del Manual de Usuario](#4-estructura-del-manual-de-usuario)
5. [Estructura del Manual Técnico](#5-estructura-del-manual-técnico)
6. [Estructura de la Memoria Técnica](#6-estructura-de-la-memoria-técnica)
7. [Proceso de Registro Paso a Paso](#7-proceso-de-registro-paso-a-paso)
8. [Checklist Final](#8-checklist-final)
9. [Notas Importantes sobre IA y Autoría](#9-notas-importantes-sobre-ia-y-autoría)

---

## 1. Marco Legal y Posición Jurídica

### 1.1 Fundamento de la Autoría Humana

El registro se basa en el principio reconocido internacionalmente de que **los derechos de autor requieren autoría humana**. En este caso, los ingenieros son los autores legítimos porque:

- Diseñaron la **arquitectura general** del sistema.
- Redactaron los **prompts, instrucciones y especificaciones** que dirigieron a la IA.
- Tomaron todas las **decisiones de lógica de negocio**.
- Realizaron la **revisión, selección, integración y validación** del código generado.
- Aportaron **creatividad y criterio intelectual** en cada etapa.

### 1.2 Naturaleza del Aporte de la IA

La IA actuó como **herramienta instrumental**, equivalente a un compilador avanzado o un editor de código asistido. No tiene capacidad legal para ser titular de derechos.

### 1.3 Marco Normativo Aplicable (Colombia)

| Norma | Relevancia |
|---|---|
| Ley 23 de 1982 | Ley sobre Derechos de Autor |
| Decisión Andina 351 de 1993 | Régimen Común sobre Derecho de Autor |
| Ley 603 de 2000 | Software como obra protegida |
| Decreto 460 de 1995 | Registro Nacional del Derecho de Autor |
| DNDA (Dirección Nacional de Derechos de Autor) | Entidad registradora |

> **Nota:** Si el registro aplica para otros países, adaptar la sección normativa según la jurisdicción (USPTO para EE.UU., EUIPO para Europa, etc.).

---

## 2. Estrategia de Titularidad

### 2.1 Opciones de Titularidad

```
┌─────────────────────────────────────────────────────┐
│              OPCIONES DE TITULARIDAD                 │
├─────────────────┬───────────────────────────────────┤
│ Persona Jurídica│ Si el software fue desarrollado   │
│ (Empresa)       │ en el marco de contrato laboral   │
│                 │ → La empresa es titular            │
├─────────────────┼───────────────────────────────────┤
│ Personas        │ Si fue desarrollo independiente   │
│ Naturales       │ → Los ingenieros son co-autores   │
│ (Ingenieros)    │                                   │
├─────────────────┼───────────────────────────────────┤
│ Obra por        │ Contrato de encargo → titular     │
│ Encargo         │ puede ser el comitente            │
└─────────────────┴───────────────────────────────────┘
```

### 2.2 Recomendación

Registrar como **obra colectiva** o **obra en colaboración** a nombre de la organización, con los ingenieros listados como autores-creadores. Incluir cláusula expresa de que la IA fue usada como herramienta auxiliar.

---

## 3. Documentación Requerida para el Registro

### 3.1 Documentos Obligatorios ante la DNDA

- Formulario de solicitud de registro (diligenciado).
- Copia del código fuente (puede ser parcial — mínimo 50 páginas representativas o el archivo completo).
- Documento de identidad del solicitante / certificado de existencia si es persona jurídica.
- Poder o autorización si actúa un apoderado.
- Comprobante de pago de tasas.
- Memoria descriptiva del software *(ver sección 6)*.

### 3.2 Documentos de Soporte Internos (No obligatorios ante DNDA, pero críticos para defensa legal)

- Manual de Usuario *(ver sección 4)*.
- Manual Técnico *(ver sección 5)*.
- Memoria Técnica con declaración del rol de la IA *(ver sección 6)*.
- Registro de commits / historial de versiones (Git log).
- Actas de reunión donde se tomaron decisiones de diseño.
- Prompts y conversaciones con la IA (evidencia de autoría humana en la dirección).
- Contratos laborales o de prestación de servicios de los ingenieros.

---

## 4. Estructura del Manual de Usuario

> **Propósito:** Documento destinado al usuario final. Explica cómo instalar, configurar y usar el software sin necesidad de conocimientos técnicos avanzados.

---

### MANUAL DE USUARIO — Estructura Completa

```
MANUAL DE USUARIO
[Nombre del Software] v[X.X]

PORTADA
  - Nombre del software
  - Versión
  - Fecha
  - Nombre de la empresa / autores
  - Logo institucional
  - Número de registro DNDA (una vez obtenido)

TABLA DE CONTENIDO

CONTROL DE VERSIONES DEL DOCUMENTO
  - Versión | Fecha | Autor | Descripción del cambio

1. INTRODUCCIÓN
   1.1 Propósito del documento
   1.2 Alcance
   1.3 Público objetivo
   1.4 Descripción general del software
       - ¿Qué hace?
       - ¿Para quién es?
       - Beneficios principales
   1.5 Glosario de términos

2. REQUISITOS DEL SISTEMA
   2.1 Requisitos de hardware mínimos y recomendados
   2.2 Sistemas operativos compatibles
   2.3 Software prerequisito (navegadores, runtimes, etc.)
   2.4 Conexión a internet / red requerida

3. INSTALACIÓN Y CONFIGURACIÓN INICIAL
   3.1 Descarga del software
   3.2 Proceso de instalación paso a paso
       (Capturas de pantalla de cada paso)
   3.3 Configuración inicial
   3.4 Creación de cuenta / primer acceso
   3.5 Activación de licencia (si aplica)

4. INTERFAZ DE USUARIO
   4.1 Descripción general de la interfaz
       (Diagrama anotado de la pantalla principal)
   4.2 Menú principal y navegación
   4.3 Iconos y convenciones visuales usadas

5. FUNCIONALIDADES PRINCIPALES
   [Una sección por módulo o función principal]
   
   5.1 [Módulo / Función 1]
       - Descripción
       - Cómo acceder
       - Paso a paso con capturas
       - Resultado esperado
       - Consideraciones / advertencias
   
   5.2 [Módulo / Función 2]
       (Repetir estructura)
   
   5.N [Módulo / Función N]

6. GESTIÓN DE DATOS
   6.1 Importar datos
   6.2 Exportar datos
   6.3 Guardar y recuperar sesiones
   6.4 Copias de seguridad (backup)

7. ADMINISTRACIÓN Y CONFIGURACIÓN
   7.1 Gestión de usuarios y perfiles
   7.2 Ajustes y preferencias
   7.3 Notificaciones
   7.4 Seguridad y contraseñas

8. RESOLUCIÓN DE PROBLEMAS (FAQ)
   8.1 Problemas frecuentes y soluciones
   8.2 Mensajes de error comunes y qué hacer
   8.3 Cómo reportar un error

9. SOPORTE TÉCNICO
   9.1 Canales de soporte disponibles
   9.2 Información que se debe proveer al contactar soporte
   9.3 Horarios de atención

APÉNDICES
   Apéndice A — Atajos de teclado
   Apéndice B — Glosario completo
   Apéndice C — Historial de versiones del software
```

---

## 5. Estructura del Manual Técnico

> **Propósito:** Documento dirigido a desarrolladores, administradores de sistemas e integradores. Describe la arquitectura, instalación técnica, APIs, base de datos y operación del sistema.

---

### MANUAL TÉCNICO — Estructura Completa

```
MANUAL TÉCNICO
[Nombre del Software] v[X.X]

PORTADA
  - Nombre del software
  - Versión
  - Clasificación: CONFIDENCIAL / USO INTERNO
  - Fecha
  - Autores / Ingenieros responsables
  - Número de registro DNDA

TABLA DE CONTENIDO

CONTROL DE VERSIONES DEL DOCUMENTO

1. INTRODUCCIÓN
   1.1 Propósito del documento
   1.2 Alcance técnico
   1.3 Audiencia objetivo
   1.4 Documentos relacionados
   1.5 Acrónimos y definiciones técnicas

2. VISIÓN GENERAL DEL SISTEMA
   2.1 Descripción de la solución
   2.2 Objetivos del sistema
   2.3 Diagrama de contexto (C4 Nivel 1)
   2.4 Restricciones y supuestos técnicos

3. ARQUITECTURA DEL SISTEMA
   3.1 Patrón arquitectónico utilizado
       (MVC, microservicios, monolito, etc.)
   3.2 Diagrama de arquitectura general
   3.3 Componentes principales y responsabilidades
   3.4 Diagrama de despliegue (deployment)
   3.5 Tecnologías y stack tecnológico
   
   Tabla de dependencias:
   | Componente | Tecnología | Versión | Licencia |
   |---|---|---|---|

4. ESTRUCTURA DEL PROYECTO (CÓDIGO FUENTE)
   4.1 Organización de directorios y archivos
       (Árbol de carpetas comentado)
   4.2 Módulos y sus responsabilidades
   4.3 Convenciones de nomenclatura usadas
   4.4 Estándares de codificación aplicados
   4.5 Módulos generados con asistencia de IA
       - Identificación de módulos
       - Descripción de los prompts utilizados
       - Validaciones y modificaciones realizadas por ingenieros

5. BASE DE DATOS
   5.1 Motor de base de datos y versión
   5.2 Diagrama Entidad-Relación (DER)
   5.3 Modelo de datos lógico
   5.4 Diccionario de datos
       (Por cada tabla: nombre, descripción, campos, tipos, restricciones)
   5.5 Stored procedures / funciones / triggers
   5.6 Estrategia de indexación
   5.7 Estrategia de respaldo y recuperación

6. APIS E INTEGRACIONES
   6.1 APIs internas expuestas
       (Endpoint | Método | Parámetros | Respuesta | Autenticación)
   6.2 APIs externas consumidas
   6.3 Formatos de intercambio (JSON / XML / etc.)
   6.4 Autenticación y autorización (OAuth, JWT, etc.)
   6.5 Documentación Swagger/OpenAPI (referencia o anexo)

7. INSTALACIÓN Y DESPLIEGUE TÉCNICO
   7.1 Requisitos de infraestructura
   7.2 Prerrequisitos de software en el servidor
   7.3 Variables de entorno y configuración
   7.4 Proceso de build y compilación
   7.5 Proceso de despliegue
       7.5.1 Despliegue en ambiente de desarrollo
       7.5.2 Despliegue en ambiente de pruebas (QA)
       7.5.3 Despliegue en producción
   7.6 Configuración de servidor web / proxy inverso
   7.7 Configuración de certificados SSL/TLS
   7.8 Rollback procedure

8. SEGURIDAD
   8.1 Modelo de seguridad aplicado
   8.2 Gestión de usuarios y roles
   8.3 Manejo de sesiones y tokens
   8.4 Protección contra vulnerabilidades comunes
       (OWASP Top 10 consideraciones)
   8.5 Cifrado de datos en tránsito y en reposo
   8.6 Registro de auditoría (logs de seguridad)

9. RENDIMIENTO Y ESCALABILIDAD
   9.1 Métricas de rendimiento objetivo
   9.2 Estrategia de caché
   9.3 Manejo de concurrencia
   9.4 Estrategia de escalado horizontal / vertical

10. MONITOREO Y OPERACIÓN
    10.1 Herramientas de monitoreo recomendadas
    10.2 Logs del sistema: ubicación y formato
    10.3 Alertas y umbrales críticos
    10.4 Procedimientos de mantenimiento rutinario

11. PRUEBAS
    11.1 Estrategia de pruebas aplicada
    11.2 Pruebas unitarias — cobertura y herramientas
    11.3 Pruebas de integración
    11.4 Pruebas de rendimiento / carga
    11.5 Resultados de pruebas previas al registro
    
APÉNDICES
   Apéndice A — Diagrama de flujo de procesos principales
   Apéndice B — Diagrama de secuencia de casos de uso críticos
   Apéndice C — Registro de decisiones de arquitectura (ADR)
   Apéndice D — Glosario técnico
   Apéndice E — Fragmentos de código con asistencia de IA (identificados)
```

---

## 6. Estructura de la Memoria Técnica

> **Propósito:** Documento clave para el registro de derechos de autor. Describe el proceso creativo e intelectual del desarrollo, justifica la autoría humana y declara explícitamente el uso de IA como herramienta auxiliar. Es el argumento jurídico-técnico de la obra.

---

### MEMORIA TÉCNICA — Estructura Completa

```
MEMORIA TÉCNICA
Registro de Derechos de Autor — Software [Nombre]
Ante: Dirección Nacional de Derechos de Autor (DNDA)

PORTADA
  - Título de la obra: [Nombre del software]
  - Tipo de obra: Programa de computador / Software
  - Versión registrada: [X.X]
  - Fecha de creación: [Fecha de inicio — Fecha de finalización]
  - Autores / Titulares: [Nombres e identificaciones]
  - Naturaleza de la obra: Original / Derivada
  - Fecha del documento: [Fecha]

DECLARACIÓN DE AUTORÍA
  Declaración formal firmada por los ingenieros responsables
  afirmando que el contenido intelectual —incluyendo lógica,
  arquitectura, diseño y dirección del desarrollo— fue
  realizado por personas naturales identificadas, y que
  las herramientas de inteligencia artificial fueron
  utilizadas como instrumentos auxiliares bajo supervisión
  y dirección humana permanente.

TABLA DE CONTENIDO

1. IDENTIFICACIÓN DE LA OBRA
   1.1 Nombre del software
   1.2 Descripción general en lenguaje accesible
       (Qué hace, para qué sirve, a quién beneficia)
   1.3 Tipo y naturaleza de la obra
   1.4 Lenguajes de programación utilizados
   1.5 Plataforma / entorno de ejecución
   1.6 Versión objeto del registro

2. IDENTIFICACIÓN DE LOS AUTORES
   Por cada autor (ingeniero):
   2.N Nombre completo
       Número de identificación
       Rol en el proyecto (cargo / función)
       Descripción específica de su contribución creativa
       Porcentaje o descripción del aporte (si aplica)
   
   Relación con el titular (contrato laboral / encargo / asociación)

3. ORIGEN Y MOTIVACIÓN DEL DESARROLLO
   3.1 Problema que resuelve el software
   3.2 Necesidad u oportunidad que motivó su creación
   3.3 Contexto organizacional o de mercado
   3.4 Fecha de inicio y duración del desarrollo

4. PROCESO CREATIVO E INTELECTUAL
   4.1 Metodología de desarrollo utilizada
   4.2 Fases del desarrollo y decisiones clave tomadas por ingenieros
       - Fase de análisis y levantamiento de requisitos
       - Fase de diseño de arquitectura
       - Fase de diseño de base de datos
       - Fase de diseño de interfaz y experiencia de usuario
       - Fase de codificación
       - Fase de pruebas
       - Fase de despliegue
   4.3 Originalidad de la solución
       (En qué aspectos el software es original o novedoso)
   4.4 Problemas técnicos encontrados y cómo fueron resueltos
       por el equipo de ingeniería

5. USO DE INTELIGENCIA ARTIFICIAL COMO HERRAMIENTA AUXILIAR

   ⚠️ SECCIÓN CRÍTICA PARA EL REGISTRO

   5.1 Declaración sobre el uso de IA
       Declaración explícita de que se utilizaron herramientas
       de IA generativa (especificar cuál: GitHub Copilot,
       ChatGPT, Claude, etc.) durante el proceso de desarrollo,
       exclusivamente como herramientas de asistencia bajo
       la dirección y supervisión de los ingenieros autores.

   5.2 Rol de la IA en el proyecto
       La IA NO tomó decisiones de diseño.
       La IA NO definió la arquitectura.
       La IA NO determinó la lógica de negocio.
       La IA fue utilizada para:
       - Sugerencia de fragmentos de código bajo especificación humana
       - Autocompletado de patrones repetitivos
       - Generación de boilerplate a partir de instrucciones precisas
       - Asistencia en documentación de código
   
   5.3 Control humano ejercido sobre la IA
       - Todos los prompts fueron redactados por ingenieros
       - Todo output de la IA fue revisado y validado manualmente
       - Todo código generado fue comprendido, modificado y adaptado
         por los ingenieros antes de su integración
       - Las decisiones sobre qué generar, cómo integrarlo
         y qué descartar fueron siempre humanas

   5.4 Inventario de módulos con asistencia de IA
   
   | Módulo / Archivo | Herramienta IA | Prompt / Instrucción dada | Modificaciones realizadas por ingeniero | % estimado IA vs. humano |
   |---|---|---|---|---|
   | [módulo_1.py] | [GitHub Copilot] | [Descripción del prompt] | [Qué se modificó] | [20% IA / 80% humano] |
   | [módulo_2.js] | [Claude Sonnet] | [Descripción del prompt] | [Qué se modificó] | [40% IA / 60% humano] |

   5.5 Evidencia de autoría humana
       - Repositorio Git con historial de commits firmados
       - Documentos de diseño previos a la codificación
       - Actas de reunión con decisiones de arquitectura
       - Prompts documentados utilizados con la IA
       - Registro de revisiones de código (code reviews)

6. DESCRIPCIÓN TÉCNICA RESUMIDA DE LA OBRA
   6.1 Arquitectura en términos no técnicos
   6.2 Funcionalidades principales
   6.3 Flujo general del sistema
   6.4 Datos que procesa y produce
   6.5 Integraciones con otros sistemas

7. ORIGINALIDAD Y DIFERENCIACIÓN
   7.1 En qué se diferencia de soluciones existentes
   7.2 Elementos creativos y originales del software
   7.3 Algoritmos o lógicas propias desarrolladas
   7.4 Declaración de que no reproduce código de terceros
       sin licencia

8. LICENCIAS DE TERCEROS INCORPORADAS
   Tabla de componentes open source o de terceros:
   | Biblioteca / Componente | Versión | Licencia | Uso dentro del software |
   |---|---|---|---|
   
   Declaración de cumplimiento con todas las licencias.

9. DERECHOS PATRIMONIALES Y MORALES
   9.1 Identificación del titular de derechos patrimoniales
   9.2 Identificación de los autores (derechos morales — irrenunciables)
   9.3 Términos de uso o licenciamiento previstos para la obra

10. DECLARACIONES FINALES
    Declaración jurada de los autores sobre:
    - La originalidad de la obra
    - La no vulneración de derechos de terceros
    - La autoría humana del contenido creativo
    - El uso instrumental de la IA
    - La veracidad de la información suministrada
    
    Firma de cada autor con fecha

ANEXOS DE LA MEMORIA TÉCNICA
   Anexo 1 — Extracto del código fuente (páginas representativas)
   Anexo 2 — Diagrama de arquitectura
   Anexo 3 — Historial de commits (Git log exportado)
   Anexo 4 — Prompts utilizados con herramientas de IA
   Anexo 5 — Contratos laborales o de prestación de servicios
               que acreditan relación de los autores con el titular
   Anexo 6 — Capturas de pantalla del software en funcionamiento
```

---

## 7. Proceso de Registro Paso a Paso

### Fase 1 — Preparación de Documentos (Semanas 1–3)

```
[ ] Definir titularidad (empresa vs. personas naturales)
[ ] Redactar Memoria Técnica con sección de IA
[ ] Redactar / completar Manual de Usuario
[ ] Redactar / completar Manual Técnico
[ ] Exportar historial Git y preparar código fuente
[ ] Documentar y archivar todos los prompts usados con IA
[ ] Reunir contratos laborales de los ingenieros autores
[ ] Preparar certificado de existencia (si es persona jurídica)
```

### Fase 2 — Revisión Legal (Semana 4)

```
[ ] Revisión por abogado especialista en propiedad intelectual
[ ] Verificar que la Memoria Técnica cubre el argumento de autoría
[ ] Verificar cumplimiento de licencias de componentes de terceros
[ ] Ajustar documentos según observaciones legales
```

### Fase 3 — Radicación ante la DNDA (Semana 5)

```
[ ] Diligenciar formulario oficial de la DNDA
    (disponible en: https://www.derechodeautor.gov.co)
[ ] Pagar tasas de registro (verificar tarifa vigente)
[ ] Radicar física o virtualmente el expediente completo
[ ] Guardar número de radicado
```

### Fase 4 — Seguimiento (Semanas 6–12)

```
[ ] Atender requerimientos adicionales de la DNDA (si los hay)
[ ] Recibir certificado de registro
[ ] Archivar certificado junto con toda la documentación de soporte
[ ] Actualizar headers / comentarios del código con número de registro
```

---

## 8. Checklist Final

### Documentos a entregar a la DNDA

| # | Documento | Estado |
|---|---|---|
| 1 | Formulario de solicitud DNDA | ☐ Pendiente |
| 2 | Código fuente (extracto representativo) | ☐ Pendiente |
| 3 | Memoria Técnica firmada | ☐ Pendiente |
| 4 | Documento de identidad / Cámara de Comercio | ☐ Pendiente |
| 5 | Comprobante de pago de tasas | ☐ Pendiente |

### Documentos de soporte interno

| # | Documento | Estado |
|---|---|---|
| 6 | Manual de Usuario completo | ☐ Pendiente |
| 7 | Manual Técnico completo | ☐ Pendiente |
| 8 | Historial de commits (Git log) | ☐ Pendiente |
| 9 | Archivo de prompts usados con IA | ☐ Pendiente |
| 10 | Contratos laborales de ingenieros | ☐ Pendiente |
| 11 | Actas de decisiones de diseño | ☐ Pendiente |

---

## 9. Notas Importantes sobre IA y Autoría

> Estas consideraciones son fundamentales para blindar el registro ante cualquier cuestionamiento.

**1. Documentar siempre los prompts.**
Cada prompt entregado a una herramienta de IA es evidencia del pensamiento creativo del ingeniero. Guardar capturas o exportaciones de las sesiones.

**2. No exagerar ni minimizar el rol de la IA.**
La declaración debe ser precisa. Indicar correctamente qué porcentaje del código tuvo asistencia de IA y qué modificaciones se hicieron. La honestidad fortalece el registro.

**3. El código revisado y modificado es de autoría humana.**
Incluso si un fragmento fue generado por IA, si el ingeniero lo revisó, entendió, adaptó e integró conscientemente, ese acto creativo es suficiente para la autoría.

**4. La lógica de negocio siempre fue humana.**
Ninguna IA decidió qué debía hacer el software. Esa decisión de alto nivel es el núcleo de la autoría intelectual.

**5. Considerar registro en múltiples jurisdicciones.**
Si el software tiene proyección internacional, evaluar registro simultáneo en países clave. Colombia es miembro del Convenio de Berna (protección automática en 170+ países), pero el registro local es la prueba más sólida.

**6. Actualizar el registro en versiones mayores.**
Cada versión significativa del software puede (y debe) registrarse por separado para proteger las nuevas funcionalidades.

---

*Documento elaborado como plan de trabajo para el equipo de ingeniería y legal.*  
*Adaptar según las especificidades del proyecto y la asesoría jurídica correspondiente.*
