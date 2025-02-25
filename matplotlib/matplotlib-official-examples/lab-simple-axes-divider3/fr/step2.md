# Configurez la figure et les axes

Nous allons créer un objet figure et configurer quatre objets axes à l'aide de la méthode `fig.add_axes`.

```python
fig = plt.figure(figsize=(5.5, 4))
rect = (0.1, 0.1, 0.8, 0.8)
ax = [fig.add_axes(rect, label="%d" % i) for i in range(4)]
```
