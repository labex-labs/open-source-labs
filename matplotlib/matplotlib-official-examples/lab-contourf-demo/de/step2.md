# Gefüllte Kontur mit automatischen Ebenen erstellen

Als nächstes erstellen wir einen gefüllten Konturplot mit automatischen Ebenen. Wir verwenden die `contourf`-Methode mit dem `cmap`-Parameter auf `plt.cm.bone` gesetzt, um die Farbskala anzugeben. Wir fügen auch Konturlinien mit der `contour`-Methode hinzu und übergeben einen Teil der für die gefüllten Konturen verwendeten Konturebenen.

```python
# Create filled contour with automatic levels
fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, 10, cmap=plt.cm.bone, origin=origin)
CS2 = ax.contour(CS, levels=CS.levels[::2], colors='r', origin=origin)

# Add title, axis labels, and colorbar
ax.set_title('Filled Contour with Automatic Levels')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z Label')
cbar.add_lines(CS2)

# Show plot
plt.show()
```
