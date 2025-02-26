# 単一継承による属性の読み取り

継承階層では、属性は順番に継承木を辿って見つけられます。

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(D): pass
```

単一継承の場合、最上位までのパスは1つだけです。最初の一致が見つかったときに探索を停止します。
