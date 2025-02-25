# Sammlung zur Grafik hinzufügen

Wir fügen die `EllipseCollection` zur Grafik hinzu.

```python
ax.add_collection(ec)
ax.autoscale_view()
ax.set_xlabel('X')
ax.set_ylabel('y')
cbar = plt.colorbar(ec)
cbar.set_label('X+Y')
plt.show()
```
