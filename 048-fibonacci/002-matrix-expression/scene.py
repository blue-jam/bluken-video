from manim import *


class FibonacciMatrixExpression(Scene):
    """フィボナッチ数を行列の累乗で表し、3乗まで確かめる。"""

    def construct(self):
        title = Text("フィボナッチ数の行列表現", font_size=42, color=BLUE).to_edge(UP)
        identity = MathTex(
            r"\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}"
            r"=\underbrace{\begin{pmatrix}1&1\\1&0\end{pmatrix}}_{A}^{\!n}",
            font_size=48,
        )
        self.play(Write(title), Write(identity))
        self.wait()
        self.play(identity.animate.scale(0.72).next_to(title, DOWN, buff=0.4))

        powers = VGroup(
            MathTex(r"A=\begin{pmatrix}1&1\\1&0\end{pmatrix}"),
            MathTex(r"A^2=\begin{pmatrix}1&1\\1&0\end{pmatrix}\begin{pmatrix}1&1\\1&0\end{pmatrix}=\begin{pmatrix}2&1\\1&1\end{pmatrix}"),
            MathTex(r"A^3=A^2A=\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}1&1\\1&0\end{pmatrix}=\begin{pmatrix}3&2\\2&1\end{pmatrix}"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).scale(0.75).next_to(identity, DOWN, buff=0.5)
        for row in powers:
            self.play(Write(row), run_time=1.5)
        box = SurroundingRectangle(powers[-1][-1], color=YELLOW, buff=0.12)
        note = Text("フィボナッチ数が現れる", font_size=27, color=YELLOW).next_to(box, DOWN)
        self.play(Create(box), FadeIn(note))
        self.wait(2)

