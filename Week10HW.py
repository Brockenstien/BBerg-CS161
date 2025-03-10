# PROBLEM 1
print("---Problem 1---")

class SolarObjects:
    def __init__(self, furthestDist, spin, ttorbit):
        self.furthestDist = furthestDist
        self.spin = spin
        self.ttorbit = ttorbit

    def colonization(self):
        if self.furthestDist < 1:
            return 6000000000 * self.furthestDist
        else:
            return 6000000000 / self.furthestDist

    def spin(self):
        pass


class Planets(SolarObjects):
    def __init__(self, furthestDist, spin, ttorbit):
        super().__init__(furthestDist, spin, ttorbit)

    def spin(self):
