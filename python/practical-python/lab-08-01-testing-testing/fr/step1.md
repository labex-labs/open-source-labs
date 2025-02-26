# Assertions

L'instruction `assert` est une vérification interne pour le programme. Si une expression n'est pas vraie, elle lève une exception `AssertionError`.

Syntaxe de l'instruction `assert`.

```python
assert <expression> [, 'Message de diagnostic']
```

Par exemple.

```python
assert isinstance(10, int), 'Attendu un int'
```

Elle ne devrait pas être utilisée pour vérifier les entrées de l'utilisateur (c'est-à-dire les données saisies dans un formulaire web ou autre chose). Son but est plutôt de vérifications internes et d'invariants (conditions qui devraient toujours être vraies).
