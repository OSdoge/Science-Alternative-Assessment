"""
*** titlecard.py ***

the titlecard for the video.
"""

import os

from manim import DOWN, FadeIn, FadeOut, ImageMobject, Scene, Text, Write

assets = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "../assets"
)

assets = os.path.join(
    os.path.dirname(__file__),
    "../assets/",
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
        self.play(FadeOut(logo), run_time=2)
        self.play(FadeOut(subtitle))
