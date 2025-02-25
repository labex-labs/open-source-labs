# Erstelle Figur 1

Wir beginnen mit der Erstellung der ersten Figur, die zwei Teilbilder enthalten wird. Wir werden die erste Sinuswelle im oberen Teilbild und die doppelte Amplitude der ersten Sinuswelle im unteren Teilbild plotten.

```python
plt.figure(1)

# Oberes Teilbild
plt.subplot(211)
plt.plot(t, s1)

# Unteres Teilbild
plt.subplot(212)
plt.plot(t, 2*s1)
```
