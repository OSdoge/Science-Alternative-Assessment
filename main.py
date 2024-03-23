"""
main.py

*** animation things and such ***
"""

import os

from manim import MathTex, Scene, Text, TexTemplate

from src.titlecard import TitleCard

assets = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")


class Main(Scene):
    """the final video."""

    def set_font(self):
        """Set the fonts used in the video."""
        Text.set_default(font="erewhon")
        preamble = TexTemplate()
        preamble.add_to_preamble(
            "\\usepackage{fourier}\n\\usepackage{tgheros}\n\\usepackage{siunitx}",
            prepend=True,
        )
        MathTex.set_default(tex_template=preamble)

    def construct(self):
        """this is the function where everything comes together."""
        self.set_font()
        self.add_sound(os.path.join(assets, "Zeta.mp3"))
        TitleCard.construct(self)
