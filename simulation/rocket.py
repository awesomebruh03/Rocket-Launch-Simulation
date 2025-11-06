import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *

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

    def draw_cylinder(self, radius, height, slices, stacks):
        quad = gluNewQuadric()
        gluCylinder(quad, radius, radius, height, slices, stacks)
        gluDeleteQuadric(quad)

    def draw_cone(self, radius, height, slices, stacks):
        quad = gluNewQuadric()
        gluCylinder(quad, radius, 0, height, slices, stacks)
        gluDeleteQuadric(quad)

    def draw(self):
        """
        Draws the N1 rocket using OpenGL.
        """
        glPushMatrix()
        glScalef(0.5, 0.5, 0.5) # Scale down the whole rocket to fit the screen
        # Stage 1 (Block A) - Height: ~50m, Diameter: ~17m
        glColor3f(0.8, 0.8, 0.8)
        glPushMatrix()
        glTranslatef(0, -5, 0)
        self.draw_cylinder(0.85, 5, 32, 32)
        glPopMatrix()

        # Transition to Stage 2
        glPushMatrix()
        glTranslatef(0, 0, 0)
        self.draw_cone(0.85, 0.5, 32, 32) # A cone to transition between stage 1 and 2
        glPopMatrix()


        # Stage 2 (Block B) - Height: ~20m, Diameter: ~10m
        glColor3f(0.7, 0.7, 0.7)
        glPushMatrix()
        glTranslatef(0, 0.5, 0)
        self.draw_cylinder(0.5, 2, 32, 32)
        glPopMatrix()

        # Transition to Stage 3
        glPushMatrix()
        glTranslatef(0, 2.5, 0)
        self.draw_cone(0.5, 0.3, 32, 32)
        glPopMatrix()

        # Stage 3 (Block V) - Height: ~10m, Diameter: ~7m
        glColor3f(0.6, 0.6, 0.6)
        glPushMatrix()
        glTranslatef(0, 2.8, 0)
        self.draw_cylinder(0.35, 1, 32, 32)
        glPopMatrix()

        # Payload Fairing
        glColor3f(1.0, 1.0, 1.0)
        glPushMatrix()
        glTranslatef(0, 3.8, 0)
        self.draw_cone(0.35, 1.5, 32, 32)
        glPopMatrix()

        # Engines (Simplified representation)
        glColor3f(0.4, 0.4, 0.4)
        glPushMatrix()
        glTranslatef(0, -5.2, 0)
        # Outer ring of 24 engines
        for i in range(12):
            glPushMatrix()
            angle = i * 30
            glRotatef(angle, 0, 1, 0)
            glTranslatef(0.6, 0, 0)
            self.draw_cylinder(0.1, 0.4, 16, 16)
            glPopMatrix()
        # Inner ring of 6 engines
        for i in range(6):
            glPushMatrix()
            angle = i * 60
            glRotatef(angle, 0, 1, 0)
            glTranslatef(0.3, 0, 0)
            self.draw_cylinder(0.08, 0.3, 16, 16)
            glPopMatrix()

        glPopMatrix()

        glPopMatrix()