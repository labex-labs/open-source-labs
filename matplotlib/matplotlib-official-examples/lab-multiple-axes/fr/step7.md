# Créer l'animation

La septième étape consiste à créer l'objet d'animation à l'aide de la fonction `FuncAnimation`. Nous passons l'objet de figure, la fonction d'animation, l'intervalle entre les trames en millisecondes, le nombre de trames et un délai avant de répéter l'animation.

```python
ani = animation.FuncAnimation(
    fig,
    animate,
    interval=50,
    blit=False,  # blitting ne peut pas être utilisé avec les artistes de Figure
    frames=x,
    repeat_delay=100,
)
```
