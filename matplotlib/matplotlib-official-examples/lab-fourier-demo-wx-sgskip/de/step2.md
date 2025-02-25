# Knob- und Param-Klassen definieren

Der nächste Schritt besteht darin, die Knob- und Param-Klassen zu definieren. Diese Klassen werden verwendet, um die Frequenz und die Amplitude der Wellenformen in der grafischen Benutzeroberfläche (GUI) zu steuern.

```python
class Knob:
    """
    Knob - einfache Klasse mit einer "setKnob"-Methode.
    Eine Knob-Instanz ist an eine Param-Instanz angehängt, z.B. param.attach(knob)
    Die Basisklasse dient der Dokumentation.
    """

    def setKnob(self, value):
        pass


class Param:
    """
    Die Idee der "Param"-Klasse ist, dass ein bestimmter Parameter in der GUI möglicherweise
    mehrere Knöpfe hat, die ihn sowohl steuern als auch den Zustand des Parameters widerspiegeln, z.B.
    ein Schieberegler, Text und Ziehen können alle den Wert der Frequenz in
    der Wellenform dieses Beispiels ändern.
    Die Klasse ermöglicht eine saubere Möglichkeit, die anderen Knöpfe zu aktualisieren/"zurückzuführen", wenn
    einer von ihnen geändert wird. Außerdem behandelt diese Klasse die Min/Max-Beschränkungen für alle
    die Knöpfe.
    Idee - Knob-Liste - in der "set"-Methode wird auch das Knob-Objekt übergeben
      - die anderen Knöpfe in der Knob-Liste haben eine "set"-Methode, die
        für die anderen aufgerufen wird.
    """

    def __init__(self, initialValue=None, minimum=0., maximum=1.):
        self.minimum = minimum
        self.maximum = maximum
        if initialValue!= self.constrain(initialValue):
            raise ValueError('illegal initial value')
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
