# Criar a Animação

Finalmente, criaremos a animação usando o objeto `FuncAnimation`, passando a figura, a função de atualização (update function), o intervalo entre os frames em milissegundos e o número de frames a serem salvos.

```python
animation = FuncAnimation(fig, update, interval=10, save_count=100)
plt.show()
```
