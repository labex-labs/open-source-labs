# Verfeine Daten

```python
refiner = UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(V, subdiv=3)
```

Erklärung:

- `UniformTriRefiner` ist eine Klasse, die eine Triangulation verfeinert, um einen genauereren Plot zu erstellen.
- `refiner` ist eine Instanz der `UniformTriRefiner`-Klasse.
- `tri_refi` und `z_test_refi` sind die verfeinerte Triangulation und die Potentialwerte respective.
