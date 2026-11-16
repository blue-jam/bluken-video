from manim import *


class FibonacciGrowthSummary(Scene):
    """ビネの公式から指数的増加を読み取り、動画をまとめる。"""

    def construct(self):
        title = Text("一般項からわかること", font_size=42, color=BLUE).to_edge(UP)
        formula = MathTex(r"F_n=\frac{\alpha^n-\beta^n}{\sqrt5}", font_size=50).next_to(title, DOWN, buff=0.45)
        conditions = MathTex(r"\alpha=\frac{1+\sqrt5}{2}>1,\qquad |\beta|=\left|\frac{1-\sqrt5}{2}\right|<1", font_size=39).next_to(formula, DOWN, buff=0.45)
        self.play(Write(title), Write(formula), Write(conditions))

        arrows = VGroup(
            MathTex(r"\alpha^n\longrightarrow\infty", color=GREEN),
            MathTex(r"\beta^n\longrightarrow0", color=RED),
        ).arrange(RIGHT, buff=1.4).next_to(conditions, DOWN, buff=0.65)
        self.play(GrowFromCenter(arrows[0]), GrowFromCenter(arrows[1]))
        conclusion = Text("フィボナッチ数は指数的に増加する", font_size=38, color=YELLOW).next_to(arrows, DOWN, buff=0.65)
        self.play(Write(conclusion))
        self.wait(2)

        self.play(FadeOut(VGroup(formula, conditions, arrows, conclusion)))
        summary = VGroup(
            Text("まとめ", font_size=44, color=YELLOW),
            Text("漸化式 → 行列の累乗", font_size=32),
            Text("固有値・固有ベクトル → 対角化", font_size=32),
            Text("対角行列の n 乗 → ビネの公式", font_size=32),
        ).arrange(DOWN, buff=0.45).move_to(ORIGIN)
        self.play(FadeTransform(title, summary[0]))
        self.play(LaggedStart(*[FadeIn(line, shift=RIGHT * 0.3) for line in summary[1:]], lag_ratio=0.35))
        self.wait(2)
