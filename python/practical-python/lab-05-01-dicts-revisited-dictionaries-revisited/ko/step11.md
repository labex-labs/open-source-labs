# 단일 상속을 사용한 속성 읽기 (Reading Attributes with Single Inheritance)

상속 계층 구조에서, 속성은 상속 트리를 위로 올라가면서 순서대로 찾아집니다.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(D): pass
```

단일 상속의 경우, 최상위 클래스까지의 경로는 하나입니다. 첫 번째 일치하는 항목에서 멈춥니다.
