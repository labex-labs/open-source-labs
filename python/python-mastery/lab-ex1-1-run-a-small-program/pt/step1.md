# Verifique a Instalação do Python e Use o Interpretador Interativo

O interpretador interativo do Python é uma ferramenta muito útil. Ele permite que você execute o código Python linha por linha e veja os resultados imediatamente. Isso é ótimo para iniciantes, porque você pode testar pequenos pedaços de código sem ter que escrever um programa inteiro. Antes de começarmos a escrever programas completos, precisamos garantir que o Python esteja instalado corretamente em seu sistema. Em seguida, aprenderemos como usar este interpretador para executar código Python.

## Inicie o Interpretador Python

1. Primeiro, precisamos abrir um terminal no WebIDE. O terminal é como um centro de comando onde você pode digitar comandos para interagir com seu computador. Você encontrará uma aba de terminal na parte inferior da tela. Depois de abri-lo, você estará pronto para começar a digitar comandos.

2. No terminal, vamos verificar se o Python está instalado e qual versão você tem. Digite o seguinte comando e pressione Enter:

   ```bash
   python3 --version
   ```

   Este comando pede ao seu sistema para mostrar a versão do Python que está atualmente instalada. Se o Python estiver instalado corretamente, você verá uma saída semelhante a:

   ```
   Python 3.10.x
   ```

   O `x` aqui representa um número de patch específico, que pode variar dependendo da sua instalação.

3. Agora que sabemos que o Python está instalado, vamos iniciar o interpretador interativo do Python. Digite o seguinte comando no terminal e pressione Enter:

   ```bash
   python3
   ```

   Depois de pressionar Enter, você verá algumas informações sobre a versão do Python e outros detalhes. A saída será algo parecido com isto:

   ```
   Python 3.10.x (default, ...)
   [GCC x.x.x] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   ```

   O prompt `>>>` é um sinal de que o interpretador Python está em execução e está esperando que você insira comandos Python.

## Experimente Comandos Python Simples

Agora que o interpretador Python está em execução, vamos experimentar alguns comandos Python básicos. Esses comandos ajudarão você a entender como o Python funciona e como usar o interpretador.

1. No prompt `>>>`, digite o seguinte comando e pressione Enter:

   ```python
   >>> print('Hello World')
   ```

   A função `print` em Python é usada para exibir texto na tela. Quando você executa este comando, você verá a seguinte saída:

   ```
   Hello World
   >>>
   ```

   Isso mostra que a função `print` exibiu com sucesso o texto 'Hello World'.

2. Vamos tentar um cálculo matemático simples. No prompt, digite:

   ```python
   >>> 2 + 3
   ```

   O Python avaliará automaticamente esta expressão e mostrará o resultado. Você verá:

   ```
   5
   >>>
   ```

   Isso demonstra que o Python pode realizar operações aritméticas básicas.

3. Em seguida, criaremos uma variável e a usaremos. Variáveis em Python são usadas para armazenar dados. Digite os seguintes comandos no prompt:

   ```python
   >>> message = "Learning Python"
   >>> print(message)
   ```

   Na primeira linha, estamos criando uma variável chamada `message` e armazenando a string "Learning Python" nela. Na segunda linha, estamos usando a função `print` para exibir o valor armazenado na variável `message`. A saída será:

   ```
   Learning Python
   >>>
   ```

   O interpretador Python executa cada linha de código assim que você a insere. Isso o torna uma ótima ferramenta para testar rapidamente ideias e aprender conceitos de Python.

## Saia do Interpretador

Quando você terminar de experimentar com o interpretador Python, você pode sair dele usando um dos seguintes métodos:

1. Você pode digitar o seguinte comando no prompt `>>>` e pressionar Enter:

   ```python
   >>> exit()
   ```

   Ou você pode usar este comando alternativo:

   ```python
   >>> quit()
   ```

   Ambos os comandos dizem ao interpretador Python para parar de executar e retornar você ao terminal normal.

2. Outra maneira de sair é pressionando Ctrl+D no seu teclado. Este é um atalho que também interrompe o interpretador Python.

Depois de sair do interpretador, você retornará ao prompt normal do terminal, onde poderá executar outros comandos em seu sistema.
