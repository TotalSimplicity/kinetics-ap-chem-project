import numpy as np
from manim import *
from manim_slides import Slide


class CatalystsAndDiagrams(Slide):
    def construct(self):
        # =========================
        # SLIDE 1: Catalysts Basics
        # =========================
        title = Text("Catalysts", color=YELLOW, font_size=56).to_edge(UP)
        self.play(Write(title))

        catalyst_bullets = (
            VGroup(
                Text("• Speed up reactions without being consumed.", font_size=32),
                Text(
                    "• Provide an alternate pathway with a lower activation energy.",
                    font_size=32,
                ),
                Text(
                    "• Multi-step: Present as a reactant in step 1, produced in the last step.",
                    font_size=32,
                ),
                Text(
                    "• Homogeneous (same phase as reactants) vs. Heterogeneous (different phase).",
                    font_size=32,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            .next_to(title, DOWN, buff=1)
        )

        self.play(FadeIn(catalyst_bullets, shift=UP))
        self.next_slide()

        # =========================
        # SLIDE 2: Reaction Diagrams
        # =========================
        self.play(FadeOut(catalyst_bullets))
        self.play(
            title.animate.become(
                Text("Reaction Diagrams", color=YELLOW, font_size=56).to_edge(UP)
            )
        )

        # 1. Setup Axes
        axes = Axes(
            x_range=[0, 9, 1],
            y_range=[0, 10, 1],
            x_length=7,
            y_length=4.5,
            axis_config={"include_numbers": False, "include_ticks": False},
        ).shift(DOWN * 0.5)

        labels = axes.get_axis_labels(
            x_label="Reaction Progress", y_label="Potential Energy"
        )
        self.play(Create(axes), Write(labels))
        self.next_slide()

        # 2. Plot Uncatalyzed Exothermic Reaction
        # Using a mathematical function to simulate an energy curve: peak + step down
        def exo_uncatalyzed(x):
            return 6 + 3 * np.exp(-((x - 3) ** 2)) - 4 / (1 + np.exp(-2 * (x - 4)))

        uncat_curve = axes.plot(exo_uncatalyzed, x_range=[0, 8.5], color=RED)

        reactants_lbl = Text("Reactants", font_size=20).next_to(
            axes.c2p(0.5, exo_uncatalyzed(0.5)), UP
        )
        products_lbl = Text("Products", font_size=20).next_to(
            axes.c2p(7.5, exo_uncatalyzed(7.5)), UP
        )

        self.play(Create(uncat_curve))
        self.play(FadeIn(reactants_lbl), FadeIn(products_lbl))
        self.next_slide()

        # 3. Highlight Transition State / Activated Complex
        peak_x = 2.85  # Approximate peak x-coordinate
        peak_y = exo_uncatalyzed(peak_x)

        ts_dot = Dot(axes.c2p(peak_x, peak_y), color=YELLOW)
        ts_lbl = Text(
            "Transition State\n(Activated Complex)",
            font_size=20,
            color=YELLOW,
            alignment="CENTER",
        ).next_to(ts_dot, UP)

        self.play(FadeIn(ts_dot), Write(ts_lbl))
        self.next_slide()

        # 4. Plot Catalyzed Pathway
        def exo_catalyzed(x):
            return 6 + 1.2 * np.exp(-((x - 3) ** 2)) - 4 / (1 + np.exp(-2 * (x - 4)))

        cat_curve = axes.plot(exo_catalyzed, x_range=[0, 8.5], color=GREEN_C)
        cat_lbl = Text("Catalyzed Pathway", font_size=20, color=GREEN_C).next_to(
            axes.c2p(3, exo_catalyzed(3)), DOWN, buff=0.2
        )

        self.play(Create(cat_curve))
        self.play(FadeIn(cat_lbl))
        self.next_slide()

        # 5. Core Rules / Summary Text
        summary_bg = (
            Rectangle(width=6.5, height=2, color=BLACK, fill_opacity=0.8)
            .to_corner(DR)
            .shift(UP * 0.5 + LEFT * 0.5)
        )
        summary_text = (
            VGroup(
                Text("• Slow step = highest peak (highest Ea)", font_size=20),
                Text(
                    "• Exothermic: Reactants sit higher than Products",
                    font_size=20,
                    color=BLUE_B,
                ),
                Text(
                    "• Endothermic: Reactants sit lower than Products",
                    font_size=20,
                    color=RED_B,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .move_to(summary_bg.get_center())
        )

        self.play(FadeIn(summary_bg), Write(summary_text))
        self.next_slide()
