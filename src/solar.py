from manim import *


class SolarCell(ThreeDScene):
    """construct the solar cell."""

    def construct(self):
        preamble = TexTemplate()
        preamble.add_to_preamble(
            "\\usepackage{fourier}\n\n\\usepackage{siunitx}\n\\usepackage{ragged2e}",
            prepend=True,
        )
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
        intro.to_corner(UL + DOWN * 0.25)
        self.add_fixed_in_frame_mobjects(intro)
        self.play(
            Rotate(layers, angle=2 * PI, about_point=ORIGIN), Write(intro)
        )
        self.wait(1)
        self.play(
            Rotate(layers, angle=2 * PI, about_point=ORIGIN),
            FadeOut(solar_cell),
            FadeOut(intro),
        )
        self.wait(1)

        desc = Text(
            "The main mechanism behind this: silicon semiconducting films.",
            width=5,
        ).scale(0.5).to_corner(UL + DOWN * 0.25)
        self.add_fixed_in_frame_mobjects(desc)
        self.play(
            Write(desc)
        )
        self.wait(1)
        self.play(FadeIn(solar_cell))
        self.play(Rotate(layers, angle=2 * PI, about_point=ORIGIN), FadeOut(desc), run_time=5)

        ray = Arrow(start=UP * 5 + LEFT * 5, end=ORIGIN, color=YELLOW, stroke_width=10)
        light = Text("Light ray",width=2.5).next_to(ray, LEFT).scale(.75)
        self.add_fixed_in_frame_mobjects(ray,light)
        self.play(GrowArrow(ray),Write(light))
        self.wait(1)
        self.play(FadeOut(ray), FadeOut(light))
