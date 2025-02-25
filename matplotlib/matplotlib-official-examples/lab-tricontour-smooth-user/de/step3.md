# Daten verfeinern

In diesem Schritt verwenden wir `tri.UniformTriRefiner`, um die Daten zu verfeinern. Mit der `refine_field`-Methode verfeinern wir die `z`-Werte und erstellen eine neue Triangulation mit höherer Auflösung.

```python
refiner = tri.UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(z, subdiv=3)
```
