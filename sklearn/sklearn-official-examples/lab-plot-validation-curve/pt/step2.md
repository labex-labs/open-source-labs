# Definindo o Intervalo de Hiperparâmetros

Vamos definir um intervalo de valores para o parâmetro do kernel SVM gama que desejamos testar.

```python
param_range = np.logspace(-6, -1, 5)
```
