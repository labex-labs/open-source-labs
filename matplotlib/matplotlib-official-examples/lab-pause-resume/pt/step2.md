# Definir a Animação

Nesta etapa, definiremos a animação que queremos criar. Criaremos uma animação que exibe uma distribuição normal que se move para a direita a cada quadro.

```python
class PauseAnimation:
    def __init__(self):
        # Criar a figura e o eixo
        fig, ax = plt.subplots()
        ax.set_title('Clique para pausar/retomar a animação')

        # Criar os valores do eixo x
        x = np.linspace(-0.1, 0.1, 1000)

        # Começar com uma distribuição normal
        self.n0 = (1.0 / ((4 * np.pi * 2e-4 * 0.1) ** 0.5)
                   * np.exp(-x ** 2 / (4 * 2e-4 * 0.1)))

        # Criar o gráfico
        self.p, = ax.plot(x, self.n0)

        # Criar a animação
        self.animation = animation.FuncAnimation(
            fig, self.update, frames=200, interval=50, blit=True)

        # Definir a animação como não pausada
        self.paused = False

        # Adicionar um evento de pressionamento de botão para alternar a pausa
        fig.canvas.mpl_connect('button_press_event', self.toggle_pause)

    def toggle_pause(self, *args, **kwargs):
        # Alternar entre pausado e não pausado
        if self.paused:
            self.animation.resume()
        else:
            self.animation.pause()
        self.paused = not self.paused

    def update(self, i):
        # Atualizar a distribuição normal
        self.n0 += i / 100 % 5
        self.p.set_ydata(self.n0 % 20)
        return (self.p,)
```
