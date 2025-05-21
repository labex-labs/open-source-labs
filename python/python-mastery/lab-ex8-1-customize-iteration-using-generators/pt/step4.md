# Criando um Gerador para Dados de Streaming

Em programação, geradores são uma ferramenta poderosa, especialmente ao lidar com problemas do mundo real, como monitorar uma fonte de dados de streaming. Nesta seção, aprenderemos como aplicar o que aprendemos sobre geradores a um cenário tão prático. Vamos criar um gerador que fica de olho em um arquivo de log e nos fornece novas linhas à medida que são adicionadas ao arquivo.

## Configurando a Fonte de Dados

Antes de começarmos a criar o gerador, precisamos configurar uma fonte de dados. Neste caso, usaremos um programa de simulação que gera dados do mercado de ações.

Primeiro, você precisa abrir um novo terminal no WebIDE. É aqui que você executará comandos para iniciar a simulação.

Depois de abrir o terminal, você executará o programa de simulação de ações. Aqui estão os comandos que você precisa inserir:

```bash
cd ~/project
python3 stocksim.py
```

O primeiro comando `cd ~/project` altera o diretório atual para o diretório `project` em seu diretório home. O segundo comando `python3 stocksim.py` executa o programa de simulação de ações. Este programa gerará dados do mercado de ações e os escreverá em um arquivo chamado `stocklog.csv` no diretório atual. Deixe este programa rodando em segundo plano enquanto trabalhamos no código de monitoramento.

## Criando um Monitor de Arquivo Simples

Agora que temos nossa fonte de dados configurada, vamos criar um programa que monitora o arquivo `stocklog.csv`. Este programa exibirá quaisquer alterações de preço que sejam negativas.

1. Primeiro, crie um novo arquivo chamado `follow.py` no WebIDE. Para fazer isso, você precisa alterar o diretório para o diretório `project` usando o seguinte comando no terminal:

```bash
cd ~/project
```

2. Em seguida, adicione o seguinte código ao arquivo `follow.py`. Este código abre o arquivo `stocklog.csv`, move o ponteiro do arquivo para o final do arquivo e, em seguida, verifica continuamente novas linhas. Se uma nova linha for encontrada e representar uma alteração de preço negativa, ela imprime o nome da ação, o preço e a alteração.

```python
# follow.py
import os
import time

f = open('stocklog.csv')
f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Sleep briefly and retry
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

3. Depois de adicionar o código, salve o arquivo. Em seguida, execute o programa usando o seguinte comando no terminal:

```bash
python3 follow.py
```

Você deve ver uma saída que mostra ações com alterações de preço negativas. Pode ser algo parecido com isto:

```
      AAPL     148.24      -1.76
      GOOG    2498.45      -1.55
```

Se você quiser parar o programa, pressione `Ctrl+C` no terminal.

## Convertendo para uma Função Geradora

Embora o código anterior funcione, podemos torná-lo mais reutilizável e modular convertendo-o em uma função geradora. Uma função geradora é um tipo especial de função que pode ser pausada e retomada, e ela produz valores um de cada vez.

1. Abra o arquivo `follow.py` novamente e modifique-o para usar uma função geradora. Aqui está o código atualizado:

```python
# follow.py
import os
import time

def follow(filename):
    """
    Generator function that yields new lines in a file as they are added.
    Similar to the 'tail -f' Unix command.
    """
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Move to the end of the file

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        yield line

# Example usage - monitor stocks with negative price changes
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))
```

A função `follow` agora é uma função geradora. Ela abre o arquivo, move para o final e, em seguida, verifica continuamente novas linhas. Quando uma nova linha é encontrada, ela produz essa linha.

2. Salve o arquivo e execute-o novamente usando o comando:

```bash
python3 follow.py
```

A saída deve ser a mesma de antes. Mas agora, a lógica de monitoramento de arquivos está bem encapsulada na função geradora `follow`. Isso significa que podemos reutilizar esta função em outros programas que precisam monitorar um arquivo.

## Compreendendo o Poder dos Geradores

Ao converter nosso código de leitura de arquivos em uma função geradora, tornamos ele muito mais flexível e reutilizável. A função `follow()` pode ser usada em qualquer programa que precise monitorar um arquivo, não apenas para dados de ações.

Por exemplo, você pode usá-la para monitorar logs de servidor, logs de aplicativos ou qualquer outro arquivo que seja atualizado ao longo do tempo. Isso mostra como os geradores são uma ótima maneira de lidar com fontes de dados de streaming de forma limpa e modular.
