# Crie um Programa Python Mais Avançado

Agora que você já entendeu os conceitos básicos do Python, é hora de dar o próximo passo e criar um programa Python mais avançado. Este programa irá gerar padrões de arte ASCII, que são designs simples, mas visualmente interessantes, feitos de caracteres de texto. Ao trabalhar neste programa, você aprenderá e aplicará vários conceitos importantes do Python, como importar módulos, definir funções e lidar com argumentos de linha de comando.

## Crie o Programa de Arte ASCII

1. Primeiro, precisamos abrir o arquivo `art.py` no WebIDE. Este arquivo foi criado durante o processo de configuração. Você pode encontrá-lo no diretório `/home/labex/project`. Abrir este arquivo é o ponto de partida para escrever nosso programa de arte ASCII.

2. Depois que o arquivo estiver aberto, você notará que ele pode ter algum conteúdo existente. Precisamos limpar isso porque vamos escrever nosso próprio código do zero. Portanto, exclua qualquer conteúdo existente no arquivo. Em seguida, copie o seguinte código no arquivo `art.py`. Este código é o núcleo do nosso gerador de arte ASCII.

   ```python
   # art.py - A program to generate ASCII art patterns

   import sys
   import random

   # Characters used for the art pattern
   chars = '\|/'

   def draw(rows, columns):
       """
       Generate and print an ASCII art pattern with the specified dimensions.

       Args:
           rows: Number of rows in the pattern
           columns: Number of columns in the pattern
       """
       for r in range(rows):
           # For each row, create a string of random characters
           line = ''.join(random.choice(chars) for _ in range(columns))
           print(line)

   # This code only runs when the script is executed directly
   if __name__ == '__main__':
       # Check if the correct number of arguments was provided
       if len(sys.argv) != 3:
           print("Error: Incorrect number of arguments")
           print("Usage: python3 art.py rows columns")
           print("Example: python3 art.py 10 20")
           sys.exit(1)

       try:
           # Convert the arguments to integers
           rows = int(sys.argv[1])
           columns = int(sys.argv[2])

           # Call the draw function with the specified dimensions
           draw(rows, columns)
       except ValueError:
           print("Error: Both arguments must be integers")
           sys.exit(1)
   ```

3. Depois de copiar o código para o arquivo, é importante salvar seu trabalho. Você pode fazer isso pressionando Ctrl + S no seu teclado. Alternativamente, você pode ir ao menu e selecionar File > Save (Arquivo > Salvar). Salvar o arquivo garante que seu código seja armazenado e esteja pronto para ser executado.

## Entendendo o Código

Vamos dar uma olhada mais de perto no que este programa faz. Entender o código é crucial para que você possa modificá-lo e expandi-lo no futuro.

- **Declarações de Importação**: As linhas `import sys` e `import random` são usadas para importar os módulos embutidos do Python. O módulo `sys` fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador Python e a funções que interagem fortemente com o interpretador. O módulo `random` nos permite gerar números aleatórios, que usaremos para criar padrões de arte ASCII aleatórios.
- **Conjunto de Caracteres**: A linha `chars = '\|/'` define o conjunto de caracteres que serão usados para criar nossa arte ASCII. Esses caracteres serão selecionados aleatoriamente para formar os padrões.
- **A Função `draw()`**: Esta função é responsável por criar os padrões de arte ASCII. Ele recebe dois argumentos, `rows` e `columns`, que especificam as dimensões do padrão. Dentro da função, ele usa um loop para criar cada linha do padrão, selecionando aleatoriamente caracteres do conjunto `chars`.
- **Bloco Principal**: O bloco `if __name__ == '__main__':` é uma construção especial em Python. Ele garante que o código dentro deste bloco seja executado somente quando o arquivo `art.py` for executado diretamente. Se o arquivo for importado para outro arquivo Python, este código não será executado.
- **Manipulação de Argumentos**: A variável `sys.argv` contém os argumentos de linha de comando passados para o programa. Verificamos se exatamente 3 argumentos são fornecidos (o nome do próprio script mais dois números representando o número de linhas e colunas). Isso nos ajuda a garantir que o usuário forneça a entrada correta.
- **Tratamento de Erros**: O bloco `try/except` é usado para capturar erros que podem ocorrer. Se o usuário fornecer entradas inválidas, como valores não inteiros para as linhas e colunas, o bloco `try` gerará um `ValueError`, e o bloco `except` imprimirá uma mensagem de erro e sairá do programa.

## Execute o Programa

1. Para executar nosso programa, primeiro precisamos abrir um terminal no WebIDE. O terminal é onde inseriremos comandos para executar nosso script Python.

2. Depois que o terminal estiver aberto, precisamos navegar até o diretório do projeto. É aqui que nosso arquivo `art.py` está localizado. Use o seguinte comando no terminal:

   ```bash
   cd ~/project
   ```

   Este comando altera o diretório de trabalho atual para o diretório do projeto.

3. Agora que estamos no diretório correto, podemos executar o programa. Use o seguinte comando:

   ```bash
   python3 art.py 5 10
   ```

   Este comando diz ao Python para executar o script `art.py` com 5 linhas e 10 colunas. Quando você executar este comando, verá um padrão de caracteres 5×10 impresso no terminal. A saída será algo parecido com isto:

   ```
   |\//\\|\//
   /\\|\|//\\
   \\\/\|/|/\
   //|\\\||\|
   \|//|/\|/\
   ```

   Lembre-se, o padrão real é aleatório, então sua saída será diferente do exemplo mostrado aqui.

4. Você pode experimentar diferentes dimensões alterando os argumentos no comando. Por exemplo, tente o seguinte comando:

   ```bash
   python3 art.py 8 15
   ```

   Isso gerará um padrão maior com 8 linhas e 15 colunas.

5. Para ver o tratamento de erros em ação, tente fornecer argumentos inválidos. Execute o seguinte comando:

   ```bash
   python3 art.py
   ```

   Você deve ver uma mensagem de erro como esta:

   ```
   Error: Incorrect number of arguments
   Usage: python3 art.py rows columns
   Example: python3 art.py 10 20
   ```

## Experimente com o Código

Você pode tornar os padrões de arte ASCII mais interessantes modificando o conjunto de caracteres. Veja como você pode fazer isso:

1. Abra o arquivo `art.py` novamente no editor. É aqui que faremos as alterações no código.

2. Encontre a variável `chars` no código. Altere-a para usar caracteres diferentes. Por exemplo, você pode usar o seguinte código:

   ```python
   chars = '*#@+.'
   ```

   Isso mudará o conjunto de caracteres usado para criar a arte ASCII.

3. Depois de fazer a alteração, salve o arquivo novamente usando Ctrl + S ou File > Save (Arquivo > Salvar). Em seguida, execute o programa com o seguinte comando:

   ```bash
   python3 art.py 5 10
   ```

   Agora você verá um padrão diferente usando seus novos caracteres.

Este exercício demonstra vários conceitos importantes do Python, incluindo:

- Importações de módulos: Como trazer funcionalidade adicional dos módulos embutidos do Python.
- Definição de função: Como definir e usar funções para organizar seu código.
- Manipulação de argumentos de linha de comando: Como aceitar e processar a entrada do usuário da linha de comando.
- Tratamento de erros com try/except: Como lidar com erros de forma elegante em seu programa.
- Manipulação de strings: Como criar e manipular strings para formar os padrões de arte ASCII.
- Geração de números aleatórios: Como gerar valores aleatórios para criar padrões exclusivos.
- List comprehensions (Compreensões de lista): Uma maneira concisa de criar listas em Python, que é usada na função `draw()`.
