# Create Another Inner GridSpec

Nous allons maintenant créer un autre gridspec interne. Cette fois-ci, nous utiliserons la méthode `subgridspec` pour créer un gridspec 3 x 3 qui sera un sous-graphe de la deuxième colonne du gridspec externe.

```python
gs01 = gs0[1].subgridspec(3, 3)
```
