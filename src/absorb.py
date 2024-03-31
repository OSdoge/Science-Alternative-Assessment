from manim import *
from manim_chemistry import *

class Absorption(Scene):
    def construct(self):
        # # CH4 = MMoleculeObject.from_mol_file("molfiles/Methane.mol")
        # # self.play(Create(CH4))
        # # self.wait(1)
        
        # # CO2 = VGroup(MMoleculeObject.from_mol_file("molfiles/C Dioxide.mol"))
        # # square = Square(side_length = 0.5, color = BLACK, fill_opacity = 1)
        # # square.z_index = 1
        # # C = Text("C", color=WHITE).scale(0.8).next_to(square, IN).set_z_index(2)
        # # C_grp = VGroup(square, C)
        # # CO2.add(C_grp)
        # # self.play(Create(CO2[1]), Create(CO2[0])) 

        # # self.wait(1)
        # # self.play(CO2.animate.shift(LEFT * 2))
        
        # O3 = VGroup(MMoleculeObject.from_mol_file("molfiles/ozone.mol"))
        # self.play(Create(O3))
        # self.wait(1)
        
        CO2 = Text("O=C=O")
        self.play(Create(CO2))
        