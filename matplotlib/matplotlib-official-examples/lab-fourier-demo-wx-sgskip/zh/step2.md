# 定义旋钮和参数类

下一步是定义 `Knob` 和 `Param` 类。这些类将用于在图形用户界面（GUI）中控制波形的频率和幅度。

```python
class Knob:
    """
    旋钮 - 具有 "setKnob" 方法的简单类。
    一个旋钮实例连接到一个参数实例，例如，param.attach(knob)
    基类仅用于文档目的。
    """

    def setKnob(self, value):
        pass


class Param:
    """
    “参数”类的概念是，GUI 中的某个参数可能有
    几个旋钮，它们既可以控制该参数，又可以反映参数的状态，例如
    在本示例的波形中，滑块、文本输入和拖动都可以改变频率值。
    当一个旋钮的值发生变化时，该类提供了一种更简洁的方式来更新/“反馈”给其他旋钮。此外，该类处理所有旋钮的最小值/最大值约束。
    思路 - 旋钮列表 - 在 "set" 方法中，旋钮对象也会被传递
      - 旋钮列表中的其他旋钮有一个 "set" 方法，该方法会被调用以更新其他旋钮。
    """

    def __init__(self, initialValue=None, minimum=0., maximum=1.):
        self.minimum = minimum
        self.maximum = maximum
        if initialValue!= self.constrain(initialValue):
            raise ValueError('非法初始值')
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
