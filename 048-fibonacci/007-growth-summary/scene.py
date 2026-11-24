from manim import *


class FibonacciGrowthSummary(Scene):
    """フィボナッチ数の一般項の導出を振り返り、ほかの導出方法を紹介する。"""

    def construct(self):
        title = Text("まとめ", font_size=44, color=BLUE).to_edge(UP)
        main_summary = VGroup(
            Text("フィボナッチ数の一般項を", font_size=34),
            Text("正方行列の対角化を使って導きました", font_size=34),
        ).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        main_summary[1].set_color(YELLOW)

        self.play(Write(title))
        self.play(FadeIn(main_summary, shift=UP * 0.25))
        self.wait(10)

        other_methods_title = Text(
            "一般項を導く、ほかの方法", font_size=34, color=YELLOW
        ).next_to(title, DOWN, buff=0.45)
        self.play(
            FadeOut(main_summary),
            FadeIn(other_methods_title, shift=UP * 0.2),
        )

        methods = VGroup(
            self._method_row(
                "母関数を使う方法",
                "『数学ガール』・『The Art of Computer Programming』",
            ),
            self._method_row(
                "ベクトル空間を使う方法",
                "『33の素敵な数学小景』",
            ),
            self._method_row(
                "特性方程式を使う方法",
                "『高校数学の美しい物語』",
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        methods.next_to(other_methods_title, DOWN, buff=0.5)

        self.play(
            LaggedStart(
                *[FadeIn(method, shift=RIGHT * 0.25) for method in methods],
                lag_ratio=0.35,
            )
        )
        self.wait(30)

        self.play(FadeOut(VGroup(other_methods_title, methods)))

        closing = VGroup(
            Text(
                "高評価・チャンネル登録をよろしくお願いします！",
                font_size=35,
                color=YELLOW,
            ),
        ).move_to(ORIGIN)
        self.play(Write(closing))
        self.wait(10)

    @staticmethod
    def _method_row(method, source):
        bullet = Text("•", font_size=30, color=BLUE)
        description = VGroup(
            Text(method, font_size=29),
            Text(source, font_size=22, color=GRAY_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        return VGroup(bullet, description).arrange(
            RIGHT, aligned_edge=UP, buff=0.22
        )
