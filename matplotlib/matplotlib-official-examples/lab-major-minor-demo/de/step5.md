# Automatische Auswahl von Markierungen für große und kleine Markierungen

```python
# Create data
t = np.arange(0.0, 100.0, 0.01)
s = np.sin(2 * np.pi * t) * np.exp(-t * 0.01)

# Plot the data
fig, ax = plt.subplots()
ax.plot(t, s)

# Set the minor locator
ax.xaxis.set_minor_locator(AutoMinorLocator())

# Set the tick parameters
ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='r')

# Display the plot
plt.show()
```

In diesem Schritt erstellen wir neue Daten und plotten sie. Anschließend legen wir den kleinen Markierungsgeber fest, um die Anzahl der kleinen Markierungen automatisch auszuwählen. Danach legen wir die Markierungs-Parameter, d.h. die Breite und Länge der Markierungen und ihre Farbe, für sowohl die großen als auch die kleinen Markierungen fest. Schließlich zeigen wir das Diagramm an.
