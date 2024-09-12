import matplotlib.pyplot as plt
import numpy as np

# Define the x values (e.g., range from -10 to 10)
range1 = int(input("Write the first range of x: "))
range2 = int(input("Write the second range of x: "))
points = int(input("How many points do you want to create? "))

x = np.linspace(range1, range2, points)

slope = int(input("Write the slope: "))
slash_point = int(input("Write the slash point: "))

# Define the linear equation y = slope * x + slash_point
y = slope * x + slash_point

# Create the plot
plt.plot(x, y, label=f"y = {slope}x + {slash_point}")

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Linear Graph: y = {slope}x + {slash_point}')

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()