import numpy as np
from manim import *
from manim_slides import Slide


class RateLawsAndHalfLives(Slide):
    def construct(self):

        # =========================
        # SLIDE 1: Rate Laws Intro
        # =========================
        title = Text("Rate Laws", color=YELLOW, font_size=56).to_edge(UP)
        self.play(Write(title))

        definition = Text(
            "Shows the relationship between reaction speed and reactant concentration.",
            font_size=26,
            color=WHITE,
        ).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(definition, shift=UP))

        formula_box = SurroundingRectangle(
            MathTex(r"\text{Rate} = k[A]^m[B]^n", font_size=48, color=GREEN_C),
            buff=0.3,
            color=GREEN_C,
        )
        formula = MathTex(r"\text{Rate} = k[A]^m[B]^n", font_size=48, color=GREEN_C)
        formula_group = VGroup(formula, formula_box).next_to(definition, DOWN, buff=0.5)
        self.play(Write(formula), Create(formula_box))

        term_bullets = (
            VGroup(
                Text(
                    "• k  — Rate constant: specific to a reaction at a given temperature.",
                    font_size=24,
                ),
                Text(
                    "       Changes if temperature changes or a catalyst is added.",
                    font_size=22,
                    color=GRAY_B,
                ),
                Text(
                    "• m, n  — Reaction orders: found from experimental data ONLY.",
                    font_size=24,
                ),
                Text(
                    "       Cannot be read from the balanced equation coefficients.",
                    font_size=22,
                    color=RED_B,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            .next_to(formula_group, DOWN, buff=0.5)
        )
        self.play(FadeIn(term_bullets, shift=UP))
        self.next_slide()

        # =========================
        # SLIDE 2: Reaction Orders
        # =========================
        self.play(FadeOut(definition), FadeOut(formula_group), FadeOut(term_bullets))

        orders_title = Text("Reaction Orders", font_size=40, color=YELLOW).next_to(
            title, DOWN, buff=0.5
        )
        self.play(Write(orders_title))

        orders_table_data = [
            ["Order", "Effect of Doubling [A]", "Example"],
            ["Zero (m=0)", "No change in rate (×1)", r"Rate = k"],
            ["First (m=1)", "Rate doubles (×2)", r"Rate = k[A]"],
            ["Second (m=2)", "Rate quadruples (×4)", r"Rate = k[A]^2"],
        ]

        col_widths = [2.8, 4.2, 3.0]
        rows = []
        for r_idx, row in enumerate(orders_table_data):
            row_group = VGroup()
            for c_idx, cell in enumerate(row):
                if r_idx == 0:
                    mob = Text(cell, font_size=22, color=YELLOW)
                elif c_idx == 2:
                    mob = MathTex(cell, font_size=22)
                else:
                    mob = Text(cell, font_size=22)
                mob.set_width(min(mob.width, col_widths[c_idx] - 0.2))
                row_group.add(mob)
            row_group.arrange(RIGHT, buff=0.0)
            for c_idx, mob in enumerate(row_group):
                mob.set_x(
                    sum(col_widths[:c_idx])
                    - sum(col_widths) / 2
                    + col_widths[c_idx] / 2
                )
            rows.append(row_group)

        table_group = (
            VGroup(*rows).arrange(DOWN, buff=0.35).next_to(orders_title, DOWN, buff=0.5)
        )

        underline = Line(
            table_group[0].get_left() + LEFT * 0.2,
            table_group[0].get_right() + RIGHT * 0.2,
            color=YELLOW,
            stroke_width=1.5,
        ).next_to(table_group[0], DOWN, buff=0.1)

        self.play(FadeIn(table_group[0]), Create(underline))
        for row in rows[1:]:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.6)

        overall_note = Text(
            "Overall Order = sum of all individual orders (m + n + …)",
            font_size=24,
            color=BLUE_B,
        ).next_to(table_group, DOWN, buff=0.5)
        self.play(Write(overall_note))
        self.next_slide()

        # ==========================================
        # SLIDE 3: Method of Initial Rates (NEW)
        # ==========================================
        self.play(
            FadeOut(orders_title),
            FadeOut(table_group),
            FadeOut(underline),
            FadeOut(overall_note),
        )

        initial_rates_title = Text(
            "Determining Orders from Data", font_size=40, color=YELLOW
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(initial_rates_title))

        # Built-in Manim Table
        data_table = (
            Table(
                [
                    ["0.10", "0.10", "0.002"],
                    ["0.20", "0.10", "0.004"],
                    ["0.10", "0.20", "0.008"],
                ],
                row_labels=[
                    Text("Exp 1", font_size=24),
                    Text("Exp 2", font_size=24),
                    Text("Exp 3", font_size=24),
                ],
                col_labels=[
                    Text("[A] (M)", font_size=24),
                    Text("[B] (M)", font_size=24),
                    Text("Initial Rate (M/s)", font_size=24),
                ],
                include_outer_lines=True,
                v_buff=0.4,
                h_buff=0.8,
            )
            .scale(0.6)
            .next_to(initial_rates_title, DOWN, buff=0.4)
        )

        self.play(Create(data_table))

        # A Order Explanation
        a_highlight = data_table.get_rows()[1:3]  # Exp 1 and 2
        a_rect = SurroundingRectangle(a_highlight, color=GREEN_C, buff=0.1)

        a_explanation = (
            VGroup(
                Text("Exp 1 → Exp 2: [B] is constant.", font_size=20),
                Text(
                    "[A] doubles (×2), Rate doubles (×2).", font_size=20, color=GREEN_C
                ),
                MathTex(
                    r"2^m = 2 \implies m = 1 \text{ (First Order in A)}",
                    font_size=24,
                    color=GREEN_C,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(data_table, DOWN, buff=0.3)
            .align_to(data_table, LEFT)
        )

        self.play(Create(a_rect))
        self.play(Write(a_explanation))
        self.next_slide()

        # B Order Explanation
        self.play(FadeOut(a_rect), FadeOut(a_explanation))

        b_highlight_1 = data_table.get_rows()[1]  # Exp 1
        b_highlight_2 = data_table.get_rows()[3]  # Exp 3
        b_rect_1 = SurroundingRectangle(b_highlight_1, color=BLUE_B, buff=0.1)
        b_rect_2 = SurroundingRectangle(b_highlight_2, color=BLUE_B, buff=0.1)

        b_explanation = (
            VGroup(
                Text("Exp 1 → Exp 3: [A] is constant.", font_size=20),
                Text(
                    "[B] doubles (×2), Rate quadruples (×4).",
                    font_size=20,
                    color=BLUE_B,
                ),
                MathTex(
                    r"2^n = 4 \implies n = 2 \text{ (Second Order in B)}",
                    font_size=24,
                    color=BLUE_B,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(data_table, DOWN, buff=0.3)
            .align_to(data_table, LEFT)
        )

        self.play(Create(b_rect_1), Create(b_rect_2))
        self.play(Write(b_explanation))

        final_rate_law = MathTex(
            r"\text{Rate} = k[A]^1[B]^2", font_size=36, color=YELLOW
        ).next_to(b_explanation, RIGHT, buff=1.0)
        final_rate_box = SurroundingRectangle(final_rate_law, color=YELLOW)
        self.play(Write(final_rate_law), Create(final_rate_box))
        self.next_slide()

        # =========================
        # SLIDE 4: Units of k
        # =========================
        self.play(
            FadeOut(initial_rates_title),
            FadeOut(data_table),
            FadeOut(b_rect_1),
            FadeOut(b_rect_2),
            FadeOut(b_explanation),
            FadeOut(final_rate_law),
            FadeOut(final_rate_box),
        )

        k_title = Text("Units of k", font_size=40, color=YELLOW).next_to(
            title, DOWN, buff=0.5
        )
        self.play(Write(k_title))

        k_bullets = (
            VGroup(
                MathTex(
                    r"\text{Zero order:} \quad k \text{ has units } \frac{M}{s}",
                    font_size=32,
                ),
                MathTex(
                    r"\text{First order:} \quad k \text{ has units } \frac{1}{s} \text{ or } s^{-1}",
                    font_size=32,
                ),
                MathTex(
                    r"\text{Second order:} \quad k \text{ has units } \frac{1}{M \cdot s} \text{ or } M^{-1}s^{-1}",
                    font_size=32,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.6)
            .next_to(k_title, DOWN, buff=0.7)
        )
        self.play(FadeIn(k_bullets, shift=UP))

        k_note = Text(
            "Units of k depend on overall reaction order so that\n"
            "Rate always ends up in units of M/s.",
            font_size=24,
            color=GRAY_B,
        ).next_to(k_bullets, DOWN, buff=0.6)
        self.play(FadeIn(k_note))
        self.next_slide()

        # ================================
        # SLIDE 5: Integrated Rate Laws
        # ================================
        self.play(FadeOut(k_title), FadeOut(k_bullets), FadeOut(k_note), FadeOut(title))

        title2 = Text("Integrated Rate Laws", color=YELLOW, font_size=52).to_edge(UP)
        self.play(Write(title2))

        irl_intro = Text(
            "Relate concentration to time — all on the AP formula sheet.",
            font_size=26,
        ).next_to(title2, DOWN, buff=0.4)
        self.play(FadeIn(irl_intro))

        irl_equations = (
            VGroup(
                VGroup(
                    Text("Zero Order:", font_size=26, color=RED),
                    MathTex(r"[A]_t - [A]_0 = -kt", font_size=34),
                ).arrange(RIGHT, buff=0.4),
                VGroup(
                    Text("First Order:", font_size=26, color=GREEN_C),
                    MathTex(r"\ln[A]_t - \ln[A]_0 = -kt", font_size=34),
                ).arrange(RIGHT, buff=0.4),
                VGroup(
                    Text("Second Order:", font_size=26, color=BLUE_B),
                    MathTex(r"\frac{1}{[A]_t} - \frac{1}{[A]_0} = +kt", font_size=34),
                ).arrange(RIGHT, buff=0.4),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            .next_to(irl_intro, DOWN, buff=0.5)
        )

        for eq in irl_equations:
            self.play(FadeIn(eq, shift=RIGHT * 0.3), run_time=0.7)

        var_note = (
            VGroup(
                Text("t = time,  k = rate constant", font_size=22, color=GRAY_B),
                Text(
                    "[A]₀ = initial concentration (constant, acts as y-intercept)",
                    font_size=22,
                    color=GRAY_B,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.15)
            .next_to(irl_equations, DOWN, buff=0.4)
        )
        self.play(FadeIn(var_note))
        self.next_slide()

        # ================================
        # SLIDE 6: Linear Plot Forms
        # ================================
        self.play(FadeOut(irl_intro), FadeOut(irl_equations), FadeOut(var_note))

        linear_title = Text(
            "Linear Plot Forms  (y = mx + b)", font_size=36, color=YELLOW
        ).next_to(title2, DOWN, buff=0.5)
        self.play(Write(linear_title))

        linear_rows = (
            VGroup(
                VGroup(
                    Text("Zero:", font_size=24, color=RED),
                    MathTex(r"[A]_t = -kt + [A]_0", font_size=28),
                    Text("  →  Plot [A] vs t", font_size=22, color=GRAY_B),
                ).arrange(RIGHT, buff=0.3),
                VGroup(
                    Text("First:", font_size=24, color=GREEN_C),
                    MathTex(r"\ln[A]_t = -kt + \ln[A]_0", font_size=28),
                    Text("  →  Plot ln[A] vs t", font_size=22, color=GRAY_B),
                ).arrange(RIGHT, buff=0.3),
                VGroup(
                    Text("Second:", font_size=24, color=BLUE_B),
                    MathTex(r"\frac{1}{[A]_t} = kt + \frac{1}{[A]_0}", font_size=28),
                    Text("  →  Plot 1/[A] vs t", font_size=22, color=GRAY_B),
                ).arrange(RIGHT, buff=0.3),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.45)
            .next_to(linear_title, DOWN, buff=0.5)
        )

        for row in linear_rows:
            self.play(FadeIn(row), run_time=0.7)

        linear_note = Text(
            "Only the correct order gives a straight line.\n"
            "Curved plots mean you chose the wrong order.",
            font_size=24,
            color=ORANGE,
        ).next_to(linear_rows, DOWN, buff=0.5)
        self.play(FadeIn(linear_note))
        self.next_slide()

        # ================================
        # SLIDE 7: Concentration vs Time Graphs
        # ================================
        self.play(FadeOut(linear_title), FadeOut(linear_rows), FadeOut(linear_note))

        graph_title = Text(
            "Concentration vs. Time Graphs", font_size=38, color=YELLOW
        ).next_to(title2, DOWN, buff=0.4)
        self.play(Write(graph_title))

        ax_cfg = {
            "x_range": [0, 5, 1],
            "y_range": [0, 3, 1],
            "x_length": 3.2,
            "y_length": 2.5,
            "axis_config": {"include_numbers": False, "include_ticks": False},
        }

        # --- Zero Order ---
        ax0 = Axes(**ax_cfg)
        lbl0_x = ax0.get_x_axis_label("t", direction=DOWN, buff=0.5)
        lbl0_y = ax0.get_y_axis_label("[A]", direction=LEFT, buff=0.5)
        curve0 = ax0.plot(lambda x: max(2.5 - 0.5 * x, 0), x_range=[0, 5], color=RED)
        title0 = Text("Zero Order", font_size=20, color=RED).next_to(
            ax0, DOWN, buff=0.15
        )
        g0 = VGroup(ax0, lbl0_x, lbl0_y, curve0, title0)

        # --- First Order ---
        ax1 = Axes(**ax_cfg)
        lbl1_x = ax1.get_x_axis_label("t", direction=DOWN, buff=0.5)
        lbl1_y = ax1.get_y_axis_label("[A]", direction=LEFT, buff=0.5)
        curve1 = ax1.plot(
            lambda x: 2.5 * np.exp(-0.5 * x), x_range=[0, 5], color=GREEN_C
        )
        title1 = Text("First Order", font_size=20, color=GREEN_C).next_to(
            ax1, DOWN, buff=0.15
        )
        g1 = VGroup(ax1, lbl1_x, lbl1_y, curve1, title1)

        # --- Second Order ---
        ax2 = Axes(**ax_cfg)
        lbl2_x = ax2.get_x_axis_label("t", direction=DOWN, buff=0.5)
        lbl2_y = ax2.get_y_axis_label("[A]", direction=LEFT, buff=0.5)
        curve2 = ax2.plot(
            lambda x: 2.5 / (1 + 2.5 * 0.4 * x), x_range=[0, 5], color=BLUE_B
        )
        title2_g = Text("Second Order", font_size=20, color=BLUE_B).next_to(
            ax2, DOWN, buff=0.15
        )
        g2 = VGroup(ax2, lbl2_x, lbl2_y, curve2, title2_g)

        all_graphs = (
            VGroup(g0, g1, g2)
            .arrange(RIGHT, buff=0.6)
            .next_to(graph_title, DOWN, buff=0.5)
        )

        self.play(
            Create(ax0),
            Create(ax1),
            Create(ax2),
            Write(lbl0_x),
            Write(lbl0_y),
            Write(lbl1_x),
            Write(lbl1_y),
            Write(lbl2_x),
            Write(lbl2_y),
            Write(title0),
            Write(title1),
            Write(title2_g),
        )
        self.play(Create(curve0), Create(curve1), Create(curve2))

        shape_note = Text(
            "Notice how [A] vs t curves for First and Second orders.",
            font_size=22,
            color=GRAY_B,
        ).next_to(all_graphs, DOWN, buff=0.4)
        self.play(FadeIn(shape_note))
        self.next_slide()

        # ================================
        # SLIDE 8: Linearized Plot Graphs (NEW)
        # ================================
        self.play(FadeOut(graph_title), FadeOut(all_graphs), FadeOut(shape_note))

        linear_graph_title = Text(
            "The Linearized Plots", font_size=38, color=YELLOW
        ).next_to(title2, DOWN, buff=0.4)
        self.play(Write(linear_graph_title))

        # --- Linear Zero Order ---
        ax_lin0 = Axes(**ax_cfg)
        lbl_lin0_x = ax_lin0.get_x_axis_label("t", direction=DOWN, buff=0.5)
        lbl_lin0_y = ax_lin0.get_y_axis_label("[A]", direction=LEFT, buff=0.5)
        curve_lin0 = ax_lin0.plot(
            lambda x: max(2.5 - 0.5 * x, 0), x_range=[0, 5], color=RED
        )
        title_lin0 = (
            VGroup(
                Text("Zero Order", font_size=20, color=RED),
                Text("Slope = -k", font_size=16),
            )
            .arrange(DOWN, buff=0.1)
            .next_to(ax_lin0, DOWN, buff=0.15)
        )
        g_lin0 = VGroup(ax_lin0, lbl_lin0_x, lbl_lin0_y, curve_lin0, title_lin0)

        # --- Linear First Order ---
        ax_lin1 = Axes(**ax_cfg)
        lbl_lin1_x = ax_lin1.get_x_axis_label("t", direction=DOWN, buff=0.5)
        lbl_lin1_y = ax_lin1.get_y_axis_label("ln[A]", direction=LEFT, buff=0.5)
        curve_lin1 = ax_lin1.plot(
            lambda x: max(2.5 - 0.5 * x, 0), x_range=[0, 5], color=GREEN_C
        )  # Drawn straight to represent ln[A]
        title_lin1 = (
            VGroup(
                Text("First Order", font_size=20, color=GREEN_C),
                Text("Slope = -k", font_size=16),
            )
            .arrange(DOWN, buff=0.1)
            .next_to(ax_lin1, DOWN, buff=0.15)
        )
        g_lin1 = VGroup(ax_lin1, lbl_lin1_x, lbl_lin1_y, curve_lin1, title_lin1)

        # --- Linear Second Order ---
        ax_lin2 = Axes(**ax_cfg)
        lbl_lin2_x = ax_lin2.get_x_axis_label("t", direction=DOWN, buff=0.5)
        lbl_lin2_y = ax_lin2.get_y_axis_label("1/[A]", direction=LEFT, buff=0.5)
        curve_lin2 = ax_lin2.plot(
            lambda x: 0.5 + 0.5 * x, x_range=[0, 5], color=BLUE_B
        )  # Drawn straight to represent 1/[A]
        title_lin2 = (
            VGroup(
                Text("Second Order", font_size=20, color=BLUE_B),
                Text("Slope = +k", font_size=16),
            )
            .arrange(DOWN, buff=0.1)
            .next_to(ax_lin2, DOWN, buff=0.15)
        )
        g_lin2 = VGroup(ax_lin2, lbl_lin2_x, lbl_lin2_y, curve_lin2, title_lin2)

        all_lin_graphs = (
            VGroup(g_lin0, g_lin1, g_lin2)
            .arrange(RIGHT, buff=0.6)
            .next_to(linear_graph_title, DOWN, buff=0.5)
        )

        self.play(
            Create(ax_lin0),
            Create(ax_lin1),
            Create(ax_lin2),
            Write(lbl_lin0_x),
            Write(lbl_lin0_y),
            Write(lbl_lin1_x),
            Write(lbl_lin1_y),
            Write(lbl_lin2_x),
            Write(lbl_lin2_y),
            Write(title_lin0),
            Write(title_lin1),
            Write(title_lin2),
        )
        self.play(Create(curve_lin0), Create(curve_lin1), Create(curve_lin2))

        lin_shape_note = Text(
            "Plotting these transformations identifies the correct reaction order.",
            font_size=22,
            color=GRAY_B,
        ).next_to(all_lin_graphs, DOWN, buff=0.4)
        self.play(FadeIn(lin_shape_note))
        self.next_slide()

        # ================================
        # SLIDE 9: Half-Lives
        # ================================
        self.play(
            FadeOut(linear_graph_title),
            FadeOut(all_lin_graphs),
            FadeOut(lin_shape_note),
            FadeOut(title2),
        )

        title3 = Text("Half-Lives", color=YELLOW, font_size=52).to_edge(UP)
        self.play(Write(title3))

        hl_def = Text(
            "The time it takes for a reactant to fall to half its original concentration.",
            font_size=26,
        ).next_to(title3, DOWN, buff=0.5)
        self.play(FadeIn(hl_def))

        hl_formula_group = (
            VGroup(
                MathTex(
                    r"t_{1/2} = \frac{\ln 2}{k} \approx \frac{0.693}{k}",
                    font_size=44,
                    color=GREEN_C,
                ),
                Text(
                    "(derived from the first-order integrated rate law)",
                    font_size=20,
                    color=GRAY_B,
                ),
            )
            .arrange(DOWN, buff=0.8)
            .next_to(hl_def, DOWN, buff=0.5)
        )

        hl_box = SurroundingRectangle(hl_formula_group[0], color=GREEN_C, buff=0.25)
        self.play(Write(hl_formula_group[0]), Create(hl_box))
        self.play(FadeIn(hl_formula_group[1]))

        hl_bullets = (
            VGroup(
                Text(
                    "• First-order reactions have a CONSTANT half-life.",
                    font_size=26,
                    color=GREEN_C,
                ),
                Text("• All radioactive decay is first order.", font_size=26),
                Text(
                    "  (Often used to solve for remaining mass or elapsed time)",
                    font_size=24,
                    color=GRAY_B,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            .next_to(hl_formula_group, DOWN, buff=0.5)
        )
        for b in hl_bullets:
            self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.6)
        self.next_slide()

        # ================================
        # SLIDE 10: Half-Life Graph (First Order)
        # ================================
        self.play(
            FadeOut(hl_def),
            FadeOut(hl_formula_group),
            FadeOut(hl_box),
            FadeOut(hl_bullets),
        )

        hl_graph_title = Text(
            "First-Order Half-Life: Constant Decay", font_size=34, color=YELLOW
        ).next_to(title3, DOWN, buff=0.4)
        self.play(Write(hl_graph_title))

        k_val = 0.5
        A0 = 8.0
        hl_ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 9, 1],
            x_length=8,
            y_length=4.5,
            axis_config={
                "include_numbers": False,
                "include_ticks": True,
                "font_size": 18,
            },
        ).next_to(hl_graph_title, DOWN, buff=0.4)
        hl_x_lbl = hl_ax.get_x_axis_label("Time (s)", direction=DOWN, buff=0.6)
        hl_y_lbl = hl_ax.get_y_axis_label("[A]", direction=LEFT, buff=0.6)

        decay_curve = hl_ax.plot(
            lambda x: A0 * np.exp(-k_val * x), x_range=[0, 9.9], color=GREEN_C
        )
        self.play(Create(hl_ax), Write(hl_x_lbl), Write(hl_y_lbl))
        self.play(Create(decay_curve))

        hl_time = np.log(2) / k_val  # ≈ 1.386
        hl_points = []
        hl_dashed_lines = []
        concentrations = [A0, A0 / 2, A0 / 4, A0 / 8]
        labels_c = ["[A]₀", "[A]₀/2", "[A]₀/4", "[A]₀/8"]
        times = [0, hl_time, 2 * hl_time, 3 * hl_time]

        for i, (t, c, lbl_text) in enumerate(zip(times, concentrations, labels_c)):
            dot = Dot(hl_ax.c2p(t, c), color=YELLOW, radius=0.08)
            hl_points.append(dot)
            if i > 0:
                h_line = DashedLine(
                    hl_ax.c2p(0, c),
                    hl_ax.c2p(t, c),
                    color=YELLOW,
                    stroke_width=1.5,
                    dash_length=0.1,
                )
                v_line = DashedLine(
                    hl_ax.c2p(t, 0),
                    hl_ax.c2p(t, c),
                    color=YELLOW,
                    stroke_width=1.5,
                    dash_length=0.1,
                )
                hl_dashed_lines.extend([h_line, v_line])
            conc_lbl = Text(lbl_text, font_size=16, color=YELLOW).next_to(
                hl_ax.c2p(0, c), LEFT, buff=0.05
            )
            hl_points.append(conc_lbl)

        self.play(
            *[FadeIn(p) for p in hl_points], *[Create(l) for l in hl_dashed_lines]
        )

        hl_span_arrow = DoubleArrow(
            hl_ax.c2p(0, -0.6),
            hl_ax.c2p(hl_time, -0.6),
            color=ORANGE,
            stroke_width=2,
            tip_length=0.12,
            buff=0,
        )
        hl_span_lbl = MathTex(r"t_{1/2}", font_size=22, color=ORANGE).next_to(
            hl_span_arrow, DOWN, buff=0.05
        )
        self.play(Create(hl_span_arrow), Write(hl_span_lbl))
        self.next_slide()

        # ================================
        # SLIDE 11: Summary
        # ================================
        self.play(
            FadeOut(hl_graph_title),
            FadeOut(hl_ax),
            FadeOut(hl_x_lbl),
            FadeOut(hl_y_lbl),
            FadeOut(decay_curve),
            *[FadeOut(p) for p in hl_points],
            *[FadeOut(l) for l in hl_dashed_lines],
            FadeOut(hl_span_arrow),
            FadeOut(hl_span_lbl),
        )

        summary_title = Text("Key Takeaways", font_size=40, color=YELLOW).next_to(
            title3, DOWN, buff=0.5
        )
        self.play(Write(summary_title))

        summary_points = (
            VGroup(
                Text(
                    "• Rate = k[A]ᵐ[B]ⁿ  —  orders from experiment, NOT coefficients.",
                    font_size=24,
                    color=WHITE,
                ),
                Text(
                    "• k changes with temperature or catalyst; orders do not.",
                    font_size=24,
                    color=BLUE_B,
                ),
                Text(
                    "• Integrated laws link [A] and t; the correct order gives a straight line.",
                    font_size=24,
                    color=GREEN_C,
                ),
                Text(
                    "• First-order half-life: t₁/₂ = 0.693/k  (constant, independent of [A]).",
                    font_size=24,
                    color=GREEN_C,
                ),
                Text(
                    "• All radioactive decay is first order.",
                    font_size=24,
                    color=ORANGE,
                ),
                Text(
                    "• Units of k depend on overall order so Rate always has units of M/s.",
                    font_size=24,
                    color=GRAY_B,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            .next_to(summary_title, DOWN, buff=0.4)
        )

        summary_bg = Rectangle(
            width=summary_points.width + 0.6,
            height=summary_points.height + 0.4,
            color=DARK_GRAY,
            fill_opacity=0.5,
        ).move_to(summary_points.get_center())

        self.play(FadeIn(summary_bg))
        for pt in summary_points:
            self.play(FadeIn(pt, shift=RIGHT * 0.2), run_time=0.5)
        self.next_slide()
