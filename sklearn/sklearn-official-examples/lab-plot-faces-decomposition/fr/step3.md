# Composantes non négatives - NMF

Ensuite, nous appliquons la Factorisation de Matrice Non Négative (NMF), qui factorise la matrice de données en deux matrices non négatives, l'une contenant les vecteurs de base et l'autre contenant les coefficients. Cela résulte en une représentation des données basée sur des parties.

```python
# Composantes non négatives - NMF
nmf_estimator = decomposition.NMF(n_components=n_components, tol=5e-3)
nmf_estimator.fit(faces)  # ensemble de données non négatif original
plot_gallery("Composantes non négatives - NMF", nmf_estimator.components_[:n_components])
```
