# Anpassen der Skalenbeschriftungen auf der vertikalen Farbskala

Als nächstes werden wir die Skalenbeschriftungen auf der vertikalen Farbskala anpassen. Wir werden eine Farbskala mit `colorbar` erstellen und die Skalenpositionen mit dem Parameter `ticks` angeben. Anschließend werden wir die Skalenbeschriftungen mit `set_yticklabels` auf dem `ax`-Attribut des Farbskala-Objekts festlegen.

```python
# Add colorbar, make sure to specify tick locations to match desired ticklabels
cbar = fig.colorbar(cax, ticks=[-1, 0, 1])
cbar.ax.set_yticklabels(['< -1', '0', '> 1'])  # vertically oriented colorbar
```
