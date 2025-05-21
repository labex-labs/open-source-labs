# Restringindo Nomes de Atributos

Atualmente, nossa classe `Structure` permite que qualquer atributo seja definido em suas instâncias. Para iniciantes, isso pode parecer conveniente a princípio, mas na verdade pode levar a muitos problemas. Quando você está trabalhando com uma classe, você espera que certos atributos estejam presentes e sejam usados de uma maneira específica. Se os usuários digitarem incorretamente os nomes dos atributos ou tentarem definir atributos que não faziam parte do design original, isso pode causar erros difíceis de encontrar.

## A Necessidade de Restrição de Atributos

Vamos analisar um cenário simples para entender por que precisamos restringir os nomes dos atributos. Considere o seguinte código:

```python
s = Stock('GOOG', 100, 490.1)
s.shares = 50      # Correct attribute name
s.share = 60       # Typo in attribute name - creates a new attribute instead of updating
```

Na segunda linha, há um erro de digitação. Em vez de `shares`, escrevemos `share`. Em Python, em vez de gerar um erro, ele simplesmente criará um novo atributo chamado `share`. Isso pode levar a bugs sutis porque você pode pensar que está atualizando o atributo `shares`, mas na verdade está criando um novo. Isso pode fazer com que seu código se comporte de forma inesperada e seja muito difícil de depurar.

## Implementando a Restrição de Atributos

Para resolver esse problema, podemos substituir o método `__setattr__`. Este método é chamado toda vez que você tenta definir um atributo em um objeto. Ao substituí-lo, podemos controlar quais atributos podem ser definidos e quais não podem.

Atualize sua classe `Structure` em `structure.py` com o seguinte código:

```python
def __setattr__(self, name, value):
    """
    Restrict attribute setting to only those defined in _fields
    or attributes starting with underscore (private attributes).
    """
    if name.startswith('_'):
        # Allow setting private attributes (starting with '_')
        super().__setattr__(name, value)
    elif name in self._fields:
        # Allow setting attributes defined in _fields
        super().__setattr__(name, value)
    else:
        # Raise an error for other attributes
        raise AttributeError(f'No attribute {name}')
```

Veja como este método funciona:

1.  Se o nome do atributo começar com um sublinhado (`_`), ele é considerado um atributo privado. Atributos privados são frequentemente usados para fins internos em uma classe. Permitimos que esses atributos sejam definidos porque eles fazem parte da implementação interna da classe.
2.  Se o nome do atributo estiver na lista `_fields`, isso significa que é um dos atributos definidos no design da classe. Permitimos que esses atributos sejam definidos porque eles fazem parte do comportamento esperado da classe.
3.  Se o nome do atributo não atender a nenhuma dessas condições, geramos um `AttributeError`. Isso informa ao usuário que ele está tentando definir um atributo que não existe na classe.

## Testando a Restrição de Atributos

Agora que implementamos a restrição de atributos, vamos testá-la para garantir que funcione conforme o esperado. Crie um arquivo chamado `test_attributes.py` com o seguinte código:

```python
# test_attributes.py
from structure import Stock

s = Stock('GOOG', 100, 490.1)

# This should work - valid attribute
print("Setting shares to 50")
s.shares = 50
print(f"Shares is now: {s.shares}")

# This should work - private attribute
print("\nSetting _internal_data")
s._internal_data = "Some data"
print(f"_internal_data is: {s._internal_data}")

# This should fail - invalid attribute
print("\nTrying to set an invalid attribute:")
try:
    s.share = 60  # Typo in attribute name
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

Para executar o teste, abra seu terminal e digite o seguinte comando:

```bash
python3 test_attributes.py
```

Você deve ver a seguinte saída:

```
Setting shares to 50
Shares is now: 50

Setting _internal_data
_internal_data is: Some data

Trying to set an invalid attribute:
Error correctly caught: No attribute share
```

Esta saída mostra que nossa classe agora impede erros acidentais de atributos. Ele nos permite definir atributos válidos e atributos privados, mas gera um erro quando tentamos definir um atributo inválido.

## O Valor da Restrição de Atributos

Restringir nomes de atributos é muito importante para escrever um código robusto e sustentável. Veja o porquê:

1.  Ajuda a detectar erros de digitação nos nomes dos atributos. Se você cometer um erro ao digitar um nome de atributo, o código gerará um erro em vez de criar um novo atributo. Isso facilita a localização e a correção de erros no início do processo de desenvolvimento.
2.  Impede tentativas de definir atributos que não existem no design da classe. Isso garante que a classe seja usada conforme o pretendido e que o código se comporte de forma previsível.
3.  Evita a criação acidental de novos atributos. A criação de novos atributos pode levar a um comportamento inesperado e tornar o código mais difícil de entender e manter.

Ao restringir os nomes dos atributos, tornamos nosso código mais confiável e mais fácil de trabalhar.
