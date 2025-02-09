from body import Body
from physics import compute_forces, update_bodies
from visualize import plot_orbits, animate_simulation
from config import dt, num_steps

# Define celestial bodies, args are name, mass, position, velocity
bodies = [
    Body("Sun", 1.989e30, [0, 0], [0, 0]),       # Sun (stationary)
    Body("Earth", 5.972e24, [1.496e11, 0], [0, 29780]),  # Earth
    Body("Mars", 6.39e23, [2.279e11, 0], [0, 24070])     # Mars
]

# Store position history
positions = {body.name: [] for body in bodies}

# Run the simulation
for _ in range(num_steps):
    forces = compute_forces(bodies)
    update_bodies(bodies, forces, dt)
    
    for body in bodies:
        positions[body.name].append(body.position.copy())

visualize_orbits = False  # Change to True to see static orbits
    
if visualize_orbits:
    plot_orbits(positions)
else:
    animate_simulation(positions)