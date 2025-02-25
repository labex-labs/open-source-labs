# Conectar los deslizadores a la función de actualización

En este paso, conectará los deslizadores a la función de actualización. Esto garantizará que la gráfica se actualice cada vez que se cambien los valores de los deslizadores.

```python
sfreq.on_changed(update)
samp.on_changed(update)
```
