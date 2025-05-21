# Python 제너레이터 이해하기

제너레이터는 Python 의 강력한 기능입니다. 제너레이터는 반복자 (iterator) 를 생성하는 간단하고 우아한 방법을 제공합니다. Python 에서 데이터 시퀀스를 다룰 때 반복자는 일련의 값을 하나씩 반복할 수 있으므로 매우 유용합니다. 일반 함수는 일반적으로 단일 값을 반환한 다음 실행을 중지합니다. 그러나 제너레이터는 다릅니다. 제너레이터는 시간이 지남에 따라 일련의 값을 yield 할 수 있으며, 이는 단계별 방식으로 여러 값을 생성할 수 있음을 의미합니다.

## 제너레이터란 무엇인가?

제너레이터 함수는 일반 함수와 유사한 외관을 가지고 있습니다. 그러나 핵심적인 차이점은 값을 반환하는 방식에 있습니다. 단일 결과를 제공하기 위해 `return` 문을 사용하는 대신, 제너레이터 함수는 `yield` 문을 사용합니다. `yield` 문은 특별합니다. 실행될 때마다 함수의 상태가 일시 중지되고, `yield` 키워드 뒤에 오는 값이 호출자에게 반환됩니다. 제너레이터 함수가 다시 호출되면 중단된 지점부터 실행이 재개됩니다.

간단한 제너레이터 함수를 생성하는 것으로 시작해 보겠습니다. Python 의 내장 함수인 `range()`는 소수점 단계를 지원하지 않습니다. 따라서 소수점 단계를 가진 숫자 범위를 생성할 수 있는 제너레이터 함수를 생성합니다.

1. 먼저 WebIDE 에서 새 Python 터미널을 열어야 합니다. 이렇게 하려면 "Terminal" 메뉴를 클릭한 다음 "New Terminal"을 선택합니다.
2. 터미널이 열리면 터미널에 다음 코드를 입력합니다. 이 코드는 제너레이터 함수를 정의한 다음 테스트합니다.

```python
def frange(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step

# Test the generator with a for loop
for x in frange(0, 2, 0.25):
    print(x, end=' ')
```

이 코드에서 `frange` 함수는 제너레이터 함수입니다. `start` 값으로 변수 `current`를 초기화합니다. 그런 다음 `current`가 `stop` 값보다 작은 동안 `current` 값을 yield 하고 `current`를 `step` 값만큼 증가시킵니다. `for` 루프는 `frange` 제너레이터 함수에서 생성된 값을 반복하고 이를 출력합니다.

다음과 같은 출력을 볼 수 있습니다.

```
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

## 제너레이터의 일회성 특성

제너레이터의 중요한 특징은 소모성 (exhaustible) 이라는 것입니다. 즉, 제너레이터가 생성한 모든 값을 반복한 후에는 동일한 값 시퀀스를 다시 생성하는 데 사용할 수 없습니다. 다음 코드를 사용하여 이를 시연해 보겠습니다.

```python
# Create a generator object
f = frange(0, 2, 0.25)

# First iteration works fine
print("First iteration:")
for x in f:
    print(x, end=' ')
print("\n")

# Second iteration produces nothing
print("Second iteration:")
for x in f:
    print(x, end=' ')
print("\n")
```

이 코드에서 먼저 `frange` 함수를 사용하여 제너레이터 객체 `f`를 생성합니다. 첫 번째 `for` 루프는 제너레이터가 생성한 모든 값을 반복하고 이를 출력합니다. 첫 번째 반복 후 제너레이터는 소모되었으며, 이는 이미 생성할 수 있는 모든 값을 생성했음을 의미합니다. 따라서 두 번째 `for` 루프에서 다시 반복하려고 하면 새로운 값을 생성하지 않습니다.

출력:

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:

```

두 번째 반복은 제너레이터가 이미 소모되었기 때문에 출력을 생성하지 않았습니다.

## 클래스를 사용하여 재사용 가능한 제너레이터 생성

동일한 값 시퀀스를 여러 번 반복해야 하는 경우 제너레이터를 클래스로 래핑할 수 있습니다. 이렇게 하면 새 반복을 시작할 때마다 새로운 제너레이터가 생성됩니다.

```python
class FRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        n = self.start
        while n < self.stop:
            yield n
            n += self.step

# Create an instance
f = FRange(0, 2, 0.25)

# We can iterate multiple times
print("First iteration:")
for x in f:
    print(x, end=' ')
print("\n")

print("Second iteration:")
for x in f:
    print(x, end=' ')
print("\n")
```

이 코드에서 `FRange` 클래스를 정의합니다. `__init__` 메서드는 `start`, `stop`, `step` 값을 초기화합니다. `__iter__` 메서드는 Python 클래스의 특수 메서드입니다. 반복자를 생성하는 데 사용됩니다. `__iter__` 메서드 내부에는 앞에서 정의한 `frange` 함수와 유사한 방식으로 값을 생성하는 제너레이터가 있습니다.

`FRange` 클래스의 인스턴스 `f`를 생성하고 여러 번 반복하면 각 반복은 `__iter__` 메서드를 호출하여 새로운 제너레이터를 생성합니다. 따라서 동일한 값 시퀀스를 여러 번 얻을 수 있습니다.

출력:

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

이번에는 `__iter__()` 메서드가 호출될 때마다 새로운 제너레이터를 생성하므로 여러 번 반복할 수 있습니다.
