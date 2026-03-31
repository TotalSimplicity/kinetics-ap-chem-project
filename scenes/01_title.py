from manim import *  # pyright: ignore[reportWildcardImportFromLibrary]
from manim_slides import Slide  # pyright: ignore[reportAttributeAccessIssue]


class Title(Slide):
    def construct(self):
        title = Text("Kinetics", font_size=64)
        subtitle = Text("By Leo, Paul, Grant, and Blake", font_size=32, color=BLUE)

        title.shift(UP * 1)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))

        self.next_slide(auto_next=True)

        self.play(FadeOut(title, subtitle))
