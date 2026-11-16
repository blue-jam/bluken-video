from manim import *


class DeriveBinetFormula(Scene):
    """対角化からAのn乗を計算し、ビネの公式を導く。"""

    def construct(self):
        title = Text("対角化から一般項へ", font_size=42, color=BLUE).to_edge(UP)
        definitions = MathTex(
            r"\alpha=\frac{1+\sqrt5}{2},\quad\beta=\frac{1-\sqrt5}{2},\quad "
            r"P=\begin{pmatrix}\alpha&\beta\\1&1\end{pmatrix}",
            font_size=39,
        ).next_to(title, DOWN)
        self.play(Write(title), Write(definitions))

        inverse = MathTex(
            r"P^{-1}=\frac1{\alpha-\beta}\begin{pmatrix}1&-\beta\\-1&\alpha\end{pmatrix}"
            r"=\frac1{\sqrt5}\begin{pmatrix}1&-\beta\\-1&\alpha\end{pmatrix}",
            font_size=38,
        ).next_to(definitions, DOWN, buff=0.45)
        diagonal = MathTex(r"P^{-1}AP=\begin{pmatrix}\alpha&0\\0&\beta\end{pmatrix}", font_size=41).next_to(inverse, DOWN, buff=0.45)
        self.play(Write(inverse))
        self.play(Write(diagonal))

        an = MathTex(
            r"A^n=P\begin{pmatrix}\alpha^n&0\\0&\beta^n\end{pmatrix}P^{-1}",
            font_size=43,
        ).next_to(diagonal, DOWN, buff=0.48)
        self.play(TransformFromCopy(diagonal, an))
        self.wait()

        entry = MathTex(r"(A^n)_{1,2}=F_n=\frac{\alpha^n-\beta^n}{\sqrt5}", font_size=47).next_to(an, DOWN, buff=0.55)
        self.play(Write(entry))
        self.play(Circumscribe(entry, color=YELLOW))

        bine = MathTex(
            r"F_n=\frac1{\sqrt5}\left\{\left(\frac{1+\sqrt5}{2}\right)^n-\left(\frac{1-\sqrt5}{2}\right)^n\right\}",
            font_size=39,
        ).move_to(entry)
        self.play(ReplacementTransform(entry, bine))
        self.wait(2)

