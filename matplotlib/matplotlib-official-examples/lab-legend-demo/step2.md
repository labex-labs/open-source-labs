# Plot more complex labels

In this step, we will plot more complex labels.

```python
# Define data for the chart
x = np.linspace(0, 1)

# Create a chart with multiple lines
fig, (ax0, ax1) = plt.subplots(2, 1)
for n in range(1, 5):
    ax0.plot(x, x**n, label=f"{n=}")

# Create a legend with multiple columns and a title
leg = ax0.legend(loc="upper left", bbox_to_anchor=[0, 1],
                 ncols=2, shadow=True, title="Legend", fancybox=True)
leg.get_title().set_color("red")

# Create a chart with multiple lines and markers
ax1.plot(x, x**2, label="multi\nline")
half_pi = np.linspace(0, np.pi / 2)
ax1.plot(np.sin(half_pi), np.cos(half_pi), label=r"$\frac{1}{2}\pi$")
ax1.plot(x, 2**(x**2), label="$2^{x^2}$")

# Create a legend with a shadow
ax1.legend(shadow=True, fancybox=True)

# Display the chart
plt.show()
```
