# Definir as Classes Knob e Param

O próximo passo é definir as classes Knob e Param. Essas classes serão usadas para controlar a frequência e a amplitude das formas de onda na GUI.

```python
class Knob:
    """
    Knob - classe simples com um método "setKnob".
    Uma instância de Knob é anexada a uma instância de Param, por exemplo, param.attach(knob)
    A classe base é para fins de documentação.
    """

    def setKnob(self, value):
        pass


class Param:
    """
    A ideia da classe "Param" é que algum parâmetro na GUI pode ter
    vários knobs que o controlam e refletem o estado do parâmetro, por exemplo,
    um controle deslizante, texto e arrastar podem alterar o valor da frequência em
    a forma de onda deste exemplo.
    A classe permite uma maneira mais limpa de atualizar/"feedback" para os outros knobs quando
    um está sendo alterado. Além disso, esta classe lida com restrições de mínimo/máximo para todos
    os knobs.
    Ideia - lista de knobs - no método "set", o objeto knob também é passado
      - os outros knobs na lista de knobs têm um método "set" que é
        chamado para os outros.
    """

    def __init__(self, initialValue=None, minimum=0., maximum=1.):
        self.minimum = minimum
        self.maximum = maximum
        if initialValue != self.constrain(initialValue):
            raise ValueError('valor inicial ilegal')
        self.value = initialValue
        self.knobs = []

    def attach(self, knob):
        self.knobs += [knob]

    def set(self, value, knob=None):
        self.value = value
        self.value = self.constrain(value)
        for feedbackKnob in self.knobs:
            if feedbackKnob != knob:
                feedbackKnob.setKnob(self.value)
        return self.value

    def constrain(self, value):
        if value <= self.minimum:
            value = self.minimum
        if value >= self.maximum:
            value = self.maximum
        return value
```
