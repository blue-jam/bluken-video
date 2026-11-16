from manim import *


class FibonacciIntroduction(Scene):
    """フィボナッチ数列とビネの公式を紹介する。"""

    def construct(self):
        title = Text("フィボナッチ数の公式を\n線形代数で導く", font_size=52, line_spacing=1.2)
        title.set_color_by_gradient(BLUE, TEAL)
        self.play(Write(title))
        self.wait()
        self.play(title.animate.scale(0.62).to_edge(UP))

        sequence = MathTex(
            r"0,\ 1,\ 1,\ 2,\ 3,\ 5,\ 8,\ 13,\ 21,\ldots",
            font_size=50,
        )
        braces = MathTex(
            r"\begin{cases}F_0=0,\quad F_1=1\\F_{n+2}=F_n+F_{n+1}\quad(n\geq0)\end{cases}",
            font_size=42,
        ).next_to(sequence, DOWN, buff=0.7)
        self.play(LaggedStart(*[FadeIn(x, shift=UP * 0.15) for x in sequence], lag_ratio=0.07))
        self.play(Write(braces))
        self.wait()

        bine = MathTex(
            r"F_n=\frac1{\sqrt5}\left\{\left(\frac{1+\sqrt5}{2}\right)^n-\left(\frac{1-\sqrt5}{2}\right)^n\right\}",
            font_size=42,
        )
        bine.set_color_by_tex(r"\sqrt5", YELLOW)
        label = Text("ビネの公式", font_size=30, color=YELLOW).next_to(bine, DOWN)
        self.play(FadeOut(sequence), FadeOut(braces), FadeIn(bine, shift=UP), Write(label))
        self.play(Circumscribe(bine, color=YELLOW))
        self.wait(2)

