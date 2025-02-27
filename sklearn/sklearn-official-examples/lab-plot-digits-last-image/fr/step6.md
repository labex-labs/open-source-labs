# Amélioration du modèle

Si la précision de notre modèle n'est pas satisfaisante, nous pouvons essayer de l'améliorer en ajustant les hyperparamètres de l'algorithme SVM. Par exemple, nous pouvons essayer de changer la valeur du paramètre `C` :

```python
# Crée le classifieur SVM avec une valeur différente de C
clf = SVC(kernel='linear', C=0.1)

# Entraîne le classifieur sur les données d'entraînement
clf.fit(X_train, y_train)

# Prédit les étiquettes de l'ensemble de test
y_pred = clf.predict(X_test)

# Calcule la précision du modèle
accuracy = accuracy_score(y_test, y_pred)

# Affiche la précision du modèle
print("Précision :", accuracy)
```
