# Definir las clases Knob y Param

El siguiente paso es definir las clases Knob y Param. Estas clases se utilizarán para controlar la frecuencia y la amplitud de las formas de onda en la interfaz gráfica de usuario (GUI).

```python
class Knob:
    """
    Knob - clase simple con un método "setKnob".
    Una instancia de Knob está adjunta a una instancia de Param, por ejemplo, param.attach(knob)
    La clase base es para fines de documentación.
    """

    def setKnob(self, value):
        pass


class Param:
    """
    La idea de la clase "Param" es que algún parámetro en la GUI puede tener
    varios pernos que tanto lo controlan como reflejan el estado del parámetro, por ejemplo,
    un deslizador, texto y arrastrar todo pueden cambiar el valor de la frecuencia en
    la forma de onda de este ejemplo.
    La clase permite una forma más limpia de actualizar/"dar retroalimentación" a los otros pernos cuando
    uno está siendo cambiado. Además, esta clase maneja las restricciones de mínimo/máximo para todos
    los pernos.
    Idea - lista de pernos - en el método "set", el objeto perno se pasa también
      - los otros pernos en la lista de pernos tienen un método "set" que se llama
        para los demás.
    """

    def __init__(self, initialValue=None, minimum=0., maximum=1.):
        self.minimum = minimum
        self.maximum = maximum
        if initialValue!= self.constrain(initialValue):
            raise ValueError('valor inicial ilegal')
        self.value = initialValue
        self.knobs = []

    def attach(self, knob):
        self.knobs += [knob]

    def set(self, value, knob=None):
        self.value = value
        self.value = self.constrain(value)
        for feedbackKnob in self.knobs:
            if feedbackKnob!= knob:
                feedbackKnob.setKnob(self.value)
        return self.value

    def constrain(self, value):
        if value <= self.minimum:
            value = self.minimum
        if value >= self.maximum:
            value = self.maximum
        return value
```
