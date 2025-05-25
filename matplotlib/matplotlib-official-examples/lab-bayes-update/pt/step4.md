# Criar Animação

Agora que definimos a classe `UpdateDist`, podemos criar a animação usando a classe `FuncAnimation` do Matplotlib. Criamos um objeto de figura e um objeto de eixo e passamos o objeto de eixo para a classe `UpdateDist` para criar uma nova instância da classe.

```python
fig, ax = plt.subplots()
ud = UpdateDist(ax, prob=0.7)
anim = FuncAnimation(fig, ud, frames=100, interval=100, blit=True)
plt.show()
```

A classe `FuncAnimation` recebe vários argumentos:

- `fig`: o objeto de figura
- `ud`: a instância `UpdateDist`
- `frames`: o número de quadros a serem animados
- `interval`: o tempo entre os quadros em milissegundos
- `blit`: se deve atualizar apenas as partes do gráfico que foram alteradas
