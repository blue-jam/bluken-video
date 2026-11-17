from manim import *


class FibonacciEigenvectors(Scene):
    """2つの固有値に対応する固有ベクトルと行列Pを求める。"""

    def construct(self):
        title = Text("固有ベクトルを求める", font_size=42, color=BLUE).to_edge(UP)
        known = MathTex(
            r"A=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad"
            r"\lambda=\frac{1\pm\sqrt5}{2}",
            font_size=39,
        ).next_to(title, DOWN, buff=0.4)
        equation = MathTex(
            r"\begin{pmatrix}1&1\\1&0\end{pmatrix}"
            r"\begin{pmatrix}x_1\\x_2\end{pmatrix}="
            r"\frac{1\pm\sqrt5}{2}\begin{pmatrix}x_1\\x_2\end{pmatrix}",
            font_size=41,
        ).next_to(known, DOWN, buff=0.55)
        expanded = MathTex(
            r"\begin{pmatrix}x_1+x_2\\x_1\end{pmatrix}="
            r"\begin{pmatrix}\frac{1\pm\sqrt5}{2}x_1\\\frac{1\pm\sqrt5}{2}x_2\end{pmatrix}",
            font_size=40,
        ).next_to(equation, DOWN, buff=0.5)
        relation = MathTex(r"x_1=\frac{1\pm\sqrt5}{2}x_2", font_size=41).next_to(expanded, DOWN, buff=0.5)
        self.play(Write(title), Write(known))
        self.play(Write(equation))
        self.play(Write(expanded))
        self.play(Write(relation))
        self.wait()

        self.play(FadeOut(VGroup(equation, expanded, relation)))
        choose = VGroup(
            MathTex(r"x_2=1", font_size=37),
            Text("とすれば", font_size=29),
        ).arrange(RIGHT, buff=0.15).next_to(known, DOWN, buff=0.45)
        vectors = MathTex(
            r"\boldsymbol{x}_1=\begin{pmatrix}\frac{1+\sqrt5}{2}\\1\end{pmatrix},\qquad"
            r"\boldsymbol{x}_2=\begin{pmatrix}\frac{1-\sqrt5}{2}\\1\end{pmatrix}",
            font_size=43,
        ).next_to(choose, DOWN, buff=0.55)
        lambdas = MathTex(
            r"\lambda_1=\frac{1+\sqrt5}{2},\qquad\lambda_2=\frac{1-\sqrt5}{2}",
            font_size=38,
        ).next_to(vectors, DOWN, buff=0.45)
        p_matrix = MathTex(
            r"P=(\boldsymbol{x}_1\ \boldsymbol{x}_2)="
            r"\begin{pmatrix}\frac{1+\sqrt5}{2}&\frac{1-\sqrt5}{2}\\1&1\end{pmatrix}",
            font_size=41,
        ).next_to(lambdas, DOWN, buff=0.5)
        self.play(Write(choose))
        self.play(Write(vectors))
        self.play(Write(lambdas))
        self.play(Write(p_matrix))
        self.play(Circumscribe(p_matrix, color=YELLOW))
        self.wait(2)
