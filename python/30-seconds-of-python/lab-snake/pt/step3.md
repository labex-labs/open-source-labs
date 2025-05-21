# Lidando com Padrões Mais Complexos

Nossa função atual funciona para camelCase, mas precisamos aprimorá-la para lidar com padrões adicionais como:

1.  PascalCase (por exemplo, `HelloWorld`)
2.  Strings com hífens (por exemplo, `hello-world`)
3.  Strings que já possuem underscores (por exemplo, `hello_world`)

Vamos atualizar nossa função para lidar com esses casos:

```python
import re

def snake(s):
    # Replace hyphens with spaces
    s = s.replace('-', ' ')

    # Handle PascalCase pattern (sequences of uppercase letters)
    s = re.sub('([A-Z]+)', r' \1', s)

    # Handle camelCase pattern (lowercase followed by uppercase)
    s = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Split by spaces, join with underscores, and convert to lowercase
    return '_'.join(s.split()).lower()

# Test with multiple examples
if __name__ == "__main__":
    test_strings = [
        "helloWorld",
        "HelloWorld",
        "hello-world",
        "hello_world",
        "some text"
    ]

    for test in test_strings:
        result = snake(test)
        print(f"Original: {test}")
        print(f"Snake case: {result}")
        print("-" * 20)
```

Os aprimoramentos que fizemos:

1.  Primeiro, substituímos quaisquer hífens por espaços.
2.  A nova regex `re.sub('([A-Z]+)', r' \1', s)` adiciona um espaço antes de qualquer sequência de letras maiúsculas, o que ajuda com PascalCase.
3.  Mantemos nossa regex de tratamento camelCase.
4.  Finalmente, dividimos a string por espaços, juntamos com underscores e convertemos para minúsculas, o que lida com quaisquer espaços restantes e garante uma saída consistente.

Execute seu script para testar com vários formatos de entrada:

```bash
python3 ~/project/snake_case.py
```

Você deve ver uma saída como:

```
Original: helloWorld
Snake case: hello_world
--------------------
Original: HelloWorld
Snake case: hello_world
--------------------
Original: hello-world
Snake case: hello_world
--------------------
Original: hello_world
Snake case: hello_world
--------------------
Original: some text
Snake case: some_text
--------------------
```

Nossa função agora é mais robusta e pode lidar com vários formatos de entrada. No próximo passo, faremos nossos refinamentos finais e testaremos em relação ao conjunto completo de testes.
