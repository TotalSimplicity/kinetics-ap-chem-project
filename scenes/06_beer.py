import numpy as np
from manim import *
from manim_slides import Slide


class BeersLawAPChem(Slide):
    def construct(self):

        # =========================
        # SLIDE 1: Intro to Beer's Law
        # =========================
        title = Text("Beer-Lambert Law", color=YELLOW, font_size=56).to_edge(UP)
        self.play(Write(title))

        definition = Text(
            "Relates the amount of light absorbed by a solution to its concentration.",
            font_size=26,
            color=WHITE,
        ).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(definition, shift=UP))

        formula_box = SurroundingRectangle(
            MathTex(r"A = \epsilon b c", font_size=56, color=GREEN_C),
            buff=0.3,
            color=GREEN_C,
        )
        formula = MathTex(r"A = \epsilon b c", font_size=56, color=GREEN_C)
        formula_group = VGroup(formula, formula_box).next_to(definition, DOWN, buff=0.5)
        self.play(Write(formula), Create(formula_box))

        term_bullets = (
            VGroup(
                Text(
                    "• A  — Absorbance: Measured by a spectrophotometer (no units).",
                    font_size=24,
                ),
                Text(
                    "• ε  — Molar Absorptivity: How strongly the chemical absorbs light.",
                    font_size=24,
                ),
                Text(
                    "       Specific to the solute and wavelength used (units: M⁻¹cm⁻¹).",
                    font_size=22,
                    color=GRAY_B,
                ),
                Text(
                    "• b  — Path Length: Width of the cuvette (usually 1.0 cm).",
                    font_size=24,
                ),
                Text(
                    "• c  — Concentration: Molarity of the colored solution (M).",
                    font_size=24,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            .next_to(formula_group, DOWN, buff=0.6)
        )
        self.play(FadeIn(term_bullets, shift=UP))
        self.next_slide()

        # =========================
        # SLIDE 2: How It Works
        # =========================
        self.play(FadeOut(definition), FadeOut(formula_group), FadeOut(term_bullets))

        mechanism_title = Text(
            "The Spectrophotometer", font_size=40, color=YELLOW
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(mechanism_title))

        # Simple diagram of light passing through a cuvette
        light_source = Circle(radius=0.4, color=YELLOW, fill_opacity=0.8)
        light_label = Text("Light", font_size=16, color=BLACK).move_to(light_source)
        source_group = VGroup(light_source, light_label).shift(LEFT * 4)

        cuvette = Rectangle(width=1.5, height=2.5, color=BLUE, fill_opacity=0.3)
        cuvette_label = Text("Sample (c)", font_size=20).move_to(cuvette)
        path_label = Text("Width = b", font_size=16, color=GRAY_B).next_to(
            cuvette, DOWN
        )
        cuvette_group = VGroup(cuvette, cuvette_label, path_label)

        detector = Square(side_length=1.0, color=GRAY, fill_opacity=0.8).shift(
            RIGHT * 4
        )
        detector_label = Text("Detector", font_size=16, color=BLACK).move_to(detector)
        detector_group = VGroup(detector, detector_label)

        arrow_in = Arrow(
            start=source_group.get_right(),
            end=cuvette.get_left(),
            color=YELLOW,
            stroke_width=6,
        )
        arrow_in_label = MathTex(r"I_0", font_size=24).next_to(arrow_in, UP)

        # Thinner arrow coming out to represent absorbed light
        arrow_out = Arrow(
            start=cuvette.get_right(),
            end=detector.get_left(),
            color=YELLOW,
            stroke_width=2,
        )
        arrow_out_label = MathTex(r"I", font_size=24).next_to(arrow_out, UP)

        diagram = VGroup(
            source_group,
            cuvette_group,
            detector_group,
            arrow_in,
            arrow_in_label,
            arrow_out,
            arrow_out_label,
        )
        diagram.next_to(mechanism_title, DOWN, buff=0.8)

        self.play(FadeIn(cuvette_group), FadeIn(detector_group), FadeIn(source_group))
        self.play(GrowArrow(arrow_in), Write(arrow_in_label))
        self.play(GrowArrow(arrow_out), Write(arrow_out_label))

        transmittance_eq = MathTex(
            r"\text{Transmittance } (T) = \frac{I}{I_0}", font_size=32
        )
        absorbance_eq = MathTex(
            r"\text{Absorbance } (A) = -\log(T)", font_size=32, color=BLUE_B
        )

        eq_group = (
            VGroup(transmittance_eq, absorbance_eq)
            .arrange(DOWN, buff=0.3)
            .next_to(diagram, DOWN, buff=0.6)
        )

        self.play(Write(transmittance_eq))
        self.play(Write(absorbance_eq))
        self.next_slide()

        # =========================
        # SLIDE 3: The Calibration Curve
        # =========================
        self.play(FadeOut(mechanism_title), FadeOut(diagram), FadeOut(eq_group))

        curve_title = Text("The Calibration Curve", font_size=40, color=YELLOW).next_to(
            title, DOWN, buff=0.4
        )
        self.play(Write(curve_title))

        cal_ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 1.5, 0.5],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True, "font_size": 18},
        ).next_to(curve_title, DOWN, buff=0.4)

        cal_x_lbl = cal_ax.get_x_axis_label(
            "Concentration (M)", direction=DOWN, buff=0.5
        )
        cal_y_lbl = cal_ax.get_y_axis_label("Absorbance", direction=LEFT, buff=0.5)

        self.play(Create(cal_ax), Write(cal_x_lbl), Write(cal_y_lbl))

        # Standard solutions (Data points)
        c_vals = [0.0, 1.0, 2.0, 3.0, 4.0]
        a_vals = [0.0, 0.28, 0.55, 0.86, 1.12]
        dots = VGroup(
            *[Dot(cal_ax.c2p(c, a), color=GREEN_C) for c, a in zip(c_vals, a_vals)]
        )

        self.play(FadeIn(dots, lag_ratio=0.2))

        # Line of best fit
        line_of_fit = cal_ax.plot(lambda x: 0.28 * x, x_range=[0, 4.5], color=YELLOW)
        self.play(Create(line_of_fit))

        curve_note = Text(
            "Directly proportional: A linear plot passing through the origin.",
            font_size=22,
            color=GRAY_B,
        ).next_to(cal_ax, DOWN, buff=0.6)
        self.play(FadeIn(curve_note))
        self.next_slide()

        # ==========================================
        # SLIDE 4: Selecting the Optimum Wavelength
        # ==========================================
        self.play(
            FadeOut(curve_title),
            FadeOut(cal_ax),
            FadeOut(cal_x_lbl),
            FadeOut(cal_y_lbl),
            FadeOut(dots),
            FadeOut(line_of_fit),
            FadeOut(curve_note),
        )

        lambda_title = Text(
            "Selecting Wavelength (λ)", font_size=40, color=YELLOW
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(lambda_title))

        spec_ax = Axes(
            x_range=[300, 800, 100],
            y_range=[0, 1.2, 0.4],
            x_length=7,
            y_length=3.5,
            axis_config={"include_numbers": True, "font_size": 18},
        ).next_to(lambda_title, DOWN, buff=0.4)

        spec_x_lbl = spec_ax.get_x_axis_label(
            "Wavelength (nm)", direction=DOWN, buff=0.5
        )
        spec_y_lbl = spec_ax.get_y_axis_label("Absorbance", direction=LEFT, buff=0.5)

        # Draw an absorption spectrum (bell-like curve)
        spectrum_curve = spec_ax.plot(
            lambda x: 1.0 * np.exp(-0.00015 * (x - 520) ** 2) + 0.1,
            x_range=[350, 750],
            color=RED,
        )

        self.play(Create(spec_ax), Write(spec_x_lbl), Write(spec_y_lbl))
        self.play(Create(spectrum_curve))

        # Maximum absorbance line
        max_x, max_y = 520, 1.1
        max_dot = Dot(spec_ax.c2p(max_x, max_y), color=YELLOW)
        v_line = DashedLine(
            spec_ax.c2p(max_x, 0),
            spec_ax.c2p(max_x, max_y),
            color=YELLOW,
        )
        lambda_max_lbl = MathTex(
            r"\lambda_{max} = 520 \text{ nm}", font_size=24, color=YELLOW
        ).next_to(max_dot, UP)

        self.play(FadeIn(max_dot), Create(v_line), Write(lambda_max_lbl))

        lambda_rule = (
            VGroup(
                Text(
                    "Always set the spectrophotometer to the wavelength of maximum absorbance.",
                    font_size=20,
                ),
                Text(
                    "This provides the highest sensitivity and minimizes measurement error.",
                    font_size=20,
                    color=GREEN_C,
                ),
            )
            .arrange(DOWN, buff=0.15)
            .next_to(spec_ax, DOWN, buff=0.6)
        )
        self.play(FadeIn(lambda_rule))
        self.next_slide()

        # ==========================================
        # SLIDE 5: AP Chemistry - Common Errors
        # ==========================================
        self.play(
            FadeOut(lambda_title),
            FadeOut(spec_ax),
            FadeOut(spec_x_lbl),
            FadeOut(spec_y_lbl),
            FadeOut(spectrum_curve),
            FadeOut(max_dot),
            FadeOut(v_line),
            FadeOut(lambda_max_lbl),
            FadeOut(lambda_rule),
        )

        errors_title = Text(
            "Common Experimental Errors", font_size=38, color=RED
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(errors_title))

        error_table_data = [
            ["Error in Lab", "Effect on Absorbance", "Effect on Calculated [c]"],
            [
                "Fingerprints / scratches on cuvette",
                "Increases (scatters light)",
                "Too High",
            ],
            [
                "Cuvette washed with water, not dried",
                "Decreases (dilutes sample)",
                "Too Low",
            ],
            [
                "Solution is too concentrated",
                "Fails to follow Beer's Law linearly",
                "Inaccurate (curve flattens)",
            ],
        ]

        col_widths = [4.5, 3.5, 3.5]
        rows = []
        for r_idx, row in enumerate(error_table_data):
            row_group = VGroup()
            for c_idx, cell in enumerate(row):
                if r_idx == 0:
                    mob = Text(cell, font_size=20, color=YELLOW)
                else:
                    color = WHITE
                    if c_idx == 2:
                        color = (
                            RED_B if "High" in cell or "Inaccurate" in cell else BLUE_B
                        )
                    mob = Text(cell, font_size=18, color=color)

                mob.set_width(min(mob.width, col_widths[c_idx] - 0.3))
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
            VGroup(*rows).arrange(DOWN, buff=0.6).next_to(errors_title, DOWN, buff=0.7)
        )

        underline = Line(
            table_group[0].get_left() + LEFT * 0.2,
            table_group[0].get_right() + RIGHT * 0.2,
            color=YELLOW,
            stroke_width=1.5,
        ).next_to(table_group[0], DOWN, buff=0.2)

        self.play(FadeIn(table_group[0]), Create(underline))
        for row in rows[1:]:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.6)

        logic_note = MathTex(
            r"\text{Logic: If Absorbance (A) reads artificially high, } A = \epsilon b c \text{ means calculated } c \text{ is artificially high.}",
            font_size=22,
            color=GRAY_B,
        ).next_to(table_group, DOWN, buff=0.8)
        self.play(Write(logic_note))
        self.next_slide()

        # ================================
        # SLIDE 6: Summary
        # ================================
        self.play(
            FadeOut(errors_title),
            FadeOut(table_group),
            FadeOut(underline),
            FadeOut(logic_note),
            FadeOut(title),
        )

        summary_title = Text(
            "Beer's Law: Key Takeaways", font_size=44, color=YELLOW
        ).to_edge(UP)
        self.play(Write(summary_title))

        summary_points = (
            VGroup(
                Text(
                    "• A = εbc shows a direct, linear relationship between Absorbance and Concentration.",
                    font_size=24,
                    color=WHITE,
                ),
                Text(
                    "• The spectrophotometer should be set to λ_max (wavelength of maximum absorbance).",
                    font_size=24,
                    color=GREEN_C,
                ),
                Text(
                    "• A calibration curve allows you to find the concentration of an unknown sample.",
                    font_size=24,
                    color=BLUE_B,
                ),
                Text(
                    "• Smudges, fingerprints, or water in the cuvette will alter the light absorbed,",
                    font_size=24,
                    color=RED_B,
                ),
                Text(
                    "  leading to an artificially high or low calculated concentration.",
                    font_size=22,
                    color=GRAY_B,
                ),
                Text(
                    "• Beer's Law only works well for dilute solutions. High concentrations deviate.",
                    font_size=24,
                    color=ORANGE,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            .next_to(summary_title, DOWN, buff=0.6)
        )

        summary_bg = Rectangle(
            width=summary_points.width + 0.8,
            height=summary_points.height + 0.6,
            color=DARK_GRAY,
            fill_opacity=0.5,
        ).move_to(summary_points.get_center())

        self.play(FadeIn(summary_bg))
        for pt in summary_points:
            self.play(FadeIn(pt, shift=RIGHT * 0.2), run_time=0.5)

        self.wait(1)
