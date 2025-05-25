# Exemplos de GPR

GPR com estimativa de nível de ruído: Este exemplo ilustra GPR com um kernel soma incluindo um `WhiteKernel` para estimar o nível de ruído dos dados.

```python
from sklearn.gaussian_process.kernels import WhiteKernel

# Cria um modelo GPR com um kernel RBF e um WhiteKernel
kernel = RBF() + WhiteKernel()
model = GaussianProcessRegressor(kernel=kernel)

# Ajusta o modelo aos dados de treino
model.fit(X_train, y_train)

# Prediz usando o modelo treinado
y_pred = model.predict(X_test)
```

Comparação de GPR e Regressão de Ridge com Kernel: Tanto a regressão de ridge com kernel (KRR) como o GPR aprendem uma função alvo usando o "truque do kernel". O GPR aprende um modelo probabilístico gerativo e pode fornecer intervalos de confiança, enquanto a KRR apenas fornece previsões.

```python
from sklearn.kernel_ridge import KernelRidge

# Cria um modelo de Regressão de Ridge com Kernel
krr_model = KernelRidge(kernel='rbf')

# Ajusta o modelo KRR aos dados de treino
krr_model.fit(X_train, y_train)

# Prediz usando o modelo KRR
krr_y_pred = krr_model.predict(X_test)

# Compara os resultados com o GPR
gpr_model = GaussianProcessRegressor(kernel=RBF())
gpr_model.fit(X_train, y_train)
gpr_y_pred = gpr_model.predict(X_test)
```

GPR em dados de CO2 de Mauna Loa: Este exemplo demonstra a engenharia de kernel complexa e a otimização de hiperparâmetros usando ascensão de gradiente na verossimilhança marginal logarítmica. Os dados consistem em concentrações médias atmosféricas mensais de CO2 coletadas no Observatório de Mauna Loa no Havaí. O objetivo é modelar a concentração de CO2 como função do tempo.

```python
from sklearn.gaussian_process.kernels import RBF, ExpSineSquared, RationalQuadratic, WhiteKernel

# Cria um modelo GPR com um kernel composto
kernel = 34.4**2 * RBF(length_scale=41.8) + 3.27**2 * RBF(length_scale=180) * ExpSineSquared(length_scale=1.44, periodicity=1) + 0.446**2 * RationalQuadratic(alpha=17.7, length_scale=0.957) + 0.197**2 * RBF(length_scale=0.138) + WhiteKernel(noise_level=0.0336)
model = GaussianProcessRegressor(kernel=kernel)

# Ajusta o modelo aos dados
model.fit(X_train, y_train)

# Prediz usando o modelo treinado
y_pred = model.predict(X_test)
```
