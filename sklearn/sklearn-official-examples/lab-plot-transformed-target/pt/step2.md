# Plotar as distribuições dos alvos

Plotamos as funções de densidade de probabilidade do alvo antes e depois de aplicar as funções logarítmicas.

```python
f, (ax0, ax1) = plt.subplots(1, 2)

ax0.hist(y, bins=100, density=True)
ax0.set_xlim([0, 2000])
ax0.set_ylabel("Probabilidade")
ax0.set_xlabel("Alvo")
ax0.set_title("Distribuição do alvo")

ax1.hist(y_trans, bins=100, density=True)
ax1.set_ylabel("Probabilidade")
ax1.set_xlabel("Alvo")
ax1.set_title("Distribuição do alvo transformado")

f.suptitle("Dados sintéticos", y=1.05)
plt.tight_layout()
```
