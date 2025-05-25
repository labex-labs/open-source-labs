# Configurar o Gráfico

Criamos um novo objeto `figure` e `axis` e inicializamos a classe `Scope`. Em seguida, passamos as funções `update` e `emitter` para o método `FuncAnimation` para criar a animação.

```python
fig, ax = plt.subplots()
scope = Scope(ax)

ani = animation.FuncAnimation(fig, scope.update, emitter, interval=50,
                              blit=True, save_count=100)

plt.show()
```
