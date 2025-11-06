import numpy as np

class Rocket:
    """
    Represents a rocket in the simulation.
    """
    def __init__(self):
        """
        Initializes the rocket's properties.
        """
        self.position = np.array([0.0, 0.0])  # [x, y]
        self.velocity = np.array([0.0, 0.0])  # [vx, vy]
        self.mass = 1000.0  # kg
        self.fuel = 500.0  # kg
        self.engine_on = False
        self.is_flying = True

    def update(self, environment):
        """
        Updates the rocket's state for a single time step.
        """
        if self.position[1] < 0:
          self.is_flying = False
          return
        # Calculate forces
        gravity_force = np.array([0.0, -environment.gravity * self.mass])
        thrust_force = np.array([0.0, 0.0])

        if self.engine_on and self.fuel > 0:
            thrust_force = np.array([0.0, 20000.0])  # N
            self.fuel -= 1.0  # kg/s

        # Update kinematics
        net_force = gravity_force + thrust_force
        acceleration = net_force / self.mass
        self.velocity += acceleration * 0.1  # 0.1 is the time step
        self.position += self.velocity * 0.1
