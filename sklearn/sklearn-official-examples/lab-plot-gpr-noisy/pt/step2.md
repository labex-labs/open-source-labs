# Visualização de Dados

Nesta etapa, visualizaremos os dados gerados.

```python
import matplotlib.pyplot as plt

plt.plot(X, y, label="Sinal esperado")
plt.legend()
plt.xlabel("X")
_ = plt.ylabel("y")
```
