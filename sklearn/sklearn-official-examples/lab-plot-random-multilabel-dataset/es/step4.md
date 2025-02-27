# Imprimir las probabilidades de clase y de características

Por último, imprimimos las probabilidades de clase y de características para cada clase utilizando las probabilidades de clase y de características devueltas por la función `plot_2d`.

```python
print("Los datos se generaron a partir de (random_state=%d):" % RANDOM_SEED)
print("Clase", "P(C)", "P(w0|C)", "P(w1|C)", sep="\t")
for k, p, p_w in zip(["rojo", "azul", "amarillo"], p_c, p_w_c.T):
    print("%s\t%0.2f\t%0.2f\t%0.2f" % (k, p, p_w[0], p_w[1]))
```
