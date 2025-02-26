# Une approche un peu meilleure

Si vous allez capturer toutes les erreurs, c'est une approche plus raisonnable.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
```

Il indique une raison spécifique pour l'échec. Il est presque toujours une bonne idée d'avoir un mécanisme pour visualiser / signaler les erreurs lorsque vous écrivez du code qui capture toutes les exceptions possibles.

En général cependant, il est préférable de capturer l'erreur de la manière la plus limitée possible. Capturer seulement les erreurs que vous pouvez réellement gérer. Laissez les autres erreurs passer - peut-être que du code autre peut les gérer.
