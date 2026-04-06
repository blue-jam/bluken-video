from manim import *


class HelloManim(Scene):
    """manimの基本的な使い方を示すシーン。テキストを表示して動かす。"""

    def construct(self):
        title = Text("ぶるけんプログラミング道場", font_size=48)
        subtitle = Text("アルゴリズム・数学", font_size=32, color=BLUE)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(1)

        self.play(FadeOut(title), FadeOut(subtitle))
