# Определение классов Knob и Param

Следующим шагом является определение классов Knob и Param. Эти классы будут использоваться для управления частотой и амплитудой волновых форм в графическом интерфейсе пользователя (GUI).

```python
class Knob:
    """
    Knob - простой класс с методом "setKnob".
    Экземпляр Knob прикрепляется к экземпляру Param, например, param.attach(knob)
    Базовый класс используется для целей документирования.
    """

    def setKnob(self, value):
        pass


class Param:
    """
    В идее класса "Param" некоторые параметры в GUI могут иметь
    несколько вращателей, которые и контролируют их, и отражают состояние параметра, например,
    ползунок, текст и перетаскивание могут все изменить значение частоты в
   波形 этом примера.
    Класс позволяет более чистый способ обновления/"отзвука" для других вращателей, когда
    один из них изменяется. Также этот класс обрабатывает ограничения min/max для всех
    вращателей.
    Идея - список вращателей - в методе "set" объект вращателя передается также
      - другие вращатели в списке вращателей имеют метод "set", который вызывается для других.
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
