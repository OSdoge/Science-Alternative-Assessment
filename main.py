"""
main.py

*** animation things and such ***
"""

from re import sub

from manim import *

# class Example(Scene):
#     """Example scene."""

#     def construct(self):
#         """Construct the scene."""
#         # background music
#         # NOTE: Start here.
#         number_plane = NumberPlane(
#             x_range=[-10, 10, 1],
#             y_range=[-10, 10, 1],
#             stroke_width=100,
#             axis_config={
#                 "stroke_color": YELLOW,
#                 "stroke_width": 1,
#             },
#             background_line_style={
#                 "stroke_color": GREY,
#                 "stroke_width": 1,
#                 "stroke_opacity": 1,
#             },
#         )
#         # NOTE: Continue here
#         self.add(number_plane)
#         a = Dot(point=[-5, 3, 0], color=BLUE)
#         b = Dot(point=[-5, 3, 0], color=RED)
#         self.add(a, b)
#         self.play(b.animate.move_to([5, -3, 0]))
#         line = Line(a.get_center(), b.get_center(), color=GREEN)
#         self.play(Create(line))
#         text_a = MathTex(r"\left(-5, 3\right)").next_to(b)
#         text_b = MathTex(r"\left(5, -3\right)").next_to(a, LEFT, buff=0.25)
#         self.play(Write(text_a), Write(text_b))
#         lineq = MathTex(r"y = -\frac{6}{10}x").next_to(
#             line.get_center(), RIGHT, buff=0.75
#         )
#         lineq_short = MathTex(r"10y = -6x").next_to(line.get_center(), RIGHT, buff=0.75)
#         lineq_simplified = MathTex(r"5y = -3x").next_to(
#             line.get_center(), RIGHT, buff=0.75
#         )

#         # Driver
#         self.play(Write(lineq))
#         self.wait(1)  # Always set to 1, otherwise it won't work.
#         self.play(Transform(lineq, lineq_short))
#         self.wait(1)
#         self.play(Transform(lineq, lineq_simplified))


# class Example3(Scene):
#     """Example scene."""

#     def set_font(self):
#         """Set the fonts used in the video."""
#         Text.set_default(font="erewhon")
#         preamble = TexTemplate()
#         preamble.add_to_preamble(
#             r"\usepackage{fourier} \usepackage{tgheros} \usepackage{siunitx}",
#             prepend=True,
#         )
#         MathTex.set_default(tex_template=preamble)

#     def construct(self):
#         """Construct the scene."""
#         self.set_font()
#         self.add_sound("assets/Zeta.mp3")
#         text1 = Text("Darren hear me out")
#         text2 = Text("This is so cool")
#         self.play(Write(text1))
#         self.wait(1)
#         self.play(Transform(text1, text2))
#         self.wait(1)
#         self.remove(text1)
#         Example.construct(self)


class TitleCard(Scene):
    """titlecard."""

    def construct(self):
        """construct the titlecard."""
        logo = ImageMobject("assets/logo-white.png")
        logo.height = 5
        subtitle = Text("presents")
        self.play(FadeIn(logo))
        self.play(Write(subtitle))


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
        self.add_sound("assets/Zeta.mp3")
        TitleCard.construct(self)
