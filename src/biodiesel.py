"""
*** biodiesel.py ***

mhm yes much fuel
"""

import os

from manim import *
from manim_chemistry import *

assets = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../assets")
mols = os.path.join(assets, "mols")


class TwoDMoleculeScene(Scene):
    """molecules!"""

    def construct(self):
        """construct some mols!"""
        t_grp = VGroup()
        triglyceride = MMoleculeObject.from_mol_file(
            os.path.join(mols, "triglyceride.mol")
        )
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
        fame = MMoleculeObject.from_mol_file(os.path.join(mols, "FAME.mol"))
        f_grp.add(fame)
        f_text = Text("Methyl ester", color=WHITE).next_to(fame, DOWN)
        f_grp.add(f_text)
        self.play(Create(f_grp))
        self.wait(1)
        f_grp.generate_target()
        f_grp.target.scale(0.5)
        f_grp.target.shift(RIGHT * 4)
        arrow = Arrow([1.5, -0.5, 0], [2.5, -0.5, 0], color=WHITE)
        self.play(MoveToTarget(f_grp), GrowArrow(arrow), run_time=1)
        self.wait(1)

        methanol = MMoleculeObject.from_mol_file(
            os.path.join(mols, "methanol.mol")
        )
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
        glycerol = MMoleculeObject.from_mol_file(
            os.path.join(mols, "glycerol.mol")
        )
        g_grp.add(glycerol)
        g_text = Text("Glycerol", color=WHITE).next_to(glycerol, DOWN)
        g_grp.add(g_text)
        g_grp.scale(0.4)
        g_grp.shift(RIGHT * 4.5)

        plus_sign2 = MathTex("+").move_to([3.5, -0.5, 0]).scale(0.80)

        self.play(
            MoveToTarget(everything),
            Create(glycerol),
            Write(g_text),
            Create(plus_sign2),
        )
        self.wait(1)


class Combustion(Scene):
    """combustion equation!"""

    def construct(self):
        preamble = TexTemplate()
        preamble.add_to_preamble("\\usepackage[version=4]{mhchem}")
        combustion = Tex(
            r"\ce{C_xH_y + $\left(x + \frac{y}{4}\right)$ O2 -> $x$ CO2 + $\frac{y}{2}$ H2O}",
            tex_template=preamble,
        )
        self.play(Write(combustion))
        combustion.generate_target()
        combustion.target.shift(UP * 0.5)
        self.play(MoveToTarget(combustion))
        self.wait(1)
        enthalpy_change = MathTex(
            r"\Delta H = \sum H_\text{products} - \sum H_\text{reactants} < 0"
        ).shift(DOWN * 0.5)
        self.play(Write(enthalpy_change))
        self.wait(1)


class methyl(Scene):
    def construct(self):
        methyl = MMoleculeObject.from_mol_file("molfiles/FAME.mol")
        text = Text("Methyl Ester", color=WHITE).next_to(methyl, DOWN).scale(0.75)
        self.play(Create(methyl), Write(text))
        self.play(Transform(methyl, methyl.copy().shift(UP * 0.5)), Transform(text, text.copy().shift(UP * 0.5)))
        text_2 = Text("(Biodiesel)", color=WHITE).next_to(text, DOWN).scale(0.5)
        
        self.play(Write(text_2))
        self.wait(1)

class trans(Scene):
    def construct(self):
        text = Text("Transesterification", color=WHITE).scale(1.5)
        self.play(Write(text))
        self.wait(1)

class trigly(ThreeDScene):
    def construct(self):
        triglyceride = MMoleculeObject.from_mol_file("molfiles/triglyceride.mol")
        self.add(triglyceride)
        self.play(Rotate(triglyceride, run_time=10, axis=Y_AXIS, angle=PI, rate_func = linear))
        self.wait()
        
class Combustion2(Scene):
    def construct(self):
        combustion = MathTex(r"C_xH_y+(x+\frac{y}{4})O_2\to xCO_2+\frac{y}{2}H_2O")
        self.play(Write(combustion))
        self.wait(1)
        self.play(FadeOut(combustion[0][:15]), FadeOut(combustion[0][19:]))
        self.wait(1)
        self.play(Transform(combustion[0][15:19], combustion[0][15:19].copy().move_to([0, 0, 0])))
        self.wait(1)