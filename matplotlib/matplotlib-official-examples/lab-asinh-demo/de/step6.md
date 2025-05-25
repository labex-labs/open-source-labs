# Vergleiche die Skalierungen "symlog" und "asinh" für 2D Cauchy-verteilte Zufallszahlen

Schließlich werden wir die Skalierungen "symlog" und "asinh" für 2D Cauchy-verteilte Zufallszahlen vergleichen. Wir werden denselben Graphen 两次 mals plotten, einmal mit "symlog" und einmal mit "asinh".

```python
fig3 = plt.figure()
ax = fig3.subplots(1, 1)
r = 3 * np.tan(np.random.uniform(-np.pi / 2.02, np.pi / 2.02,
                                 size=(5000,)))
th = np.random.uniform(0, 2*np.pi, size=r.shape)

ax.scatter(r * np.cos(th), r * np.sin(th), s=4, alpha=0.5)
ax.set_xscale('asinh')
ax.set_yscale('symlog')
ax.set_xlabel('asinh')
ax.set_ylabel('symlog')
ax.set_title('2D Cauchy random deviates')
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.grid()
```

注：原文中“两次”表述有误，已按正确意思翻译。
