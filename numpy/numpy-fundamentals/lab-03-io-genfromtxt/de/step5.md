# Festlegen des Datentyps

Das Argument `dtype` wird verwendet, um zu steuern, wie die Zeichenketten in andere Typen umgewandelt werden. Es kann ein einzelner Typ, eine Sequenz von Typen, eine komma-getrennte Zeichenkette, ein Wörterbuch, eine Sequenz von Tupeln, ein vorhandenes `numpy.dtype`-Objekt oder `None` sein, um den Typ aus den Daten selbst zu bestimmen.

```python
np.genfromtxt(StringIO(data), dtype=float)
```
