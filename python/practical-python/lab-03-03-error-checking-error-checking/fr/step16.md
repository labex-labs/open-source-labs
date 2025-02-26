# Exercice 3.10 : Rétablir le silence des erreurs

Modifiez la fonction `parse_csv()` de sorte que les messages d'erreur de l'analyse puissent être silencés si l'utilisateur le souhaite explicitement. Par exemple :

```python
>>> portfolio = parse_csv('missing.csv', types=[str,int,float], silence_errors=True)
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}]
>>>
```

La gestion des erreurs est l'une des choses les plus difficiles à bien faire dans la plupart des programmes. En règle générale, vous ne devriez pas ignorer silencieusement les erreurs. Au contraire, il est préférable de signaler les problèmes et de donner à l'utilisateur l'option de silencer le message d'erreur s'il le souhaite.
