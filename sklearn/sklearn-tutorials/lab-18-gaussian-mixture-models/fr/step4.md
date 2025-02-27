# Regroupez les données

Une fois que le modèle a été ajusté, nous pouvons l'utiliser pour regrouper les données en assignant chaque échantillon au composant gaussien auquel il appartient. La méthode `predict` de la classe `GaussianMixture` peut être utilisée à cette fin.

```python
# Regroupez les données
cluster_labels = gmm.predict(X_test)
```
