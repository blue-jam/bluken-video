from manim import *


class FibonacciMatrixExpression(Scene):
    """行列積の仕組みを示し、フィボナッチ行列を3乗まで計算する。"""

    def construct(self):
        title = Text("行列とその掛け算", font_size=42, color=BLUE).to_edge(UP)
        matrix = Matrix([[r"a_{11}", r"a_{12}"], [r"a_{21}", r"a_{22}"]]).scale(0.9).shift(UP * 0.8)
        row_box = SurroundingRectangle(matrix.get_rows()[0], color=RED, buff=0.18)
        column_box = SurroundingRectangle(matrix.get_columns()[1], color=BLUE, buff=0.18)
        row_label = Text("行", color=RED, font_size=28).next_to(row_box, RIGHT)
        column_label = Text("列", color=BLUE, font_size=28).next_to(column_box, DOWN)
        entry_label = Text("成分", color=GREEN, font_size=26).next_to(matrix.get_entries()[3], RIGHT, buff=0.45)
        entry_arrow = Arrow(entry_label.get_left(), matrix.get_entries()[3].get_right(), color=GREEN, buff=0.08)
        self.play(Write(title))
        self.play(Create(matrix), Create(row_box), Create(column_box), Write(row_label), Write(column_label))  # 下書き3・①
        self.play(GrowArrow(entry_arrow), Write(entry_label))
        self.wait()

        self.play(FadeOut(VGroup(matrix, row_box, column_box, row_label, column_label, entry_label, entry_arrow)))
        left_matrix = Matrix(
            [[r"a_{11}", r"a_{12}"], [r"a_{21}", r"a_{22}"]],
            h_buff=1.25,
        ).scale(0.72)
        right_matrix = Matrix(
            [[r"b_{11}", r"b_{12}"], [r"b_{21}", r"b_{22}"]],
            h_buff=1.25,
        ).scale(0.72)
        result_matrix = Matrix([[r"?", r"?"], [r"?", r"?"]], h_buff=1.65).scale(0.72)
        times = MathTex(r"\times", font_size=38)
        equals = MathTex(r"=", font_size=38)
        product = VGroup(left_matrix, times, right_matrix, equals, result_matrix).arrange(RIGHT, buff=0.35)
        product.shift(UP * 0.7)

        guide = Text(
            "左の行と右の列を取り出し、対応する数を掛けて足す",
            font_size=27,
        ).next_to(product, DOWN, buff=0.35)
        self.play(Write(product))  # 下書き3・②
        self.play(Write(guide))

        calculations = [
            (0, 0, r"a_{11}b_{11}", r"a_{12}b_{21}", r"a_{11}b_{11}+a_{12}b_{21}"),
            (0, 1, r"a_{11}b_{12}", r"a_{12}b_{22}", r"a_{11}b_{12}+a_{12}b_{22}"),
            (1, 0, r"a_{21}b_{11}", r"a_{22}b_{21}", r"a_{21}b_{11}+a_{22}b_{21}"),
            (1, 1, r"a_{21}b_{12}", r"a_{22}b_{22}", r"a_{21}b_{12}+a_{22}b_{22}"),
        ]

        for row_index, column_index, first_product, second_product, answer in calculations:
            row = left_matrix.get_rows()[row_index]
            column = right_matrix.get_columns()[column_index]
            result_entry = result_matrix.get_entries()[row_index * 2 + column_index]

            row_box = SurroundingRectangle(row, color=RED, buff=0.12)
            column_box = SurroundingRectangle(column, color=BLUE, buff=0.12)
            result_box = SurroundingRectangle(result_entry, color=GREEN, buff=0.14)
            self.play(Create(row_box), Create(column_box), Create(result_box))

            extracted_row = row.copy()
            extracted_column = column.copy()
            extracted_row.arrange(RIGHT, buff=0.38)
            extracted_column.arrange(DOWN, buff=0.22)
            extracted = VGroup(
                extracted_row,
                MathTex(r"\cdot", font_size=34),
                extracted_column,
            ).arrange(RIGHT, buff=0.35).to_edge(DOWN, buff=0.8).shift(LEFT * 3.7)
            self.play(
                TransformFromCopy(row, extracted_row),
                Write(extracted[1]),
                TransformFromCopy(column, extracted_column),
            )

            calculation = MathTex(
                first_product,
                "+",
                second_product,
                "=",
                answer,
                font_size=31,
            ).next_to(extracted, RIGHT, buff=0.55)
            self.play(Write(calculation[:3]))
            self.play(Write(calculation[3:]))

            answer_in_matrix = MathTex(answer, font_size=31).move_to(result_entry)
            self.play(
                Transform(result_entry, answer_in_matrix),
                Flash(result_box, color=GREEN),
            )
            self.wait(0.35)
            self.play(
                FadeOut(VGroup(row_box, column_box, result_box, extracted, calculation)),
            )

        self.wait()
        self.play(FadeOut(VGroup(product, guide)), FadeOut(title))
        title = Text("フィボナッチ数の行列表現", font_size=40, color=BLUE).to_edge(UP)
        identity = MathTex(
            r"\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}"
            r"=\begin{pmatrix}1&1\\1&0\end{pmatrix}^{n}\quad(n\geq1)",
            font_size=43,
        ).next_to(title, DOWN, buff=0.4)
        square = MathTex(
            r"\begin{pmatrix}1&1\\1&0\end{pmatrix}^{2}=\begin{pmatrix}2&1\\1&1\end{pmatrix}",
            font_size=40,
        ).next_to(identity, DOWN, buff=0.55)
        cube = MathTex(
            r"\begin{pmatrix}1&1\\1&0\end{pmatrix}^{3}="
            r"\begin{pmatrix}1&1\\1&0\end{pmatrix}\begin{pmatrix}2&1\\1&1\end{pmatrix}="
            r"\begin{pmatrix}3&2\\2&1\end{pmatrix}",
            font_size=38,
        ).next_to(square, DOWN, buff=0.5)
        self.play(Write(title), Write(identity))
        self.play(Write(square))  # 下書き4・①
        self.play(Write(cube))  # 下書き4・②
        self.play(Circumscribe(cube[-1], color=YELLOW))
        self.wait(2)
