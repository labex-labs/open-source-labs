# Visualiser la fonction prédite optimisée

Enfin, visualisons la fonction prédite en utilisant les hyperparamètres optimisés.

```python
# Predict the target values using the optimized model
y_pred_opt = best_krr.predict(X_test)

# Visualize the data and the optimized predicted function
plt.scatter(X, y, color='blue', label='Données')
plt.plot(X_test, y_pred_opt, color='green', label='Fonction prédite optimisée')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
