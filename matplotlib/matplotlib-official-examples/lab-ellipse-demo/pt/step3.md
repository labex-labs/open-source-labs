# Desenhando Elipses com Ângulos Diferentes

Neste exemplo, desenharemos várias elipses com ângulos diferentes. Usaremos um loop para criar uma instância `Ellipse` para cada ângulo que desejamos desenhar.

```python
# Define the angle step and the range of angles to draw
angle_step = 45  # degrees
angles = np.arange(0, 180, angle_step)

# Create the plot and set the aspect ratio to 'equal'
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# Loop over the angles and draw an ellipse for each angle
for angle in angles:
    ellipse = Ellipse((0, 0), 4, 2, angle=angle, alpha=0.1)
    ax.add_artist(ellipse)

# Set the x and y limits of the plot
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)

# Show the plot
plt.show()
```
