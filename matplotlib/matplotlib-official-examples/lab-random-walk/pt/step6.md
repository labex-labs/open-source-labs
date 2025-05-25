# Criar Animação

Criamos uma animação usando a classe `FuncAnimation` de `matplotlib.animation`. Passamos o objeto da figura, a função de atualização, o número total de frames (que é igual ao número de passos nos passeios aleatórios), a lista de todos os passeios aleatórios e a lista de todas as linhas como argumentos para o construtor `FuncAnimation`.

```python
# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(walks, lines), interval=100)
```
