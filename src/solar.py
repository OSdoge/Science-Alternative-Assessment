from manim import *
from manim_chemistry import *

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
        # solar_cell = Prism(dimensions=[6.0, 8.0, 0.5]).rotate(PI / 4)
        # solar_cell.set_fill(color=BLUE, opacity=0.8)
        # make solar_cell a group of two layers
        solar_cell = VGroup()
        top = Prism(dimensions=[6.0, 8.0, 0.2]).rotate(PI / 4).shift([0,0,0.15])
        bottom = Prism(dimensions=[6.0, 8.0, 0.2]).rotate(PI / 4).shift([0,0,-0.15])
        solar_cell.add(top)
        solar_cell.add(bottom)
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
        
        self.play(
            Rotate(layers, angle=2 * PI, about_point=ORIGIN),
            FadeOut(solar_cell),
            FadeOut(intro),
        )
        self.wait(1)

        desc = Text(
            "The main mechanism behind this: Silicon Semiconducting Films.",
            width=5,
        ).scale(2).to_corner(UL + DOWN * 0.25)
        self.add_fixed_in_frame_mobjects(desc)
        self.play(Write(desc))
        self.wait(1)
        self.play(FadeIn(solar_cell))
        self.play(
            Rotate(layers, angle=2 * PI, about_point=ORIGIN),
            FadeOut(desc),
            run_time=5,
        )

        ray = Arrow(start=UP * 5 + LEFT * 5, end=ORIGIN, color=YELLOW, stroke_width=10)
        light = Text("Light ray").move_to(UP * 2 + LEFT * 3.5).scale(0.75)
        self.add_fixed_in_frame_mobjects(ray,light)
        self.play(GrowArrow(ray),Write(light))
        self.wait(1)
        self.play(FadeOut(ray), FadeOut(light))
        self.wait(1)

class Atoms(Scene):
    def construct(self):
        
        arrow = Arrow([-3, -3, 0], [-3, 3.5, 0], color=WHITE)
        text_a = Text("Electron Energy").next_to(arrow, LEFT, buff=-2.2).rotate(PI/2).scale(0.5)
        self.add(arrow, text_a)
        valence = Rectangle(height=1.5, width=6, color=BLUE).shift(DOWN * 2)
        text = Text("Valence Band").next_to(valence, IN).scale(0.5)
        band = Rectangle(height=1.5, width=6, color=RED).shift(UP * 2)
        text2 = Text("Conduction Band").next_to(band, OUT).scale(0.5)
        #double arrowheads
        band_gap_bot = Arrow([0, 0.25, 0], [0, -1.5, 0], color=WHITE).shift(LEFT)
        band_gap_top = Arrow([0, -0.25, 0], [0, 1.5, 0], color=WHITE).shift(LEFT)
        text3 = Text("Band Gap").move_to([0,0,0]).scale(0.5)
        self.play(Create(valence), Write(text), GrowArrow(band_gap_bot), GrowArrow(band_gap_top), Create(band), Write(text2), Write(text3))
        self.wait(1)
         
        photon = Circle(radius = 0.125, color=YELLOW, fill_opacity=1).shift(UP * 5, RIGHT * 6)
        self.add(photon)
        new_photon = photon.copy().move_to([2, -2, 0])
        arrow = Arrow([6, 5, 0], [2, -2, 0], color=YELLOW_B)
        name = Text("Photon", color=WHITE).scale(0.50).next_to(arrow, RIGHT, buff=-1.60)
        electron = Circle(radius = 0.150, color=BLUE_D, fill_opacity=1).move_to([1.875, -2.125, 0])
        text4 = MathTex("e^-", color=WHITE).next_to(electron, IN).scale(0.50)
        self.play(Transform(photon, new_photon), Write(name), GrowArrow(arrow), Create(electron), Write(text4))
        self.play(FadeOut(photon), FadeOut(arrow), FadeOut(name), Transform(electron, electron.copy().shift(UP * 4.25)), Transform(text4, text4.copy().shift(UP * 4.25)))
        
class junctions(ZoomedScene):
    def construct(self):
        p_type = Rectangle(height=1.5, width=6, color=RED).shift(UP * 1.5)
        silicon = Rectangle(height=1.5, width=6, color=BLUE)
        n_type = Rectangle(height=1.5, width=6, color=GREEN).shift(DOWN * 1.5)
        
        text = Text("n-Type").next_to(p_type, IN).scale(0.5)
        text2 = Text("Silicon").next_to(silicon, IN).scale(0.5)
        text3 = Text("p-Type").next_to(n_type, IN).scale(0.5)
        
        photon_arrow = Arrow([0, 5, 0], [0, 0, 0], color=YELLOW_B)
        
        self.play(Create(p_type), Create(silicon), Create(n_type), Create(text), Create(text2), Create(text3))
        
        grp = VGroup(p_type, silicon, n_type, text, text2, text3)
        
        self.play(GrowArrow(photon_arrow), ScaleInPlace(grp, 2))
        
        hole = Circle(radius = 0.150, color=RED, fill_opacity=1).move_to([-0.150, 0, 0])
        text_h = Text("+", color=WHITE).next_to(hole, IN).scale(0.50)
        electron = Circle(radius = 0.150, color=BLUE_D, fill_opacity=1).move_to([0.150, 0, 0])
        text_e = Text("-", color=WHITE).next_to(electron, IN).scale(0.50)
        self.play(FadeIn(hole), FadeIn(electron), Write(text_h), Write(text_e), FadeOut(photon_arrow))
        
        self.play(Transform(hole, hole.copy().shift(DOWN * 2)), Transform(text_h, text_h.copy().shift(DOWN * 2)), Transform(electron, electron.copy().shift(UP * 2)), Transform(text_e, text_e.copy().shift(UP * 2)))
        
        wires = VGroup()
        
        wire1 = Line([2, 2, 0], [5, 2, 0], color=WHITE)
        wire2 = Line([5, -2, 0], [2, -2, 0], color=WHITE)
        wire3 = Line([5, 2, 0], [5, -2, 0], color=WHITE)
        
        grp.add(hole, electron, text_h, text_e)
        
        self.play(Succession(Transform(grp, grp.copy().shift(LEFT * 4)), AnimationGroup(Create(wire1), Create(wire2), Create(wire3))))
        
        self.play(Transform(electron, electron.copy().move_to([5, 2, 0])), Transform(text_e, text_e.copy().move_to([5, 2, 0])), rate_functions=linear)
        self.play(MoveAlongPath(text_e, wire3), MoveAlongPath(electron, wire3), rate_functions=linear)
        self.play(MoveAlongPath(text_e, wire2), MoveAlongPath(electron, wire2), rate_functions=linear)

class PB(Scene):
    def construct(self):
        diagram_2 = BohrAtom(e=15, p=15, n=16).scale(0.75)
        b_text_2 = Text("Phosphorus").next_to(diagram_2, DOWN).scale(0.5)
        self.play(Create(diagram_2), Write(b_text_2))
        grp2 = VGroup(diagram_2, b_text_2)
        self.play(grp2.animate.shift(LEFT * 3))
        self.wait(1)
    
        diagram = BohrAtom(e=5, p=5, n=6).shift(RIGHT * 3)
        b_text = Text("Boron").next_to(diagram, DOWN).scale(0.5)
        self.play(Create(diagram), Write(b_text))
        self.wait(1)