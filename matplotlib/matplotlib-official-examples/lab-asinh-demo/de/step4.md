# Vergleiche das Verhalten von "symlog" und "asinh" auf einem Beispiel y=x-Graphen

Wir werden das Verhalten von "symlog" und "asinh" auf einem Beispiel y=x-Graphen vergleichen. Wir werden denselben Graphen 两次 mals plotten, einmal mit "symlog" und einmal mit "asinh".

```python
fig1 = plt.figure()
ax0, ax1 = fig1.subplots(1, 2, sharex=True)

ax0.plot(x, x)
ax0.set_yscale('symlog')
ax0.grid()
ax0.set_title('symlog')

ax1.plot(x, x)
ax1.set_yscale('asinh')
ax1.grid()
ax1.set_title('asinh')
```

注：原文中“两次”表述有误，已按正确意思翻译。
