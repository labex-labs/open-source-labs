# Comparer les temps de SVR et de régression ridge du noyau

Nous allons comparer les temps d'ajustement et de prédiction des modèles SVR et KRR en utilisant les meilleurs hyperparamètres trouvés dans l'Étape 2.

```python
import time

# Ajuster SVR
t0 = time.time()
svr.fit(X[:train_size], y[:train_size])
svr_fit = time.time() - t0

# Afficher les meilleurs paramètres et le score pour le modèle SVR
print(f"Meilleur SVR avec paramètres : {svr.best_params_} et score R2 : {svr.best_score_:.3f}")
print("Complexité et largeur de bande de SVR sélectionnées et modèle ajusté en %.3f s" % svr_fit)

# Ajuster KRR
t0 = time.time()
kr.fit(X[:train_size], y[:train_size])
kr_fit = time.time() - t0

# Afficher les meilleurs paramètres et le score pour le modèle KRR
print(f"Meilleur KRR avec paramètres : {kr.best_params_} et score R2 : {kr.best_score_:.3f}")
print("Complexité et largeur de bande de KRR sélectionnées et modèle ajusté en %.3f s" % kr_fit)

# Calculer le rapport de vecteurs de support pour SVR
sv_ratio = svr.best_estimator_.support_.shape[0] / train_size
print("Rapport de vecteurs de support : %.3f" % sv_ratio)

# Prédire à l'aide de SVR
t0 = time.time()
y_svr = svr.predict(X_plot)
svr_predict = time.time() - t0
print("Prédiction SVR pour %d entrées en %.3f s" % (X_plot.shape[0], svr_predict))

# Prédire à l'aide de KRR
t0 = time.time()
y_kr = kr.predict(X_plot)
kr_predict = time.time() - t0
print("Prédiction KRR pour %d entrées en %.3f s" % (X_plot.shape[0], kr_predict))
```
