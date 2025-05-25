# Lendo Atributos com Herança Simples

Em hierarquias de herança, os atributos são encontrados percorrendo a árvore de herança em ordem.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(D): pass
```

Com herança simples, há um único caminho para o topo. Você para com a primeira correspondência.
