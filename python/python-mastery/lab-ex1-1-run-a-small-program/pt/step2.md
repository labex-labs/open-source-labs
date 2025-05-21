# Crie um Programa Python Simples

Agora que confirmamos que o Python está funcionando corretamente, é hora de criar nosso primeiro arquivo de programa Python. Para iniciantes, é sempre uma boa ideia começar com algo simples antes de passar para programas mais complexos. Dessa forma, você pode entender gradualmente os conceitos básicos e a sintaxe do Python.

## Crie Seu Primeiro Arquivo Python

Primeiro, criaremos um novo arquivo Python. Veja como você pode fazer isso:

1. No WebIDE, você notará um painel no lado esquerdo da tela chamado painel Explorer. Este painel ajuda você a navegar por diferentes arquivos e diretórios em seu projeto. Localize este painel.

2. Depois de encontrar o painel Explorer, você precisa navegar até o diretório `/home/labex/project`. É aqui que armazenaremos nosso programa Python.

3. Clique com o botão direito em qualquer lugar no painel Explorer. Um menu aparecerá. Neste menu, selecione "New File" (Novo Arquivo). Esta ação criará um novo arquivo vazio.

4. Depois de criar o novo arquivo, você precisa dar um nome a ele. Nomeie o arquivo `hello.py`. Em Python, os arquivos geralmente têm a extensão `.py`, que indica que eles contêm código Python.

5. Agora, abra o arquivo `hello.py` recém-criado no editor. No editor, digite o seguinte código:

   ```python
   # This is a simple Python program

   name = input("Enter your name: ")
   print(f"Hello, {name}! Welcome to Python programming.")
   ```

   Vamos analisar este código. A linha que começa com `#` é um comentário. Os comentários são usados para explicar o que o código faz e são ignorados pelo interpretador Python. A função `input()` é usada para obter a entrada do usuário. Ele exibe a mensagem "Enter your name: " e espera que o usuário digite algo. O valor inserido pelo usuário é então armazenado na variável `name`. A função `print()` é usada para exibir a saída na tela. O `f"Hello, {name}!"` é uma f-string, que é uma maneira conveniente de formatar strings em Python. Ele permite que você insira o valor de uma variável diretamente em uma string.

6. Depois de digitar o código, você precisa salvar o arquivo. Você pode fazer isso pressionando Ctrl+S no seu teclado ou selecionando File > Save (Arquivo > Salvar) no menu. Salvar o arquivo garante que suas alterações sejam preservadas.

## Execute Seu Primeiro Programa Python

Agora que você criou e salvou seu programa Python, é hora de executá-lo. Veja como:

1. Abra um terminal no WebIDE, se ele ainda não estiver aberto. O terminal permite que você execute comandos e execute programas.

2. Antes de executar o programa Python, você precisa ter certeza de que está no diretório correto. Digite o seguinte comando no terminal:

   ```bash
   cd ~/project
   ```

   Este comando altera o diretório de trabalho atual para o diretório `project` em seu diretório home.

3. Depois de estar no diretório correto, você pode executar seu programa Python. Digite o seguinte comando no terminal:

   ```bash
   python3 hello.py
   ```

   Este comando diz ao interpretador Python para executar o arquivo `hello.py`.

4. Quando o programa for executado, ele solicitará que você insira seu nome. Digite seu nome e pressione Enter.

5. Depois de pressionar Enter, você deverá ver uma saída semelhante a:

   ```
   Enter your name: John
   Hello, John! Welcome to Python programming.
   ```

   A saída real mostrará o nome que você inseriu em vez de "John".

Este programa simples demonstra vários conceitos importantes em Python:

- Criando um arquivo Python: Você aprendeu como criar um novo arquivo Python no WebIDE.
- Adicionando comentários: Os comentários são usados para explicar o código e torná-lo mais compreensível.
- Obtendo a entrada do usuário com a função `input()`: Esta função permite que seu programa interaja com o usuário.
- Usando variáveis para armazenar dados: As variáveis são usadas para armazenar valores que podem ser usados posteriormente no programa.
- Exibindo a saída com a função `print()`: Esta função é usada para mostrar informações na tela.
- Usando f-strings para formatação de strings: As f-strings fornecem uma maneira conveniente de inserir variáveis em strings.
