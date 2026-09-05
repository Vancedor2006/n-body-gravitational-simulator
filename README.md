# n-body-gravitational-simulator
Object-oriented N-body gravitational physics engine built in Python.
# N-Body Gravitational Simulator

A procedural, object-oriented physics engine built in Python to simulate gravitational interactions between celestial bodies using Newton's Law of Universal Gravitation. 

![Orbit Trajectory](orbit.png)

## Architecture & Engineering
This engine was designed to prevent state-contamination during calculation loops. It utilizes a **two-pass update system**:
1. **Calculate State:** The system computes the net forces and predicts the next kinematic state for all bodies simultaneously.
2. **Apply State:** Positions and velocities are updated globally via `zip()` mapping, ensuring that a body moving early in the loop doesn't skew the gravitational calculations for bodies later in the loop.

## Physics Implementation

The simulation calculates gravitational force vectors in 3D space using NumPy arrays and SI Units (meters, kilograms, seconds). 

The force between any two bodies is determined by:

$$
F = G \frac{m_1 m_2}{r^2}
$$

To prevent mathematical singularities (division by zero) when bodies pass extremely close to one another, a distance softening parameter is applied during the vector normalization:

$$
r_{softened} = \sqrt{||\vec{r}||^2 + \epsilon^2}
$$

Markdown
## How to Run

**1. Clone the repository and navigate to the directory**
```bash
git clone [https://github.com/YOUR_USERNAME/n-body-gravitational-simulator.git](https://github.com/YOUR_USERNAME/n-body-gravitational-simulator.git)
cd n-body-gravitational-simulator
2. Set up a virtual environment (Optional but recommended)

Bash
python -m venv venv

# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install the required dependencies

Bash
pip install numpy matplotlib
4. Execute the simulation

Bash
python n_body_sim.py
Note: Running the script will compute the kinematic updates, open a window displaying the Matplotlib 2D orbit, and automatically save a high-resolution orbit.png to your local directory.


*(Remember to swap `YOUR_USERNAME` with your actual GitHub username before committing!)*
