# Create the Inner GridSpec

Maintenant, nous allons créer le gridspec interne. Nous utiliserons la méthode `GridSpecFromSubplotSpec` pour créer un gridspec 3 x 3 qui sera un sous-graphe du gridspec externe.

```python
gs00 = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec=gs0[0])
```
