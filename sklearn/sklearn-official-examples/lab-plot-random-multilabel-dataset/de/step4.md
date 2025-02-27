# Drucken der Klass- und Merkmalswahrscheinlichkeiten

Schließlich drucken wir die Klass- und Merkmalswahrscheinlichkeiten für jede Klasse mit den von der Funktion `plot_2d` zurückgegebenen Klass- und Merkmalswahrscheinlichkeiten.

```python
print("The data was generated from (random_state=%d):" % RANDOM_SEED)
print("Class", "P(C)", "P(w0|C)", "P(w1|C)", sep="\t")
for k, p, p_w in zip(["red", "blue", "yellow"], p_c, p_w_c.T):
    print("%s\t%0.2f\t%0.2f\t%0.2f" % (k, p, p_w[0], p_w[1]))
```
