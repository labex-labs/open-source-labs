# Verificar Propriedade

Crie uma função chamada `check_prop` que recebe dois parâmetros: `fn` e `prop`. O parâmetro `fn` é uma função predicado que será aplicada à propriedade especificada de um dicionário. O parâmetro `prop` é uma string que representa o nome da propriedade à qual a função predicado será aplicada.

A função `check_prop` deve retornar uma função lambda que recebe um dicionário e aplica a função predicado, `fn`, à propriedade especificada.

```python
def check_prop(fn, prop):
  return lambda obj: fn(obj[prop])
```

```python
check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
```
