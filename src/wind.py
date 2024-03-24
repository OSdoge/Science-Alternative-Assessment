"""
wind.py

*** kinetic energy for electrical generation ***
"""

from manim import *


def CreateAirfoil(scale: int = 2):
    """create an airfoil shape."""
    airfoil = VMobject()
    points = [
        [1, 0.001, 0],
        [0.76, 0.08, 0],
        [0.52, 0.125, 0],
        [0.25, 0.12, 0],
        [0.1, 0.08, 0],
        [0, 0.03, 0],
        [0, -0.03, 0],
        [0.15, -0.08, 0],
        [0.37, -0.01, 0],
        [0.69, 0.04, 0],
        [1, -0.001, 0],
    ]

    new_points = []
    for point in points:
        arr = [val * scale for val in point]
        new_points.append(arr)

    airfoil.set_points_as_corners(new_points)
    airfoil.make_smooth()
    airfoil.set_fill(color=BLUE, opacity=1)
    airfoil.set_stroke(color=BLUE, width=1)
    return airfoil


class Flow(ThreeDScene):
    """flow of wind into turbines."""

    def construct(self):
        """construct the scene."""
        scale = 5
        foil_x_shift = 3
        airfoil = CreateAirfoil(scale)
        self.add(airfoil)
        top_dot = Dot([0, 0, 0], fill_opacity=1)
        bottom_dot = Dot([0, 0, 0], fill_opacity=1)

        arrow = Arrow([-5, 0, 0], [-1.2, 0, 0], color=RED)
        text = Text("Flow direction", color=WHITE, font_size=35).next_to(
            arrow, UP, buff=0.25
        )

        new_airfoil = CreateAirfoil(scale * 1.5)
        self.play(Transform(airfoil, new_airfoil), GrowArrow(arrow), Create(text))

        top_points = [
            [1, 0.001, 0],
            [0.76, 0.08, 0],
            [0.52, 0.125, 0],
            [0.25, 0.12, 0],
            [0.1, 0.08, 0],
            [0, 0.03, 0],
        ][::-1]
        bottom_points = [
            [0, -0.03, 0],
            [0.15, -0.08, 0],
            [0.37, -0.01, 0],
            [0.69, 0.04, 0],
            [1, -0.001, 0],
        ]
        top_path = (
            VMobject()
            .set_points_as_corners([[j * 1.5 * scale for j in i] for i in top_points])
            .make_smooth()
        )
        bottom_path = (
            VMobject()
            .set_points_as_corners(
                [[j * 1.5 * scale for j in i] for i in bottom_points]
            )
            .make_smooth()
        )

        top_mover = Dot([0, 0, 0], fill_opacity=0)
        bottom_mover = Dot([0, 0, 0], fill_opacity=0)

        trace_top = TracedPath(top_mover.get_center, stroke_color=RED, stroke_width=3)
        trace_bottom = TracedPath(
            bottom_mover.get_center, stroke_color=RED, stroke_width=3
        )

        self.add(trace_top, trace_bottom)
        new_airfoil.stroke_color = RED
        new_airfoil.stroke_width = 3

        self.play(
            MoveAlongPath(top_mover, top_path),
            MoveAlongPath(bottom_mover, bottom_path),
            Transform(airfoil, new_airfoil),
        )

        # shift all objects to the left


class TurbineFan(Scene):
    def construct(self):
        """construct the turbine."""
        self.add(CreateAirfoil(2))
