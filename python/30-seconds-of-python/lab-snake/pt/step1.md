# Compreendendo o Problema

Antes de escrever nossa função de conversão para snake case, vamos entender o que precisamos realizar:

1.  Precisamos converter uma string de qualquer formato para snake case.
2.  Snake case significa todas as letras minúsculas com underscores (sublinhados) entre as palavras.
3.  Precisamos lidar com diferentes formatos de entrada:
    - camelCase (por exemplo, `camelCase` → `camel_case`)
    - Strings com espaços (por exemplo, `some text` → `some_text`)
    - Strings com formatação mista (por exemplo, hífens, underscores e letras maiúsculas e minúsculas misturadas)

Vamos começar criando um novo arquivo Python para nossa função snake case. No WebIDE, navegue até o diretório do projeto e crie um novo arquivo chamado `snake_case.py`:

```python
# Esta função converterá uma string para snake case
def snake(s):
    # Implementaremos esta função passo a passo
    pass  # Placeholder (espaço reservado) por enquanto

# Teste com um exemplo simples
if __name__ == "__main__":
    test_string = "helloWorld"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

Salve este arquivo. No próximo passo, começaremos a implementar a função.

Por enquanto, vamos executar nossa função placeholder para garantir que nosso arquivo esteja configurado corretamente. Abra um terminal e execute:

```bash
python3 ~/project/snake_case.py
```

![python-prompt](../assets/screenshot-20250306-B5lI9tyo@2x.png)

Você deve ver uma saída como:

```
Original: helloWorld
Snake case: None
```

O resultado é `None` porque nossa função está atualmente apenas retornando o valor padrão `None` do Python. No próximo passo, adicionaremos a lógica de conversão real.
