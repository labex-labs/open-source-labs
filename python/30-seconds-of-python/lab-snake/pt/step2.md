# Usando Expressões Regulares para Correspondência de Padrões

Para converter strings para snake case, usaremos expressões regulares (regex) para identificar limites de palavras. O módulo `re` no Python fornece recursos poderosos de correspondência de padrões que podemos usar para esta tarefa.

Vamos atualizar nossa função para lidar com strings camelCase:

1.  Primeiro, precisamos identificar o padrão onde uma letra minúscula é seguida por uma letra maiúscula (como em "camelCase")
2.  Em seguida, inseriremos um espaço entre elas
3.  Finalmente, converteremos tudo para minúsculas e substituiremos os espaços por underscores

Atualize seu arquivo `snake_case.py` com esta função aprimorada:

```python
import re

def snake(s):
    # Replace pattern of a lowercase letter followed by uppercase with lowercase, space, uppercase
    s1 = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Replace spaces with underscores and convert to lowercase
    return s1.lower().replace(' ', '_')

# Test with a simple example
if __name__ == "__main__":
    test_string = "helloWorld"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

Vamos detalhar o que esta função faz:

- `re.sub('([a-z])([A-Z])', r'\1 \2', s)` procura padrões onde uma letra minúscula `([a-z])` é seguida por uma letra maiúscula `([A-Z])`. Em seguida, substitui este padrão pelas mesmas letras, mas adiciona um espaço entre elas usando `\1` e `\2`, que se referem aos grupos capturados.
- Então, convertemos tudo para minúsculas com `lower()` e substituímos os espaços por underscores.

Execute seu script novamente para ver se ele funciona para camelCase:

```bash
python3 ~/project/snake_case.py
```

A saída agora deve ser:

```
Original: helloWorld
Snake case: hello_world
```

Ótimo! Nossa função agora pode lidar com strings camelCase. No próximo passo, vamos aprimorá-la para lidar com casos mais complexos.
