from manim import *


class DiagonalizationIdea(Scene):
    """正方行列の対角化と、対角行列のべき乗を説明する。"""

    def construct(self):
        title = Text("正方行列の対角化", font_size=42, color=BLUE).to_edge(UP)
        definition = VGroup(
            Text("行の数と列の数が同じ行列を正方行列という", font_size=30),
            VGroup(
                Text("正方行列", font_size=30),
                MathTex("A", font_size=36),
                Text("は、別の行列", font_size=30),
                MathTex("P", font_size=36),
                Text("を用いて", font_size=30),
            ).arrange(RIGHT, buff=0.12),
        ).arrange(DOWN, buff=0.35).next_to(title, DOWN, buff=0.45)
        equation = MathTex(
            r"P^{-1}AP=",
            r"\begin{pmatrix}\lambda_1&0\\0&\lambda_2\end{pmatrix}",
            font_size=50,
        ).next_to(definition, DOWN, buff=0.55)
        lambda_note = VGroup(
            MathTex(r"\lambda", font_size=33),
            Text("（ラムダ）は実数", font_size=27),
        ).arrange(RIGHT, buff=0.08).next_to(equation, RIGHT, buff=0.5)
        diagonal_box = SurroundingRectangle(equation[1], color=RED, buff=0.12)
        diagonal_label = Text("対角行列", font_size=28, color=RED).next_to(diagonal_box, DOWN)
        inverse = MathTex(
            r"P^{-1}P=PP^{-1}=\begin{pmatrix}1&0\\0&1\end{pmatrix}=E",
            font_size=39,
        )
        inverse.next_to(equation, DOWN, buff=1.0)
        self.play(Write(title), Write(definition))
        self.play(Write(equation), Write(lambda_note), Create(diagonal_box), Write(diagonal_label))
        self.play(Write(inverse))
        self.wait()

        # 下書き6: ①2乗、②k乗
        self.play(FadeOut(VGroup(definition, lambda_note, diagonal_box, diagonal_label, inverse)))
        equation.generate_target()
        equation.target.next_to(title, DOWN, buff=0.45)
        self.play(MoveToTarget(equation))
        diagonal_left = Matrix(
            [[r"\lambda_1", "0"], ["0", r"\lambda_2"]],
            left_bracket="(",
            right_bracket=")",
        ).scale(0.68)
        diagonal_right = Matrix(
            [[r"\lambda_1", "0"], ["0", r"\lambda_2"]],
            left_bracket="(",
            right_bracket=")",
        ).scale(0.68)
        square_result = Matrix(
            [[r"\lambda_1^2", "0"], ["0", r"\lambda_2^2"]],
            left_bracket="(",
            right_bracket=")",
        ).scale(0.68)
        square_result.get_entries().set_opacity(0)
        square = VGroup(
            diagonal_left,
            diagonal_right,
            MathTex("="),
            square_result,
        ).arrange(RIGHT, buff=0.35).next_to(equation, DOWN, buff=0.55)
        general = MathTex(
            r"\begin{pmatrix}\lambda_1&0\\0&\lambda_2\end{pmatrix}^{k}="
            r"\begin{pmatrix}\lambda_1^k&0\\0&\lambda_2^k\end{pmatrix}",
            font_size=42,
        ).next_to(square, DOWN, buff=0.35)
        self.play(Write(square))  # 下書き6・①

        square_calculations = [
            (0, 0, r"\lambda_1", r"\lambda_1", "0", "0", r"\lambda_1^2"),
            (0, 1, r"\lambda_1", "0", "0", r"\lambda_2", "0"),
            (1, 0, "0", r"\lambda_1", r"\lambda_2", "0", "0"),
            (1, 1, "0", "0", r"\lambda_2", r"\lambda_2", r"\lambda_2^2"),
        ]
        displayed_answers = VGroup()
        for row_index, column_index, first_a, first_b, second_a, second_b, answer in square_calculations:
            row = diagonal_left.get_rows()[row_index]
            column = diagonal_right.get_columns()[column_index]
            result_entry = square_result.get_entries()[row_index * 2 + column_index]
            row_box = SurroundingRectangle(row, color=RED, buff=0.1)
            column_box = SurroundingRectangle(column, color=BLUE, buff=0.1)
            result_box = SurroundingRectangle(result_entry, color=GREEN, buff=0.12)
            self.play(Create(row_box), Create(column_box), Create(result_box))

            expression_layout = MathTex(
                first_a,
                "\\cdot",
                first_b,
                "+",
                second_a,
                "\\cdot",
                second_b,
                "=",
                answer,
                font_size=31,
            ).next_to(square, DOWN, buff=0.35)
            row_terms = VGroup(
                MathTex(first_a, font_size=31).move_to(expression_layout[0]),
                MathTex(second_a, font_size=31).move_to(expression_layout[4]),
            )
            column_terms = VGroup(
                MathTex(first_b, font_size=31).move_to(expression_layout[2]),
                MathTex(second_b, font_size=31).move_to(expression_layout[6]),
            )
            plus = expression_layout[3].copy()
            dot1 = expression_layout[1].copy()
            dot2 = expression_layout[5].copy()
            self.play(
                TransformFromCopy(row[0], row_terms[0]),
                TransformFromCopy(row[1], row_terms[1]),
                TransformFromCopy(column[0], column_terms[0]),
                TransformFromCopy(column[1], column_terms[1]),
                Write(plus),
                Write(dot1),
                Write(dot2),
            )
            equals_and_answer = VGroup(expression_layout[7].copy(), expression_layout[8].copy())
            self.play(Write(equals_and_answer))

            answer_in_matrix = result_entry.copy().set_opacity(1)
            self.play(
                TransformFromCopy(equals_and_answer[1], answer_in_matrix),
                Flash(result_box, color=GREEN),
            )
            displayed_answers.add(answer_in_matrix)
            self.play(
                FadeOut(
                    VGroup(
                        row_box,
                        column_box,
                        result_box,
                        row_terms,
                        column_terms,
                        plus,
                        dot1,
                        dot2,
                        equals_and_answer,
                    )
                )
            )

        self.play(Write(general))  # 下書き6・②
        self.wait(2)
