# Erreurs et exceptions

Les fonctions signalent les erreurs sous forme d'exceptions. Une exception provoque l'arrêt d'une fonction et peut entraîner l'arrêt de votre programme entier si elle n'est pas gérée.

Essayez ceci dans votre interpréteur Python interactif (REPL).

```python
>>> int('N/A')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'N/A'
>>>
```

À des fins de débogage, le message décrit ce qui s'est passé, où l'erreur s'est produite et une trace rétrospective montrant les autres appels de fonction qui ont entraîné l'échec.
