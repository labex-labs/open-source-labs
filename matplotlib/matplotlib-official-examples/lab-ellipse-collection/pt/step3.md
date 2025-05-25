# Criar a Coleção de Elipses

Criamos um `EllipseCollection` com os dados acima e especificamos as unidades como 'x' e os deslocamentos como `XY`.

```python
fig, ax = plt.subplots()

ec = EllipseCollection(ww, hh, aa, units='x', offsets=XY,
                       offset_transform=ax.transData)
```
