# Definir a Classe `UpdateDist`

Em seguida, definimos uma classe chamada `UpdateDist` que será usada para atualizar a distribuição beta à medida que novos dados são observados. A classe `UpdateDist` recebe dois argumentos: o objeto de eixo do Matplotlib e a probabilidade inicial de sucesso.

```python
class UpdateDist:
    def __init__(self, ax, prob=0.5):
        self.success = 0
        self.prob = prob
        self.line, = ax.plot([], [], 'k-')
        self.x = np.linspace(0, 1, 200)
        self.ax = ax

        # Set up plot parameters
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 10)
        self.ax.grid(True)

        # This vertical line represents the theoretical value, to
        # which the plotted distribution should converge.
        self.ax.axvline(prob, linestyle='--', color='black')
```

O método `__init__` inicializa a instância da classe definindo o número inicial de sucessos como zero (`self.success = 0`) e a probabilidade inicial de sucesso para o valor passado como argumento (`self.prob = prob`). Também criamos um objeto de linha para representar a distribuição beta e configuramos os parâmetros do gráfico.

O método `__call__` é chamado toda vez que a animação é atualizada. Ele simula um experimento de lançamento de moeda e atualiza a distribuição beta de acordo.

```python
def __call__(self, i):
        # This way the plot can continuously run and we just keep
        # watching new realizations of the process
        if i == 0:
            self.success = 0
            self.line.set_data([], [])
            return self.line,

        # Choose success based on exceed a threshold with a uniform pick
        if np.random.rand() < self.prob:
            self.success += 1
        y = beta_pdf(self.x, self.success + 1, (i - self.success) + 1)
        self.line.set_data(self.x, y)
        return self.line,
```

Se este for o primeiro quadro da animação (`if i == 0`), redefinimos o número de sucessos para zero e limpamos o objeto de linha. Caso contrário, simulamos um experimento de lançamento de moeda gerando um número aleatório entre 0 e 1 (`np.random.rand()`) e comparando-o com a probabilidade de sucesso (`self.prob`). Se o número aleatório for menor que a probabilidade de sucesso, contamos como um sucesso e atualizamos a distribuição beta usando a função `beta_pdf`. Finalmente, atualizamos o objeto de linha com os novos dados e o retornamos.
