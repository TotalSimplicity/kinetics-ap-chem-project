import numpy as np
from manim import *
from manim_slides import Slide


class CatalystsAndDiagrams(Slide):
    def construct(self):
        # =========================
        # SLIDE 1: Catalysts Basics
        # =========================
        title = Text(
            "Catalysts & Reaction Diagrams", color=YELLOW, font_size=56
        ).to_edge(UP)
        self.play(Write(title))

        catalyst_bullets = (
            VGroup(
                Text("• Speed up reactions without being consumed.", font_size=32),
                Text(
                    "• Provide an alternate pathway with a lower activation energy.",
                    font_size=24,
                ),
                Text(
                    "• Multi-step: Present as a reactant in step 1, produced in the last step.",
                    font_size=24,
                ),
                Text(
                    "• Homogeneous (same phase as reactants) vs. Heterogeneous (different phase).",
                    font_size=24,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            .next_to(title, DOWN, buff=1)
        )

        self.play(FadeIn(catalyst_bullets, shift=UP))
        self.next_slide()

        # =========================
        # SLIDE 2: Focus on Catalysis (Exothermic)
        # =========================
        self.play(FadeOut(catalyst_bullets))

        # Define the original graph parameters for reuse
        ax_config = {
            "x_range": [0, 9, 1],
            "y_range": [0, 10, 1],
            "x_length": 7,
            "y_length": 4.5,
            "axis_config": {
                "include_numbers": False,
                "include_ticks": False,
                "font_size": 20,
            },
        }

        # Mathematical functions for the original (exothermic) graph
        def exo_uncatalyzed(x):
            return 6 + 3 * np.exp(-((x - 3) ** 2)) - 4 / (1 + np.exp(-2 * (x - 4)))

        def exo_catalyzed(x):
            return 6 + 1.2 * np.exp(-((x - 3) ** 2)) - 4 / (1 + np.exp(-2 * (x - 4)))

        # 1. Setup Main Axes (initially large)
        axes1 = Axes(**ax_config).shift(DOWN * 0.5)
        labels1 = axes1.get_axis_labels(
            x_label="Reaction Progress", y_label="Potential Energy"
        )
        t1_label = Text("Exothermic Reaction", font_size=28, color=BLUE).next_to(
            axes1, DOWN
        )
        graph1_all = VGroup(axes1, labels1, t1_label)

        self.play(Create(axes1), Write(labels1), Write(t1_label))

        # 2. Plot Uncatalyzed
        uncat_curve1 = axes1.plot(exo_uncatalyzed, x_range=[0, 8.5], color=RED)
        reactants_lbl1 = Text("Reactants", font_size=20).next_to(
            axes1.c2p(0.5, exo_uncatalyzed(0.5)), UP
        )
        products_lbl1 = Text("Products", font_size=20).next_to(
            axes1.c2p(7.5, exo_uncatalyzed(7.5)), UP
        )
        self.play(Create(uncat_curve1), FadeIn(reactants_lbl1), FadeIn(products_lbl1))

        # 3. Highlight Transition State
        peak_x = 2.85
        ts_dot1 = Dot(axes1.c2p(peak_x, exo_uncatalyzed(peak_x)), color=YELLOW)
        ts_lbl1 = Text(
            "TS (Uncat)",
            font_size=16,
            color=YELLOW,
        ).next_to(ts_dot1, UP * 0.4)
        self.play(FadeIn(ts_dot1), Write(ts_lbl1))

        # 4. Plot Catalyzed Pathway
        cat_curve1 = axes1.plot(exo_catalyzed, x_range=[0, 8.5], color=GREEN_C)
        cat_lbl1 = Text("Catalyzed", font_size=18, color=GREEN_C).next_to(
            axes1.c2p(4, exo_catalyzed(4)), DOWN + RIGHT, buff=0.1
        )
        self.play(Create(cat_curve1), FadeIn(cat_lbl1))

        # Group all elements of the first graph
        graph1_contents = VGroup(
            graph1_all,
            uncat_curve1,
            reactants_lbl1,
            products_lbl1,
            ts_dot1,
            ts_lbl1,
            cat_curve1,
            cat_lbl1,
        )

        self.next_slide()

        # ============================================
        # SLIDE 3: Shrink and Show Exo vs Endo Side-by-Side
        # ============================================
        # 1. Shrink and Move the first graph
        self.play(graph1_contents.animate.scale(0.6).to_corner(UL).shift(DOWN * 2.5))

        # 2. Create the second graph (Endothermic)
        # Build axes2 at the SAME config size as axes1 was originally,
        # then scale the ENTIRE group (axes + labels + title) together.
        axes2 = Axes(**ax_config)
        labels2 = axes2.get_axis_labels(
            x_label="Reaction Progress", y_label="Potential Energy"
        )
        t2_label = Text("Endothermic Reaction", font_size=28, color=RED).next_to(
            axes2, DOWN
        )
        graph2_all = VGroup(axes2, labels2, t2_label)
        # Scale and position the whole group so fonts match the first graph
        graph2_all.scale(0.6).to_corner(UR).shift(DOWN * 2.5)

        # Mathematical functions for Endothermic graph (flip the step)
        def endo_uncatalyzed(x):
            return 3 + 4 * np.exp(-((x - 3) ** 2)) + 4 / (1 + np.exp(-2 * (x - 4)))

        def endo_catalyzed(x):
            return 3 + 1.8 * np.exp(-((x - 3) ** 2)) + 4 / (1 + np.exp(-2 * (x - 4)))

        self.play(Create(axes2), Write(labels2), Write(t2_label))

        # 3. Plot Endothermic Curves
        uncat_curve2 = axes2.plot(endo_uncatalyzed, x_range=[0, 8.5], color=RED)
        cat_curve2 = axes2.plot(endo_catalyzed, x_range=[0, 8.5], color=GREEN_C)

        reactants_lbl2 = Text("Reactants", font_size=16).next_to(
            axes2.c2p(0.5, endo_uncatalyzed(0.5)), UP
        )
        products_lbl2 = Text("Products", font_size=16).next_to(
            axes2.c2p(7.5, endo_uncatalyzed(7.5)), UP
        )

        self.play(
            Create(uncat_curve2),
            Create(cat_curve2),
            FadeIn(reactants_lbl2),
            FadeIn(products_lbl2),
        )
        self.next_slide()

        graph2_contents = VGroup(
            graph2_all,
            uncat_curve2,
            reactants_lbl2,
            products_lbl2,
            cat_curve2,
        )

        # ============================================
        # SLIDE 4: Compare Ea and ΔH (Summary)
        # ============================================

        # Add arrows for Activation Energy (Ea) and Enthalpy change (ΔH)

        # Graph 1 (Exo) Annotations
        # ΔH arrow (Reactants to Products)
        r_y1 = exo_uncatalyzed(0.5)
        p_y1 = exo_uncatalyzed(7.5)
        # Coordinates must be transformed to scene space for arrows across Mobjects
        start_dh1 = axes1.c2p(7.0, r_y1)
        end_dh1 = axes1.c2p(7.0, p_y1)
        arrow_dh1 = DoubleArrow(
            start_dh1, end_dh1, color=BLUE_B, stroke_width=2, tip_length=0.1
        )
        lbl_dh1 = MathTex(r"\Delta H < 0", color=BLUE_B, font_size=20).next_to(
            arrow_dh1, RIGHT, buff=0.1
        )

        # Graph 2 (Endo) Annotations
        r_y2 = endo_uncatalyzed(0.5)
        p_y2 = endo_uncatalyzed(7.5)
        start_dh2 = axes2.c2p(7.0, r_y2)
        end_dh2 = axes2.c2p(7.0, p_y2)
        arrow_dh2 = DoubleArrow(
            start_dh2, end_dh2, color=RED_B, stroke_width=2, tip_length=0.1
        )
        lbl_dh2 = MathTex(r"\Delta H > 0", color=RED_B, font_size=20).next_to(
            arrow_dh2, RIGHT, buff=0.1
        )

        graph1_contents.add(arrow_dh1, lbl_dh1)
        graph2_contents.add(arrow_dh2, lbl_dh2)

        self.play(Create(arrow_dh1), Write(lbl_dh1), Create(arrow_dh2), Write(lbl_dh2))
        self.next_slide()

        self.play(
            graph1_contents.animate.shift(UP * 1.5),
            graph2_contents.animate.shift(UP * 1.5),
        )
        # Final Summary Text
        summary_bg = Rectangle(width=12, height=2, color=WHITE).to_edge(DOWN)
        summary_text = (
            VGroup(
                Text(
                    "• Exothermic: Releases energy. ΔH is negative. Products are stable.",
                    font_size=22,
                    color=BLUE_B,
                ),
                Text(
                    "• Endothermic: Absorbs energy. ΔH is positive. Products are less stable.",
                    font_size=22,
                    color=RED_B,
                ),
                Text(
                    "• Catalysts reduce Ea for BOTH forward and reverse reactions, maintaining ΔH.",
                    font_size=22,
                    color=GREEN_C,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .move_to(summary_bg.get_center())
        )

        self.play(FadeIn(summary_bg), Write(summary_text))
        self.next_slide()
