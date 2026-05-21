# 🌐 Selector de idioma / 语言切换

[![简体中文](https://img.shields.io/badge/-简体中文-000000?style=flat-square)](README.md)
[![繁體中文](https://img.shields.io/badge/-繁體中文-000000?style=flat-square)](README_TC.md)
[![English](https://img.shields.io/badge/-English-000000?style=flat-square)](README_EN.md)
[![日本語](https://img.shields.io/badge/-日本語-000000?style=flat-square)](README_JA.md)
[![한국어](https://img.shields.io/badge/-한국어-000000?style=flat-square)](README_KO.md)
[![Español](https://img.shields.io/badge/-Español-000000?style=flat-square)](README_ES.md)

---

# 📸 ScreenGraph-Vision

### Motor de Análisis Inteligente de Capturas de Pantalla para Terminal Ligero | Potenciado por GLM-5.1 Multimodal

[![Licencia MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-green.svg)](https://www.python.org/)
[![Sin dependencias](https://img.shields.io/badge/dependencias-cero-brightgreen.svg)](#inicio-rápido)
[![Estrellas](https://img.shields.io/github/stars/gitstq/ScreenGraph-Vision?style=social)](https://github.com/gitstq/ScreenGraph-Vision/stargazers)

> 🎯 **¡Dale ojos a la IA - Analiza cualquier captura de pantalla con un clic!**

---

## 🎉 Introducción del Proyecto

**ScreenGraph-Vision** es un **motor de análisis inteligente de capturas de pantalla basado en terminal** diseñado específicamente para desarrolladores. Potenciado por las capacidades multimodales de GLM-5.1 de Zhipu AI, permite a los usuarios realizar rápidamente análisis de capturas, reconocimiento de elementos UI, evaluación de accesibilidad y más directamente en el entorno terminal.

### ✨ Valores Centrales

- 🔍 **Análisis Inteligente de Capturas** - Identificación automática del contenido de la captura
- 🎨 **Reconocimiento de Elementos UI** - Localización precisa de botones, campos de entrada, enlaces
- ♿ **Evaluación de Accesibilidad** - Análisis de contraste de color, legibilidad del texto
- 📊 **Comparación de Diferencias** - Comparación inteligente de cambios entre capturas
- ⚡ **Diseño Sin Dependencias** - Implementación pura con biblioteca estándar de Python
- 🎮 **Interfaz TUI Interactiva** - Interfaz de usuario de terminal elegante

### 🚀 Puntos Diferenciales de Desarrollo Propio

1. **Soporte Nativo GLM-5.1** - Integración profunda con el último LLM multimodal de Zhipu
2. **Experiencia Nativa de Terminal** - Diseño TUI optimizado para usuarios CLI
3. **Mecanismo de Caché Inteligente** - Evita análisis duplicados, ahorra consumo de Token
4. **Compatibilidad Multiplataforma** - Soporte completo para macOS / Linux / Windows
5. **Capacidad de Procesamiento por Lotes** - Soporte para análisis de capturas por directorio

---

## ✨ Características Principales

| Característica | Descripción |
|----------------|-------------|
| 🖼️ **Análisis Multimodal** | Potenciado por GLM-5.1 |
| 🎯 **Reconocimiento de Elementos UI** | Identificación automática de botones, formularios, menús |
| ♿ **Verificación de Accesibilidad** | Evaluación automática de cumplimiento WCAG |
| 📊 **Detección de Diferencias** | Comparación inteligente de cambios |
| 💾 **Caché Inteligente** | Caché local basado en hash de contenido |
| 🌐 **Soporte Multiidioma** | Interfaz en Chino / Inglés / Japonés / Coreano |
| ⚡ **Sin Dependencias** | Solo biblioteca estándar de Python |
| 🔧 **Múltiples Entradas** | Archivo / Captura / Portapapeles |

---

## 🚀 Inicio Rápido

### Requisitos

- 🐍 Python 3.7+
- 🔑 Clave API GLM（[Obtener en Zhipu AI Platform](https://open.bigmodel.cn/)）

### 📦 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/gitstq/ScreenGraph-Vision.git
cd ScreenGraph-Vision

# Ejecutar directamente
python screengraph.py
```

### 🔧 Configuración Inicial

```bash
# Ejecutar asistente de configuración
python screengraph.py config

# O establecer variable de entorno
export GLM_API_KEY="your_api_key_here"
```

### 🚀 Uso Básico

#### Modo Interactivo

```bash
python screengraph.py
```

#### Capturar y Analizar

```bash
python screengraph.py capture
```

#### Analizar Archivo de Imagen

```bash
python screengraph.py analyze /ruta/a/captura.png
```

#### Especificar Tipo de Análisis

```bash
# Descripción general (predeterminado)
python screengraph.py analyze captura.png --type general

# Análisis de elementos UI
python screengraph.py analyze captura.png --type ui

# Evaluación de accesibilidad
python screengraph.py analyze captura.png --type accessibility

# Comparación de diferencias
python screengraph.py analyze captura.png --type diff
```

#### Análisis por Lotes

```bash
python screengraph.py batch /ruta/a/capturas/ --pattern "*.png"
```

---

## 🤝 Contribuir

¡Damos la bienvenida a Issues y Pull Requests!

---

## 📄 Licencia de Código Abierto

Este proyecto es de código abierto bajo la [Licencia MIT](LICENSE).

---

<div align="center">

**Si te ayuda, ¡danos una ⭐️!**

Hecho con ❤️ por [gitstq](https://github.com/gitstq)

</div>
