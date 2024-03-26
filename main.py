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
        """set the fonts used in the video."""
        Text.set_default(font="erewhon")
        preamble = TexTemplate()
        preamble.add_to_preamble(
            "\\usepackage{fourier}\n\n\\usepackage{siunitx}\n\\usepackage{ragged2e}",
            prepend=True,
        )
        MathTex.set_default(tex_template=preamble)

    def play_music(self, path: str = "Zeta.mp3"):
        """play the background music."""
        self.add_sound(os.path.join(assets, path))

    def construct(self):
        """this is the function where everything comes together."""
        self.play_music()
        self.set_font()

        # start the scenes in order.
        TitleCard.construct(self)
