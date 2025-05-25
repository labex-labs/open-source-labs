# Definindo Post e Criando uma Nova Instância no Estado de Rascunho

Vamos começar a implementação da biblioteca! Sabemos que precisamos de uma struct `Post` pública que contenha algum conteúdo, então começaremos com a definição da struct e uma função `new` pública associada para criar uma instância de `Post`, conforme mostrado na Listagem 17-12. Também criaremos um trait `State` privado que definirá o comportamento que todos os objetos de estado para um `Post` devem ter.

Então, `Post` conterá um objeto trait de `Box<dyn State>` dentro de um `Option<T>` em um campo privado chamado `state` para conter o objeto de estado. Você verá por que o `Option<T>` é necessário em breve.

Nome do arquivo: `src/lib.rs`

```rust
pub struct Post {
    state: Option<Box<dyn State>>,
    content: String,
}

impl Post {
    pub fn new() -> Post {
        Post {
          1 state: Some(Box::new(Draft {})),
          2 content: String::new(),
        }
    }
}

trait State {}

struct Draft {}

impl State for Draft {}
```

Listagem 17-12: Definição de uma struct `Post` e uma função `new` que cria uma nova instância de `Post`, um trait `State` e uma struct `Draft`

O trait `State` define o comportamento compartilhado pelos diferentes estados da postagem. Os objetos de estado são `Draft`, `PendingReview` e `Published`, e todos eles implementarão o trait `State`. Por enquanto, o trait não possui nenhum método, e começaremos definindo apenas o estado `Draft` porque esse é o estado em que queremos que uma postagem comece.

Quando criamos um novo `Post`, definimos seu campo `state` como um valor `Some` que contém um `Box` \[1]. Este `Box` aponta para uma nova instância da struct `Draft`. Isso garante que sempre que criarmos uma nova instância de `Post`, ela começará como um rascunho. Como o campo `state` de `Post` é privado, não há como criar um `Post` em nenhum outro estado! Na função `Post::new`, definimos o campo `content` como uma nova `String` vazia \[2].
