# 🌐 언어 선택 / Language Selector

[![简体中文](https://img.shields.io/badge/-简体中文-000000?style=flat-square)](README.md)
[![繁�체中文](https://img.shields.io/badge/-繁體中文-000000?style=flat-square)](README_TC.md)
[![English](https://img.shields.io/badge/-English-000000?style=flat-square)](README_EN.md)
[![日本語](https://img.shields.io/badge/-日本語-000000?style=flat-square)](README_JA.md)
[![한국어](https://img.shields.io/badge/-한국어-000000?style=flat-square)](README_KO.md)
[![Español](https://img.shields.io/badge/-Español-000000?style=flat-square)](README_ES.md)

---

# 📸 ScreenGraph-Vision

### 경량 터미널 화면 캡처 지능형 분석 엔진 | GLM-5.1 멀티모달 지원

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-green.svg)](https://www.python.org/)
[![종속성 없음](https://img.shields.io/badge/종속성-없음-brightgreen.svg)](#빠른-시작)
[![스타](https://img.shields.io/github/stars/gitstq/ScreenGraph-Vision?style=social)](https://github.com/gitstq/ScreenGraph-Vision/stargazers)

> 🎯 **AI에게 "눈"을 부여하고 원클릭으로 모든 스크린샷을 분석하세요!**

---

## 🎉 프로젝트 소개

**ScreenGraph-Vision**은 개발자를 위한**경량 터미널 화면 캡처 지능형 분석 엔진**입니다. Zhipu AI의 GLM-5.1 멀티모달 능력을 기반으로 터미널 환경에서 캡처 분석, UI 요소 인식, 접근성 평가 등을 빠르게 수행할 수 있습니다.

### ✨ 핵심 가치

- 🔍 **지능형 캡처 분석** - 캡처 내용을 자동으로識別하고 상세한 설명을 생성
- 🎨 **UI 요소 인식** - 버튼, 입력 필드, 링크 등의 대화형 요소를 정확하게 위치 파악
- ♿ **접근성 평가** - 색 대비, 텍스트 가독성 등 접근성 지표 분석
- 📊 **차이점 비교** - 두 스크린샷 간의 변화를 지능적으로 비교
- ⚡ **종속성 없음 설계** - 순수 Python 표준 라이브러리로 구현
- 🎮 **TUI 인터페이스** - 세련된 터미널 UI

### 🚀 자체 개발 차별화 포인트

1. **GLM-5.1 네이티브 지원** - Zhipu 최신 멀티모달 LLM과 깊이 통합
2. **터미널 네이티브 경험** - CLI 사용자를 위해 최적화된 TUI 디자인
3. **지능형 캐싱 메커니즘** - 중복 분석을 방지하여 Token 소비 절약
4. **크로스 플랫폼 호환성** - macOS / Linux / Windows 완전 지원
5. **배치 처리 능력** - 디렉토리 일괄 캡처 분석 지원

---

## ✨ 핵심 기능

| 기능 | 설명 |
|------|------|
| 🖼️ **멀티모달 분석** | GLM-5.1의 강력한 시각 이해 능력 기반 |
| 🎯 **UI 요소 인식** | 버튼, 폼, 메뉴 등의 자동 인식 |
| ♿ **접근성 검사** | WCAG 준수 자동 평가 |
| 📊 **차이점 감지** | 스크린샷 변화 지능형 비교 |
| 💾 **지능형 캐싱** | 콘텐츠 해시 기반 로컬 캐시 |
| 🌐 **다국어 지원** | 중국어 / 영어 / 일본어 / 한국어 인터페이스 |
| ⚡ **종속성 없음** | Python 표준 라이브러리만 사용 |
| 🔧 **다중 입력** | 파일 입력 / 캡처 / 클립보드 |

---

## 🚀 빠른 시작

### 환경 요구사항

- 🐍 Python 3.7+
- 🔑 GLM API 키（[Zhipu AI 플랫폼에서 획득](https://open.bigmodel.cn/)）

### 📦 설치 방법

```bash
# 저장소 클론
git clone https://github.com/gitstq/ScreenGraph-Vision.git
cd ScreenGraph-Vision

# 직접 실행
python screengraph.py
```

### 🔧 초기 설정

```bash
# 설정 마법사 실행
python screengraph.py config

# 또는 환경 변수 설정
export GLM_API_KEY="your_api_key_here"
```

### 🚀 기본 사용법

#### 인터랙티브 모드

```bash
python screengraph.py
```

#### 캡처 및 분석

```bash
python screengraph.py capture
```

#### 이미지 파일 분석

```bash
python screengraph.py analyze /path/to/screenshot.png
```

#### 분석 유형 지정

```bash
# 일반 설명 (기본값)
python screengraph.py analyze screenshot.png --type general

# UI 요소 분석
python screengraph.py analyze screenshot.png --type ui

# 접근성 평가
python screengraph.py analyze screenshot.png --type accessibility

# 차이점 비교
python screengraph.py analyze screenshot.png --type diff
```

#### 배치 분석

```bash
python screengraph.py batch /path/to/screenshots/ --pattern "*.png"
```

---

## 🤝 기여하기

Issue 및 Pull Request를 환영합니다!

---

## 📄 오픈소스 라이선스

이 프로젝트는 [MIT 라이선스](LICENSE)로 공개되어 있습니다.

---

<div align="center">

**도움이 되셨다면 ⭐️을 눌러주세요!**

Made with ❤️ by [gitstq](https://github.com/gitstq)

</div>
