# Knob 및 Param 클래스 정의

다음 단계는 Knob 및 Param 클래스를 정의하는 것입니다. 이 클래스는 GUI 에서 파형의 주파수와 진폭을 제어하는 데 사용됩니다.

```python
class Knob:
    """
    Knob - "setKnob" 메서드를 가진 간단한 클래스.
    Knob 인스턴스는 Param 인스턴스에 연결됩니다 (예: param.attach(knob)).
    기본 클래스는 문서화 목적으로 사용됩니다.
    """

    def setKnob(self, value):
        pass


class Param:
    """
    "Param" 클래스의 아이디어는 GUI 의 일부 매개변수가
    여러 개의 노브를 가지고 있어 이를 제어하고 매개변수의 상태를 반영할 수 있다는 것입니다.
    예를 들어, 슬라이더, 텍스트 및 드래깅은 모두 이 예제의 파형에서 주파수 값을 변경할 수 있습니다.
    이 클래스는 하나가 변경될 때 다른 노브에 대한 "피드백"을 업데이트하는 더 깔끔한 방법을 제공합니다.
    또한, 이 클래스는 모든 노브에 대한 최소/최대 제약 조건을 처리합니다.
    아이디어 - 노브 목록 - "set" 메서드에서 노브 객체도 전달됩니다.
      - 노브 목록의 다른 노브에는 다른 노브에 대해 호출되는 "set" 메서드가 있습니다.
    """

    def __init__(self, initialValue=None, minimum=0., maximum=1.):
        self.minimum = minimum
        self.maximum = maximum
        if initialValue != self.constrain(initialValue):
            raise ValueError('illegal initial value')
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
