# Create SkewT-logP Diagram

We will now create the SkewT-logP diagram using the SkewXAxes projection that we registered earlier. We will first create a figure object and add a subplot with the SkewXAxes projection. We will then plot the temperature and dew point data on the diagram using the semilogy function. Finally, we will set the limits and ticks for the X and Y axis and display the plot.

```python
fig = plt.figure(figsize=(6.5875, 6.2125))
ax = fig.add_subplot(projection='skewx')

ax.semilogy(T, p, color='C3')
ax.semilogy(Td, p, color='C2')

ax.axvline(0, color='C0')

ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_minor_formatter(NullFormatter())
ax.set_yticks(np.linspace(100, 1000, 10))
ax.set_ylim(1050, 100)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.set_xlim(-50, 50)

plt.grid(True)
plt.show()
```
