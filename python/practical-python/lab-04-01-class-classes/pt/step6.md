# Escopo de Classe (Class Scoping)

Classes não definem um escopo de nomes.

```python
class Player:
    ...
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def left(self, amt):
        move(-amt, 0)       # NÃO. Chama uma função global `move`
        self.move(-amt, 0)  # SIM. Chama o método `move` de cima.
```

Se você deseja operar em uma instância, você sempre se refere a ela explicitamente (por exemplo, `self`).

Começando com este conjunto de exercícios, começamos a fazer uma série de mudanças no código existente das seções anteriores. É fundamental que você tenha uma versão funcional do Exercício 3.18 para começar. Se você não tiver isso, trabalhe a partir do código da solução encontrado no diretório `Solutions/3_18`. É bom copiá-lo.
