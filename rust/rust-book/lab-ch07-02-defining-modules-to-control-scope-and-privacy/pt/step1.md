# Definindo Módulos para Controlar Escopo e Privacidade

Nesta seção, falaremos sobre módulos e outras partes do sistema de módulos, nomeadamente _paths_ (caminhos), que permitem nomear itens; a palavra-chave `use` que traz um caminho para o escopo; e a palavra-chave `pub` para tornar os itens públicos. Também discutiremos a palavra-chave `as`, pacotes externos e o operador glob.

_Módulos_ nos permitem organizar o código dentro de um crate para legibilidade e fácil reutilização. Módulos também nos permitem controlar a _privacidade_ dos itens porque o código dentro de um módulo é privado por padrão. Itens privados são detalhes de implementação interna não disponíveis para uso externo. Podemos optar por tornar os módulos e os itens dentro deles públicos, o que os expõe para permitir que o código externo os use e dependa deles.

Como exemplo, vamos escrever um crate de biblioteca que fornece a funcionalidade de um restaurante. Definiremos as assinaturas das funções, mas deixaremos seus corpos vazios para nos concentrarmos na organização do código em vez da implementação de um restaurante.

Na indústria de restaurantes, algumas partes de um restaurante são referidas como _front of house_ (frente da casa) e outras como _back of house_ (fundo da casa). A frente da casa é onde os clientes estão; isso engloba onde os anfitriões acomodam os clientes, os garçons recebem pedidos e pagamentos, e os bartenders preparam bebidas. O fundo da casa é onde os chefs e cozinheiros trabalham na cozinha, os lavadores de louça limpam e os gerentes fazem trabalho administrativo.

Para estruturar nosso crate dessa forma, podemos organizar suas funções em módulos aninhados. Crie uma nova biblioteca chamada `restaurant` executando `cargo new restaurant --lib`. Em seguida, insira o código na Listagem 7-1 em `src/lib.rs` para definir alguns módulos e assinaturas de funções; este código é a seção da frente da casa.

Nome do arquivo: `src/lib.rs`

```rust
mod front_of_house {
    mod hosting {
        fn add_to_waitlist() {}

        fn seat_at_table() {}
    }

    mod serving {
        fn take_order() {}

        fn serve_order() {}

        fn take_payment() {}
    }
}
```

Listagem 7-1: Um módulo `front_of_house` contendo outros módulos que, por sua vez, contêm funções

Definimos um módulo com a palavra-chave `mod` seguida pelo nome do módulo (neste caso, `front_of_house`). O corpo do módulo então vai dentro de chaves. Dentro dos módulos, podemos colocar outros módulos, como neste caso com os módulos `hosting` e `serving`. Os módulos também podem conter definições para outros itens, como structs, enums, constantes, traits e - como na Listagem 7-1 - funções.

Ao usar módulos, podemos agrupar definições relacionadas e nomear por que elas estão relacionadas. Os programadores que usam este código podem navegar no código com base nos grupos, em vez de ter que ler todas as definições, tornando mais fácil encontrar as definições relevantes para eles. Os programadores que adicionam novas funcionalidades a este código saberiam onde colocar o código para manter o programa organizado.

Anteriormente, mencionamos que `src/main.rs` e `src/lib.rs` são chamados de raízes do crate. A razão para seus nomes é que o conteúdo de qualquer um desses dois arquivos forma um módulo chamado `crate` na raiz da estrutura do módulo do crate, conhecida como _árvore de módulos_.

A Listagem 7-2 mostra a árvore de módulos para a estrutura na Listagem 7-1.

```bash
crate
└── front_of_house
├── hosting
│ ├── add_to_waitlist
│ └── seat_at_table
└── serving
├── take_order
├── serve_order
└── take_payment
```

Listagem 7-2: A árvore de módulos para o código na Listagem 7-1

Esta árvore mostra como alguns dos módulos se aninham dentro de outros módulos; por exemplo, `hosting` se aninha dentro de `front_of_house`. A árvore também mostra que alguns módulos são _irmãos_, o que significa que eles são definidos no mesmo módulo; `hosting` e `serving` são irmãos definidos dentro de `front_of_house`. Se o módulo A estiver contido dentro do módulo B, dizemos que o módulo A é o _filho_ do módulo B e que o módulo B é o _pai_ do módulo A. Observe que toda a árvore de módulos está enraizada sob o módulo implícito chamado `crate`.

A árvore de módulos pode lembrá-lo da árvore de diretórios do sistema de arquivos em seu computador; esta é uma comparação muito apropriada! Assim como os diretórios em um sistema de arquivos, você usa módulos para organizar seu código. E assim como os arquivos em um diretório, precisamos de uma maneira de encontrar nossos módulos.
