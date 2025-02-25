# Daten mit linearer Methode interpolieren

Der zweite Schritt besteht darin, die Daten mit der linearen Methode zu interpolieren. Wir werden ein regelmäßiges Quadgitter erstellen und dann die Methode LinearTriInterpolator verwenden, um die Daten zu interpolieren. Schließlich werden wir die interpolierten Daten plotten.

```python
# Interpoliere auf ein regelmäßiges Quadgitter.
z = np.cos(1.5 * x) * np.cos(1.5 * y)
xi, yi = np.meshgrid(np.linspace(0, 3, 20), np.linspace(0, 3, 20))

# Interpoliere mit linearer Methode.
interp_lin = mtri.LinearTriInterpolator(triang, z)
zi_lin = interp_lin(xi, yi)

# Plotten der interpolierten Daten.
plt.contourf(xi, yi, zi_lin)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Linear interpolation")
plt.show()
```
