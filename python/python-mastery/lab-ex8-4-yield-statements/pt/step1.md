# Compreendendo o Ciclo de Vida (Lifetime) e o Fechamento de Geradores

Nesta etapa, vamos explorar o ciclo de vida (lifetime) dos geradores Python e aprender como fechá-los corretamente. Geradores em Python são um tipo especial de iterador que permite gerar uma sequência de valores em tempo real (on-the-fly), em vez de calculá-los todos de uma vez e armazená-los na memória. Isso pode ser muito útil ao lidar com grandes conjuntos de dados ou sequências infinitas.

## O que é o Gerador `follow()`?

Vamos começar analisando o arquivo `follow.py` no diretório do projeto. Este arquivo contém uma função geradora chamada `follow()`. Uma função geradora é definida como uma função normal, mas em vez de usar a palavra-chave `return`, ela usa `yield`. Quando uma função geradora é chamada, ela retorna um objeto gerador, que você pode iterar para obter os valores que ele produz.

A função geradora `follow()` lê continuamente linhas de um arquivo e produz cada linha à medida que é lida. Isso é semelhante ao comando Unix `tail -f`, que monitora continuamente um arquivo em busca de novas linhas.

Abra o arquivo `follow.py` no editor WebIDE:

```python
import os
import time

def follow(filename):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)    # Sleep briefly to avoid busy wait
                continue
            yield line
```

Neste código, a instrução `with open(filename, 'r') as f` abre o arquivo no modo de leitura e garante que ele seja fechado corretamente quando o bloco for finalizado. A linha `f.seek(0, os.SEEK_END)` move o ponteiro do arquivo para o final do arquivo, para que o gerador comece a ler a partir do final. O loop `while True` lê continuamente linhas do arquivo. Se a linha estiver vazia, significa que ainda não há novas linhas, então o programa dorme por 0,1 segundos para evitar uma espera ocupada (busy wait) e, em seguida, continua para a próxima iteração. Se a linha não estiver vazia, ela é produzida.

Este gerador é executado em um loop infinito, o que levanta uma questão importante: o que acontece quando paramos de usar o gerador ou queremos terminá-lo antecipadamente?

## Modificando o Gerador para Lidar com o Fechamento

Precisamos modificar a função `follow()` em `follow.py` para lidar com o caso em que o gerador é fechado corretamente. Para fazer isso, adicionaremos um bloco `try-except` que captura a exceção `GeneratorExit`. A exceção `GeneratorExit` é lançada quando um gerador é fechado, seja pela coleta de lixo (garbage collection) ou pela chamada do método `close()`.

```python
import os
import time

def follow(filename):
    try:
        with open(filename,'r') as f:
            f.seek(0,os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    time.sleep(0.1)    # Sleep briefly to avoid busy wait
                    continue
                yield line
    except GeneratorExit:
        print('Following Done')
```

Neste código modificado, o bloco `try` contém a lógica principal do gerador. Se uma exceção `GeneratorExit` for lançada, o bloco `except` a captura e imprime a mensagem 'Following Done'. Esta é uma maneira simples de realizar ações de limpeza quando o gerador é fechado.

Salve o arquivo após fazer essas alterações.

## Experimentando com o Fechamento de Geradores

Agora, vamos conduzir alguns experimentos para ver como os geradores se comportam quando são coletados pelo coletor de lixo (garbage collected) ou fechados explicitamente.

Abra um terminal e execute o interpretador Python:

```bash
cd ~/project
python3
```

### Experimento 1: Coleta de Lixo (Garbage Collection) de um Gerador em Execução

```python
>>> from follow import follow
>>> # Experiment: Garbage collection of a running generator
>>> f = follow('stocklog.csv')
>>> next(f)
'"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314\n'
>>> del f  # Delete the generator object
Following Done  # This message appears because of our GeneratorExit handler
```

Neste experimento, primeiro importamos a função `follow` do arquivo `follow.py`. Em seguida, criamos um objeto gerador `f` chamando `follow('stocklog.csv')`. Usamos a função `next()` para obter a próxima linha do gerador. Finalmente, excluímos o objeto gerador usando a instrução `del`. Quando o objeto gerador é excluído, ele é fechado automaticamente, o que aciona nosso manipulador de exceção `GeneratorExit`, e a mensagem 'Following Done' é impressa.

### Experimento 2: Fechando Explicitamente um Gerador

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         f.close()  # Explicitly close the generator
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
Following Done
>>> for line in f:
...     print(line, end='')  # No output: generator is closed
...
```

Neste experimento, criamos um novo objeto gerador `f` e iteramos sobre ele usando um loop `for`. Dentro do loop, imprimimos cada linha e verificamos se a linha contém a string 'IBM'. Se contiver, chamamos o método `close()` no gerador para fechá-lo explicitamente. Quando o gerador é fechado, a exceção `GeneratorExit` é lançada, e nosso manipulador de exceção imprime a mensagem 'Following Done'. Depois que o gerador é fechado, se tentarmos iterar sobre ele novamente, não haverá saída porque o gerador não está mais ativo.

### Experimento 3: Saindo e Retomando um Gerador

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         break  # Break out of the loop, but don't close the generator
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
>>> # Resume iteration - the generator is still active
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         break
...
"CAT",78.36,"6/11/2007","09:37.19",-0.16,78.32,78.36,77.99,237714
"VZ",42.99,"6/11/2007","09:37.20",-0.08,42.95,42.99,42.78,268459
"IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859
>>> del f  # Clean up
Following Done
```

Neste experimento, criamos um objeto gerador `f` e iteramos sobre ele usando um loop `for`. Dentro do loop, imprimimos cada linha e verificamos se a linha contém a string 'IBM'. Se contiver, usamos a instrução `break` para sair do loop. Sair do loop não fecha o gerador, então o gerador ainda está ativo. Podemos então retomar a iteração iniciando um novo loop `for` sobre o mesmo objeto gerador. Finalmente, excluímos o objeto gerador para limpar, o que aciona o manipulador de exceção `GeneratorExit`.

## Principais Conclusões

1. Quando um gerador é fechado (seja por coleta de lixo ou chamando `close()`), uma exceção `GeneratorExit` é lançada dentro do gerador.
2. Você pode capturar essa exceção para realizar ações de limpeza quando o gerador é fechado.
3. Sair da iteração de um gerador (com `break`) não fecha o gerador, permitindo que ele seja retomado mais tarde.

Saia do interpretador Python digitando `exit()` ou pressionando `Ctrl+D`.
