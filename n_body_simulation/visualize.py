import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import config as g

def plot_orbits(positions):
    """Plots the orbits of celestial bodies."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-2.5e11, 2.5e11)
    ax.set_ylim(-2.5e11, 2.5e11)
    ax.set_xlabel("X Position (m)")
    ax.set_ylabel("Y Position (m)")
    ax.set_title("N-Body Simulation")

    for body_name, pos_list in positions.items():
        pos_array = np.array(pos_list)
        ax.plot(pos_array[:, 0], pos_array[:, 1], label=body_name)

    ax.legend()
    plt.show()

def animate_simulation(positions, dt=g.dt):
    """Creates an animation of the celestial bodies in motion with a clock."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-2.5e11, 2.5e11)
    ax.set_ylim(-2.5e11, 2.5e11)
    
    lines = {body_name: ax.plot([], [], "o", markersize=5)[0] for body_name in positions}
    for line in lines.values():
        line.set_data([], [])
    
    # Add a clock text
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes, fontsize=12)
    
    def animate(i):
        for body_name, line in lines.items():
            pos = positions[body_name][i]
            line.set_data([pos[0]], [pos[1]])  # Ensure data is in list format
        
        # Update clock
        elapsed_days = (i * dt) / (24 * 60 * 60)  # Convert seconds to days
        time_text.set_text(f'Time: {elapsed_days:.1f} days')
        
        return list(lines.values()) + [time_text]

    ani = animation.FuncAnimation(fig, animate, frames=len(list(positions.values())[0]), interval=30, blit=False)
    plt.show()
