from manim import *


class FibonacciIntroduction(Scene):
    """フィボナッチ数列、漸化式、ビネの公式を下書き順に紹介する。"""

    def construct(self):
        title = Text("フィボナッチ数の一般項を\n線形代数で導く", font_size=54, line_spacing=1.15)
        self.play(Write(title))
        self.wait()
        self.play(title.animate.scale(0.64).to_edge(UP))

        sequence = MathTex(r"0,\ 1,\ 1,\ 2,\ 3,\ 5,\ 8,\ 13,\ 21,\ldots", font_size=48)
        sequence.next_to(title, DOWN, buff=0.65)
        recurrence = MathTex(
            r"\begin{cases}F_0=0,\quad F_1=1\\F_{n+2}=F_n+F_{n+1}\quad(n\geq0)\end{cases}",
            font_size=43,
        ).next_to(sequence, DOWN, buff=0.75)
        self.play(Write(sequence))  # 下書き1・①
        self.play(Write(recurrence))  # 下書き1・②
        self.wait()

        self.play(FadeOut(sequence), FadeOut(recurrence))
        heading = Text("フィボナッチ数の一般項（ビネの公式）", font_size=34).next_to(title, DOWN, buff=0.5)
        formula = MathTex(
            r"F_n=\frac1{\sqrt5}\left\{\left(\frac{1+\sqrt5}{2}\right)^n-"
            r"\left(\frac{1-\sqrt5}{2}\right)^n\right\}",
            font_size=47,
        ).next_to(heading, DOWN, buff=0.55)
        formula.set_color_by_tex(r"\sqrt5", YELLOW)
        policy = Text("大学で勉強する線形代数を使って、導いてみよう！", font_size=34, color=BLUE)
        policy.next_to(formula, DOWN, buff=0.9)
        self.play(Write(heading), Write(formula))  # 下書き2・①
        self.play(FadeIn(policy, shift=UP * 0.2))  # 下書き2・②
        self.wait(2)
