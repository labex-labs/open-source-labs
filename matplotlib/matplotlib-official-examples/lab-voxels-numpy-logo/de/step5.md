# Vereng die Lücken

Wir verengen die Lücken zwischen jedem Voxel, indem wir die Koordinaten jedes Voxels mithilfe der `indices`-Funktion von NumPy modifizieren.

```python
x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float) // 2
x[0::2, :, :] += 0.05
y[:, 0::2, :] += 0.05
z[:, :, 0::2] += 0.05
x[1::2, :, :] += 0.95
y[:, 1::2, :] += 0.95
z[:, :, 1::2] += 0.95
```
