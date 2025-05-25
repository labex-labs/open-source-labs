# Criar uma Máscara

Neste exemplo, criamos uma máscara para remover triângulos indesejados. Primeiro, criamos os espaços paramétricos `radii` e `angles`.

```python
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi/n_angles
```
