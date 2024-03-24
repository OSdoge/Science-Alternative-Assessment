"""
wind.py

*** kinetic energy for electrical generation ***
"""

from manim import *


def CreateAirfoil(scale: int = 2):
    """points are courtesy of https://nathanrooy.github.io/posts/2016-09-14/airfoil-manipulation-via-bezier-curves-with-python/"""
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

def Create2DTurbine(scale = 2):
    group = VGroup()
    mob = Circle(stroke_color=WHITE, stroke_width=1)
    mob.scale(scale)
    group.add(mob)
    for i in range(16):
        group.add(Line(mob.get_center(), mob.point_at_angle(22.5 + i * 22.5 * DEGREES), color=WHITE))
    return group

def CreateTurbine(scale = 2):
    group = VGroup()
    mob = Cylinder(height=1, radius=scale, stroke_color=WHITE, direction=X_AXIS, fill_opacity=0)
    group.add(mob)
    # create rectangle from centre of cylinder to circumference
    group.add(Create2DTurbine(scale).rotate(PI / 2, axis=Y_AXIS))
    return group

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
        self.play(Transform(airfoil, new_airfoil), GrowArrow(arrow), Write(text))

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
        
        # create airfoil that is centered
        new_airfoil = CreateAirfoil(scale * 1.5)
        new_airfoil.stroke_color = RED
        new_airfoil.stroke_width = 3
        new_airfoil.shift([-new_airfoil.width / 2, 0, 0])
        new_arrow = arrow.copy().shift([-new_airfoil.width / 2, 0, 0]).set_opacity(0)
        new_text = text.copy().shift([-new_airfoil.width / 2, 0, 0]).set_opacity(0)

        self.play(Transform(arrow, new_arrow), Transform(text, new_text), Transform(airfoil, new_airfoil))
        
        

class TurbineFan(ThreeDScene):
    def construct(self):
        """construct the turbine."""
        cam_orientation = self.camera.get_phi(), self.camera.get_theta()
        self.set_camera_orientation(phi=PI / 5, theta= -3 * PI / 4)
        
        arr = Arrow([-5, 0, 0], [0, 0, 0], color=RED)
        turbine = CreateTurbine()
        
        self.add(turbine)
        
        # rotate camera such that we are facing the direction of the arrow
        self.move_camera(phi= PI / 2, theta=-PI, added_anims=[GrowArrow(arr)], run_time=2)
        self.remove(arr, turbine)
        
        self.play(Transform(turbine, Create2DTurbine().rotate(PI / 2, axis=Y_AXIS).flip()))
        # reset orientation of camera
        self.set_camera_orientation(phi=cam_orientation[0], theta=cam_orientation[1])
        # self.play(Transform(turbine, CreateTurbine()))
        self.remove(turbine)
        TurbineFan2D.construct(self)

class TurbineFan2D(Scene):
    def construct(self):
        """construct the turbine."""
        self.add(Create2DTurbine())
        self.wait(1)