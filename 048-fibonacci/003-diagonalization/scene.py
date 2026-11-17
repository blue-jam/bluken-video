from manim import *


class DiagonalizationIdea(Scene):
    """正方行列の対角化と、対角行列のべき乗を説明する。"""

    def construct(self):
        title = Text("正方行列の対角化", font_size=42, color=BLUE).to_edge(UP)
        definition = VGroup(
            Text("行の数と列の数が同じ行列を正方行列という", font_size=30),
            Text("正方行列 A は、別の行列 P を用いて", font_size=30),
        ).arrange(DOWN, buff=0.35).next_to(title, DOWN, buff=0.45)
        equation = MathTex(
            r"P^{-1}AP=",
            r"\begin{pmatrix}\lambda_1&0\\0&\lambda_2\end{pmatrix}",
            font_size=50,
        ).next_to(definition, DOWN, buff=0.55)
        lambda_note = Text("λ（ラムダ）は数", font_size=27).next_to(equation, RIGHT, buff=0.5)
        diagonal_box = SurroundingRectangle(equation[1], color=RED, buff=0.12)
        diagonal_label = Text("対角行列", font_size=28, color=RED).next_to(diagonal_box, DOWN)
        inverse = MathTex(r"P^{-1}P=PP^{-1}=\begin{pmatrix}1&0\\0&1\end{pmatrix}", font_size=39)
        inverse.next_to(equation, DOWN, buff=0.75)
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
            [["?", "?"], ["?", "?"]],
            h_buff=2.2,
            left_bracket="(",
            right_bracket=")",
        ).scale(0.68)
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
        ).to_edge(DOWN, buff=0.35)
        self.play(Write(square))  # 下書き6・①

        square_calculations = [
            (0, 0, r"\lambda_1\cdot\lambda_1", r"0\cdot0", r"\lambda_1^2"),
            (0, 1, r"\lambda_1\cdot0", r"0\cdot\lambda_2", "0"),
            (1, 0, r"0\cdot\lambda_1", r"\lambda_2\cdot0", "0"),
            (1, 1, r"0\cdot0", r"\lambda_2\cdot\lambda_2", r"\lambda_2^2"),
        ]
        for row_index, column_index, first_product, second_product, answer in square_calculations:
            row = diagonal_left.get_rows()[row_index]
            column = diagonal_right.get_columns()[column_index]
            result_entry = square_result.get_entries()[row_index * 2 + column_index]
            row_box = SurroundingRectangle(row, color=RED, buff=0.1)
            column_box = SurroundingRectangle(column, color=BLUE, buff=0.1)
            result_box = SurroundingRectangle(result_entry, color=GREEN, buff=0.12)
            self.play(Create(row_box), Create(column_box), Create(result_box))

            calculation = MathTex(
                first_product,
                "+",
                second_product,
                "=",
                answer,
                font_size=31,
            ).to_edge(DOWN, buff=0.45)
            self.play(
                TransformFromCopy(row, calculation[0]),
                Write(calculation[1]),
                TransformFromCopy(column, calculation[2]),
            )
            self.play(Write(calculation[3:]))
            self.play(
                Transform(result_entry, MathTex(answer, font_size=32).move_to(result_entry)),
                Flash(result_box, color=GREEN),
            )
            self.play(FadeOut(VGroup(row_box, column_box, result_box, calculation)))

        self.play(Write(general))  # 下書き6・②
        self.wait(2)
