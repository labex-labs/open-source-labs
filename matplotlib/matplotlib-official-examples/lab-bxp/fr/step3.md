# Personnaliser les statistiques du diagramme en boîte

Nous pouvons modifier n'importe laquelle des statistiques du diagramme en boîte calculées dans l'Étape 2. Dans cet exemple, nous définissons la médiane de chaque ensemble sur la médiane de toutes les données et doublons les moyennes.

```python
for n in range(len(stats)):
    stats[n]['med'] = np.median(data)
    stats[n]['mean'] *= 2
```
