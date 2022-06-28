import cmd
import random


class Battle(cmd.Cmd, object):
    """Demo / easter egg. Punch left, punch right."""

    def __init__(self, run_code, left, right):
        self.run_gcode = run_code
        self.left = left
        self.right = right
        super(Battle, self).__init__()

    @staticmethod
    def random_y():
        return random.randint(30, 90)

    def do_l(self, arg):
        print("Doing left")
        self.run_gcode(self.left, "G0 X15 F1200")
        self.run_gcode(self.left, "G0 X60 Y%s F6000" % self.random_y())

    def do_r(self, arg):
        print("Doing right")
        self.run_gcode(self.right, "G0 X100 F1200")
        self.run_gcode(self.right, "G0 X60 Y%s F6000" % self.random_y())
