# Die Animation erstellen

Schließlich können wir die Animation mithilfe der `FuncAnimation`-Klasse erstellen. Wir werden die Parameter `fig`, `run`, `data_gen`, `init_func` und `interval` übergeben, um die Animation zu erstellen. Wir werden auch den Parameter `save_count` auf 100 setzen, um sicherzustellen, dass nur die letzten 100 Frames gespeichert werden.

```python
ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init,
                              save_count=100)
```
