# Crear el contenedor de barras y la animación

Utilizar `plt.hist` nos permite obtener una instancia de `BarContainer`, que es una colección de instancias de `Rectangle`. Utilizamos `FuncAnimation` para configurar la animación.

```python
# Usar plt.hist nos permite obtener una instancia de BarContainer, que es una
# colección de instancias de Rectangle. Llamar a prepare_animation definirá
# la función animate que trabaja con el BarContainer suministrado. Todo esto se utiliza para configurar FuncAnimation.
fig, ax = plt.subplots()
_, _, bar_container = ax.hist(data, HIST_BINS, lw=1, ec="yellow", fc="green", alpha=0.5)
ax.set_ylim(top=55)  # establece un límite seguro para asegurarse de que todos los datos sean visibles.

ani = animation.FuncAnimation(fig, animate, 50, repeat=False, blit=True)
plt.show()
```
