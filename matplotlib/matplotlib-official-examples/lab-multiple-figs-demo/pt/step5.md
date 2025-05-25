# Fazer alterações na figura 1

Agora, voltaremos para a primeira figura e faremos algumas alterações. Plotaremos a segunda onda senoidal no subplot superior usando marcadores quadrados e removeremos os rótulos de marcação do eixo x do subplot superior.

```python
plt.figure(1)

# Top subplot
plt.subplot(211)
plt.plot(t, s2, 's')
ax = plt.gca()
ax.set_xticklabels([])
```
