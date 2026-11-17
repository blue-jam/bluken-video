from manim import *


class FibonacciMatrixExpression(Scene):
    """行列積の仕組みを示し、フィボナッチ行列を3乗まで計算する。"""

    def construct(self):
        title = Text("行列とその掛け算", font_size=42, color=BLUE).to_edge(UP)
        matrix = Matrix(
            [[r"a_{11}", r"a_{12}"], [r"a_{21}", r"a_{22}"]],
            left_bracket="(",
            right_bracket=")",
        ).scale(0.9).shift(UP * 0.8)
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
            left_bracket="(",
            right_bracket=")",
        ).scale(0.72)
        right_matrix = Matrix(
            [[r"b_{11}", r"b_{12}"], [r"b_{21}", r"b_{22}"]],
            left_bracket="(",
            right_bracket=")",
        ).scale(0.72)
        result_matrix = Matrix(
            [
                [r"a_{11}b_{11}+a_{12}b_{21}", r"a_{11}b_{12}+a_{12}b_{22}"],
                [r"a_{21}b_{11}+a_{22}b_{21}", r"a_{21}b_{12}+a_{22}b_{22}"],
            ],
            h_buff=4.3,
            left_bracket="(",
            right_bracket=")",
        ).scale(0.72)
        # 最終結果を透明なプレースホルダーにして、最初から必要な列幅を確保する。
        result_matrix.get_entries().set_opacity(0)
        equals = MathTex(r"=", font_size=38)
        product = VGroup(left_matrix, right_matrix, equals, result_matrix).arrange(RIGHT, buff=0.35)
        product.shift(UP * 0.7)

        guide = Text(
            "左の行と右の列を取り出し、対応する数を掛けて足す",
            font_size=27,
        ).next_to(product, DOWN, buff=0.35)
        self.play(Write(product))  # 下書き3・②
        self.play(Write(guide))

        calculations = [
            (0, 0, r"a_{11}", r"b_{11}", r"a_{12}", r"b_{21}"),
            (0, 1, r"a_{11}", r"b_{12}", r"a_{12}", r"b_{22}"),
            (1, 0, r"a_{21}", r"b_{11}", r"a_{22}", r"b_{21}"),
            (1, 1, r"a_{21}", r"b_{12}", r"a_{22}", r"b_{22}"),
        ]
        displayed_answers = VGroup()

        for row_index, column_index, first_a, first_b, second_a, second_b in calculations:
            row = left_matrix.get_rows()[row_index]
            column = right_matrix.get_columns()[column_index]
            result_entry = result_matrix.get_entries()[row_index * 2 + column_index]

            row_box = SurroundingRectangle(row, color=RED, buff=0.12)
            column_box = SurroundingRectangle(column, color=BLUE, buff=0.12)
            result_box = SurroundingRectangle(result_entry, color=GREEN, buff=0.14)
            self.play(Create(row_box), Create(column_box), Create(result_box))

            # 完成形を先に組んで各項の位置を決める。表示はコピーした項だけにする。
            expression_layout = MathTex(
                first_a,
                first_b,
                "+",
                second_a,
                second_b,
                font_size=31,
            ).next_to(guide, DOWN, buff=0.35)
            row_terms = VGroup(
                MathTex(first_a, font_size=31).move_to(expression_layout[0]),
                MathTex(second_a, font_size=31).move_to(expression_layout[3]),
            )
            self.play(
                TransformFromCopy(row[0], row_terms[0]),
                TransformFromCopy(row[1], row_terms[1]),
            )

            column_terms = VGroup(
                MathTex(first_b, font_size=31).move_to(expression_layout[1]),
                MathTex(second_b, font_size=31).move_to(expression_layout[4]),
            )
            self.play(
                TransformFromCopy(column[0], column_terms[0]),
                TransformFromCopy(column[1], column_terms[1]),
            )

            plus = expression_layout[2].copy()
            self.play(Write(plus))

            answer_in_matrix = result_entry.copy().set_opacity(1)
            calculation = VGroup(row_terms, column_terms, plus)
            self.play(
                TransformFromCopy(calculation, answer_in_matrix),
                Flash(result_box, color=GREEN),
            )
            displayed_answers.add(answer_in_matrix)
            self.wait(0.35)
            self.play(
                FadeOut(
                    VGroup(
                        row_box,
                        column_box,
                        result_box,
                        row_terms,
                        column_terms,
                        plus,
                    )
                ),
            )

        self.wait()
        self.play(FadeOut(VGroup(product, guide, displayed_answers)), FadeOut(title))
        title = Text("フィボナッチ数の行列表現", font_size=40, color=BLUE).to_edge(UP)
        identity = MathTex(
            r"\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}"
            r"=\begin{pmatrix}1&1\\1&0\end{pmatrix}^{n}\quad(n\geq1)",
            font_size=43,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(title), Write(identity))

        def animate_numeric_product(obj, power, left_values, right_values, result_values):
            """行と列を順に取り出して、数値行列の積を1成分ずつ計算する。"""
            power_label = MathTex(rf"A^{power}=", font_size=38)
            left = Matrix(left_values, left_bracket="(", right_bracket=")").scale(0.72)
            right = Matrix(right_values, left_bracket="(", right_bracket=")").scale(0.72)
            equals = MathTex("=", font_size=38)
            result = Matrix(
                result_values,
                left_bracket="(",
                right_bracket=")",
            ).scale(0.72)
            result.get_entries().set_opacity(0)
            equation = VGroup(power_label, left, right, equals, result).arrange(RIGHT, buff=0.3)
            equation.next_to(obj, DOWN, buff=0.55)

            self.play(Write(power_label))
            # A^2 を A・A に、A^3 を A・A^2 に分ける段階を明示する。
            self.play(Write(left), Write(right), Write(equals), Write(result.get_brackets()))

            answers = VGroup()
            for row_index in range(2):
                for column_index in range(2):
                    row = left.get_rows()[row_index]
                    column = right.get_columns()[column_index]
                    result_entry = result.get_entries()[row_index * 2 + column_index]
                    first_a = left_values[row_index][0]
                    first_b = right_values[0][column_index]
                    second_a = left_values[row_index][1]
                    second_b = right_values[1][column_index]
                    answer = result_values[row_index][column_index]

                    row_box = SurroundingRectangle(row, color=RED, buff=0.12)
                    column_box = SurroundingRectangle(column, color=BLUE, buff=0.12)
                    result_box = SurroundingRectangle(result_entry, color=GREEN, buff=0.12)
                    self.play(Create(row_box), Create(column_box), Create(result_box))

                    expression_layout = MathTex(
                        str(first_a),
                        r"\cdot",
                        str(first_b),
                        "+",
                        str(second_a),
                        r"\cdot",
                        str(second_b),
                        "=",
                        str(answer),
                        font_size=34,
                    ).next_to(equation, DOWN, buff=0.75)
                    row_terms = VGroup(
                        MathTex(str(first_a), font_size=34).move_to(expression_layout[0]),
                        MathTex(str(second_a), font_size=34).move_to(expression_layout[4]),
                    )
                    self.play(
                        TransformFromCopy(row[0], row_terms[0]),
                        TransformFromCopy(row[1], row_terms[1]),
                    )

                    column_terms = VGroup(
                        MathTex(str(first_b), font_size=34).move_to(expression_layout[2]),
                        MathTex(str(second_b), font_size=34).move_to(expression_layout[6]),
                    )
                    multiplication_dots = VGroup(
                        expression_layout[1].copy(),
                        expression_layout[5].copy(),
                    )
                    self.play(
                        TransformFromCopy(column[0], column_terms[0]),
                        TransformFromCopy(column[1], column_terms[1]),
                        Write(multiplication_dots),
                    )

                    plus = expression_layout[3].copy()
                    self.play(Write(plus))
                    equals_and_answer = VGroup(
                        expression_layout[7].copy(),
                        expression_layout[8].copy(),
                    )
                    self.play(Write(equals_and_answer))

                    answer_in_matrix = result_entry.copy().set_opacity(1)
                    self.play(
                        TransformFromCopy(equals_and_answer[1], answer_in_matrix),
                        Flash(result_box, color=GREEN),
                    )
                    answers.add(answer_in_matrix)
                    self.play(
                        FadeOut(
                            VGroup(
                                row_box,
                                column_box,
                                result_box,
                                row_terms,
                                column_terms,
                                multiplication_dots,
                                plus,
                                equals_and_answer,
                            )
                        )
                    )

            self.play(Circumscribe(VGroup(result.get_brackets(), answers), color=YELLOW))
            self.wait(0.5)
            return VGroup(equation, answers)

        square = animate_numeric_product(identity, 2, [[1, 1], [1, 0]], [[1, 1], [1, 0]], [[2, 1], [1, 1]])
        animate_numeric_product(square, 3, [[1, 1], [1, 0]], [[2, 1], [1, 1]], [[3, 2], [2, 1]])
        self.wait(2)
