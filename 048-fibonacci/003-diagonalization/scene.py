from manim import *


class DiagonalizationIdea(Scene):
    """正方行列の対角化と、対角行列のべき乗の利点を説明する。"""

    def construct(self):
        title = Text("正方行列の対角化", font_size=42, color=BLUE).to_edge(UP)
        equation = MathTex(
            r"P^{-1}AP=", r"\begin{pmatrix}\lambda_1&0\\0&\lambda_2\end{pmatrix}",
            font_size=50,
        )
        self.play(Write(title), Write(equation))
        diagonal_box = SurroundingRectangle(equation[1], color=YELLOW)
        label = Text("対角行列", font_size=28, color=YELLOW).next_to(diagonal_box, DOWN)
        self.play(Create(diagonal_box), Write(label))
        self.wait()

        inverse = MathTex(r"P^{-1}P=PP^{-1}=E", r",\qquad E=\begin{pmatrix}1&0\\0&1\end{pmatrix}", font_size=40)
        inverse.next_to(equation, DOWN, buff=0.9)
        self.play(Write(inverse))
        self.wait()
        self.play(FadeOut(diagonal_box), FadeOut(label), FadeOut(inverse), equation.animate.next_to(title, DOWN, buff=0.5))

        power = MathTex(
            r"(P^{-1}AP)^k=P^{-1}A^kP=",
            r"\begin{pmatrix}\lambda_1^k&0\\0&\lambda_2^k\end{pmatrix}",
            font_size=43,
        ).next_to(equation, DOWN, buff=0.8)
        self.play(Write(power))
        self.play(Indicate(power[1], color=GREEN))
        note = Text("行列のべき乗が、数のべき乗になる", font_size=31, color=GREEN).next_to(power, DOWN, buff=0.6)
        self.play(FadeIn(note, shift=UP))
        self.wait(2)

