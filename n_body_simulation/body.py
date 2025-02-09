import numpy as np

class Body:
    """Represents a celestial body with mass, position, and velocity."""

    def __init__(self, name, mass, position, velocity):
        self.name = name
        self.mass = mass  # in kg
        self.position = np.array(position, dtype=float)  # in meters
        self.velocity = np.array(velocity, dtype=float)  # in m/s
        self.acceleration = np.zeros(2)  # Initialize acceleration as zero
