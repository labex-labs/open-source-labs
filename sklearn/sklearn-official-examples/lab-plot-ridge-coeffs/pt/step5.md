# Plotar os resultados

Plotaremos os coeficientes e os erros em função da força de regularização usando Matplotlib.

```python
plt.figure(figsize=(20, 6))

plt.subplot(121)
ax = plt.gca()
ax.plot(alphas, coefs)
ax.set_xscale("log")
plt.xlabel("alpha")
plt.ylabel("pesos")
plt.title("Coeficientes Ridge em função da regularização")
plt.axis("tight")

plt.subplot(122)
ax = plt.gca()
ax.plot(alphas, errors)
ax.set_xscale("log")
plt.xlabel("alpha")
plt.ylabel("erro")
plt.title("Erro dos coeficientes em função da regularização")
plt.axis("tight")

plt.show()
```
