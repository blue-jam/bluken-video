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

        self.play(FadeOut(equation))
        coefficient_matrix = Matrix(
            [["1", "1"], ["1", "0"]],
            left_bracket="(",
            right_bracket=")",
        ).scale(0.72)
        vector = Matrix(
            [[r"x_1"], [r"x_2"]],
            left_bracket="(",
            right_bracket=")",
        ).scale(0.72)
        result_vector = Matrix(
            [["?"], ["?"]],
            h_buff=2.1,
            left_bracket="(",
            right_bracket=")",
        ).scale(0.72)
        vector_product = VGroup(
            coefficient_matrix,
            vector,
            MathTex("="),
            result_vector,
        ).arrange(RIGHT, buff=0.4).move_to(equation)
        self.play(Write(vector_product))

        vector_calculations = [
            (0, r"1\cdot x_1", r"1\cdot x_2", r"x_1+x_2"),
            (1, r"1\cdot x_1", r"0\cdot x_2", r"x_1"),
        ]
        for row_index, first_product, second_product, answer in vector_calculations:
            row = coefficient_matrix.get_rows()[row_index]
            column = vector.get_columns()[0]
            result_entry = result_vector.get_entries()[row_index]
            row_box = SurroundingRectangle(row, color=RED, buff=0.12)
            column_box = SurroundingRectangle(column, color=BLUE, buff=0.12)
            result_box = SurroundingRectangle(result_entry, color=GREEN, buff=0.14)
            self.play(Create(row_box), Create(column_box), Create(result_box))

            extracted_row = row.copy().arrange(RIGHT, buff=0.35)
            extracted_column = column.copy().arrange(DOWN, buff=0.18)
            extracted = VGroup(
                extracted_row,
                MathTex(r"\cdot"),
                extracted_column,
            ).arrange(RIGHT, buff=0.3).to_edge(DOWN, buff=0.7).shift(LEFT * 3.5)
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
                font_size=33,
            ).next_to(extracted, RIGHT, buff=0.5)
            self.play(Write(calculation[:3]))
            self.play(Write(calculation[3:]))
            self.play(
                Transform(result_entry, MathTex(answer, font_size=34).move_to(result_entry)),
                Flash(result_box, color=GREEN),
            )
            self.play(FadeOut(VGroup(row_box, column_box, result_box, extracted, calculation)))

        self.play(FadeOut(vector_product))
        expanded.move_to(equation)
        relation.next_to(expanded, DOWN, buff=0.5)
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
