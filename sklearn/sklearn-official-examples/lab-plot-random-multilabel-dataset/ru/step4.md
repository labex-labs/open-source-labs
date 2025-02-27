# Выводим вероятности классов и признаков

Наконец, мы выводим вероятности классов и признаков для каждого класса с использованием вероятностей классов и вероятностей признаков, возвращаемых функцией `plot_2d`.

```python
print("The data was generated from (random_state=%d):" % RANDOM_SEED)
print("Class", "P(C)", "P(w0|C)", "P(w1|C)", sep="\t")
for k, p, p_w in zip(["red", "blue", "yellow"], p_c, p_w_c.T):
    print("%s\t%0.2f\t%0.2f\t%0.2f" % (k, p, p_w[0], p_w[1]))
```
