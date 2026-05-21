# 🌐 言語選択 / Language Selector

[![简体中文](https://img.shields.io/badge/-简体中文-000000?style=flat-square)](README.md)
[![繁體中文](https://img.shields.io/badge/-繁體中文-000000?style=flat-square)](README_TC.md)
[![English](https://img.shields.io/badge/-English-000000?style=flat-square)](README_EN.md)
[![日本語](https://img.shields.io/badge/-日本語-000000?style=flat-square)](README_JA.md)
[![한국어](https://img.shields.io/badge/-한국어-000000?style=flat-square)](README_KO.md)
[![Español](https://img.shields.io/badge/-Español-000000?style=flat-square)](README_ES.md)

---

# 📸 ScreenGraph-Vision

### 軽量ターミナル画面キャプチャ知的分析エンジン | GLM-5.1 マルチモーダル対応

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-green.svg)](https://www.python.org/)
[![依存関係ゼロ](https://img.shields.io/badge/依存関係-ゼロ-brightgreen.svg)](#クイックスタート)
[![スター](https://img.shields.io/github/stars/gitstq/ScreenGraph-Vision?style=social)](https://github.com/gitstq/ScreenGraph-Vision/stargazers)

> 🎯 **AIに「目」を与えワンクリックで任意のスクリーンショットを分析！**

---

## 🎉 プロジェクト紹介

**ScreenGraph-Vision** は開発者向けに設計された**軽量ターミナル画面キャプチャ知的分析エンジン**です。Zhipu AI の GLM-5.1 マルチモーダル能力を基盤に、ターミナル環境下でキャプチャ分析、UI要素認識、アクセシビリティ評価などを素早く実行できます。

### ✨ コアバリュー

- 🔍 **知的キャプチャ分析** - キャプチャ内容を自動識別し、詳細な説明文章を生成
- 🎨 **UI要素認識** - ボタン、入力フィールド、リンクなどのインタラクティブ要素を正確に検出
- ♿ **アクセシビリティ評価** - 色のコントラスト、テキスト読み取りやすさの分析
- 📊 **差分比較** - 2つのキャプチャの変化を智能的に比較
- ⚡ **ゼロ依存設計** - ピュアPython標準ライブラリ実装
- 🎮 **TUIインターフェース** - エレガントなターミナルUI

### 🚀 独自開発の差別化ポイント

1. **GLM-5.1ネイティブサポート** - Zhipu最新のマルチモーダルLLMと深層統合
2. **ターミナルネイティブ体験** - CLIユーザー向けに最適化されたTUIデザイン
3. **知的キャッシュ機構** - 重複分析を回避しToken消費を節約
4. **クロスプラットフォーム互換** - macOS / Linux / Windows完全対応
5. **バッチ処理能力** - ディレクトリ一括キャプチャ分析をサポート

---

## ✨ コア機能

| 機能 | 説明 |
|------|------|
| 🖼️ **マルチモーダル分析** | GLM-5.1の強大な視覚理解能力を基盤 |
| 🎯 **UI要素認識** - ボタン、フォーム、メニューなどの自動識別 |
| ♿ **アクセシビリティチェック** | WCAG準拠の自動評価 |
| 📊 **差分検出** | キャプチャ変化の智能比較 |
| 💾 **知的キャッシュ** | コンテンツハッシュベースのローカルキャッシュ |
| 🌐 **多言語サポート** | 中国語 / 英語 / 日本語 / 韓国語インターフェース |
| ⚡ **ゼロ依存** | Python標準ライブラリのみ |
| 🔧 **複数入力方式** | ファイル入力 / キャプチャ / クリップボード |

---

## 🚀 クイックスタート

### 環境要件

- 🐍 Python 3.7+
- 🔑 GLM APIキー（[Zhipu AIプラットフォームで取得](https://open.bigmodel.cn/)）

### 📦 インストール方法

#### 方法1：直接実行（推奨）

```bash
# リポジトリをクローン
git clone https://github.com/gitstq/ScreenGraph-Vision.git
cd ScreenGraph-Vision

# 直接実行
python screengraph.py
```

#### 方法2：CLIツールとしてインストール

```bash
# インストール
pip install -e .

# グローバルで使用
screengraph interactive
```

#### 方法3：pipインストール

```bash
pip install screengraph-vision
```

### 🔧 初期設定

```bash
# 設定ウィザードを実行
python screengraph.py config

# または環境変数を設定
export GLM_API_KEY="your_api_key_here"
```

### 🚀 基本使用方法

#### インタラクティブモード（初心者向け）

```bash
python screengraph.py
```

#### キャプチャして分析

```bash
python screengraph.py capture
```

#### 画像ファイルを分析

```bash
python screengraph.py analyze /path/to/screenshot.png
```

#### 分析タイプを指定

```bash
# 一般説明（デフォルト）
python screengraph.py analyze screenshot.png --type general

# UI要素分析
python screengraph.py analyze screenshot.png --type ui

# アクセシビリティ評価
python screengraph.py analyze screenshot.png --type accessibility

# 差分比較
python screengraph.py analyze screenshot.png --type diff
```

#### バッチ分析

```bash
python screengraph.py batch /path/to/screenshots/ --pattern "*.png"
```

---

## 📖 詳細な使用方法

### 🎯 分析モードの詳細

#### 1. 一般説明モード (general)

キャプチャ内容を自動分析し詳細な説明文章を生成：

```
入力: 任意のキャプチャ
出力:
- 主要コンテンツ概要
- 重要情報の抽出
- レイアウト構造の説明
- カラースタイル分析
```

#### 2. UI要素分析モード (ui)

インターフェース内のインタラクティブ要素を正確に識別：

```
入力: UIキャプチャ
出力:
- ボタンリスト（位置 + 名前）
- 入力フィールドリスト
- リンクリスト
- メニュー項目リスト
- アイコンボタン説明
```

#### 3. アクセシビリティ評価モード (accessibility)

インターフェースのアクセシビリティ機能をチェック：

```
入力: 任意のインターフェースキャプチャ
出力:
- 主要機能説明
- テキスト読み取りやすさスコア
- カラーコントラスト分析
- 潜在的な問題リスト
- 改善提案
```

#### 4. 差分比較モード (diff)

2つのキャプチャの変化を比較：

```
入力: 現在のキャプチャ + 過去のキャプチャ
出力:
- 新規要素
- 削除された要素
- 変化した要素
- レイアウト変更の説明
```

---

## 🤝 コントリビューション

IssueとPull Requestの提出を歓迎します！

---

## 📄 オープンソースライセンス

このプロジェクトは [MIT License](LICENSE) で公開されています。

---

<div align="center">

**参考になったら⭐️をください！**

Made with ❤️ by [gitstq](https://github.com/gitstq)

</div>
