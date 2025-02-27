# Affichez les probabilités de classe et de caractéristique

Enfin, nous affichons les probabilités de classe et de caractéristique pour chaque classe en utilisant les probabilités de classe et de caractéristique renvoyées par la fonction `plot_2d`.

```python
print("Les données ont été générées à partir de (random_state=%d):" % RANDOM_SEED)
print("Classe", "P(C)", "P(w0|C)", "P(w1|C)", sep="\t")
for k, p, p_w in zip(["rouge", "bleu", "jaune"], p_c, p_w_c.T):
    print("%s\t%0.2f\t%0.2f\t%0.2f" % (k, p, p_w[0], p_w[1]))
```
