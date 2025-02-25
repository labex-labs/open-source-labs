# Crear el diagrama

Ahora podemos crear nuestro diagrama utilizando los datos y los colores que hemos especificado:

```python
fig, ax = plt.subplots(facecolor=(.18,.31,.31))
ax.set_facecolor('#eafff5')
ax.set_title('Voltage vs. time chart', color='0.7')
ax.set_xlabel('Time [s]', color='c')
ax.set_ylabel('Voltage [mV]', color='peachpuff')
ax.plot(t, s, 'xkcd:crimson')
ax.plot(t,.7*s, color='C4', linestyle='--')
ax.tick_params(labelcolor='tab:orange')
```
