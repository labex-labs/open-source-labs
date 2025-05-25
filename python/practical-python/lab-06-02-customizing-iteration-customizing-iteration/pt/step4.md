# Exercício 6.5: Monitorando uma fonte de dados de streaming

Geradores (generators) podem ser uma maneira interessante de monitorar fontes de dados em tempo real, como arquivos de log ou feeds do mercado de ações. Nesta parte, exploraremos essa ideia. Para começar, siga as próximas instruções cuidadosamente.

O programa `stocksim.py` é um programa que simula dados do mercado de ações. Como saída, o programa escreve constantemente dados em tempo real em um arquivo `stocklog.csv`. Em uma janela de comando separada, entre no diretório `` e execute este programa:

```bash
$ python3 stocksim.py
```

Se você estiver no Windows, basta localizar o programa `stocksim.py` e clicar duas vezes nele para executá-lo. Agora, esqueça este programa (apenas deixe-o rodando). Usando outra janela, observe o arquivo `stocklog.csv` sendo escrito pelo simulador. Você deve ver novas linhas de texto sendo adicionadas ao arquivo a cada poucos segundos. Novamente, apenas deixe este programa rodando em segundo plano---ele rodará por várias horas (você não deve precisar se preocupar com isso).

Depois que o programa acima estiver rodando, vamos escrever um pequeno programa para abrir o arquivo, procurar o final e observar a nova saída. Crie um arquivo `follow.py` e coloque este código nele:

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
        print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

Se você executar o programa, verá um ticker de ações em tempo real. Por baixo dos panos, este código é parecido com o comando Unix `tail -f` que é usado para observar um arquivo de log.

Observação: O uso do método `readline()` neste exemplo é um tanto incomum, pois não é a maneira usual de ler linhas de um arquivo (normalmente você usaria um loop `for`). No entanto, neste caso, estamos usando-o para sondar repetidamente o final do arquivo para ver se mais dados foram adicionados (`readline()` retornará novos dados ou uma string vazia).
