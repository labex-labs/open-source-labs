# Pré-calcul de la matrice de Gram avec des échantillons pondérés

Pour ajuster le réseau élastique en utilisant l'option `precompute` avec les poids d'échantillonnage, nous devons tout d'abord centrer la matrice de conception et la redimensionner par les poids normalisés avant de calculer la matrice de Gram. Nous centrons la matrice de conception en soustrayant la moyenne pondérée de chaque colonne de caractéristiques à chaque ligne. Ensuite, nous redimensionnons la matrice de conception centrée en multipliant chaque ligne par la racine carrée du poids normalisé correspondant. Enfin, nous calculons la matrice de Gram en prenant le produit scalaire de la matrice de conception redimensionnée avec sa transposée.

```python
X_offset = np.average(X, axis=0, weights=normalized_weights)
X_centered = X - np.average(X, axis=0, weights=normalized_weights)
X_scaled = X_centered * np.sqrt(normalized_weights)[:, np.newaxis]
gram = np.dot(X_scaled.T, X_scaled)
```
