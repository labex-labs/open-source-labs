# Criar a animação

Finalmente, podemos criar a animação usando a classe `FuncAnimation`. Passaremos os parâmetros `fig`, `run`, `data_gen`, `init_func` e `interval` para criar a animação. Também definiremos o parâmetro `save_count` como 100 para garantir que apenas os últimos 100 quadros sejam salvos.

```python
ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init,
                              save_count=100)
```
