# Évaluez le modèle

Enfin, nous pouvons évaluer la précision de notre modèle en comparant les valeurs prédites avec les valeurs réelles.

```python
# Calculez la précision du modèle
accuracy = accuracy_score(y_test, y_pred)

# Affichez la précision
print("Précision :", accuracy)
```
