# Implementando um Padrão de Design Orientado a Objetos

O _padrão de estado_ (state pattern) é um padrão de design orientado a objetos. O cerne do padrão é que definimos um conjunto de estados que um valor pode ter internamente. Os estados são representados por um conjunto de _objetos de estado_ (state objects), e o comportamento do valor muda com base em seu estado. Vamos trabalhar em um exemplo de uma struct de postagem de blog que possui um campo para manter seu estado, que será um objeto de estado do conjunto "rascunho", "revisão" ou "publicado".

Os objetos de estado compartilham funcionalidade: em Rust, é claro, usamos structs e traits em vez de objetos e herança. Cada objeto de estado é responsável por seu próprio comportamento e por governar quando deve mudar para outro estado. O valor que contém um objeto de estado não sabe nada sobre o comportamento diferente dos estados ou quando fazer a transição entre os estados.

A vantagem de usar o padrão de estado é que, quando os requisitos de negócios do programa mudam, não precisaremos alterar o código do valor que contém o estado ou o código que usa o valor. Só precisaremos atualizar o código dentro de um dos objetos de estado para alterar suas regras ou talvez adicionar mais objetos de estado.

Primeiro, vamos implementar o padrão de estado de uma maneira mais tradicional orientada a objetos, então usaremos uma abordagem que é um pouco mais natural em Rust. Vamos mergulhar na implementação incremental de um fluxo de trabalho de postagem de blog usando o padrão de estado.

A funcionalidade final terá a seguinte aparência:

1.  Uma postagem de blog começa como um rascunho vazio.
2.  Quando o rascunho é concluído, uma revisão da postagem é solicitada.
3.  Quando a postagem é aprovada, ela é publicada.
4.  Apenas as postagens de blog publicadas retornam conteúdo para impressão, para que as postagens não aprovadas não possam ser publicadas acidentalmente.

Quaisquer outras alterações tentadas em uma postagem não devem ter efeito. Por exemplo, se tentarmos aprovar um rascunho de postagem de blog antes de solicitar uma revisão, a postagem deverá permanecer um rascunho não publicado.

A Listagem 17-11 mostra este fluxo de trabalho em forma de código: este é um exemplo de uso da API que implementaremos em uma crate de biblioteca chamada `blog`. Isso ainda não compilará porque ainda não implementamos a crate `blog`.

Nome do arquivo: `src/main.rs`

```rust
use blog::Post;

fn main() {
  1 let mut post = Post::new();

  2 post.add_text("I ate a salad for lunch today");
  3 assert_eq!("", post.content());

  4 post.request_review();
  5 assert_eq!("", post.content());

  6 post.approve();
  7 assert_eq!("I ate a salad for lunch today", post.content());
}
```

Listagem 17-11: Código que demonstra o comportamento desejado que queremos que nossa crate `blog` tenha

Queremos permitir que o usuário crie uma nova postagem de blog de rascunho com `Post::new` \[1]. Queremos permitir que o texto seja adicionado à postagem do blog \[2]. Se tentarmos obter o conteúdo da postagem imediatamente, antes da aprovação, não devemos obter nenhum texto porque a postagem ainda é um rascunho. Adicionamos `assert_eq!` no código para fins de demonstração \[3]. Um excelente teste de unidade para isso seria afirmar que uma postagem de blog de rascunho retorna uma string vazia do método `content`, mas não vamos escrever testes para este exemplo.

Em seguida, queremos habilitar uma solicitação de revisão da postagem \[4], e queremos que `content` retorne uma string vazia enquanto aguarda a revisão \[5]. Quando a postagem recebe aprovação \[6], ela deve ser publicada, o que significa que o texto da postagem será retornado quando `content` for chamado \[7].

Observe que o único tipo com o qual estamos interagindo da crate é o tipo `Post`. Este tipo usará o padrão de estado e conterá um valor que será um de três objetos de estado representando os vários estados em que uma postagem pode estar --- rascunho, revisão ou publicado. A mudança de um estado para outro será gerenciada internamente dentro do tipo `Post`. Os estados mudam em resposta aos métodos chamados pelos usuários de nossa biblioteca na instância `Post`, mas eles não precisam gerenciar as mudanças de estado diretamente. Além disso, os usuários não podem cometer um erro com os estados, como publicar uma postagem antes que ela seja revisada.
