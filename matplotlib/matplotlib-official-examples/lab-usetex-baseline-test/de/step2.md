# Setzen der Matplotlib-Schriftart

Wir müssen die Schriftart festlegen, die für Matplotlib-Text verwendet werden soll. Wir werden die Computer Modern-Schriftart verwenden und sie als Standardschriftart für Matplotlib festlegen.

```python
plt.rcParams.update({"mathtext.fontset": "cm", "mathtext.rm": "serif"})
```
