# Exemplos de GPC

Previsões probabilísticas com GPC: Este exemplo ilustra a probabilidade prevista de GPC com diferentes escolhas de hiperparâmetros.

```python
# Cria um modelo GPC com um kernel RBF
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Ajusta o modelo aos dados de treino
model.fit(X_train, y_train)

# Prediz as probabilidades de classe dos dados de teste
y_prob = model.predict_proba(X_test)
```

Ilustração de GPC no conjunto de dados XOR: Este exemplo demonstra o uso de GPC no conjunto de dados XOR. Comparamos os resultados do uso de um kernel estacionário e isotrópico (RBF) e um kernel não estacionário (DotProduct).

```python
# Cria modelos GPC com diferentes kernels
kernel_isotrópico = RBF(length_scale=1.0)
kernel_não_estacionário = DotProduct(sigma_0=1.0)

# Ajusta os modelos ao conjunto de dados XOR
modelo_isotrópico = GaussianProcessClassifier(kernel=kernel_isotrópico)
modelo_não_estacionário = GaussianProcessClassifier(kernel=kernel_não_estacionário)
modelo_isotrópico.fit(X_xor, y_xor)
modelo_não_estacionário.fit(X_xor, y_xor)

# Prediz usando os modelos treinados
pred_isotrópico = modelo_isotrópico.predict(X_test)
pred_não_estacionário = modelo_não_estacionário.predict(X_test)
```

GPC no conjunto de dados iris: Este exemplo ilustra o GPC no conjunto de dados iris usando um kernel RBF isotrópico e um kernel RBF anisotrópico. Mostra como diferentes escolhas de hiperparâmetros podem afetar a probabilidade prevista.

```python
# Cria modelos GPC com diferentes kernels e ajusta-os ao conjunto de dados iris
kernel_isotrópico = RBF(length_scale=1.0)
kernel_anisotrópico = RBF(length_scale=[1.0, 2.0])
modelo_isotrópico = GaussianProcessClassifier(kernel=kernel_isotrópico)
modelo_anisotrópico = GaussianProcessClassifier(kernel=kernel_anisotrópico)
modelo_isotrópico.fit(X_train, y_train)
modelo_anisotrópico.fit(X_train, y_train)

# Prediz as probabilidades de classe
prob_isotrópico = modelo_isotrópico.predict_proba(X_test)
prob_anisotrópico = modelo_anisotrópico.predict_proba(X_test)
```
