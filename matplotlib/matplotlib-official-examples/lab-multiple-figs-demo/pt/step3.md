# Criar a figura 1

Começaremos criando a primeira figura, que conterá dois subplots. Plotaremos a primeira onda senoidal no subplot superior e o dobro da amplitude da primeira onda senoidal no subplot inferior.

```python
plt.figure(1)

# Top subplot
plt.subplot(211)
plt.plot(t, s1)

# Bottom subplot
plt.subplot(212)
plt.plot(t, 2*s1)
```
