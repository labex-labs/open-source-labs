# Criar o Gráfico

Agora podemos criar nosso gráfico usando os dados e as cores que especificamos:

```python
fig, ax = plt.subplots(facecolor=(.18, .31, .31))
ax.set_facecolor('#eafff5')
ax.set_title('Gráfico de tensão vs. tempo', color='0.7')
ax.set_xlabel('Tempo [s]', color='c')
ax.set_ylabel('Tensão [mV]', color='peachpuff')
ax.plot(t, s, 'xkcd:crimson')
ax.plot(t, .7*s, color='C4', linestyle='--')
ax.tick_params(labelcolor='tab:orange')
```
