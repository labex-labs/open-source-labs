# Gefüllte Kontur mit expliziten Ebenen erstellen

Jetzt erstellen wir einen gefüllten Konturplot mit expliziten Ebenen. Wir verwenden die `contourf`-Methode mit dem `levels`-Parameter auf eine Liste von Werten gesetzt, um die Konturebenen anzugeben. Wir setzen auch die Farbskala auf eine Liste von Farben und den `extend`-Parameter auf `'both'`, um Werte außerhalb des Bereichs der Ebenen anzuzeigen.

```python
# Create filled contour with explicit levels
fig, ax = plt.subplots()
levels = [-1.5, -1, -0.5, 0, 0.5, 1]
CS = ax.contourf(X, Y, Z, levels, colors=('r', 'g', 'b'),
                 origin=origin, extend='both')
CS2 = ax.contour(X, Y, Z, levels, colors=('k',),
                 linewidths=(3,), origin=origin)

# Add title, axis labels, and colorbar
ax.set_title('Filled Contour with Explicit Levels')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z Label')

# Show plot
plt.show()
```
