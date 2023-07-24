# Add Title, X-label, and Y-label

We can add title, X-label, and Y-label to the graph using `title()`, `xlabel()`, and `ylabel()` methods of `pyplot` library. We will add "Voltage vs Time" as the title, "Time [s]" as X-label, and "Voltage [mV]" as Y-label.

```python
plt.title(r'Voltage vs Time', fontsize=20)
plt.xlabel('Time [s]')
plt.ylabel('Voltage [mV]')
```
