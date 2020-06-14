import sys

import matplotlib.pyplot as plt
import mpmath

from mandelbrot.orbit_calculator import OrbitCalculator

zx = sys.argv[1]
zy = sys.argv[2]
num_iterations = int(sys.argv[3])

print("Generation of orbit for point (", zx, " , ", zy, ") with ", num_iterations, " iterations ...")

# Calculate orbit
c = mpmath.mpc(real=zx, imag=zy)
orbit_re, orbit_im = OrbitCalculator.generate(c, num_iterations)

# Format data for plot
x = range(num_iterations)
orbit_re_float = list(map(float, orbit_re))
orbit_im_float = list(map(float, orbit_im))

# Plot real and imaginary parts
plt.plot(x, orbit_re_float, color="orange", linewidth=1.5)
plt.plot(x, orbit_im_float, color="blue", linewidth=1.5)

# Show grid
plt.grid(True)

# Image size
plt.gcf().set_size_inches(12, 4)

# x axis
plt.xlim([0, 100])

# Save image
plt.savefig("./mandelbrot-orbit.png", bbox_inches="tight")
