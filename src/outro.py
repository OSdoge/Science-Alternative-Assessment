"""
*** titlecard.py ***

the titlecard for the video.
"""

import os

from manim import DOWN, FadeIn, FadeOut, ImageMobject, Scene, Succession, Tex, Text, Write

assets = os.path.join(
    os.path.dirname(__file__),
    "../assets",
)


class TitleCard(Scene):
    """titlecard."""

    def construct(self):
        """construct the titlecard."""
        logo = ImageMobject(os.path.join(assets, "logo-white.png"))
        logo.height = 5
        subtitle = Text("presents").to_edge(DOWN).shift([0, 1, 0])
        self.wait(1)
        self.play(FadeIn(logo), run_time=2)
        self.play(Write(subtitle))
        self.wait(2)
        self.play(Succession(FadeOut(logo), FadeOut(subtitle)))

        disclaimer = Tex(r"All animations are computer-generated and coded out manually.")
        self.play(FadeIn(disclaimer))
        self.wait(1)
        self.play(FadeOut(disclaimer))
        self.wait(1)
