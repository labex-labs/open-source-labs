# Ejemplos de GPC

Predicciones probabilísticas con GPC: Este ejemplo ilustra la probabilidad predicha de GPC con diferentes elecciones de hiperparámetros.

```python
# Crea un modelo GPC con un kernel RBF
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Ajusta el modelo a los datos de entrenamiento
model.fit(X_train, y_train)

# Predice las probabilidades de clase de los datos de prueba
y_prob = model.predict_proba(X_test)
```

Ilustración de GPC en el conjunto de datos XOR: Este ejemplo demuestra el uso de GPC en el conjunto de datos XOR. Comparamos los resultados de utilizar un kernel estacionario, isotrópico (RBF) y un kernel no estacionario (DotProduct).

```python
# Crea modelos GPC con diferentes kernels
isotropic_kernel = RBF(length_scale=1.0)
non_stationary_kernel = DotProduct(sigma_0=1.0)

# Ajusta los modelos al conjunto de datos XOR
isotropic_model = GaussianProcessClassifier(kernel=isotropic_kernel)
non_stationary_model = GaussianProcessClassifier(kernel=non_stationary_kernel)
isotropic_model.fit(X_xor, y_xor)
non_stationary_model.fit(X_xor, y_xor)

# Realiza predicciones utilizando los modelos entrenados
isotropic_y_pred = isotropic_model.predict(X_test)
non_stationary_y_pred = non_stationary_model.predict(X_test)
```

GPC en el conjunto de datos iris: Este ejemplo ilustra GPC en el conjunto de datos iris utilizando un kernel RBF isotrópico y un kernel RBF anisotrópico. Muestra cómo diferentes elecciones de hiperparámetros pueden afectar la probabilidad predicha.

```python
# Crea modelos GPC con diferentes kernels y ajusta them al conjunto de datos iris
isotropic_kernel = RBF(length_scale=1.0)
anisotropic_kernel = RBF(length_scale=[1.0, 2.0])
isotropic_model = GaussianProcessClassifier(kernel=isotropic_kernel)
anisotropic_model = GaussianProcessClassifier(kernel=anisotropic_kernel)
isotropic_model.fit(X_train, y_train)
anisotropic_model.fit(X_train, y_train)

# Predice las probabilidades de clase
isotropic_y_prob = isotropic_model.predict_proba(X_test)
anisotropic_y_prob = anisotropic_model.predict_proba(X_test)
```
