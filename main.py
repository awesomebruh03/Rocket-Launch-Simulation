import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from simulation.rocket import Rocket
from simulation.environment import Environment

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 500.0)

    rocket = Rocket()
    environment = Environment()

    camera_y = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    rocket.engine_on = not rocket.engine_on

        # Update rocket physics
        if rocket.is_flying:
            rocket.update(environment)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Set up the camera
        glLoadIdentity()
        camera_y = max(0, rocket.position[1] / 10) # Adjust the divisor to control the camera's zoom
        gluLookAt(0, camera_y + 2, 10,  # Camera position
                  0, camera_y, 0,      # Look at point
                  0, 1, 0)             # Up vector

        # Draw the rocket
        glPushMatrix()
        glTranslatef(rocket.position[0], rocket.position[1], 0)
        rocket.draw()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()