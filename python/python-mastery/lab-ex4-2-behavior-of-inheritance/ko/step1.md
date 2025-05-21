# 단일 상속과 다중 상속 이해하기

이 단계에서는 Python 의 두 가지 주요 상속 유형인 단일 상속과 다중 상속에 대해 배우겠습니다. 상속은 객체 지향 프로그래밍의 기본 개념으로, 클래스가 다른 클래스에서 속성과 메서드를 상속받을 수 있도록 합니다. 또한 여러 후보가 있을 때 Python 이 어떤 메서드를 호출할지 결정하는 방법, 즉 메서드 결정 (method resolution) 이라고 하는 프로세스도 살펴보겠습니다.

## 단일 상속

단일 상속은 클래스가 단일 조상 계열을 형성하는 경우입니다. 각 클래스가 하나의 직접적인 부모만 있는 가계도와 같습니다. 작동 방식을 이해하기 위해 예시를 만들어 보겠습니다.

먼저 WebIDE 에서 새 터미널을 엽니다. 터미널이 열리면 다음 명령을 입력하고 Enter 키를 눌러 Python 인터프리터를 시작합니다.

```bash
python3
```

이제 Python 인터프리터에 들어갔으므로 단일 상속 체인을 형성하는 세 개의 클래스를 만들겠습니다. 다음 코드를 입력합니다.

```python
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

class C(B):
    def spam(self):
        print('C.spam')
        super().spam()
```

이 코드에서 클래스 `B`는 클래스 `A`를 상속하고, 클래스 `C`는 클래스 `B`를 상속합니다. `super()` 함수는 부모 클래스의 메서드를 호출하는 데 사용됩니다.

이러한 클래스를 정의한 후 Python 이 메서드를 검색하는 순서를 알 수 있습니다. 이 순서를 메서드 결정 순서 (Method Resolution Order, MRO) 라고 합니다. 클래스 `C`의 MRO 를 보려면 다음 코드를 입력합니다.

```python
C.__mro__
```

다음과 유사한 출력을 볼 수 있습니다.

```
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

이 출력은 Python 이 먼저 클래스 `C`에서 메서드를 찾고, 다음으로 클래스 `B`에서, 그 다음으로 클래스 `A`에서, 마지막으로 기본 `object` 클래스에서 메서드를 찾는다는 것을 보여줍니다.

이제 클래스 `C`의 인스턴스를 생성하고 `spam()` 메서드를 호출해 보겠습니다. 다음 코드를 입력합니다.

```python
c = C()
c.spam()
```

다음 출력을 볼 수 있습니다.

```
C.spam
B.spam
A.spam
```

이 출력은 단일 상속 체인에서 `super()`가 어떻게 작동하는지 보여줍니다. `C.spam()`이 `super().spam()`을 호출하면 `B.spam()`을 호출합니다. 그런 다음 `B.spam()`이 `super().spam()`을 호출하면 `A.spam()`을 호출합니다.

## 다중 상속

다중 상속을 사용하면 클래스가 둘 이상의 부모 클래스에서 상속받을 수 있습니다. 이를 통해 클래스는 모든 부모 클래스의 속성과 메서드에 액세스할 수 있습니다. 이 경우 메서드 결정이 어떻게 작동하는지 살펴보겠습니다.

Python 인터프리터에 다음 코드를 입력합니다.

```python
class Base:
    def spam(self):
        print('Base.spam')

class X(Base):
    def spam(self):
        print('X.spam')
        super().spam()

class Y(Base):
    def spam(self):
        print('Y.spam')
        super().spam()

class Z(Base):
    def spam(self):
        print('Z.spam')
        super().spam()
```

이제 여러 부모 클래스 `X`, `Y`, `Z`에서 상속하는 클래스 `M`을 만들겠습니다. 다음 코드를 입력합니다.

```python
class M(X, Y, Z):
    pass

M.__mro__
```

다음 출력을 볼 수 있습니다.

```
(<class '__main__.M'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.Base'>, <class 'object'>)
```

이 출력은 클래스 `M`의 메서드 결정 순서를 보여줍니다. Python 은 이 순서대로 메서드를 검색합니다.

클래스 `M`의 인스턴스를 생성하고 `spam()` 메서드를 호출해 보겠습니다.

```python
m = M()
m.spam()
```

다음 출력을 볼 수 있습니다.

```
X.spam
Y.spam
Z.spam
Base.spam
```

`super()`가 바로 상위 부모 클래스의 메서드만 호출하는 것이 아님을 알 수 있습니다. 대신, 자식 클래스에 의해 정의된 메서드 결정 순서 (MRO) 를 따릅니다.

다른 순서로 부모 클래스를 가진 다른 클래스 `N`을 만들어 보겠습니다.

```python
class N(Z, Y, X):
    pass

N.__mro__
```

다음 출력을 볼 수 있습니다.

```
(<class '__main__.N'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.Base'>, <class 'object'>)
```

이제 클래스 `N`의 인스턴스를 생성하고 `spam()` 메서드를 호출합니다.

```python
n = N()
n.spam()
```

다음 출력을 볼 수 있습니다.

```
Z.spam
Y.spam
X.spam
Base.spam
```

이것은 중요한 개념을 보여줍니다. Python 의 다중 상속에서 클래스 정의의 부모 클래스 순서가 메서드 결정 순서를 결정합니다. `super()` 함수는 호출되는 클래스에 관계없이 이 순서를 따릅니다.

이러한 개념을 모두 탐색했으면 다음 코드를 입력하여 Python 인터프리터를 종료할 수 있습니다.

```python
exit()
```
