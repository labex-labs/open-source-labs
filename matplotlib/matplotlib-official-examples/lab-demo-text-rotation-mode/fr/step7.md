# Créez les sous-figures et appelez la fonction `test_rotation_mode`

Nous allons créer deux sous-figures et appeler la fonction `test_rotation_mode` avec les paramètres `fig` et `mode`.

```python
fig = plt.figure(figsize=(8, 5))
subfigs = fig.subfigures(1, 2)
test_rotation_mode(subfigs[0], "default")
test_rotation_mode(subfigs[1], "anchor")
plt.show()
```
