from manim import *
from manim_slides import Slide


class Final(Slide):
    def construct(self):
        # Your existing image
        blake = (
            ImageMobject("../assets/blake.png")
            .scale(0.4)
            .to_edge(DOWN)
            .shift(DOWN + (RIGHT))
        )

        # 1. Create the text
        bubble_text = Text("Time for some MCQs", color=BLACK).scale(0.6)

        # 2. Create the main bubble shape
        bubble_box = RoundedRectangle(
            width=bubble_text.width + 1,
            height=bubble_text.height + 0.8,
            corner_radius=0.5,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_color=WHITE,
            stroke_width=2,
        )
        bubble_text.move_to(bubble_box.get_center())

        # 3. Create the tail pointing down and right towards the image
        tail = Polygon(
            ORIGIN,
            RIGHT * 0.5,
            DOWN * 0.8 + RIGHT * 0.3,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_color=WHITE,
            stroke_width=2,
        )
        # Position the tail at the bottom right corner of the bubble box
        tail.move_to(bubble_box.get_corner(DR), aligned_edge=UL)
        # Shift slightly so it overlaps seamlessly with the rounded rectangle
        tail.shift(LEFT * 0.5 + UP * 0.3).rotate(45 * DEGREES)

        # 4. Group the components together
        speech_bubble = VGroup(tail, bubble_box, bubble_text)

        # 5. Position the entire group to the upper left of the image
        speech_bubble.next_to(blake, UL, buff=-0.4).shift(DOWN + RIGHT)

        # Add or animate into the scene
        self.play(FadeIn(blake))
        self.play(FadeIn(bubble_box, tail), Write(bubble_text))
        self.wait()
