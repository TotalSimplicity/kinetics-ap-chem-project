import numpy as np
from manim import *
from manim_slides import Slide


class ReactionMechanisms(Slide):
    def construct(self):

        # =========================
        # SLIDE 1: Why Mechanisms?
        # =========================
        blake = (
            ImageMobject("../assets/blake.png").scale(0.25).to_corner(DR).shift(DOWN)
        )
        self.play(FadeIn(blake, shift=UP))
        title = (
            Text("Reaction Mechanisms", color=YELLOW, font_size=56)
            .to_edge(UP)
            .shift(DOWN * 2)
        )
        self.play(Write(title))

        self.next_slide()
        self.play(title.animate.shift(UP * 2), blake.animate.scale(0.5, about_edge=DR))
        why_bullets = (
            VGroup(
                Text(
                    "• Most reactions cannot happen in a single collision.",
                    font_size=28,
                ),
                Text(
                    "• Unimolecular (1 reactant) and bimolecular (2 reactants) steps are realistic.",
                    font_size=26,
                ),
                Text(
                    "• Termolecular (3 reactants colliding at once) is extremely rare — essentially impossible.",
                    font_size=26,
                    color=RED_B,
                ),
                Text(
                    "• So complex reactions must proceed through a series of simpler steps.",
                    font_size=26,
                    color=GREEN_C,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.45)
            .next_to(title, DOWN, buff=0.7)
        )
        why_bullets.set(width=config.frame_width * 0.8)
        self.play(FadeIn(why_bullets, shift=UP))
        self.next_slide()

        # =========================
        # SLIDE 2: What is a Mechanism?
        # =========================
        self.play(FadeOut(why_bullets))

        defn_title = Text(
            "What is a Reaction Mechanism?", font_size=38, color=YELLOW
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(defn_title))

        defn_text = Text(
            "A step-by-step sequence of elementary reactions that\n"
            "together produce the overall composite reaction.",
            font_size=26,
            line_spacing=1.3,
        ).next_to(defn_title, DOWN, buff=0.5)
        self.play(FadeIn(defn_text))

        # Visual: steps → overall
        step_box_cfg = dict(width=3.8, height=0.65, color=BLUE, fill_opacity=0.15)
        step1_box = Rectangle(**step_box_cfg)
        step1_lbl = Text("Step 1:  A  →  B + C", font_size=22).move_to(step1_box)
        step2_box = Rectangle(**step_box_cfg)
        step2_lbl = Text("Step 2:  B + D  →  E", font_size=22).move_to(step2_box)
        arrow_down = Arrow(UP * 0.25, DOWN * 0.25, color=GRAY_B, stroke_width=2)
        overall_box = Rectangle(width=3.8, height=0.65, color=GREEN_C, fill_opacity=0.2)
        overall_lbl = Text(
            "Overall:  A + D  →  C + E", font_size=22, color=GREEN_C
        ).move_to(overall_box)

        steps_group = VGroup(
            VGroup(step1_box, step1_lbl),
            VGroup(step2_box, step2_lbl),
        ).arrange(DOWN, buff=0.2)
        plus_arrow = Arrow(
            steps_group.get_bottom() + DOWN * 0.05,
            steps_group.get_bottom() + DOWN * 0.6,
            color=GRAY_B,
            stroke_width=2,
        )
        overall_group = VGroup(overall_box, overall_lbl).next_to(
            plus_arrow, DOWN, buff=0.05
        )

        diagram = VGroup(steps_group, plus_arrow, overall_group).next_to(
            defn_text, DOWN, buff=0.4
        )
        self.play(
            FadeIn(VGroup(step1_box, step1_lbl)),
            FadeIn(VGroup(step2_box, step2_lbl)),
        )
        self.play(Create(plus_arrow))
        self.play(FadeIn(overall_group))

        intermediate_note = Text(
            "B is an intermediate — formed in Step 1, consumed in Step 2,\nnot in the overall equation.",
            font_size=22,
            color=ORANGE,
            line_spacing=1.2,
        ).next_to(diagram, DOWN, buff=0.35)
        self.play(FadeIn(intermediate_note))
        self.next_slide()

        # =========================
        # SLIDE 3: Elementary Steps vocab
        # =========================
        self.play(
            FadeOut(defn_title),
            FadeOut(defn_text),
            FadeOut(diagram),
            FadeOut(intermediate_note),
        )

        vocab_title = Text(
            "Elementary Steps — Key Terms", font_size=38, color=YELLOW
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(vocab_title))

        terms = (
            VGroup(
                VGroup(
                    Text("Elementary Step", font_size=26, color=BLUE_B),
                    Text(
                        "A single bond-breaking or bond-forming event.\n"
                        "The molecularity equals the number of reactant particles.",
                        font_size=23,
                        color=WHITE,
                        line_spacing=1.2,
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
                VGroup(
                    Text("Intermediate", font_size=26, color=ORANGE),
                    Text(
                        "A species produced in one step and consumed in a later step.\n"
                        "Does NOT appear in the overall balanced equation.",
                        font_size=23,
                        color=WHITE,
                        line_spacing=1.2,
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
                VGroup(
                    Text("Rate-Determining Step  (RDS)", font_size=26, color=RED),
                    Text(
                        "The SLOWEST elementary step — acts as the bottleneck.\n"
                        "Has the highest activation energy. Sets the overall rate.",
                        font_size=23,
                        color=WHITE,
                        line_spacing=1.2,
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            .next_to(vocab_title, DOWN, buff=0.5)
        )

        for term in terms:
            self.play(FadeIn(term, shift=RIGHT * 0.3), run_time=0.7)
        self.next_slide()

        # =========================
        # SLIDE 4: Finding the Rate Law from a Mechanism
        # =========================
        self.play(FadeOut(vocab_title), FadeOut(terms))

        rds_title = Text(
            "Finding the Rate Law from a Mechanism", font_size=36, color=YELLOW
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(rds_title))

        case1_header = Text(
            "Case 1 — RDS is the FIRST step:", font_size=28, color=GREEN_C
        ).next_to(rds_title, DOWN, buff=0.5)
        case1_body = (
            VGroup(
                Text("Write the rate law directly from the RDS.", font_size=24),
                Text(
                    "Coefficients in that step become the exponents.",
                    font_size=24,
                    color=GRAY_B,
                ),
                MathTex(
                    r"A + B \xrightarrow{\text{slow}} \text{products} \quad \Rightarrow \quad \text{Rate} = k[A][B]",
                    font_size=30,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            .next_to(case1_header, DOWN, buff=0.3)
        )
        self.play(Write(case1_header))
        self.play(FadeIn(case1_body))
        self.next_slide()

        case2_header = Text(
            "Case 2 — RDS is a LATER step:", font_size=28, color=ORANGE
        ).next_to(case1_body, DOWN, buff=0.45)
        case2_body = (
            VGroup(
                Text("1.  Write the rate law from the RDS.", font_size=24),
                Text(
                    "2.  Intermediates appear in the rate law — you must eliminate them.",
                    font_size=24,
                    color=ORANGE,
                ),
                Text(
                    "3.  Use the equilibrium expression from the step(s) before to substitute.",
                    font_size=24,
                ),
                Text(
                    "4.  Cancel intermediates; simplify to get a rate law in terms of reactants only.",
                    font_size=24,
                    color=GRAY_B,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .next_to(case2_header, DOWN, buff=0.3)
        )
        self.play(Write(case2_header))
        self.play(FadeIn(case2_body))
        self.next_slide()

        # =========================
        # SLIDE 5: Worked Example — RDS not first
        # =========================
        self.play(
            FadeOut(rds_title),
            FadeOut(case1_header),
            FadeOut(case1_body),
            FadeOut(case2_header),
            FadeOut(case2_body),
        )

        ex_title = Text(
            "Worked Example — RDS is Step 2", font_size=36, color=YELLOW
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(ex_title))

        mechanism = (
            VGroup(
                MathTex(
                    r"\text{Step 1 (fast):} \quad A + B \rightleftharpoons C \quad \text{(intermediate)}",
                    font_size=28,
                ),
                MathTex(
                    r"\text{Step 2 (slow/RDS):} \quad C + B \rightarrow \text{products}",
                    font_size=28,
                    color=RED,
                ),
                MathTex(
                    r"\text{Overall:} \quad A + 2B \rightarrow \text{products}",
                    font_size=28,
                    color=GREEN_C,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            .next_to(ex_title, DOWN, buff=0.5)
        )

        self.play(FadeIn(mechanism))

        steps_label = Text("Working through it:", font_size=26, color=YELLOW).next_to(
            mechanism, DOWN, buff=0.4
        )
        work_steps = (
            VGroup(
                MathTex(
                    r"1.\ \text{Rate} = k_2 [C][B] \quad \leftarrow \text{from RDS, but C is intermediate}",
                    font_size=24,
                ),
                MathTex(
                    r"2.\ K_{eq} = \frac{[C]}{[A][B]} \quad \Rightarrow \quad [C] = K_{eq}[A][B]",
                    font_size=24,
                ),
                MathTex(
                    r"3.\ \text{Rate} = k_2 K_{eq} [A][B][B] = k[A][B]^2",
                    font_size=24,
                    color=GREEN_C,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            .next_to(steps_label, DOWN, buff=0.25)
        )

        self.play(Write(steps_label))
        for step in work_steps:
            self.play(FadeIn(step, shift=RIGHT * 0.3), run_time=0.7)
        self.next_slide()

        # =========================
        # SLIDE 6: Reaction Order Visual
        # =========================
        self.play(
            FadeOut(ex_title),
            FadeOut(mechanism),
            FadeOut(steps_label),
            FadeOut(work_steps),
            FadeOut(title),
        )

        title2 = Text("Reaction Order", color=YELLOW, font_size=52).to_edge(UP)
        self.play(Write(title2))

        order_intro = Text(
            "Describes how the concentration of a reactant affects the reaction rate.",
            font_size=26,
        ).next_to(title2, DOWN, buff=0.4)
        self.play(FadeIn(order_intro))

        ax_cfg = {
            "x_range": [0, 5, 1],
            "y_range": [0, 6, 1],
            "x_length": 3.2,
            "y_length": 2.8,
            "axis_config": {"include_numbers": False, "include_ticks": False},
        }

        # --- Zero Order ---
        ax0 = Axes(**ax_cfg)
        c0 = ax0.plot(lambda x: 3.0, x_range=[0.1, 4.9], color=RED)
        lbl0_x = ax0.get_x_axis_label("[A]", direction=DOWN)
        lbl0_y = ax0.get_y_axis_label("Rate", direction=LEFT)
        t0 = Text("Zero Order", font_size=20, color=RED).next_to(ax0, DOWN, buff=0.1)
        note0 = Text("Rate = k\nNo effect", font_size=17, color=GRAY_B).next_to(
            t0, DOWN, buff=0.1
        )
        g0 = VGroup(ax0, c0, lbl0_x, lbl0_y, t0, note0)

        # --- First Order ---
        ax1 = Axes(**ax_cfg)
        c1 = ax1.plot(lambda x: 1.1 * x, x_range=[0.1, 4.9], color=GREEN_C)
        lbl1_x = ax1.get_x_axis_label("[A]", direction=DOWN)
        lbl1_y = ax1.get_y_axis_label("Rate", direction=LEFT)
        t1 = Text("First Order", font_size=20, color=GREEN_C).next_to(
            ax1, DOWN, buff=0.1
        )
        note1 = Text(
            "Rate = k[A]\nDoubling [A] → doubles Rate", font_size=17, color=GRAY_B
        ).next_to(t1, DOWN, buff=0.1)
        g1 = VGroup(ax1, c1, lbl1_x, lbl1_y, t1, note1)

        # --- Second Order ---
        ax2 = Axes(**ax_cfg)
        c2 = ax2.plot(lambda x: 0.22 * x**2, x_range=[0.1, 4.9], color=BLUE_B)
        lbl2_x = ax2.get_x_axis_label("[A]", direction=DOWN)
        lbl2_y = ax2.get_y_axis_label("Rate", direction=LEFT)
        t2 = Text("Second Order", font_size=20, color=BLUE_B).next_to(
            ax2, DOWN, buff=0.1
        )
        note2 = Text(
            "Rate = k[A]²\nDoubling [A] → quadruples Rate", font_size=17, color=GRAY_B
        ).next_to(t2, DOWN, buff=0.1)
        g2 = VGroup(ax2, c2, lbl2_x, lbl2_y, t2, note2)

        all_graphs = (
            VGroup(g0, g1, g2)
            .arrange(RIGHT, buff=0.55)
            .next_to(order_intro, DOWN, buff=0.5)
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
            Write(t0),
            Write(t1),
            Write(t2),
        )
        self.play(Create(c0), Create(c1), Create(c2))
        self.play(FadeIn(note0), FadeIn(note1), FadeIn(note2))
        self.next_slide()

        # =========================
        # SLIDE 7: Summary
        # =========================
        self.play(FadeOut(order_intro), FadeOut(all_graphs), FadeOut(title2))

        title3 = Text("Key Takeaways", color=YELLOW, font_size=52).to_edge(UP)
        self.play(Write(title3))

        summary_points = (
            VGroup(
                Text(
                    "• Only unimolecular and bimolecular steps are realistic.",
                    font_size=24,
                ),
                Text(
                    "• A mechanism is the sequence of elementary steps that sum to the overall reaction.",
                    font_size=24,
                    color=WHITE,
                ),
                Text(
                    "• Intermediates appear and disappear within the mechanism — not in the overall equation.",
                    font_size=24,
                    color=ORANGE,
                ),
                Text(
                    "• The RDS (slowest step, highest Ea) determines the overall rate law.",
                    font_size=24,
                    color=RED,
                ),
                Text(
                    "• If RDS is step 1: rate law comes directly from it.",
                    font_size=24,
                    color=GREEN_C,
                ),
                Text(
                    "• If RDS is a later step: substitute out intermediates using prior equilibria.",
                    font_size=24,
                    color=GREEN_C,
                ),
                Text(
                    "• Zero order: flat; First order: linear; Second order: quadratic (Rate vs [A]).",
                    font_size=24,
                    color=BLUE_B,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.28)
            .next_to(title3, DOWN, buff=0.45)
        )
        summary_points.set(width=config.frame_width * 0.8)

        summary_bg = Rectangle(
            width=summary_points.width + 0.6,
            height=summary_points.height + 0.4,
            color=DARK_GRAY,
            fill_opacity=0.5,
        ).move_to(summary_points.get_center())

        self.play(FadeIn(summary_bg))
        for pt in summary_points:
            self.play(FadeIn(pt, shift=RIGHT * 0.2), run_time=0.45)
        self.next_slide()
