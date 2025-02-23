# Crear la animación

Finalmente, podemos crear la animación utilizando la clase `FuncAnimation`. Pasaremos los parámetros `fig`, `run`, `data_gen`, `init_func` e `interval` para crear la animación. También estableceremos el parámetro `save_count` en 100 para asegurarnos de que solo se guarden los últimos 100 fotogramas.

```python
ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init,
                              save_count=100)
```
