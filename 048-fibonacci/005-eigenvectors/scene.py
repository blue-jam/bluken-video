from manim import *


class FibonacciEigenvectors(Scene):
    """2つの固有値に対応する固有ベクトルと行列Pを求める。"""

    def construct(self):
        title = Text("固有ベクトルを求める", font_size=42, color=BLUE).to_edge(UP)
        known = MathTex(
            r"A=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad"
            r"\lambda=\frac{1\pm\sqrt5}{2},\qquad"
            r"\boldsymbol{x}=\begin{pmatrix}a \\ b\end{pmatrix}",
            font_size=39,
        ).next_to(title, DOWN, buff=0.4)
        orig_eq = MathTex(
            r"A \boldsymbol{x} = \lambda \boldsymbol{x}"
        ).next_to(known, DOWN, buff=0.70)
        self.play(Write(title), Write(known))
        self.wait(duration=10)
        self.play(Write(orig_eq))
        self.wait(duration=20)

        equation = MathTex(
            r"\begin{pmatrix}1&1\\1&0\end{pmatrix}"
            r"\begin{pmatrix}a\\b\end{pmatrix}="
            r"\frac{1\pm\sqrt5}{2}\begin{pmatrix}a\\b\end{pmatrix}",
            font_size=41,
        ).move_to(orig_eq)
        self.play(ReplacementTransform(orig_eq, equation))
        self.wait(20)

        coefficient_matrix = Matrix(
            [["1", "1"], ["1", "0"]],
            left_bracket="(",
            right_bracket=")",
        ).scale(0.72)
        vector = Matrix(
            [[r"a"], [r"b"]],
            left_bracket="(",
            right_bracket=")",
        ).scale(0.72)
        result_vector = Matrix(
            [[r"a+b"], [r"a"]],
            h_buff=2.1,
            left_bracket="(",
            right_bracket=")",
        ).scale(0.72)
        result_vector.get_entries().set_opacity(0)
        vector_product = VGroup(
            coefficient_matrix,
            vector,
            MathTex("="),
            result_vector,
        ).arrange(RIGHT, buff=0.4).next_to(equation, DOWN, buff=0.55)
        self.play(Write(vector_product))

        vector_calculations = [
            (0, "1", r"a", "1", r"b", r"a+b"),
            (1, "1", r"a", "0", r"b", r"a"),
        ]
        displayed_answers = VGroup()
        for row_index, first_a, first_b, second_a, second_b, answer in vector_calculations:
            row = coefficient_matrix.get_rows()[row_index]
            column = vector.get_columns()[0]
            result_entry = result_vector.get_entries()[row_index]
            row_box = SurroundingRectangle(row, color=RED, buff=0.12)
            column_box = SurroundingRectangle(column, color=BLUE, buff=0.12)
            result_box = SurroundingRectangle(result_entry, color=GREEN, buff=0.14)
            self.play(Create(row_box), Create(column_box), Create(result_box))

            expression_layout = MathTex(
                first_a,
                first_b,
                "+",
                second_a,
                second_b,
                "=",
                answer,
                font_size=33,
            ).next_to(vector_product, DOWN, buff=0.7)
            row_terms = VGroup(
                MathTex(first_a, font_size=33).move_to(expression_layout[0]),
                MathTex(second_a, font_size=33).move_to(expression_layout[3]),
            )
            column_terms = VGroup(
                MathTex(first_b, font_size=33).move_to(expression_layout[1]),
                MathTex(second_b, font_size=33).move_to(expression_layout[4]),
            )
            plus = expression_layout[2].copy()
            self.play(
                TransformFromCopy(row[0], row_terms[0]),
                TransformFromCopy(row[1], row_terms[1]),
                TransformFromCopy(column[0], column_terms[0]),
                TransformFromCopy(column[1], column_terms[1]),
                Write(plus),
            )
            equals_and_answer = VGroup(expression_layout[5].copy(), expression_layout[6].copy())
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
                        equals_and_answer,
                    )
                )
            )
        self.wait(duration=20)

        expanded = MathTex(
            r"\begin{pmatrix}a+b\\a\end{pmatrix}="
            r"\begin{pmatrix}\frac{1\pm\sqrt5}{2}a\\\frac{1\pm\sqrt5}{2}b\end{pmatrix}",
            font_size=40,
        ).move_to(equation)
        relation = MathTex(r"a=\frac{1\pm\sqrt5}{2}b", font_size=41).next_to(expanded, DOWN, buff=0.5)
        relation.next_to(expanded, DOWN, buff=0.5)
        self.play(ReplacementTransform(VGroup(equation, vector_product, displayed_answers), expanded))
        self.wait(duration=20)
        self.play(Write(relation))
        self.wait(duration=20)

        self.play(FadeOut(VGroup(expanded, relation)))
        choose = VGroup(
            MathTex(r"b=1", font_size=37),
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
        self.play(Write(choose))
        self.play(Write(vectors))
        self.play(Write(lambdas))
        self.wait(duration=20)

        shifted_vectors = vectors.copy().next_to(title, DOWN, buff=1)
        shifted_lambdas = lambdas.copy().next_to(shifted_vectors, DOWN, buff=0.45)
        self.play(
            FadeOut(known, choose),
            vectors.animate.move_to(shifted_vectors),
            lambdas.animate.move_to(shifted_lambdas),
        )
        p_matrix = MathTex(
            r"P=(\boldsymbol{x}_1\ \boldsymbol{x}_2)="
            r"\begin{pmatrix}\frac{1+\sqrt5}{2}&\frac{1-\sqrt5}{2}\\1&1\end{pmatrix}",
            font_size=41,
        ).next_to(lambdas, DOWN, buff=0.5)
        self.play(Write(p_matrix))
        self.play(Circumscribe(p_matrix, color=YELLOW))
        self.wait(20)
