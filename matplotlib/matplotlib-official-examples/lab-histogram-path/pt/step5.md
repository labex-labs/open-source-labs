# Gerar o objeto Path e criar um patch a partir dele

Em seguida, geraremos um objeto Path e criaremos um patch a partir dele. Usaremos o objeto Path para desenhar nosso histograma usando retângulos. Adicione o seguinte código:

```python
XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T
barpath = path.Path.make_compound_path_from_polys(XY)
patch = patches.PathPatch(barpath)
patch.sticky_edges.y[:] = [0]
axs[0].add_patch(patch)
axs[0].autoscale_view()
```
