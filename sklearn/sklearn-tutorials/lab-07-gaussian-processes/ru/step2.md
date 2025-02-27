# Примеры GPR

GPR с оценкой уровня шума: Этот пример иллюстрирует GPR с суммарным ядром, включающим WhiteKernel для оценки уровня шума в данных.

```python
from sklearn.gaussian_process.kernels import WhiteKernel

# Создаем модель GPR с ядром RBF и WhiteKernel
kernel = RBF() + WhiteKernel()
model = GaussianProcessRegressor(kernel=kernel)

# Подгоняем модель под обучающие данные
model.fit(X_train, y_train)

# Предсказываем с использованием обученной модели
y_pred = model.predict(X_test)
```

Сравнение GPR и Кернел-регрессии с гребневым штрафом: И кернел-регрессия с гребневым штрафом (Kernel Ridge Regression, KRR), и GPR обучают целевую функцию с использованием "ядерного трюка". GPR обучает генеративную, вероятностную модель и может предоставлять доверительные интервалы, в то время как KRR только дает предсказания.

```python
from sklearn.kernel_ridge import KernelRidge

# Создаем модель Кернел-регрессии с гребневым штрафом
krr_model = KernelRidge(kernel='rbf')

# Подгоняем модель KRR под обучающие данные
krr_model.fit(X_train, y_train)

# Предсказываем с использованием модели KRR
krr_y_pred = krr_model.predict(X_test)

# Сравниваем результаты с GPR
gpr_model = GaussianProcessRegressor(kernel=RBF())
gpr_model.fit(X_train, y_train)
gpr_y_pred = gpr_model.predict(X_test)
```

GPR на данных о CO2 на Мауна-Лоа: Этот пример демонстрирует комплексное проектирование ядра и оптимизацию гиперпараметров с использованием градиентного подъема по логарифмической маргинальной правдоподобию. Данные состоят из месячных средних концентраций CO2 в атмосфере, собранных на обсерватории Мауна-Лоа в Гавайях. Задача - построить модель зависимости концентрации CO2 от времени.

```python
from sklearn.gaussian_process.kernels import RBF, ExpSineSquared, RationalQuadratic, WhiteKernel

# Создаем модель GPR с составным ядром
kernel = 34.4**2 * RBF(length_scale=41.8) + 3.27**2 * RBF(length_scale=180) * ExpSineSquared(length_scale=1.44, periodicity=1) + 0.446**2 * RationalQuadratic(alpha=17.7, length_scale=0.957) + 0.197**2 * RBF(length_scale=0.138) + WhiteKernel(noise_level=0.0336)
model = GaussianProcessRegressor(kernel=kernel)

# Подгоняем модель под данные
model.fit(X_train, y_train)

# Предсказываем с использованием обученной модели
y_pred = model.predict(X_test)
```
