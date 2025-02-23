# Создаем анимацию

Наконец, мы можем создать анимацию с использованием класса `FuncAnimation`. Мы передадим параметры `fig`, `run`, `data_gen`, `init_func` и `interval` для создания анимации. Также мы установим параметр `save_count` равным 100, чтобы гарантировать, что будут сохранены только последние 100 кадров.

```python
ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init,
                              save_count=100)
```
