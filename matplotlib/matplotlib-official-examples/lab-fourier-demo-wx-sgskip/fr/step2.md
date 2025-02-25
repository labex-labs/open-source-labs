# Définition des classes Knob et Param

L'étape suivante consiste à définir les classes Knob et Param. Ces classes seront utilisées pour contrôler la fréquence et l'amplitude des formes d'ondes dans l'interface graphique utilisateur (GUI).

```python
class Knob:
    """
    Knob - simple class with a "setKnob" method.
    A Knob instance is attached to a Param instance, e.g., param.attach(knob)
    Base class is for documentation purposes.
    """

    def setKnob(self, value):
        pass


class Param:
    """
    L'idée de la classe "Param" est que certains paramètres dans l'interface graphique peuvent avoir
    plusieurs boutons de réglage qui le contrôlent et reflètent également l'état du paramètre, par exemple
    un curseur, du texte et le fait de faire glisser peuvent tous modifier la valeur de la fréquence dans
    la forme d'onde de cet exemple.
    Cette classe permet une manière plus propre de mettre à jour / "renvoyer des informations" aux autres boutons de réglage lorsque
    l'un d'entre eux est modifié.  De plus, cette classe gère les contraintes min/max pour tous
    les boutons de réglage.
    Idée - liste de boutons de réglage - dans la méthode "set", l'objet bouton de réglage est également passé
      - les autres boutons de réglage dans la liste des boutons de réglage ont une méthode "set" qui est
        appelée pour les autres.
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
