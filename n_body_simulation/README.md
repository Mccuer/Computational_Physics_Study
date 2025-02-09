# N-Body Simulation

## Overview
This project implements an N-body simulation to model the gravitational interactions of multiple celestial bodies. The simulation numerically integrates Newton's laws of motion to compute the orbits of bodies under mutual gravitational attraction.

## Features
- Simulates gravitational interactions of `N` bodies
- Uses numerical integration (e.g., Euler's method)
- Supports visualization of orbits and animated simulations
- Configurable initial conditions

## Installation
### Prerequisites
Ensure you have Python installed (version 3.8 or higher recommended). Install the required dependencies using:

```bash
pip install -r requirements.txt
```

### Dependencies
- `numpy` for numerical computations
- `matplotlib` for visualization

## Usage
### Running the Simulation
To execute the simulation and generate results, run:

```bash
python main.py
```

### Visualization
The project provides two visualization tools:
1. **Plot Orbits** (static visualization):
In main.py
   ```bash
   visualize_orbits = true
   ```
2. **Animate Simulation** (dynamic visualization):
In main.py
   ```bash
   visualize_orbits = False
   ```

## Project Structure
```
.
├── main.py         # Entry point for the simulation
├── physics.py        # Core physics engine for N-body simulation
├── visualize.py    # Visualization functions (plotting and animation)
├── config.py        # Defines constants and time increments for the simulation
├── requirements.txt # List of dependencies
└── README.md       # Project documentation
```

