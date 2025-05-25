# Verificando Onde os Erros São Escritos

Primeiro, vamos observar como o conteúdo impresso por `minigrep` está sendo escrito atualmente na saída padrão, incluindo quaisquer mensagens de erro que queremos escrever na saída de erro padrão. Faremos isso redirecionando o fluxo de saída padrão para um arquivo, enquanto intencionalmente causamos um erro. Não redirecionaremos o fluxo de erro padrão, então qualquer conteúdo enviado para a saída de erro padrão continuará a ser exibido na tela.

Espera-se que os programas de linha de comando enviem mensagens de erro para o fluxo de erro padrão, para que ainda possamos ver as mensagens de erro na tela, mesmo que redirecionemos o fluxo de saída padrão para um arquivo. Nosso programa não está se comportando bem no momento: estamos prestes a ver que ele salva a saída da mensagem de erro em um arquivo!

Para demonstrar esse comportamento, executaremos o programa com `>` e o caminho do arquivo, _output.txt_, para o qual queremos redirecionar o fluxo de saída padrão. Não passaremos nenhum argumento, o que deve causar um erro:

```bash
cargo run > output.txt
```

A sintaxe `>` diz ao shell para escrever o conteúdo da saída padrão em _output.txt_ em vez da tela. Não vimos a mensagem de erro que esperávamos impressa na tela, então isso significa que ela deve ter acabado no arquivo. É isso que _output.txt_ contém:

```rust
Problem parsing arguments: not enough arguments
```

Sim, nossa mensagem de erro está sendo impressa na saída padrão. É muito mais útil que mensagens de erro como essa sejam impressas na saída de erro padrão, para que apenas dados de uma execução bem-sucedida acabem no arquivo. Vamos mudar isso.
