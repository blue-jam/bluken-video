# bluken-video

YouTubeチャンネル「ぶるけんプログラミング道場」向けのアルゴリズム・数学動画を [manim](https://www.manim.community/) で制作するリポジトリです。

## ディレクトリ構成

動画はYouTubeに投稿する順番でディレクトリを作成します。

```
<投稿順番号>-<短い動画名>/
```

1本のYouTube動画に複数のシーンが必要な場合は、さらにサブディレクトリを作成します。

```
<投稿順番号>-<短い動画名>/
  <使用順番号>-<短いシーン名>/
    scene.py
```

例:

```
000-example/
  001-hello-manim/
    scene.py
  002-math-basics/
    scene.py
```

## セットアップ

パッケージ管理には [uv](https://docs.astral.sh/uv/) を使います。

```bash
uv sync
```

## 動画のレンダリング

```bash
# 低画質でプレビュー
uv run manim -ql 000-example/001-hello-manim/scene.py HelloManim

# 高画質でレンダリング
uv run manim -qh 000-example/001-hello-manim/scene.py HelloManim
```

レンダリング結果は `media/` ディレクトリに出力されます。
