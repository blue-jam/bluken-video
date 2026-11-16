# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

YouTubeチャンネル「ぶるけんプログラミング道場」向けのアルゴリズム・数学動画を [manim](https://www.manim.community/) で制作するリポジトリ。

## セットアップ

```bash
uv sync
```

## 動画のレンダリング

```bash
# 低画質でプレビュー（開発時）
uv run manim -ql <path>/scene.py <ClassName>

# 高画質でレンダリング（本番）
uv run manim -qh <path>/scene.py <ClassName>
```

レンダリング結果は `media/` ディレクトリに出力される。

## ディレクトリ構成

動画はYouTube投稿順番号でディレクトリを作成する:

```
<投稿順番号>-<短い動画名>/
  <使用順番号>-<短いシーン名>/
    scene.py
  script.md   # 動画スクリプト（必要に応じて）
```

各 `scene.py` は `manim.Scene` を継承したクラスを定義し、`construct()` メソッドにアニメーションを記述する。

## コード規約

- 各シーンクラスにdocstringでシーンの概要を記述する
- 日本語テキストをアニメーション内に使用する（`Text()`、`MathTex()` など）
- シーンファイルは1ファイルに1シーンクラスを基本とする
