from manim import *


class SolarCell(ThreeDScene):
    """construct the solar cell."""

    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=150 * DEGREES)
        self.begin_ambient_camera_rotation()
        top_layer = Prism(dimensions=[6.0, 8.0, 0.1]).rotate(PI / 4)
        top_layer.set_fill(color=WHITE, opacity=0.8)
        solar_cell = Prism(dimensions=[6.0, 8.0, 0.5]).rotate(PI / 4)
        solar_cell.set_fill(color=BLUE, opacity=0.8)

        layers = Group(solar_cell, top_layer)
        self.play(Rotate(layers, angle=2 * PI, about_point=ORIGIN), run_time=5)
        intro = Text(
            "This is a solar cell.", font_size=40, gradient=(BLUE, WHITE)
        )
        intro.to_corner(UL)
        self.add_fixed_in_frame_mobjects(intro)
        self.play(
            Rotating(layers, angle=2 * PI, about_point=ORIGIN), Write(intro)
        )
        self.wait(1)
        self.play(
            Rotating(layers, angle=2 * PI, about_point=ORIGIN),
            FadeOut(solar_cell),
            FadeOut(intro),
        )
        self.wait(1)

        desc = Text(
            "The main mechanism behind this: silicon semiconducting films."
        )
        self.play(
            Rotating(top_layer, angle=2 * PI, about_point=ORIGIN), Write(desc)
        )
