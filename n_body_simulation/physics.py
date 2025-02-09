import numpy as np
from config import G

def compute_forces(bodies):
    """Computes gravitational forces between celestial bodies."""
    n = len(bodies)
    forces = [np.zeros(2) for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            r_vec = bodies[j].position - bodies[i].position  # Distance vector
            r_mag = np.linalg.norm(r_vec)  # Magnitude
            
            if r_mag == 0:
                continue  # Avoid division by zero
            
            force_mag = G * bodies[i].mass * bodies[j].mass / r_mag**2
            force_vec = force_mag * r_vec / r_mag  # Normalize direction

            forces[i] += force_vec
            forces[j] -= force_vec  # Newton's Third Law

    return forces

def update_bodies(bodies, forces, dt):
    """Updates body positions and velocities using Euler’s Method."""
    for i, body in enumerate(bodies):
        acceleration = forces[i] / body.mass  # F = ma → a = F/m
        body.velocity += acceleration * dt  # v = v + a*dt
        body.position += body.velocity * dt  # x = x + v*dt
