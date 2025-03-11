class SolarObjects:
    def __init__(self, name, furthestDist, spintype, ttorbit):
        self.name = name
        self.furthestDist = furthestDist
        self.spintype = spintype
        self.ttorbit = ttorbit

    # Estimate the colonization potential population in billions by taking the default value of Earth (6 bil) and
    # dividing it by the distance from the sun (multiplying if it is less than 1 au)
    def colonization(self):
        if self.furthestDist < 1:
            return format(((6000000000 * self.furthestDist) / 1000000000), ".2f")
        else:
            return format(((6000000000 / self.furthestDist) / 1000000000), ".2f")

    # Define a method that passes
    def spin(self):
        pass

    # Give info on the solar object
    def info(self):
        return (f"{self.name} is {self.furthestDist} au from the sun, spins {self.spin()}, and has an orbit"
                f" taking {self.ttorbit} days. Its colonization potential is {self.colonization()} billion")


class Planets(SolarObjects):
    def __init__(self, name, furthestDist, spintype, ttorbit):
        super().__init__(name, furthestDist, spintype, ttorbit)

    # set the spin value
    def spin(self):
        return "slightly elliptical"


class Comets(SolarObjects):
    def __init__(self, name, furthestDist, spintype, ttorbit):
        super().__init__(name, furthestDist, spintype, ttorbit)

    # set the spin value
    def spin(self):
        return "like crazy"

    # Copy the info method but change "days" to "years"
    def info(self):
        return (f"{self.name} is {self.furthestDist} au from the sun, spins {self.spin()}, and has an orbit"
                f" taking {self.ttorbit} years. Its colonization potential is {self.colonization()} billion")

# Create instances of planets and comets
Earth = Planets("Earth", 1, "normal", 365)
Mars = Planets("Mars", 1.524, "normal", 687)

Halley = Comets("Halley's Comet", 35, "normal", 76.95)
HaleBopp = Comets("Hale-Bopp", 354, "normal", 2397.29)

# Print the info of the instances created
print(Earth.info())
print(Mars.info())
print(Halley.info())
print(HaleBopp.info())
