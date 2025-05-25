# Expondo Caminhos com a Palavra-chave `pub`

Vamos voltar ao erro na Listagem 7-4 que nos informou que o módulo `hosting` é privado. Queremos que a função `eat_at_restaurant` no módulo pai tenha acesso à função `add_to_waitlist` no módulo filho, então marcamos o módulo `hosting` com a palavra-chave `pub`, conforme mostrado na Listagem 7-5.

Nome do arquivo: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        fn add_to_waitlist() {}
    }
}

--snip--
```

Listagem 7-5: Declarando o módulo `hosting` como `pub` para usá-lo de `eat_at_restaurant`

Infelizmente, o código na Listagem 7-5 ainda resulta em erros do compilador, conforme mostrado na Listagem 7-6.

```bash
$ cargo build
   Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0603]: function `add_to_waitlist` is private
 --> src/lib.rs:9:37
  |
9 |     crate::front_of_house::hosting::add_to_waitlist();
  |                                     ^^^^^^^^^^^^^^^ private function
  |
note: the function `add_to_waitlist` is defined here
 --> src/lib.rs:3:9
  |
3 |         fn add_to_waitlist() {}
  |         ^^^^^^^^^^^^^^^^^^^^

error[E0603]: function `add_to_waitlist` is private
  --> src/lib.rs:12:30
   |
12 |     front_of_house::hosting::add_to_waitlist();
   |                              ^^^^^^^^^^^^^^^ private function
   |
note: the function `add_to_waitlist` is defined here
  --> src/lib.rs:3:9
   |
3  |         fn add_to_waitlist() {}
   |         ^^^^^^^^^^^^^^^^^^^^
```

Listagem 7-6: Erros do compilador ao construir o código na Listagem 7-5

O que aconteceu? Adicionar a palavra-chave `pub` na frente de `mod hosting` torna o módulo público. Com essa alteração, se pudermos acessar `front_of_house`, podemos acessar `hosting`. Mas o _conteúdo_ de `hosting` ainda é privado; tornar o módulo público não torna seu conteúdo público. A palavra-chave `pub` em um módulo só permite que o código em seus módulos ancestrais se refira a ele, não acesse seu código interno. Como os módulos são contêineres, não há muito que possamos fazer apenas tornando o módulo público; precisamos ir mais longe e escolher tornar um ou mais dos itens dentro do módulo público também.

Os erros na Listagem 7-6 dizem que a função `add_to_waitlist` é privada. As regras de privacidade se aplicam a structs, enums, funções e métodos, bem como a módulos.

Vamos também tornar a função `add_to_waitlist` pública adicionando a palavra-chave `pub` antes de sua definição, como na Listagem 7-7.

Nome do arquivo: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

--snip--
```

Listagem 7-7: Adicionar a palavra-chave `pub` a `mod hosting` e `fn add_to_waitlist` nos permite chamar a função de `eat_at_restaurant`.

Agora o código compilará! Para ver por que adicionar a palavra-chave `pub` nos permite usar esses caminhos em `add_to_waitlist` com relação às regras de privacidade, vamos analisar os caminhos absolutos e relativos.

No caminho absoluto, começamos com `crate`, a raiz da árvore de módulos da nossa crate. O módulo `front_of_house` é definido na raiz da crate. Embora `front_of_house` não seja público, como a função `eat_at_restaurant` é definida no mesmo módulo que `front_of_house` (ou seja, `eat_at_restaurant` e `front_of_house` são irmãos), podemos nos referir a `front_of_house` de `eat_at_restaurant`. Em seguida, está o módulo `hosting` marcado com `pub`. Podemos acessar o módulo pai de `hosting`, então podemos acessar `hosting`. Finalmente, a função `add_to_waitlist` é marcada com `pub` e podemos acessar seu módulo pai, então essa chamada de função funciona!

No caminho relativo, a lógica é a mesma do caminho absoluto, exceto pela primeira etapa: em vez de começar da raiz da crate, o caminho começa de `front_of_house`. O módulo `front_of_house` é definido dentro do mesmo módulo que `eat_at_restaurant`, então o caminho relativo começando do módulo em que `eat_at_restaurant` é definido funciona. Então, como `hosting` e `add_to_waitlist` são marcados com `pub`, o restante do caminho funciona, e essa chamada de função é válida!

Se você planeja compartilhar sua biblioteca crate para que outros projetos possam usar seu código, sua API pública é seu contrato com os usuários da sua crate que determina como eles podem interagir com seu código. Existem muitas considerações em torno do gerenciamento de alterações em sua API pública para facilitar a dependência de sua crate pelas pessoas. Essas considerações estão além do escopo deste livro; se você estiver interessado neste tópico, consulte as Diretrizes da API Rust em *https://rust-lang.github.io/api-guidelines*.

> **Melhores Práticas para Pacotes com um Binário e uma Biblioteca**
>
> Mencionamos que um pacote pode conter tanto uma raiz de crate binária `src/main.rs` quanto uma raiz de crate de biblioteca `src/lib.rs`, e ambas as crates terão o nome do pacote por padrão. Normalmente, pacotes com esse padrão de conter tanto uma biblioteca quanto uma crate binária terão código suficiente na crate binária para iniciar um executável que chama código com a crate de biblioteca. Isso permite que outros projetos se beneficiem da maior parte da funcionalidade que o pacote fornece, porque o código da crate de biblioteca pode ser compartilhado.
>
> A árvore de módulos deve ser definida em `src/lib.rs`. Em seguida, quaisquer itens públicos podem ser usados na crate binária, começando os caminhos com o nome do pacote. A crate binária se torna um usuário da crate de biblioteca, assim como uma crate completamente externa usaria a crate de biblioteca: ela só pode usar a API pública. Isso ajuda você a projetar uma boa API; você não é apenas o autor, você também é um cliente!
>
> No Capítulo 12, demonstraremos essa prática organizacional com um programa de linha de comando que conterá tanto uma crate binária quanto uma crate de biblioteca.
