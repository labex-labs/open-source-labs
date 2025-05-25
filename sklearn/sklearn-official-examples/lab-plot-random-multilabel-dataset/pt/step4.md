# Imprimir as Probabilidades de Classe e de Característica

Finalmente, imprimimos as probabilidades de classe e de característica para cada classe utilizando as probabilidades de classe e de característica retornadas pela função `plot_2d`.

```python
print("Os dados foram gerados de (random_state=%d):" % RANDOM_SEED)
print("Classe", "P(C)", "P(w0|C)", "P(w1|C)", sep="\t")
for k, p, p_w in zip(["red", "blue", "yellow"], p_c, p_w_c.T):
    print("%s\t%0.2f\t%0.2f\t%0.2f" % (k, p, p_w[0], p_w[1]))
```
