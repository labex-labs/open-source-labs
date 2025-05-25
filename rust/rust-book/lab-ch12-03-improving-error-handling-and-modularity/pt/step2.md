# Separação de Preocupações para Projetos Binários

O problema organizacional de alocar responsabilidade por múltiplas tarefas à função `main` é comum a muitos projetos binários. Como resultado, a comunidade Rust desenvolveu diretrizes para dividir as diferentes preocupações de um programa binário quando `main` começa a ficar grande. Esse processo tem as seguintes etapas:

- Divida seu programa em um arquivo `main.rs` e um arquivo `lib.rs` e mova a lógica do seu programa para `lib.rs`.
- Contanto que sua lógica de análise da linha de comando seja pequena, ela pode permanecer em `main.rs`.
- Quando a lógica de análise da linha de comando começar a ficar complicada, extraia-a de `main.rs` e mova-a para `lib.rs`.

As responsabilidades que permanecem na função `main` após este processo devem ser limitadas ao seguinte:

- Chamar a lógica de análise da linha de comando com os valores dos argumentos
- Configurar qualquer outra configuração
- Chamar uma função `run` em `lib.rs`
- Lidar com o erro se `run` retornar um erro

Este padrão é sobre separar as preocupações: `main.rs` lida com a execução do programa e `lib.rs` lida com toda a lógica da tarefa em questão. Como você não pode testar a função `main` diretamente, essa estrutura permite que você teste toda a lógica do seu programa, movendo-a para funções em `lib.rs`. O código que permanece em `main.rs` será pequeno o suficiente para verificar sua correção lendo-o. Vamos reformular nosso programa seguindo este processo.
