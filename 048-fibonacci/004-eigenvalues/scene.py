from manim import *


class FibonacciEigenvalues(Scene):
    """固有値・固有ベクトルを定義し、フィボナッチ行列の固有値を求める。"""

    def construct(self):
        title = Text("固有値と固有ベクトル", font_size=42, color=BLUE).to_edge(UP)
        conditions = VGroup(
            MathTex(r"A:\ 2\times2", font_size=34),
            Text("行列、", font_size=27),
            MathTex(r"\lambda", font_size=34),
            Text("：実数、", font_size=27),
            MathTex(
                r"\boldsymbol{x}=\begin{pmatrix}x_1\\x_2\end{pmatrix}"
                r"\ne\begin{pmatrix}0\\0\end{pmatrix}",
                font_size=34,
            ),
        ).arrange(RIGHT, buff=0.08).next_to(title, DOWN, buff=0.4)
        definition = MathTex(r"A\boldsymbol{x}=\lambda\boldsymbol{x}", font_size=54).next_to(conditions, DOWN, buff=0.55)
        labels = VGroup(
            VGroup(MathTex(r"\lambda:", color=YELLOW), Text("固有値", font_size=28, color=YELLOW)).arrange(RIGHT, buff=0.12),
            VGroup(MathTex(r"\boldsymbol{x}:", color=GREEN), Text("固有ベクトル", font_size=28, color=GREEN)).arrange(RIGHT, buff=0.12),
        ).arrange(RIGHT, buff=1.2).next_to(definition, DOWN, buff=0.55)
        general = MathTex(r"A=\begin{pmatrix}a&b\\c&d\end{pmatrix}", font_size=42).next_to(labels, DOWN, buff=0.55)
        characteristic = MathTex(r"(\lambda-a)(\lambda-d)-bc=0", font_size=42).next_to(general, DOWN, buff=0.4)
        self.play(Write(title))
        self.play(Write(conditions), Write(definition), Write(labels))  # 下書き7・①
        self.play(Write(general), Write(characteristic))  # 下書き7・②
        self.wait()

        self.play(FadeOut(VGroup(conditions, definition, labels, general, characteristic)))
        subtitle = Text("固有値を求める", font_size=32).next_to(title, DOWN, buff=0.4)
        lines = VGroup(
            MathTex(r"A=\begin{pmatrix}1&1\\1&0\end{pmatrix}"),
            MathTex(r"(\lambda-1)\lambda-1=0"),
            MathTex(r"\lambda^2-\lambda-1=0"),
            MathTex(r"\lambda=\frac{1\pm\sqrt5}{2}"),
        ).arrange(DOWN, buff=0.48).scale(0.95).next_to(subtitle, DOWN, buff=0.45)
        self.play(Write(subtitle), Write(lines[0]))
        for line in lines[1:]:
            self.play(Write(line))
        self.play(Circumscribe(lines[-1], color=YELLOW))
        self.wait(2)
