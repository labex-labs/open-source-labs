# Plotar o caminho de regularização

Vamos plotar o caminho de regularização usando os coeficientes dos modelos treinados. Os coeficientes serão plotados contra o logaritmo da força de regularização. No lado esquerdo do gráfico (regularizadores fortes), todos os coeficientes são exatamente 0. À medida que a regularização se torna progressivamente menos restritiva, os coeficientes podem assumir valores não nulos um após o outro.

```python
import matplotlib.pyplot as plt

plt.plot(np.log10(cs), coefs_, marker="o")
ymin, ymax = plt.ylim()
plt.xlabel("log(C)")
plt.ylabel("Coeficientes")
plt.title("Caminho da Regressão Logística")
plt.axis("tight")
plt.show()
```
