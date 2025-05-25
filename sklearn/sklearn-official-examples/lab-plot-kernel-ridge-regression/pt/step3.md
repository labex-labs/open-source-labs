# Comparar Tempos de SVR e Regressão de Ridge Kernel

Vamos comparar os tempos de ajuste e previsão dos modelos SVR e KRR usando os melhores hiperparâmetros encontrados na Etapa 2.

```python
import time

# Ajustar SVR
t0 = time.time()
svr.fit(X[:train_size], y[:train_size])
svr_fit = time.time() - t0

# Imprimir os melhores parâmetros e pontuação para o modelo SVR
print(f"Melhor SVR com parâmetros: {svr.best_params_} e pontuação R2: {svr.best_score_:.3f}")
print("Complexidade SVR e largura de banda selecionadas e modelo ajustado em %.3f s" % svr_fit)

# Ajustar KRR
t0 = time.time()
kr.fit(X[:train_size], y[:train_size])
kr_fit = time.time() - t0

# Imprimir os melhores parâmetros e pontuação para o modelo KRR
print(f"Melhor KRR com parâmetros: {kr.best_params_} e pontuação R2: {kr.best_score_:.3f}")
print("Complexidade KRR e largura de banda selecionadas e modelo ajustado em %.3f s" % kr_fit)

# Calcular a razão de vetores de suporte para SVR
sv_ratio = svr.best_estimator_.support_.shape[0] / train_size
print("Razão de vetores de suporte: %.3f" % sv_ratio)

# Prever usando SVR
t0 = time.time()
y_svr = svr.predict(X_plot)
svr_predict = time.time() - t0
print("Previsão SVR para %d entradas em %.3f s" % (X_plot.shape[0], svr_predict))

# Prever usando KRR
t0 = time.time()
y_kr = kr.predict(X_plot)
kr_predict = time.time() - t0
print("Previsão KRR para %d entradas em %.3f s" % (X_plot.shape[0], kr_predict))
```
