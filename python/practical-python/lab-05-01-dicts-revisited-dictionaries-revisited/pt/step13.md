# MRO em Herança Múltipla

Com herança múltipla, não há um único caminho para o topo. Vamos dar uma olhada em um exemplo.

```python
class A: pass
class B: pass
class C(A, B): pass
class D(B): pass
class E(C, D): pass
```

O que acontece quando você acessa um atributo?

```python
e = E()
e.attr
```

Um processo de busca de atributo é realizado, mas qual é a ordem? Esse é um problema.

O Python usa _herança múltipla cooperativa_ (cooperative multiple inheritance), que obedece a algumas regras sobre a ordenação de classes.

- Filhos são sempre verificados antes dos pais
- Pais (se múltiplos) são sempre verificados na ordem listada.

O MRO é computado ordenando todas as classes em uma hierarquia de acordo com essas regras.

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

O algoritmo subjacente é chamado de "Algoritmo de Linearização C3" (C3 Linearization Algorithm). Os detalhes precisos não são importantes, desde que você se lembre que uma hierarquia de classes obedece às mesmas regras de ordenação que você pode seguir se sua casa estivesse pegando fogo e você tivesse que evacuar - primeiro os filhos, seguidos pelos pais.
