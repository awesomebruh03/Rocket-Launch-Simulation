from simulation.rocket import Rocket
from simulation.environment import Environment

def main():
    """
    Main function to run the rocket launch simulation.
    """
    # Create the rocket and environment
    rocket = Rocket()
    environment = Environment()

    # Run the simulation
    while rocket.is_flying:
        rocket.update(environment)
        print(f"Altitude: {rocket.position.y:.2f} m, Velocity: {rocket.velocity.y:.2f} m/s, Fuel: {rocket.fuel:.2f} kg")

if __name__ == "__main__":
    main()
