# Ejemplos de GPR

GPR con estimación del nivel de ruido: Este ejemplo ilustra GPR con un kernel de suma que incluye un WhiteKernel para estimar el nivel de ruido de los datos.

```python
from sklearn.gaussian_process.kernels import WhiteKernel

# Crea un modelo GPR con un kernel RBF y un WhiteKernel
kernel = RBF() + WhiteKernel()
model = GaussianProcessRegressor(kernel=kernel)

# Ajusta el modelo a los datos de entrenamiento
model.fit(X_train, y_train)

# Realiza predicciones utilizando el modelo entrenado
y_pred = model.predict(X_test)
```

Comparación de GPR y Regresión Ridge con Kernel: Tanto la regresión ridge con kernel (KRR) como GPR aprenden una función objetivo utilizando el "truco del kernel". GPR aprende un modelo generativo y probabilístico y puede proporcionar intervalos de confianza, mientras que KRR solo proporciona predicciones.

```python
from sklearn.kernel_ridge import KernelRidge

# Crea un modelo de Regresión Ridge con Kernel
krr_model = KernelRidge(kernel='rbf')

# Ajusta el modelo KRR a los datos de entrenamiento
krr_model.fit(X_train, y_train)

# Realiza predicciones utilizando el modelo KRR
krr_y_pred = krr_model.predict(X_test)

# Compara los resultados con GPR
gpr_model = GaussianProcessRegressor(kernel=RBF())
gpr_model.fit(X_train, y_train)
gpr_y_pred = gpr_model.predict(X_test)
```

GPR en datos de CO2 de Mauna Loa: Este ejemplo demuestra la ingeniería de kernel compleja y la optimización de hiperparámetros utilizando el ascenso del gradiente en la log-verosimilitud marginal. Los datos consisten en concentraciones mensuales promedio de CO2 atmosférico recolectadas en el Observatorio de Mauna Loa en Hawái. El objetivo es modelar la concentración de CO2 como una función del tiempo.

```python
from sklearn.gaussian_process.kernels import RBF, ExpSineSquared, RationalQuadratic, WhiteKernel

# Crea un modelo GPR con un kernel compuesto
kernel = 34.4**2 * RBF(length_scale=41.8) + 3.27**2 * RBF(length_scale=180) * ExpSineSquared(length_scale=1.44, periodicity=1) + 0.446**2 * RationalQuadratic(alpha=17.7, length_scale=0.957) + 0.197**2 * RBF(length_scale=0.138) + WhiteKernel(noise_level=0.0336)
model = GaussianProcessRegressor(kernel=kernel)

# Ajusta el modelo a los datos
model.fit(X_train, y_train)

# Realiza predicciones utilizando el modelo entrenado
y_pred = model.predict(X_test)
```
