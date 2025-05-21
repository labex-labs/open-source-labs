# Entendendo Corrotinas com um Seguidor de Arquivo

Vamos começar entendendo o que são corrotinas e como elas funcionam em Python. Uma corrotina é uma versão especializada de uma função geradora (generator function). Em Python, as funções geralmente começam do início toda vez que são chamadas. Mas as corrotinas são diferentes. Elas podem consumir e produzir dados, e têm a capacidade de suspender e retomar sua execução. Isso significa que uma corrotina pode pausar sua operação em um determinado ponto e, em seguida, retomar exatamente de onde parou mais tarde.

## Criando um Seguidor de Arquivo de Corrotina Básico

Nesta etapa, criaremos um seguidor de arquivo que usa corrotinas para monitorar um arquivo em busca de novo conteúdo e processá-lo. Isso é semelhante ao comando Unix `tail -f`, que mostra continuamente o final de um arquivo e atualiza à medida que novas linhas são adicionadas.

1. Abra o editor de código e crie um novo arquivo chamado `cofollow.py` no diretório `/home/labex/project`. É aqui que escreveremos nosso código Python para implementar o seguidor de arquivo usando corrotinas.

2. Copie o seguinte código para o arquivo:

```python
# cofollow.py
import os
import time

# Data source
def follow(filename, target):
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)  # Move to the end of the file
        while True:
            line = f.readline()
            if line != '':
                target.send(line)  # Send the line to the target coroutine
            else:
                time.sleep(0.1)  # Sleep briefly if no new content

# Decorator for coroutine functions
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args, **kwargs):
        f = func(*args, **kwargs)
        f.send(None)  # Prime the coroutine (necessary first step)
        return f
    return start

# Sample coroutine
@consumer
def printer():
    while True:
        item = yield     # Receive an item sent to me
        print(item)

# Example use
if __name__ == '__main__':
    follow('stocklog.csv', printer())
```

3. Vamos entender os componentes-chave deste código:

   - `follow(filename, target)`: Esta função é responsável por abrir um arquivo. Primeiro, ela move o ponteiro do arquivo para o final do arquivo usando `f.seek(0, os.SEEK_END)`. Em seguida, ela entra em um loop infinito onde tenta continuamente ler novas linhas do arquivo. Se uma nova linha for encontrada, ela envia essa linha para a corrotina de destino usando o método `send`. Se não houver novo conteúdo, ela pausa por um curto período de tempo (0,1 segundos) usando `time.sleep(0.1)` antes de verificar novamente.
   - `@consumer` decorator: Em Python, as corrotinas precisam ser "preparadas" (primed) antes que possam começar a receber dados. Este decorador cuida disso. Ele envia automaticamente um valor inicial `None` para a corrotina, que é um primeiro passo necessário para preparar a corrotina para receber dados reais.
   - `printer()` corrotina: Esta é uma corrotina simples. Ela tem um loop infinito onde usa a palavra-chave `yield` para receber um item enviado a ela. Depois de receber um item, ela simplesmente o imprime.

4. Salve o arquivo e execute-o a partir do terminal:

```bash
cd /home/labex/project
python3 cofollow.py
```

5. Você deve ver o script imprimindo o conteúdo do arquivo de log de ações, e ele continuará a imprimir novas linhas à medida que forem adicionadas ao arquivo. Pressione `Ctrl+C` para parar o programa.

O conceito-chave aqui é que os dados fluem da função `follow` para a corrotina `printer` através do método `send`. Este "empurrar" (pushing) de dados é o oposto dos geradores, que "puxam" (pull) dados através da iteração. Em um gerador, você normalmente usa um loop `for` para iterar sobre os valores que ele produz. Mas neste exemplo de corrotina, os dados são enviados ativamente de uma parte do código para outra.
