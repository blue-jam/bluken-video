from manim import *


class CircleToSquare(Scene):
    """円から正方形への変形アニメーション。manimの基本的な図形変換を示す。"""

    def construct(self):
        circle = Circle(radius=1.5, color=BLUE)
        square = Square(side_length=3, color=GREEN)

        label_circle = Text("円", font_size=36).next_to(circle, DOWN)
        label_square = Text("正方形", font_size=36).next_to(square, DOWN)

        self.play(Create(circle), Write(label_circle))
        self.wait(0.5)

        self.play(
            Transform(circle, square),
            Transform(label_circle, label_square),
        )
        self.wait(1)

        self.play(FadeOut(circle), FadeOut(label_circle))
