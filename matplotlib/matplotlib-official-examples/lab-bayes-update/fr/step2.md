# Définir la fonction de densité de probabilité (PDF) de la distribution bêta

La distribution bêta est une distribution de probabilité continue qui est souvent utilisée pour représenter la distribution des probabilités. Dans la mise à jour bayésienne, nous utilisons la distribution bêta comme distribution a priori pour représenter nos croyances sur la probabilité d'une hypothèse avant d'observer toute donnée. Nous mettons ensuite à jour la distribution bêta à mesure que nous observons de nouvelles données.

Pour simuler la mise à jour bayésienne, nous devons définir une fonction qui calcule la fonction de densité de probabilité (PDF) de la distribution bêta. Nous pouvons utiliser la fonction `math.gamma` pour calculer la fonction gamma, qui est utilisée dans la PDF de la distribution bêta.

```python
def beta_pdf(x, a, b):
    return (x**(a-1) * (1-x)**(b-1) * math.gamma(a + b)
            / (math.gamma(a) * math.gamma(b)))
```
