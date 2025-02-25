# Setzen der Striche und Beschriftungen für die zweite y-Achse

Wir können die Striche und Beschriftungen für die zweite y-Achse setzen, indem wir die Funktion `set_xticks` verwenden und die Strichpositionen und -beschriftungen als Argumente übergeben.

```python
ax2.set_xticks([0.,.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi],
               labels=["$0$", r"$\frac{1}{2}\pi$",
                       r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
```
