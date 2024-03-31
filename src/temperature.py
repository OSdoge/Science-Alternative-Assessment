from manim import *
from manim_chemistry import *

class Absorption(Scene):
    def construct(self):
        c_grp = VGroup()
        CO = MMoleculeObject.from_mol_file("molfiles/C Monoxide.mol").shift(LEFT * 1)
        CO2 = MMoleculeObject.from_mol_file("molfiles/C Dioxide.mol").shift(RIGHT * 1)
        CO2.representation_type = "complete"
        c_grp.add(CO)
        c_grp.add(CO2)
        
        c_text = Text("Carbon Contaning Compounds", color=WHITE).next_to(c_grp, DOWN)
        c_grp.add(c_text).scale(0.8)
        
        ozone = MMoleculeObject.from_mol_file("molfiles/ozone.mol")
        o_text = Text("Ozone", color=WHITE).next_to(ozone, DOWN)
        
        self.play(Create(c_grp))
        
        c_grp.generate_target()
        c_grp.target.scale(0.5)
        c_grp.target.shift(LEFT * 2.5)
        
        self.play(MoveToTarget(c_grp))
        
        self.play(Create(ozone), Write(o_text))