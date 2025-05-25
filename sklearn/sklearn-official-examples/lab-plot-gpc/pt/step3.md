# Treinar o Modelo

Treinaremos o modelo GPC usando hiperparâmetros fixos e otimizados. Imprimiremos o log-marginal-likelihood, a precisão e a log-loss dos modelos.

```python
# Hiperparâmetros Fixos
gp_fix = GaussianProcessClassifier(kernel=1.0 * RBF(length_scale=1.0), optimizer=None)
gp_fix.fit(X[:train_size], y[:train_size])

# Hiperparâmetros Otimizados
gp_opt = GaussianProcessClassifier(kernel=1.0 * RBF(length_scale=1.0))
gp_opt.fit(X[:train_size], y[:train_size])

# Resultados
print("Log Marginal Likelihood (inicial): %.3f" % gp_fix.log_marginal_likelihood(gp_fix.kernel_.theta))
print("Log Marginal Likelihood (otimizado): %.3f" % gp_opt.log_marginal_likelihood(gp_opt.kernel_.theta))
print("Precisão: %.3f (inicial) %.3f (otimizado)" % (accuracy_score(y[:train_size], gp_fix.predict(X[:train_size])), accuracy_score(y[:train_size], gp_opt.predict(X[:train_size]))))
print("Log-loss: %.3f (inicial) %.3f (otimizado)" % (log_loss(y[:train_size], gp_fix.predict_proba(X[:train_size])[:, 1]), log_loss(y[:train_size], gp_opt.predict_proba(X[:train_size])[:, 1])))
```
