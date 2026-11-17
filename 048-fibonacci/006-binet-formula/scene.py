from manim import *


class DeriveBinetFormula(Scene):
    """対角化の計算を画面ごとに差し替え、ビネの公式を導く。"""

    def construct(self):
        title = Text("対角化", font_size=42, color=BLUE).to_edge(UP)
        a_matrix = MathTex(r"A=\begin{pmatrix}1&1\\1&0\end{pmatrix}", font_size=38)
        p_matrix = MathTex(
            r"P=\begin{pmatrix}\frac{1+\sqrt5}{2}&\frac{1-\sqrt5}{2}\\1&1\end{pmatrix}",
            font_size=38,
        )
        givens = VGroup(a_matrix, p_matrix).arrange(RIGHT, buff=1.0).next_to(title, DOWN, buff=0.4)

        inverse_rule = MathTex(
            r"\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}="
            r"\frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}",
            font_size=39,
        ).next_to(givens, DOWN, buff=0.55)
        inverse = MathTex(
            r"P^{-1}=\frac1{\sqrt5}"
            r"\begin{pmatrix}1&-\frac{1-\sqrt5}{2}\\-1&\frac{1+\sqrt5}{2}\end{pmatrix}",
            font_size=42,
        ).next_to(inverse_rule, DOWN, buff=0.65)
        self.play(Write(title), Write(givens))
        self.play(Write(inverse_rule))
        self.play(Write(inverse))
        self.wait()

        # 同じ「対角化」の下書き12。前の計算を消して、同時表示量を抑える。
        self.play(FadeOut(inverse_rule), inverse.animate.next_to(givens, DOWN, buff=0.45).scale(0.88))
        diagonal = MathTex(
            r"P^{-1}AP=\begin{pmatrix}\frac{1+\sqrt5}{2}&0\\0&\frac{1-\sqrt5}{2}\end{pmatrix}",
            font_size=40,
        ).next_to(inverse, DOWN, buff=0.45)
        power_identity = MathTex(
            r"(P^{-1}AP)^n=P^{-1}A^nP",
            font_size=39,
        ).next_to(diagonal, DOWN, buff=0.45)
        diagonal_power = MathTex(
            r"P^{-1}A^nP="
            r"\begin{pmatrix}"
            r"\left(\frac{1+\sqrt5}{2}\right)^n&0\\"
            r"0&\left(\frac{1-\sqrt5}{2}\right)^n"
            r"\end{pmatrix}",
            font_size=38,
        ).next_to(power_identity, DOWN, buff=0.4)
        self.play(Write(diagonal))
        self.play(Write(power_identity))
        self.play(Write(diagonal_power))
        self.wait()

        # 下書き13: A^n=P D^n P^{-1} を展開する。
        self.play(FadeOut(VGroup(givens, inverse, diagonal, power_identity, diagonal_power)))
        title2 = Text("公式を導く", font_size=42, color=BLUE).to_edge(UP)
        relation = MathTex(
            r"A^n=P"
            r"\begin{pmatrix}\alpha^n&0\\0&\beta^n\end{pmatrix}P^{-1}",
            font_size=48,
        ).next_to(title2, DOWN, buff=0.5)
        definitions = MathTex(
            r"\alpha=\frac{1+\sqrt5}{2},\qquad\beta=\frac{1-\sqrt5}{2}",
            font_size=39,
        ).next_to(relation, DOWN, buff=0.45)
        product = MathTex(
            r"A^n=\frac1{\sqrt5}"
            r"\begin{pmatrix}\alpha^{n+1}&\beta^{n+1}\\\alpha^n&\beta^n\end{pmatrix}"
            r"\begin{pmatrix}1&-\beta\\-1&\alpha\end{pmatrix}",
            font_size=41,
        ).next_to(definitions, DOWN, buff=0.65)
        self.play(ReplacementTransform(title, title2))
        self.play(Write(relation), Write(definitions))
        self.play(Write(product))
        self.wait()

        # 下書き14: 積を計算し、1行2列成分だけを取り出す。
        expanded = MathTex(
            r"A^n=\frac1{\sqrt5}\begin{pmatrix}"
            r"\alpha^{n+1}-\beta^{n+1}&-\beta\alpha^{n+1}+\alpha\beta^{n+1}\\"
            r"\alpha^n-\beta^n&-\beta\alpha^n+\alpha\beta^n"
            r"\end{pmatrix}",
            font_size=34,
        ).move_to(product)
        self.play(ReplacementTransform(product, expanded))
        self.wait()

        entry = MathTex(r"F_n=(A^n)_{1,2}=\frac{\alpha^n-\beta^n}{\sqrt5}", font_size=47)
        entry.next_to(expanded, DOWN, buff=0.6)
        self.play(Write(entry))
        self.play(Circumscribe(entry, color=YELLOW))

        bine = MathTex(
            r"F_n=\frac1{\sqrt5}\left\{\left(\frac{1+\sqrt5}{2}\right)^n-"
            r"\left(\frac{1-\sqrt5}{2}\right)^n\right\}",
            font_size=43,
        ).move_to(ORIGIN)
        self.play(FadeOut(VGroup(expanded, relation, definitions, entry)), title2.animate.to_edge(UP))
        self.play(Write(bine))
        self.play(Circumscribe(bine, color=YELLOW))
        self.wait(2)
