from manim import *
from manim_slides import Slide


class ReactionRates(Slide):
    def construct(self):
        # =========================
        # TITLE SEQUENCE
        # =========================
        title = Text("Reaction Rates", font_size=64)

        self.play(Write(title))
        self.next_slide()

        self.play(title.animate.shift(UP * 3.5 + LEFT * 4.6).scale(0.7))

        # =========================
        # SLIDE 1: The Basics
        # =========================
        basics_group = VGroup(
            Text("• Units: Molarity / time (s, min, hr)", font_size=36),
            Text("• Focus: Aqueous (aq) & Gases (g)", font_size=36),
            Text("• Exclude: Solids (s) & Liquids (l)", font_size=36, color=RED_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(FadeIn(basics_group, shift=UP))
        self.next_slide()

        # =========================
        # SLIDE 2: The Math (WITH TANGENT GRAPH)
        # =========================
        self.play(FadeOut(*self.mobjects[1:]))

        math_title = Text("Calculating Rate", color=YELLOW).shift(UP)
        rate_eq = MathTex(
            r"\text{Rate} = -\text{slope of tangent} = -\frac{\Delta[\text{Reactant}]}{\Delta t}",
            font_size=40,
        ).next_to(math_title, DOWN, buff=0.3)

        self.play(FadeIn(math_title))
        self.play(Write(rate_eq))

        self.next_slide()

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": False, "font_size": 24},
        ).shift(DOWN * 0.7)

        labels = axes.get_axis_labels(x_label="Time (s)", y_label="[Reactant] (M)")

        # 2. Plot Reactant Concentration Curve (Exponential Decay)
        curve = axes.plot(lambda x: 4.5 * np.exp(-0.8 * x), color=BLUE)
        curve_label = (
            Text("Reactant", font_size=24, color=BLUE).next_to(curve, RIGHT).shift(UP)
        )
        self.play(math_title.animate.shift(UP * 10), rate_eq.animate.shift(UP * 2.5))
        self.play(Create(axes), Write(labels))
        self.play(Create(curve), FadeIn(curve_label))
        self.next_slide()

        # 3. Calculate and Draw Tangent Line at x = 1.5
        x_val = 1.5
        y_val = 4.5 * np.exp(-0.8 * x_val)
        slope = -0.8 * 4.5 * np.exp(-0.8 * x_val)  # Derivative of the curve

        tangent_line = axes.plot(
            lambda x: slope * (x - x_val) + y_val,
            x_range=[0.2, 3.5],  # Bound the line so it doesn't overshoot the axes
            color=YELLOW,
        )

        # Point of tangency
        dot = Dot(axes.c2p(x_val, y_val), color=RED)
        tangent_label = Text("Tangent Line", font_size=24, color=YELLOW).next_to(
            tangent_line, DOWN, buff=0.1
        )

        self.play(FadeIn(dot))
        self.play(Create(tangent_line))
        self.play(Write(tangent_label))
        self.next_slide()

        # =========================
        # SLIDE 3: Stoichiometry & Relative Rates
        # =========================
        self.play(FadeOut(*self.mobjects[1:]))

        rxn = MathTex(r"2A + 3B \rightarrow 4C + D", font_size=56, color=BLUE)
        rxn.shift(UP * 1.5)

        rel_rates = MathTex(
            r"\text{Rate} = -\frac{1}{2}\frac{\Delta[A]}{\Delta t} = -\frac{1}{3}\frac{\Delta[B]}{\Delta t} = +\frac{1}{4}\frac{\Delta[C]}{\Delta t} = +\frac{\Delta[D]}{\Delta t}",
            font_size=36,
        )

        self.play(Write(rxn))
        self.play(FadeIn(rel_rates, shift=UP))
        self.next_slide(auto_next=True)

        # =========================
        # SLIDE 4: Speeding it Up
        # =========================
        self.play(FadeOut(*self.mobjects[1:]))

        speed_title = Text("How to Speed Up a Reaction:", color=YELLOW).shift(UP * 2)
        speed_factors = (
            VGroup(
                Text("1. Add Heat (Temperature)", font_size=36),
                Text("2. Increase Surface Area", font_size=36),
                Text("3. Increase Concentration / Pressure", font_size=36),
                Text("4. Add a Catalyst", font_size=36, color=GREEN_C),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            .next_to(speed_title, DOWN, buff=0.5)
        )

        self.play(FadeIn(speed_title))
        self.play(Write(speed_factors))

        # 1. Turn it red BEFORE starting the loop!
        heat_text = speed_factors[0]
        self.play(heat_text.animate.set_color(RED))

        # --- START OF THE LOOPED VIDEO SEGMENT ---
        self.next_slide(loop=True)

        # Setup base properties
        heat_text.base_center = heat_text.get_center()
        heat_text.time = 0

        sa_text = speed_factors[1]
        sa_text.base_height = sa_text.height
        sa_text.base_left = sa_text.get_left()

        # High-frequency math for a seamless shake
        def heat_updater(m, dt):
            m.time += dt
            # Using sin/cos with a multiple of 2*PI ensures it loops perfectly at t=1 second
            x_shake = 0.04 * np.sin(m.time * 10 * PI)
            y_shake = 0.04 * np.cos(m.time * 10 * PI)
            m.move_to(m.base_center + np.array([x_shake, y_shake, 0]))

        heat_text.add_updater(heat_updater)
        self.wait(1)
        self.next_slide()

        heat_text.clear_updaters()
        # =========================
        # SLIDE 5: Collision Theory
        # =========================
        self.play(FadeOut(*self.mobjects[1:]))

        collision_title = Text("Collision Theory", color=YELLOW).shift(UP * 2.5)

        collision_bullets = (
            VGroup(
                Text("• Particles must collide to react.", font_size=36),
                Text("• Require sufficient energy (Activation Energy).", font_size=36),
                Text("• Molecules must have the proper orientation.", font_size=36),
                Text(
                    '➔ Results in an "Effective Collision"', font_size=36, color=GREEN_C
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            .next_to(collision_title, DOWN, buff=0.5)
        )

        self.play(FadeIn(collision_title))
        self.play(Write(collision_bullets), run_time=7)
        self.next_slide()

        # Visualizing an Effective Collision
        particle_a = Circle(radius=0.5, color=BLUE, fill_opacity=0.8).shift(
            LEFT * 4 + DOWN * 2.25
        )
        particle_b = Circle(radius=0.5, color=RED, fill_opacity=0.8).shift(
            RIGHT * 4 + DOWN * 2.25
        )

        a_label = Text("A", font_size=24).move_to(particle_a.get_center())
        b_label = Text("B", font_size=24).move_to(particle_b.get_center())

        group_a = VGroup(particle_a, a_label)
        group_b = VGroup(particle_b, b_label)

        self.play(FadeIn(group_a), FadeIn(group_b))

        # Animate particles crashing into each other
        self.play(
            group_a.animate.shift(RIGHT * 3.5),
            group_b.animate.shift(LEFT * 3.5),
            rate_func=rush_into,
            run_time=0.8,
        )

        # The reaction (effective collision)
        flash = Star(color=YELLOW, outer_radius=1.2, inner_radius=0.6).shift(
            DOWN * 2.25
        )
        product = Circle(radius=0.7, color=PURPLE, fill_opacity=0.8).shift(DOWN * 2.25)
        ab_label = Text("AB", font_size=28).move_to(product.get_center())
        group_product = VGroup(product, ab_label)

        self.play(
            FadeIn(flash, scale=0.5), FadeOut(group_a), FadeOut(group_b), run_time=0.1
        )
        self.play(Transform(flash, group_product), run_time=0.5)
        self.next_slide()
