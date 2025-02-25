# Ändere Figur 1

Jetzt kehren wir zur ersten Figur zurück und machen einige Änderungen. Wir werden die zweite Sinuswelle im oberen Teilbild mit quadratischen Markern plotten und die x-Achsenbeschriftungen im oberen Teilbild entfernen.

```python
plt.figure(1)

# Oberes Teilbild
plt.subplot(211)
plt.plot(t, s2,'s')
ax = plt.gca()
ax.set_xticklabels([])
```
