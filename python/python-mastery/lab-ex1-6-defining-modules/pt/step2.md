# Compreendendo o Módulo Principal em Python

Em Python, quando você executa um script diretamente, ele age como o módulo "principal". Python tem uma variável especial chamada `__name__`. Quando um arquivo é executado diretamente, o Python define o valor de `__name__` como `"__main__"`. Isso é diferente de quando o arquivo é importado como um módulo.

Este recurso é muito útil porque permite que você escreva código que se comporta de maneira diferente, dependendo se o arquivo é executado diretamente ou importado. Por exemplo, você pode querer que algum código seja executado apenas quando você executa o arquivo como um script, mas não quando ele é importado por outro script.

## Modificando pcost.py para Usar o Padrão de Módulo Principal

Vamos modificar o programa `pcost.py` para tirar proveito desse padrão.

1. Primeiro, você precisa abrir o arquivo `pcost.py` no editor. Você pode usar os seguintes comandos para navegar até o diretório do projeto e criar o arquivo, caso ele não exista:

```bash
cd ~/project
touch pcost.py
```

O comando `cd` altera o diretório atual para o diretório `project` em seu diretório home. O comando `touch` cria um novo arquivo chamado `pcost.py` se ele ainda não existir.

2. Agora, modifique o arquivo `pcost.py` para que ele se pareça com isto:

```python
# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost += nshares * price
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")

    return total_cost

# This code only runs when the file is executed as a script
if __name__ == "__main__":
    total = portfolio_cost('portfolio.dat')
    print(total)
```

A principal mudança aqui é que envolvemos o código no final em uma condição `if __name__ == "__main__":`. Isso significa que o código dentro deste bloco só será executado quando o arquivo for executado diretamente como um script, não quando for importado como um módulo.

3. Depois de fazer essas alterações, salve o arquivo e saia do editor.

## Testando o Módulo Modificado

Agora, vamos testar nosso módulo modificado de duas maneiras diferentes para ver como ele se comporta.

1. Primeiro, execute o programa diretamente como um script usando o seguinte comando:

```bash
python3 pcost.py
```

Você deve ver a saída `44671.15`, assim como antes. Isso ocorre porque, quando você executa o script diretamente, a variável `__name__` é definida como `"__main__"`, então o código dentro do bloco `if __name__ == "__main__":` é executado.

2. Em seguida, inicie o interpretador Python novamente e importe o módulo:

```bash
python3
```

```python
import pcost
```

Desta vez, você não verá nenhuma saída. Quando você importa o módulo, a variável `__name__` é definida como `"pcost"` (o nome do módulo), não `"__main__"`. Portanto, o código dentro do bloco `if __name__ == "__main__":` não é executado.

3. Para verificar se a função `portfolio_cost` ainda funciona, você pode chamá-la assim:

```python
pcost.portfolio_cost('portfolio.dat')
```

A função deve retornar `44671.15`, o que significa que ela está funcionando corretamente.

4. Finalmente, saia do interpretador Python usando o seguinte comando:

```python
exit()
```

Este padrão é muito útil ao criar arquivos Python que podem ser usados ​​tanto como módulos importáveis ​​quanto como scripts independentes. O código dentro do bloco `if __name__ == "__main__":` só é executado quando o arquivo é executado diretamente, não quando é importado como um módulo.
