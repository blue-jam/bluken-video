from manim import *


class FibonacciEigenvectors(Scene):
    """2つの固有値に対応する固有ベクトルと行列Pを求める。"""

    def construct(self):
        title = Text("固有ベクトルを求める", font_size=42, color=BLUE).to_edge(UP)
        lambdas = MathTex(r"\lambda_1=\frac{1+\sqrt5}{2},\qquad\lambda_2=\frac{1-\sqrt5}{2}", font_size=40).next_to(title, DOWN)
        self.play(Write(title), Write(lambdas))

        derivation = VGroup(
            MathTex(r"\begin{pmatrix}1&1\\1&0\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\lambda\begin{pmatrix}x\\y\end{pmatrix}"),
            MathTex(r"x=\lambda y"),
            MathTex(r"\boldsymbol{x}=\begin{pmatrix}\lambda\\1\end{pmatrix}"),
        ).arrange(DOWN, buff=0.42).scale(0.85).next_to(lambdas, DOWN, buff=0.55)
        for line in derivation:
            self.play(Write(line))

        vectors = MathTex(
            r"\boldsymbol{x}_1=\begin{pmatrix}\lambda_1\\1\end{pmatrix},\quad"
            r"\boldsymbol{x}_2=\begin{pmatrix}\lambda_2\\1\end{pmatrix}",
            font_size=40,
        ).next_to(derivation, DOWN, buff=0.55)
        p_matrix = MathTex(
            r"P=(\boldsymbol{x}_1\ \boldsymbol{x}_2)=\begin{pmatrix}\lambda_1&\lambda_2\\1&1\end{pmatrix}",
            font_size=42,
        ).next_to(vectors, DOWN, buff=0.45)
        self.play(Write(vectors))
        self.play(TransformFromCopy(vectors, p_matrix))
        self.play(Circumscribe(p_matrix, color=YELLOW))
        self.wait(2)

