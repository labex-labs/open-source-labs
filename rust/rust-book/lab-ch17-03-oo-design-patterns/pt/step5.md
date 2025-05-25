# Solicitar uma Revisão Altera o Estado da Postagem

Em seguida, precisamos adicionar funcionalidade para solicitar uma revisão de uma postagem, o que deve alterar seu estado de `Draft` para `PendingReview`. A Listagem 17-15 mostra este código.

Nome do arquivo: `src/lib.rs`

```rust
impl Post {
    --snip--
  1 pub fn request_review(&mut self) {
      2 if let Some(s) = self.state.take() {
          3 self.state = Some(s.request_review())
        }
    }
}

trait State {
  4 fn request_review(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
      5 Box::new(PendingReview {})
    }
}

struct PendingReview {}

impl State for PendingReview {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
      6 self
    }
}
```

Listagem 17-15: Implementando os métodos `request_review` em `Post` e o trait `State`

Damos a `Post` um método público chamado `request_review` que receberá uma referência mutável a `self` \[1]. Em seguida, chamamos um método interno `request_review` no estado atual de `Post` \[3], e este segundo método `request_review` consome o estado atual e retorna um novo estado.

Adicionamos o método `request_review` ao trait `State` \[4]; todos os tipos que implementam o trait agora precisarão implementar o método `request_review`. Observe que, em vez de ter `self`, `&self` ou `&mut self` como o primeiro parâmetro do método, temos `self: Box<Self>`. Esta sintaxe significa que o método é válido apenas quando chamado em um `Box` que contém o tipo. Esta sintaxe assume a propriedade de `Box<Self>`, invalidando o estado antigo para que o valor do estado de `Post` possa se transformar em um novo estado.

Para consumir o estado antigo, o método `request_review` precisa assumir a propriedade do valor do estado. É aqui que o `Option` no campo `state` de `Post` entra em ação: chamamos o método `take` para tirar o valor `Some` do campo `state` e deixar um `None` em seu lugar porque o Rust não nos permite ter campos não preenchidos em structs \[2]. Isso nos permite mover o valor `state` de `Post` em vez de emprestá-lo. Em seguida, definiremos o valor `state` da postagem para o resultado desta operação.

Precisamos definir `state` temporariamente como `None` em vez de defini-lo diretamente com código como `self.state = self.state.request_review();` para obter a propriedade do valor `state`. Isso garante que `Post` não possa usar o valor `state` antigo depois de transformá-lo em um novo estado.

O método `request_review` em `Draft` retorna uma nova instância, em caixa, de uma nova struct `PendingReview` \[5], que representa o estado quando uma postagem está aguardando uma revisão. A struct `PendingReview` também implementa o método `request_review`, mas não faz nenhuma transformação. Em vez disso, ele retorna a si mesmo \[6] porque, quando solicitamos uma revisão em uma postagem já no estado `PendingReview`, ela deve permanecer no estado `PendingReview`.

Agora podemos começar a ver as vantagens do padrão de estado: o método `request_review` em `Post` é o mesmo, independentemente do seu valor `state`. Cada estado é responsável por suas próprias regras.

Deixaremos o método `content` em `Post` como está, retornando uma fatia de string vazia. Agora podemos ter um `Post` no estado `PendingReview`, bem como no estado `Draft`, mas queremos o mesmo comportamento no estado `PendingReview`. A Listagem 17-11 agora funciona até a linha em \[5]!
