# Caminhos para Referenciar um Item na Árvore de Módulos

Para mostrar ao Rust onde encontrar um item em uma árvore de módulos, usamos um caminho da mesma forma que usamos um caminho ao navegar em um sistema de arquivos. Para chamar uma função, precisamos saber seu caminho.

Um caminho pode ter duas formas:

- Um _caminho absoluto_ é o caminho completo começando da raiz da crate; para código de uma crate externa, o caminho absoluto começa com o nome da crate, e para código da crate atual, ele começa com o literal `crate`.
- Um _caminho relativo_ começa do módulo atual e usa `self`, `super` ou um identificador no módulo atual.

Tanto os caminhos absolutos quanto os relativos são seguidos por um ou mais identificadores separados por dois pontos (`::`).

Voltando à Listagem 7-1, digamos que queremos chamar a função `add_to_waitlist`. Isso é o mesmo que perguntar: qual é o caminho da função `add_to_waitlist`? A Listagem 7-3 contém a Listagem 7-1 com alguns dos módulos e funções removidos.

Mostraremos duas maneiras de chamar a função `add_to_waitlist` de uma nova função, `eat_at_restaurant`, definida na raiz da crate. Esses caminhos estão corretos, mas ainda há outro problema que impedirá que este exemplo seja compilado como está. Explicaremos o porquê em breve.

A função `eat_at_restaurant` faz parte da API pública da nossa biblioteca crate, então a marcamos com a palavra-chave `pub`. Em "Expondo Caminhos com a Palavra-chave pub", entraremos em mais detalhes sobre `pub`.

Nome do arquivo: `src/lib.rs`

```rust
mod front_of_house {
    mod hosting {
        fn add_to_waitlist() {}
    }
}

pub fn eat_at_restaurant() {
    // Absolute path
    crate::front_of_house::hosting::add_to_waitlist();

    // Relative path
    front_of_house::hosting::add_to_waitlist();
}
```

Listagem 7-3: Chamando a função `add_to_waitlist` usando caminhos absolutos e relativos

A primeira vez que chamamos a função `add_to_waitlist` em `eat_at_restaurant`, usamos um caminho absoluto. A função `add_to_waitlist` é definida na mesma crate que `eat_at_restaurant`, o que significa que podemos usar a palavra-chave `crate` para iniciar um caminho absoluto. Em seguida, incluímos cada um dos módulos sucessivos até chegarmos a `add_to_waitlist`. Você pode imaginar um sistema de arquivos com a mesma estrutura: especificaríamos o caminho `/front_of_house/hosting/add_to_waitlist` para executar o programa `add_to_waitlist`; usar o nome da `crate` para começar da raiz da crate é como usar `/` para começar da raiz do sistema de arquivos em seu shell.

A segunda vez que chamamos `add_to_waitlist` em `eat_at_restaurant`, usamos um caminho relativo. O caminho começa com `front_of_house`, o nome do módulo definido no mesmo nível da árvore de módulos que `eat_at_restaurant`. Aqui, o equivalente do sistema de arquivos seria usar o caminho `front_of_house/hosting/add_to_waitlist`. Começar com um nome de módulo significa que o caminho é relativo.

Escolher entre usar um caminho relativo ou absoluto é uma decisão que você tomará com base no seu projeto, e depende se é mais provável que você mova o código de definição do item separadamente ou junto com o código que usa o item. Por exemplo, se movêssemos o módulo `front_of_house` e a função `eat_at_restaurant` para um módulo chamado `customer_experience`, precisaríamos atualizar o caminho absoluto para `add_to_waitlist`, mas o caminho relativo ainda seria válido. No entanto, se movêssemos a função `eat_at_restaurant` separadamente para um módulo chamado `dining`, o caminho absoluto para a chamada `add_to_waitlist` permaneceria o mesmo, mas o caminho relativo precisaria ser atualizado. Nossa preferência em geral é especificar caminhos absolutos porque é mais provável que queiramos mover definições de código e chamadas de itens independentemente umas das outras.

Vamos tentar compilar a Listagem 7-3 e descobrir por que ela ainda não compilará! Os erros que obtemos são mostrados na Listagem 7-4.

```bash
$ cargo build
   Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0603]: module `hosting` is private
 --> src/lib.rs:9:28
  |
9 |     crate::front_of_house::hosting::add_to_waitlist();
  |                            ^^^^^^^ private module
  |
note: the module `hosting` is defined here
 --> src/lib.rs:2:5
  |
2 |     mod hosting {
  |     ^^^^^^^^^^^

error[E0603]: module `hosting` is private
  --> src/lib.rs:12:21
   |
12 |     front_of_house::hosting::add_to_waitlist();
   |                     ^^^^^^^ private module
   |
note: the module `hosting` is defined here
  --> src/lib.rs:2:5
   |
2  |     mod hosting {
   |     ^^^^^^^^^^^
```

Listagem 7-4: Erros do compilador ao construir o código na Listagem 7-3

As mensagens de erro dizem que o módulo `hosting` é privado. Em outras palavras, temos os caminhos corretos para o módulo `hosting` e a função `add_to_waitlist`, mas o Rust não nos permitirá usá-los porque não tem acesso às seções privadas. Em Rust, todos os itens (funções, métodos, structs, enums, módulos e constantes) são privados para os módulos pai por padrão. Se você quiser tornar um item como uma função ou struct privado, você o coloca em um módulo.

Itens em um módulo pai não podem usar os itens privados dentro dos módulos filhos, mas itens em módulos filhos podem usar os itens em seus módulos ancestrais. Isso ocorre porque os módulos filhos envolvem e ocultam seus detalhes de implementação, mas os módulos filhos podem ver o contexto em que são definidos. Para continuar com nossa metáfora, pense nas regras de privacidade como sendo como os bastidores de um restaurante: o que acontece lá é privado para os clientes do restaurante, mas os gerentes de escritório podem ver e fazer tudo no restaurante que operam.

Rust escolheu que o sistema de módulos funcionasse dessa forma para que ocultar detalhes internos de implementação seja o padrão. Dessa forma, você sabe quais partes do código interno pode alterar sem quebrar o código externo. No entanto, o Rust oferece a opção de expor partes internas do código dos módulos filhos para os módulos ancestrais externos usando a palavra-chave `pub` para tornar um item público.
