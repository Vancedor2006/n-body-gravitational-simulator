# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:26:34 2026

@author: Vezin
"""


'''
want to create an n body graviational system
object oriented programming so define a class called body
body class will have associated starting mass, position and velocity 
and it will also hold rules for how to update the system for each new time step
'''
import numpy as np
import matplotlib.pyplot as plt

class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        
    def calculate_force(self, other):
        displacement = other.position - self.position 
        distance = np.linalg.norm(displacement)
        softened_distance = np.sqrt((distance)**2+(0.000000001)**2)
        self.force = 6.6743 * 10**(-11) * self.mass * other.mass * displacement * (softened_distance)**(-3)
        return self.force
    
    def net_force(self):
        self.net_force_a = np.array([0.0,0.0,0.0])
        for other in bodies:
            if other is not self:
                self.net_force_a += self.calculate_force(other)
        return self.net_force_a
    
    def updated_position(self, dt):
        self.acceleration = self.net_force() / self.mass
        self.new_velocity = self.velocity + self.acceleration * dt
        self.new_position = self.position + self.new_velocity * dt
        return self.new_position
    
    def updated_velocity(self, dt):
        self.acceleration = self.net_force() / self.mass
        self.new_velocity = self.velocity + self.acceleration * dt
        return self.new_velocity
              
# Initialize system
Earth = Body(5.97*10**24, np.array([1.46*10**11,0.0,0.0]), np.array([0.0,28780.0,0.0]))
Sun = Body(1.989*10**30, np.array([0.0,0.0,0.0]), np.array([0.0,0.0,0.0]))
bodies = [Earth, Sun]

earth_x, earth_y = [], []
sun_x, sun_y = [], []

# Simulation loop (100 days at 1-hour timesteps)
dt = 3600 
for step in range(2400):
    updated_positions = [body.updated_position(dt) for body in bodies]
    updated_velocities = [body.updated_velocity(dt) for body in bodies]
    
    for body, new_pos, new_vel in zip(bodies, updated_positions, updated_velocities):
        body.position = new_pos
        body.velocity = new_vel
        
    earth_x.append(Earth.position[0])
    earth_y.append(Earth.position[1])
    sun_x.append(Sun.position[0])
    sun_y.append(Sun.position[1])

# Plotting
plt.figure(figsize=(8, 8))
plt.plot(earth_x, earth_y, label="Earth Orbit", color="blue")
plt.scatter(sun_x[-1], sun_y[-1], color="orange", s=150, label="Sun")
plt.scatter(earth_x[-1], earth_y[-1], color="blue", s=50, label="Earth")

plt.xlabel("X Position (meters)")
plt.ylabel("Y Position (meters)")
plt.title("2D Gravitational N-Body Orbit")
plt.gca().set_aspect("equal", adjustable="datalim") 
plt.legend()
plt.grid(True)


plt.savefig("orbit.png", dpi=300, bbox_inches="tight")
plt.show()
