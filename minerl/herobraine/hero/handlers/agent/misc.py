# Copyright (c) 2020 All Rights Reserved
# Author: William H. Guss, Brandon Houghton

"""Defines miscellaneous agent handlers"""

from minerl.herobraine.hero.handler import Handler
# class PauseAction(Handler):
#     def to_string(self):
#         return "pause"

#     @property
#     def xml_element(self) -> str:
#         return "PauseCommand"

# <DiscreteMovementCommands>
    # <ModifierList type="deny-list">
    #     <command>attack</command>
    # </ModifierList>
# </DiscreteMovementCommands> 
class DiscreteMovementCommands(Handler):
    """
    Allow discrete movements from thee agent, i.e. moving from the center of one block to the next one

    Example usage: 

    .. code-block:: python

        DiscreteMovementCommands(to_draw="")
    """
    def __init__(self, to_draw= ""):
        self.to_draw = to_draw

    def to_string(self) -> str:
        return "discrete_movement_commands" 

    def xml_template(self) -> str:
        tmp = str(
           """<DiscreteMovementCommands>
                </DiscreteMovementCommands>"""
        )
        #print("\n\n\nXML DISC CMDS CALLED: ", tmp)
        return tmp