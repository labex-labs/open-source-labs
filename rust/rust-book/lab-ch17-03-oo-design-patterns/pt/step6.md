# Adicionando `approve` para Alterar o Comportamento de `content`

O método `approve` será semelhante ao método `request_review`: ele definirá `state` para o valor que o estado atual diz que ele deve ter quando esse estado for aprovado, conforme mostrado na Listagem 17-16.

Nome do arquivo: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn approve(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.approve())
        }
    }
}

trait State {
    fn request_review(self: Box<Self>) -> Box<dyn State>;
    fn approve(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
      1 self
    }
}

struct PendingReview {}

impl State for PendingReview {
    --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
      2 Box::new(Published {})
    }
}

struct Published {}

impl State for Published {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }
}
```

Listagem 17-16: Implementando o método `approve` em `Post` e o trait `State`

Adicionamos o método `approve` ao trait `State` e adicionamos uma nova struct que implementa `State`, o estado `Published`.

Semelhante à forma como `request_review` em `PendingReview` funciona, se chamarmos o método `approve` em um `Draft`, ele não terá efeito porque `approve` retornará `self` \[1]. Quando chamamos `approve` em `PendingReview`, ele retorna uma nova instância, em caixa, da struct `Published` \[2]. A struct `Published` implementa o trait `State`, e para os métodos `request_review` e `approve`, ele retorna a si mesmo porque a postagem deve permanecer no estado `Published` nesses casos.

Agora precisamos atualizar o método `content` em `Post`. Queremos que o valor retornado de `content` dependa do estado atual de `Post`, então vamos fazer com que `Post` delegue a um método `content` definido em seu `state`, conforme mostrado na Listagem 17-17.

Nome do arquivo: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn content(&self) -> &str {
        self.state.as_ref().unwrap().content(self)
    }
    --snip--
}
```

Listagem 17-17: Atualizando o método `content` em `Post` para delegar a um método `content` em `State`

Como o objetivo é manter todas essas regras dentro das structs que implementam `State`, chamamos um método `content` no valor em `state` e passamos a instância da postagem (ou seja, `self`) como um argumento. Em seguida, retornamos o valor que é retornado ao usar o método `content` no valor `state`.

Chamamos o método `as_ref` em `Option` porque queremos uma referência ao valor dentro de `Option` em vez da propriedade do valor. Como `state` é um `Option<Box<dyn State>>`, quando chamamos `as_ref`, um `Option<&Box<dyn State>>` é retornado. Se não chamássemos `as_ref`, receberíamos um erro porque não podemos mover `state` de `&self` emprestado do parâmetro da função.

Em seguida, chamamos o método `unwrap`, que sabemos que nunca entrará em pânico porque sabemos que os métodos em `Post` garantem que `state` sempre conterá um valor `Some` quando esses métodos forem concluídos. Este é um dos casos sobre os quais falamos em "Casos em que você tem mais informações do que o compilador" quando sabemos que um valor `None` nunca é possível, embora o compilador não consiga entender isso.

Neste ponto, quando chamamos `content` em `&Box<dyn State>`, a coerção de deref entrará em vigor no `&` e no `Box`, para que o método `content` seja, em última análise, chamado no tipo que implementa o trait `State`. Isso significa que precisamos adicionar `content` à definição do trait `State`, e é aí que colocaremos a lógica para qual conteúdo retornar dependendo de qual estado temos, conforme mostrado na Listagem 17-18.

Nome do arquivo: `src/lib.rs`

```rust
trait State {
    --snip--
    fn content<'a>(&self, post: &'a Post) -> &'a str {
      1 ""
    }
}

--snip--
struct Published {}

impl State for Published {
    --snip--
    fn content<'a>(&self, post: &'a Post) -> &'a str {
      2 &post.content
    }
}
```

Listagem 17-18: Adicionando o método `content` ao trait `State`

Adicionamos uma implementação padrão para o método `content` que retorna uma fatia de string vazia \[1]. Isso significa que não precisamos implementar `content` nas structs `Draft` e `PendingReview`. A struct `Published` substituirá o método `content` e retornará o valor em `post.content` \[2].

Observe que precisamos de anotações de tempo de vida neste método, como discutimos no Capítulo 10. Estamos pegando uma referência a um `post` como um argumento e retornando uma referência a parte desse `post`, então o tempo de vida da referência retornada está relacionado ao tempo de vida do argumento `post`.

E terminamos---tudo na Listagem 17-11 agora funciona! Implementamos o padrão de estado com as regras do fluxo de trabalho da postagem do blog. A lógica relacionada às regras reside nos objetos de estado em vez de ser espalhada por todo o `Post`.

> **Por que não um Enum?**
>
> Você pode estar se perguntando por que não usamos um `enum` com os diferentes estados possíveis da postagem como variantes. Essa é certamente uma solução possível; experimente e compare os resultados finais para ver qual você prefere! Uma desvantagem de usar um enum é que todo lugar que verifica o valor do enum precisará de uma expressão `match` ou semelhante para lidar com todas as variantes possíveis. Isso pode ficar mais repetitivo do que esta solução de objeto de trait.
