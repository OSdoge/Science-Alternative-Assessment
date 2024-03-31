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
        
        note = Text("Note: This explanation is one of the many grossly simplified explanations of lift", color=WHITE, font_size=25).to_edge(DOWN)
        self.play(Write(note))
        self.wait(1)
        
        push_arrow = Arrow([3, 0, 0], [6, -1, 0], color=RED)
        text_push = Text("Action", color=WHITE, font_size=20).move_to([5.8, -1.3, 0])
        self.play(GrowArrow(push_arrow), Write(text_push))
        self.wait(1)
        
        lift_arrow = Arrow([2.2, 0.26, 0], [-0.8, 1, 0], color=RED)
        text_lift = Text("Reaction", color=WHITE, font_size=20).move_to([-1, 1.3, 0])
        self.play(GrowArrow(lift_arrow), Write(text_lift))
        
        self.wait(1)
        
        

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
        self.play(Rotate(turbine, angle=PI / 2, axis=RIGHT, run_time=3))

class wrongGenerator(ThreeDScene):
    def construct(self):
        # construct a cuboid magnet, made up of two cuboids that add up to 4, 2, 1
        magnet = VGroup()
        magnet.add(Prism(dimensions=[2, 2, 1], fill_color=RED, stroke_width=1).shift([-1, 0, 0]))
        magnet.add(Prism(dimensions=[2, 2, 1], fill_color=BLUE, stroke_width=1).shift([1, 0, 0]))
        # construct a rod with height in the y-axis
        rod = Cylinder(height=6, radius=0.1, stroke_color=WHITE, stroke_width=1, direction=Y_AXIS).shift([0, 2, 0])
        self.add(rod)
        wires = Rectangle(height=6, width=6, stroke_color=WHITE, stroke_width=1, fill_opacity = 0)
        connecting_wire = Line([0, -3, 0], [0, -10, 0], color=WHITE)
        self.add(wires, connecting_wire)
        self.set_camera_orientation(phi= - PI / 5)
        note = Text("Note: ", color=WHITE, font_size=25).to_edge(DOWN)
        self.play(Rotate(magnet, angle=6 * PI, axis=UP, run_time=6, rate_func=linear), Rotate(rod, angle=6 * PI, axis=DOWN, run_time=6, rate_func=linear))
        # move camera slightly up
        # move camera slightly up and face the magnet

class Generator(ThreeDScene):
    def construct(self):
        wires = Rectangle(height=6, width=6, stroke_color=WHITE, stroke_width=1, fill_opacity = 0)
        connecting_wire = Line([0, -3, 0], [0, -10, 0], color=WHITE)
        self.add(wires, connecting_wire)
        self.set_camera_orientation(phi= - PI / 5)
        magnet_left = Prism(dimensions=[1, 8, 2], fill_color=RED, stroke_width=1).shift([-5, 0, 0])
        magnet_right = Prism(dimensions=[1, 8, 2], fill_color=BLUE, stroke_width=1).shift([5, 0, 0])
        self.add(magnet_left, magnet_right)
        note = Text("Note: This is an AC generator", color=WHITE, font_size=25).to_edge(DOWN).rotate(-PI / 4, axis=RIGHT)
        self.play(Rotate(wires, angle=-24 * PI, axis=UP, run_time=24, rate_func=linear), Write(note))

class MaxwellEq(Scene):
    def construct(self):
        faraday = MathTex(r"\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}").scale(1)
        self.play(Write(faraday))
        self.wait(1)
        delcross_meaning = MathTex(r"\nabla \times \vec{E} \implies \text{curl of } \vec{E}").scale(1)
        self.play(Transform(faraday[0][0:4], delcross_meaning), Unwrite(faraday[0][4:]))
        self.wait(1)
        curl_E = MathTex(r"\text{curl of } \vec{E} = -\frac{\partial \vec{B}}{\partial t}").scale(1)
        self.play(Transform(faraday, curl_E))
        self.wait(1)
        word_eq = MathTex(r"\text{curl of electric field} = -\text{rate of change of magnetic field}").scale(1)
        self.play(Transform(faraday, word_eq))
        self.wait(1)

class Steam2(Scene):
    def construct(self):
        geothermal_src = Ellipse(color= BLUE_E, fill_opacity=1).shift([-4, -2, 0]) 
        text = Text("Hot Water Source", color=WHITE).next_to(geothermal_src, DOWN, buff=0.1).scale(0.5)
        note = Text("(Heated from biodiesel or geothermal energy)", color=WHITE).next_to(text, DOWN, buff=0.1).scale(0.3)
        self.play(Create(geothermal_src), Write(text), Write(note))
        
        turbine = RoundedRectangle(corner_radius=0.5, color= MAROON, fill_opacity=1).shift([3, 1, 0]).scale(0.75)
        text_2 = Text("Turbine", color=WHITE).next_to(turbine, DOWN, buff=0.1).scale(0.5)
        self.play(Create(turbine), Write(text_2))
        
        line = Line([-4, -1.5, 0], [-4, 1, 0], color=BLUE_A)
        text_3 = Text("Steam", color=WHITE).next_to(line, RIGHT, buff=0.1).scale(0.5)
        arrow = Arrow([-4.268, 1, 0], [1.70, 1, 0], color=BLUE_A, stroke_width=4)
        
        self.wait(1)
        self.play(Succession(Create(line), GrowArrow(arrow), rate_functions=linear), Write(text_3), rate_functions=[linear, linear])
        self.wait(1)
        
        
class magneticfield(ThreeDScene):
    def construct(self):
        func = lambda pos: -pos[1]*RIGHT+pos[0]*UP  
        mob = ArrowVectorField(func)  
        arrow = Arrow3D([0, 0, -2], [0, 0, 2], color=RED)
        arrow_text = MathTex(r"\vec{B}", color=WHITE).next_to(arrow, Z_AXIS, buff=0.5).rotate(PI/2, axis=X_AXIS)
        self.add(mob, arrow, arrow_text) 
        
        self.move_camera(phi=PI/4, zoom=1.5)
        
        self.wait(3)

class windAndWater(Scene):
    def construct(self):
        turbine = RoundedRectangle(height=2, width=1, color=MAROON, fill_opacity=1, corner_radius=0.1).shift([2, 0, 0])
        text = Text("Turbine", color=WHITE).next_to(turbine, DOWN, buff=0.1).scale(0.5)
        self.play(Create(turbine), Write(text))
        self.wait(1)
        
        arrow = Arrow([-3, 0, 0], [1, 0, 0], color=BLUE_D)
        text_2 = Text("Air/Water Flow", color=WHITE).next_to(arrow, UP, buff=0.1).scale(0.5)
        self.play(GrowArrow(arrow), Write(text_2))
        self.wait(1)