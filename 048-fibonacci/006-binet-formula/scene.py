from manim import *


class DeriveBinetFormula(Scene):
    """対角化の計算を画面ごとに差し替え、ビネの公式を導く。"""

    def construct(self):
        title = Text("対角化", font_size=42, color=BLUE).to_edge(UP)
        a_matrix = MathTex(r"A=\begin{pmatrix}1&1\\1&0\end{pmatrix}", font_size=38)
        p_matrix = MathTex(
            r"P=\begin{pmatrix}\lambda_1&\lambda_2\\1&1\end{pmatrix}",
            font_size=38,
        )
        givens = VGroup(a_matrix, p_matrix).arrange(RIGHT, buff=1.0).next_to(title, DOWN, buff=0.4)

        self.play(Write(title), Write(givens))
        # B=(a b; c d) に右肩の -1 を付けるのと同時に、逆行列の形へ変形する。
        general_label = MathTex("B", "=", font_size=44)
        general_matrix = Matrix(
            [["a", "b"], ["c", "d"]], left_bracket="(", right_bracket=")"
        ).scale(0.9)
        general_expression = VGroup(general_label, general_matrix).arrange(RIGHT, buff=0.2)
        general_expression.next_to(givens, DOWN, buff=0.65)
        self.play(Write(general_label), Write(general_matrix))
        self.wait(0.4)

        inverse_label = MathTex("B", "=", font_size=44)
        inverse_power = MathTex("-1", font_size=25)
        inverse_factor = MathTex(r"\frac1{ad-bc}", font_size=42)
        general_result_matrix = Matrix(
            [["d", "-b"], ["-c", "a"]], left_bracket="(", right_bracket=")"
        ).scale(0.9)
        inverse_expression = VGroup(
            inverse_label, inverse_factor, general_result_matrix
        ).arrange(RIGHT, buff=0.2)
        inverse_expression.next_to(givens, DOWN, buff=0.65)
        inverse_power.next_to(inverse_label[0], UR, buff=0.02)

        source_entries = general_matrix.get_entries()
        result_entries = general_result_matrix.get_entries()
        self.play(
            ReplacementTransform(general_label[0], inverse_label[0]),
            ReplacementTransform(general_label[1], inverse_label[1]),
            Write(inverse_power),
            GrowFromCenter(inverse_factor),
            ReplacementTransform(general_matrix.get_brackets(), general_result_matrix.get_brackets()),
            ReplacementTransform(source_entries[0], result_entries[3], path_arc=-PI / 2),
            ReplacementTransform(source_entries[3], result_entries[0], path_arc=-PI / 2),
            ReplacementTransform(source_entries[1], result_entries[1]),
            ReplacementTransform(source_entries[2], result_entries[2]),
            run_time=2.2,
        )
        self.play(Circumscribe(VGroup(inverse_label, inverse_power, inverse_factor, general_result_matrix), color=GREEN))
        self.wait(10)
        self.play(FadeOut(VGroup(
            inverse_label, inverse_power, inverse_factor, general_result_matrix
        )))

        source_label = MathTex("P", "=", font_size=42)
        source_matrix = Matrix(
            [[r"\lambda_1", r"\lambda_2"], ["1", "1"]],
            left_bracket="(",
            right_bracket=")",
        ).scale(0.72)
        source_group = VGroup(source_label, source_matrix).arrange(RIGHT, buff=0.2)
        source_group.next_to(givens, DOWN, buff=0.45)

        self.play(Write(source_label), Write(source_matrix))
        source_entries = source_matrix.get_entries()

        p_inverse_label = MathTex("P", "=", font_size=42)
        p_inverse_power = MathTex("-1", font_size=24)
        p_inverse_factor = MathTex(r"\frac1{\lambda_1-\lambda_2}", font_size=40)
        inverse_matrix = Matrix(
            [["1", r"-\lambda_2"], ["-1", r"\lambda_1"]],
            left_bracket="(",
            right_bracket=")",
        ).scale(0.72)
        inverse_parts = VGroup(
            p_inverse_label, p_inverse_factor, inverse_matrix
        ).arrange(RIGHT, buff=0.2)
        inverse_parts.next_to(givens, DOWN, buff=0.45)
        p_inverse_power.next_to(p_inverse_label[0], UR, buff=0.02)
        target_entries = inverse_matrix.get_entries()

        self.play(
            ReplacementTransform(source_label[0], p_inverse_label[0]),
            ReplacementTransform(source_label[1], p_inverse_label[1]),
            Write(p_inverse_power),
            GrowFromCenter(p_inverse_factor),
            ReplacementTransform(source_matrix.get_brackets(), inverse_matrix.get_brackets()),
            ReplacementTransform(source_entries[0], target_entries[3], path_arc=-PI / 2),
            ReplacementTransform(source_entries[3], target_entries[0], path_arc=-PI / 2),
            ReplacementTransform(source_entries[1], target_entries[1]),
            ReplacementTransform(source_entries[2], target_entries[2]),
            run_time=2.2,
        )
        self.play(Circumscribe(
            VGroup(p_inverse_label, p_inverse_power, p_inverse_factor, inverse_matrix),
            color=GREEN,
        ))

        # 逆行列を別の MathTex に置き換えず、いま表示している各部品を
        # そのまま A、P と同じ行へ移動する。
        inverse = VGroup(
            p_inverse_label,
            p_inverse_power,
            p_inverse_factor,
            inverse_matrix,
        )
        top_row = VGroup(givens, inverse)
        self.play(
            top_row.animate.arrange(RIGHT, buff=0.5).next_to(title, DOWN, buff=0.4),
            run_time=1.5,
        )
        self.wait(20)

        # 同じ「対角化」の下書き12。前の計算を消して、同時表示量を抑える。
        diagonal = MathTex(
            r"P^{-1}AP=\begin{pmatrix}\lambda_1&0\\0&\lambda_2\end{pmatrix}",
            font_size=40,
        ).next_to(top_row, DOWN, buff=0.45)
        self.play(Write(diagonal))
        self.wait(20)

        # (P^{-1}AP) を n 個並べ、境目の PP^{-1} が消える様子を見せる。
        # 下書き12の横長な式を2段に分け、打ち消す箇所を色で追いやすくする。
        self.play(FadeOut(VGroup(givens, inverse)))
        self.play(diagonal.animate.next_to(title, DOWN, buff=0.55))

        power_lhs_shift = DOWN * 0 + LEFT * 4.0
        power_lhs = MathTex(
            r"(P^{-1}AP)^n", "=", font_size=39,
        )
        power_lhs.next_to(diagonal, DOWN, buff=0.55)
        power_lhs.shift(power_lhs_shift)
        repeated_rhs_offset = DOWN * 0.3 + RIGHT * 0.0
        repeated_rhs = MathTex(
            r"\underbrace{(P^{-1}AP)(P^{-1}AP)\cdots(P^{-1}AP)}_{n}",
            font_size=39,
        ).next_to(power_lhs, RIGHT, buff=0.18)
        repeated_rhs.shift(repeated_rhs_offset)
        self.play(Write(power_lhs))
        self.play(Write(repeated_rhs), run_time=1.8)

        cancellation_product = MathTex(
            "=", r"P^{-1}", "A", "P", r"P^{-1}", "A",
            r"\cdots", "A", "P", r"P^{-1}", "A", "P",
            font_size=39,
        ).next_to(repeated_rhs, DOWN, buff=0.5)
        cancellation_product.set_color_by_tex("P", BLUE)
        cancellation_product.set_color_by_tex("A", YELLOW)
        self.play(Write(cancellation_product))

        # 代表として両端の境目を囲む。途中のすべての境目でも同じことが起きる。
        left_pair = VGroup(cancellation_product[3], cancellation_product[4])
        right_pair = VGroup(cancellation_product[8], cancellation_product[9])
        left_box = SurroundingRectangle(left_pair, color=RED, buff=0.09)
        right_box = SurroundingRectangle(right_pair, color=RED, buff=0.09)
        identity_left = MathTex("E", font_size=34, color=GREEN).move_to(left_pair)
        identity_right = MathTex("E", font_size=34, color=GREEN).move_to(right_pair)
        self.play(Create(left_box), Create(right_box))
        self.play(
            FadeOut(left_pair),
            FadeOut(right_pair),
            FadeIn(identity_left),
            FadeIn(identity_right),
        )

        collapsed_rhs_offset = DOWN * 0.1 + RIGHT * 0.0
        collapsed_rhs = MathTex(
            r"P^{-1}",
            r"\underbrace{A A\cdots A}_{n}",
            "P",
            "=",
            r"P^{-1}A^nP",
            "=",
            r"\begin{pmatrix}\lambda_1^n&0\\0&\lambda_2^n\end{pmatrix}",
            font_size=36,
        ).next_to(power_lhs, RIGHT, buff=0.18)
        collapsed_rhs.shift(collapsed_rhs_offset)
        collapsed_rhs.set_color_by_tex("P", BLUE)
        collapsed_rhs.set_color_by_tex("A", YELLOW)
        self.play(
            FadeOut(VGroup(left_box, right_box, identity_left, identity_right, cancellation_product)),
            ReplacementTransform(repeated_rhs, collapsed_rhs[0:3]),
        )

        self.play(Write(collapsed_rhs[3:]), run_time=1.2)
        power_identity = VGroup(power_lhs, collapsed_rhs)
        self.wait(20)

        # 下書き13: A^n=P D^n P^{-1} を展開する。
        self.play(FadeOut(VGroup(diagonal, power_identity)))
        title2 = Text("公式を導く", font_size=42, color=BLUE).to_edge(UP)
        givens2 = VGroup(
            a_matrix,
            p_matrix,
            MathTex(
                r"P^{-1}=\frac1{\lambda_1-\lambda_2}"
                r"\begin{pmatrix}1&-\lambda_2\\-1&\lambda_1\end{pmatrix}",
                font_size=38,
            ),
        ).arrange(RIGHT, buff=1.0).next_to(title2, DOWN, buff=0.4)
        relation = MathTex(
            r"A^n=P"
            r"\begin{pmatrix}\lambda_1^n&0\\0&\lambda_2^n\end{pmatrix}P^{-1}",
            font_size=48,
        ).next_to(givens2, DOWN, buff=0.5)
        self.wait(20)

        # 1 本の等式の中で、まず P だけを具体的な行列に置き換える。
        p_substituted = MathTex(
            r"A^n="
            r"\begin{pmatrix}\lambda_1&\lambda_2\\1&1\end{pmatrix}"
            r"\begin{pmatrix}\lambda_1^n&0\\0&\lambda_2^n\end{pmatrix}"
            r"P^{-1}",
            font_size=43,
        ).move_to(relation)

        # P と対角行列の積を、各成分の計算が見える形で表示する。
        p_for_product = Matrix(
            [[r"\lambda_1", r"\lambda_2"], ["1", "1"]],
            left_bracket="(",
            right_bracket=")",
        ).scale(0.62)
        diagonal_for_product = Matrix(
            [[r"\lambda_1^n", "0"], ["0", r"\lambda_2^n"]],
            h_buff=1.35,
            left_bracket="(",
            right_bracket=")",
        ).scale(0.62)
        p_inv_for_product = MathTex(r"P^{-1}", font_size=33)
        first_result_matrix = Matrix(
            [
                [r"\lambda_1^{n+1}", r"\lambda_2^{n+1}"],
                [r"\lambda_1^n", r"\lambda_2^n"],
            ],
            h_buff=1.65,
            left_bracket="(",
            right_bracket=")",
        ).scale(0.62)
        first_result_matrix.get_entries().set_opacity(0)
        animated_product = VGroup(
            MathTex(r"A^n=", font_size=33),
            p_for_product,
            diagonal_for_product,
            p_inv_for_product,
            MathTex("=", font_size=33),
            first_result_matrix,
            MathTex(r"P^{-1}", font_size=33),
        ).arrange(RIGHT, buff=0.22).next_to(givens2, DOWN, buff=0.5)
        self.wait(10)

        # 最後に P^{-1} も具体化する。
        product = MathTex(
            r"A^n=\frac1{\lambda_1-\lambda_2}"
            r"\begin{pmatrix}\lambda_1^{n+1}&\lambda_2^{n+1}\\\lambda_1^n&\lambda_2^n\end{pmatrix}"
            r"\begin{pmatrix}1&-\lambda_2\\-1&\lambda_1\end{pmatrix}",
            font_size=41,
        ).move_to(animated_product)
        self.play(
            ReplacementTransform(title, title2),
            Write(givens2)
        )
        self.play(Write(relation))
        self.play(ReplacementTransform(relation, p_substituted))
        self.wait(0.4)
        self.play(ReplacementTransform(p_substituted, animated_product))

        first_calculations = [
            (0, 0, r"\lambda_1", r"\lambda_1^n", r"\lambda_2", "0", r"\lambda_1^{n+1}"),
            (0, 1, r"\lambda_1", "0", r"\lambda_2", r"\lambda_2^n", r"\lambda_2^{n+1}"),
            (1, 0, "1", r"\lambda_1^n", "1", "0", r"\lambda_1^n"),
            (1, 1, "1", "0", "1", r"\lambda_2^n", r"\lambda_2^n"),
        ]
        first_answers = VGroup()
        for row_index, column_index, left_1, right_1, left_2, right_2, answer in first_calculations:
            row = p_for_product.get_rows()[row_index]
            column = diagonal_for_product.get_columns()[column_index]
            result_entry = first_result_matrix.get_entries()[row_index * 2 + column_index]
            row_box = SurroundingRectangle(row, color=RED, buff=0.1)
            column_box = SurroundingRectangle(column, color=BLUE, buff=0.1)
            result_box = SurroundingRectangle(result_entry, color=GREEN, buff=0.12)
            self.play(Create(row_box), Create(column_box), Create(result_box))

            calculation = MathTex(
                left_1,
                rf"\left({right_1}\right)",
                "+",
                left_2,
                rf"\left({right_2}\right)",
                "=",
                answer,
                font_size=25,
            ).next_to(animated_product, DOWN, buff=0.5)
            self.play(
                TransformFromCopy(row[0], calculation[0]),
                TransformFromCopy(column[0], calculation[1]),
                Write(calculation[2]),
                TransformFromCopy(row[1], calculation[3]),
                TransformFromCopy(column[1], calculation[4]),
            )
            self.play(Write(calculation[5:]))
            answer_in_matrix = result_entry.copy().set_opacity(1)
            self.play(
                TransformFromCopy(calculation[-1], answer_in_matrix),
                Flash(result_box, color=GREEN),
            )
            first_answers.add(answer_in_matrix)
            self.play(FadeOut(VGroup(row_box, column_box, result_box, calculation)))

        self.wait(0.4)
        self.play(
            ReplacementTransform(VGroup(animated_product, first_answers), product),
        )
        self.wait(10)

        # 下書き14: 積を計算し、1行2列成分だけを取り出す。
        left_matrix = Matrix(
            [[r"\lambda_1^{n+1}", r"\lambda_2^{n+1}"], [r"\lambda_1^n", r"\lambda_2^n"]],
            h_buff=1.65,
            left_bracket="(",
            right_bracket=")",
        ).scale(0.62)
        right_matrix = Matrix(
            [["1", r"-\lambda_2"], ["-1", r"\lambda_1"]],
            h_buff=1.35,
            left_bracket="(",
            right_bracket=")",
        ).scale(0.62)
        result_matrix = Matrix(
            [
                [r"\lambda_1^{n+1}-\lambda_2^{n+1}", r"-\lambda_2\lambda_1^{n+1}+\lambda_1\lambda_2^{n+1}"],
                [r"\lambda_1^n-\lambda_2^n", r"-\lambda_2\lambda_1^n+\lambda_1\lambda_2^n"],
            ],
            h_buff=4.5,
            left_bracket="(",
            right_bracket=")",
        ).scale(0.62)
        result_matrix.get_entries().set_opacity(0)
        final_animated_product = VGroup(
            MathTex(r"A^n=\frac1{\lambda_1-\lambda_2}", font_size=33),
            left_matrix,
            right_matrix,
            MathTex("=", font_size=33),
            result_matrix,
        ).arrange(RIGHT, buff=0.25).next_to(givens2, DOWN, buff=0.45)
        self.play(ReplacementTransform(product, final_animated_product))

        calculations = [
            (0, 0, r"\lambda_1^{n+1}", r"1", r"\lambda_2^{n+1}", r"-1", r"\lambda_1^{n+1}-\lambda_2^{n+1}"),
            (0, 1, r"\lambda_1^{n+1}", r"-\lambda_2", r"\lambda_2^{n+1}", r"\lambda_1", r"-\lambda_2\lambda_1^{n+1}+\lambda_1\lambda_2^{n+1}"),
            (1, 0, r"\lambda_1^n", r"1", r"\lambda_2^n", r"-1", r"\lambda_1^n-\lambda_2^n"),
            (1, 1, r"\lambda_1^n", r"-\lambda_2", r"\lambda_2^n", r"\lambda_1", r"-\lambda_2\lambda_1^n+\lambda_1\lambda_2^n"),
        ]
        displayed_answers = VGroup()
        for row_index, column_index, left_1, right_1, left_2, right_2, answer in calculations:
            row = left_matrix.get_rows()[row_index]
            column = right_matrix.get_columns()[column_index]
            result_entry = result_matrix.get_entries()[row_index * 2 + column_index]
            row_box = SurroundingRectangle(row, color=RED, buff=0.1)
            column_box = SurroundingRectangle(column, color=BLUE, buff=0.1)
            result_box = SurroundingRectangle(result_entry, color=GREEN, buff=0.12)
            self.play(Create(row_box), Create(column_box), Create(result_box))

            expression_layout = MathTex(
                left_1,
                rf"\left({right_1}\right)",
                "+",
                left_2,
                rf"\left({right_2}\right)",
                "=",
                answer,
                font_size=25,
            ).next_to(final_animated_product, DOWN, buff=0.55)
            row_terms = VGroup(
                MathTex(left_1, font_size=25).move_to(expression_layout[0]),
                MathTex(left_2, font_size=25).move_to(expression_layout[3]),
            )
            column_terms = VGroup(
                MathTex(rf"\left({right_1}\right)", font_size=25).move_to(expression_layout[1]),
                MathTex(rf"\left({right_2}\right)", font_size=25).move_to(expression_layout[4]),
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

        expanded = MathTex(
            r"A^n=\frac1{\lambda_1-\lambda_2}\begin{pmatrix}"
            r"\lambda_1^{n+1}-\lambda_2^{n+1}&-\lambda_2\lambda_1^{n+1}+\lambda_1\lambda_2^{n+1}\\"
            r"\lambda_1^n-\lambda_2^n&-\lambda_2\lambda_1^n+\lambda_1\lambda_2^n"
            r"\end{pmatrix}"
            r"=\begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1}\end{pmatrix}",
            font_size=34,
        ).next_to(title2, DOWN, buff=0.55)
        self.play(
            FadeOut(VGroup(final_animated_product, displayed_answers, givens2)),
            Write(expanded),
        )
        self.wait(20)

        entry = MathTex(
            r"F_n=\frac{1}{\lambda_1-\lambda_2}(\lambda_1^n-\lambda_2^n)",
            font_size=47,
        )
        entry.next_to(expanded, DOWN, buff=0.6)
        self.play(Write(entry))
        self.wait(20)

        # 固有値を一般項へ代入し、分母が sqrt(5) になるまでを段階的に示す。
        eigenvalues = MathTex(
            r"\lambda_1=\frac{1+\sqrt5}{2},\qquad"
            r"\lambda_2=\frac{1-\sqrt5}{2}",
            font_size=43,
        ).next_to(entry, DOWN, buff=0.45)
        self.play(Write(eigenvalues))
        self.wait(20)

        substituted = MathTex(
            r"F_n=\frac{1}{"
            r"\frac{1+\sqrt5}{2}-\frac{1-\sqrt5}{2}"
            r"}"
            r"\left\{\left(\frac{1+\sqrt5}{2}\right)^n-"
            r"\left(\frac{1-\sqrt5}{2}\right)^n\right\}"
            ,
            font_size=40,
        ).next_to(title2, DOWN, 0.55)
        self.play(
            FadeOut(expanded),
            ReplacementTransform(VGroup(entry, eigenvalues), substituted),
            title2.animate.to_edge(UP),
            run_time=1.8,
        )
        self.wait(0.5)

        denominator_steps = VGroup(
            MathTex(
                r"\lambda_1-\lambda_2"
                r"=\frac{1+\sqrt5}{2}-\frac{1-\sqrt5}{2}",
                font_size=38,
            ),
            MathTex(
                r"=\frac{(1+\sqrt5)-(1-\sqrt5)}{2}",
                font_size=38,
            ),
            MathTex(
                r"=\frac{2\sqrt5}{2}=\sqrt5",
                font_size=38,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        denominator_steps.next_to(substituted, DOWN, buff=0.55)
        denominator_steps.set_color(YELLOW)

        self.play(Write(denominator_steps[0]))
        self.play(Write(denominator_steps[1]))
        self.play(Write(denominator_steps[2]))
        self.play(Circumscribe(denominator_steps[2][-2:], color=YELLOW))
        self.wait(15)

        bine = MathTex(
            r"F_n=\frac1{\sqrt5}\left\{\left(\frac{1+\sqrt5}{2}\right)^n-"
            r"\left(\frac{1-\sqrt5}{2}\right)^n\right\}",
            font_size=43,
        ).move_to(ORIGIN)
        self.play(
            FadeOut(denominator_steps),
            ReplacementTransform(substituted, bine),
            run_time=1.6,
        )
        self.play(Circumscribe(bine, color=YELLOW))
        self.wait(20)
