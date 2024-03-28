from manim import *
from manim_chemistry import *

class TwoDMoleculeScene(Scene):
   def construct(self):
        # Example.construct(self)
        t_grp = VGroup()
        triglyceride = MMoleculeObject.from_mol_file("molfiles/triglyceride.mol")
        t_grp.add(triglyceride)
        t_text = Text("Triglyceride", color=WHITE).next_to(triglyceride, DOWN)
        t_grp.add(t_text)
        self.play(Create(t_grp))
        self.wait(1)
        t_grp.generate_target()
        t_grp.target.scale(0.5)
        t_grp.target.shift(LEFT * 4)
        self.play(MoveToTarget(t_grp), run_time=1)
        self.wait(1)
        
        f_grp = VGroup()
        fame = MMoleculeObject.from_mol_file("molfiles/FAME.mol")
        f_grp.add(fame)
        f_text = Text("Methyl Ester", color=WHITE).next_to(fame, DOWN)
        f_grp.add(f_text)
        self.play(Create(f_grp))
        self.wait(1)
        f_grp.generate_target()
        f_grp.target.scale(0.5)
        f_grp.target.shift(RIGHT * 4)
        arrow = Arrow([1.5, -0.5, 0], [2.5, -0.5, 0], color=WHITE)
        self.play(MoveToTarget(f_grp), GrowArrow(arrow), run_time=1)
        self.wait(1)
        
        methanol = MMoleculeObject.from_mol_file("molfiles/methanol.mol")
        m_grp = VGroup()
        m_grp.add(methanol)
        m_text = Text("Methanol", color=WHITE).next_to(methanol, DOWN)
        plus_sign = MathTex("+").move_to([-1.5, -0.5, 0])
        m_grp.add(m_text)
        self.play(Create(m_grp))
        self.wait(1)
        m_grp.generate_target()
        m_grp.target.scale(0.5)
        self.play(MoveToTarget(m_grp), Create(plus_sign), run_time=2)
        self.wait(1)
        
        everything = VGroup()
        everything.add(t_grp, f_grp, m_grp, arrow, plus_sign)
        everything.generate_target()
        everything.target.scale(0.80)
        everything.target.shift(LEFT * 1)
        
        g_grp = VGroup()
        glycerol = MMoleculeObject.from_mol_file("molfiles/glycerol.mol")
        g_grp.add(glycerol)
        g_text = Text("Glycerol", color=WHITE).next_to(glycerol, DOWN)
        g_grp.add(g_text)
        g_grp.scale(0.4)
        g_grp.shift(RIGHT * 4.5)
        
        plus_sign2 = MathTex("+").move_to([3.5, -0.5, 0]).scale(0.80)
        
        self.play(MoveToTarget(everything), Create(glycerol), Write(g_text), Create(plus_sign2))
        self.wait(1)

class Combustion(Scene):
    def construct(self):
        combustion = MathTex(r"C_xH_y+(x+\frac{y}{4})O_2\to xCO_2+\frac{y}{2}H_2O")
        self.play(Write(combustion))
        combustion.generate_target()
        combustion.target.shift(UP*0.5)
        self.play(MoveToTarget(combustion))
        self.wait(1)
        enthalpy_change = MathTex(r"\Delta H = \Sigma H_{products} - \Sigma H_{reactants} < 0").shift(DOWN*0.5)
        self.play(Write(enthalpy_change))
        self.wait(1)

class Example(Scene):
        def construct(self):
            number_plane = NumberPlane( #HEREFROM
                x_range=[-10, 10, 1],
                y_range=[-10, 10, 1],
                stroke_width=100,
                axis_config = {
                    'stroke_color': YELLOW,
                    'stroke_width': 20,
                },
                background_line_style={
                    'stroke_color': GREY,
                    'stroke_width': 15,
                    'stroke_opacity': 1
                }
            )
            self.add(number_plane)