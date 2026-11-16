from manim import *


class FibonacciEigenvalues(Scene):
    """フィボナッチ行列の固有値を特性方程式から求める。"""

    def construct(self):
        title = Text("固有値を求める", font_size=42, color=BLUE).to_edge(UP)
        definition = MathTex(r"A\boldsymbol{x}=\lambda\boldsymbol{x}\quad(\boldsymbol{x}\ne\boldsymbol{0})", font_size=46)
        self.play(Write(title), Write(definition))
        self.wait()
        self.play(definition.animate.scale(0.78).next_to(title, DOWN))

        lines = VGroup(
            MathTex(r"A=\begin{pmatrix}1&1\\1&0\end{pmatrix}"),
            MathTex(r"(\lambda-a)(\lambda-d)-bc=0"),
            MathTex(r"(\lambda-1)\lambda-1=0"),
            MathTex(r"\lambda^2-\lambda-1=0"),
            MathTex(r"\lambda_1=\frac{1+\sqrt5}{2},\qquad\lambda_2=\frac{1-\sqrt5}{2}"),
        ).arrange(DOWN, buff=0.34).scale(0.86).next_to(definition, DOWN, buff=0.45)
        for previous, current in zip(lines, lines[1:]):
            if previous is lines[0]:
                self.play(Write(previous))
            self.play(TransformFromCopy(previous, current))
        result_box = SurroundingRectangle(lines[-1], color=YELLOW, buff=0.14)
        self.play(Create(result_box))
        self.wait(2)

