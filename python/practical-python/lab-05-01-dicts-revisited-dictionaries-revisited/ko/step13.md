# 다중 상속에서의 MRO (MRO in Multiple Inheritance)

다중 상속의 경우, 최상위 클래스까지의 경로는 하나가 아닙니다. 예시를 살펴보겠습니다.

```python
class A: pass
class B: pass
class C(A, B): pass
class D(B): pass
class E(C, D): pass
```

속성에 접근할 때 어떤 일이 발생할까요?

```python
e = E()
e.attr
```

속성 검색 프로세스가 수행되지만, 순서는 어떻게 될까요? 이것이 문제입니다.

Python 은 클래스 순서에 대한 몇 가지 규칙을 따르는 _협력적 다중 상속 (cooperative multiple inheritance)_ 을 사용합니다.

- 자식 클래스는 항상 부모 클래스보다 먼저 확인됩니다.
- 부모 클래스 (여러 개인 경우) 는 항상 나열된 순서대로 확인됩니다.

MRO 는 이러한 규칙에 따라 계층 구조의 모든 클래스를 정렬하여 계산됩니다.

```python
>>> E.__mro__
(
  <class 'E'>,
  <class 'C'>,
  <class 'A'>,
  <class 'D'>,
  <class 'B'>,
  <class 'object'>)
>>>
```

기본 알고리즘은 "C3 선형화 알고리즘 (C3 Linearization Algorithm)"이라고 불립니다. 집에서 화재가 발생하여 대피해야 하는 경우와 마찬가지로, 자식 클래스부터 시작하여 부모 클래스 순으로 진행한다는 점만 기억하면 세부 사항은 중요하지 않습니다.
