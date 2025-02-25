# Färbskala hinzufügen

Fügen Sie eine Färbskala hinzu, indem Sie die `colorbar`-Methode verwenden. Wir werden die Parameter `fraction` und `pad` einstellen, um die Position der Färbskala zu verändern, und das Label festlegen, um den Namen und die Maßeinheiten der Daten anzuzeigen.

```python
# Colorbar
fig.colorbar(C, ax=ax, fraction=0.02, pad=0.1, label='Name [units]')
```
