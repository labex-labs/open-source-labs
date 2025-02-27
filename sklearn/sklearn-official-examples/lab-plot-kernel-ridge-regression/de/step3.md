# Vergleiche die Zeiten von SVR und Kernel Ridge Regression

Wir werden die Anpassungs- und Vorhersagezeiten von SVR- und KRR-Modellen mit den besten Hyperparametern vergleichen, die in Schritt 2 gefunden wurden.

```python
import time

# Fit SVR
t0 = time.time()
svr.fit(X[:train_size], y[:train_size])
svr_fit = time.time() - t0

# Drucke die besten Parameter und den Score für das SVR-Modell
print(f"Bestes SVR mit Parametern: {svr.best_params_} und R2-Score: {svr.best_score_:.3f}")
print("SVR-Komplexität und Bandbreite ausgewählt und Modell in %.3f s angepasst" % svr_fit)

# Fit KRR
t0 = time.time()
kr.fit(X[:train_size], y[:train_size])
kr_fit = time.time() - t0

# Drucke die besten Parameter und den Score für das KRR-Modell
print(f"Bestes KRR mit Parametern: {kr.best_params_} und R2-Score: {kr.best_score_:.3f}")
print("KRR-Komplexität und Bandbreite ausgewählt und Modell in %.3f s angepasst" % kr_fit)

# Berechne das Support-Vektor-Verhältnis für SVR
sv_ratio = svr.best_estimator_.support_.shape[0] / train_size
print("Support-Vektor-Verhältnis: %.3f" % sv_ratio)

# Vorhersage mit SVR
t0 = time.time()
y_svr = svr.predict(X_plot)
svr_predict = time.time() - t0
print("SVR-Vorhersage für %d Eingaben in %.3f s" % (X_plot.shape[0], svr_predict))

# Vorhersage mit KRR
t0 = time.time()
y_kr = kr.predict(X_plot)
kr_predict = time.time() - t0
print("KRR-Vorhersage für %d Eingaben in %.3f s" % (X_plot.shape[0], kr_predict))
```
