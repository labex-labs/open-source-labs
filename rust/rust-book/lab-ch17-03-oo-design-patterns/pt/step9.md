# Implementando Transições como Transformações em Tipos Diferentes

Então, como obtemos uma postagem publicada? Queremos impor a regra de que uma postagem de rascunho precisa ser revisada e aprovada antes que possa ser publicada. Uma postagem no estado de revisão pendente ainda não deve exibir nenhum conteúdo. Vamos implementar essas restrições adicionando outra struct, `PendingReviewPost`, definindo o método `request_review` em `DraftPost` para retornar um `PendingReviewPost` e definindo um método `approve` em `PendingReviewPost` para retornar um `Post`, conforme mostrado na Listagem 17-20.

Nome do arquivo: `src/lib.rs`

```rust
impl DraftPost {
    --snip--
    pub fn request_review(self) -> PendingReviewPost {
        PendingReviewPost {
            content: self.content,
        }
    }
}

pub struct PendingReviewPost {
    content: String,
}

impl PendingReviewPost {
    pub fn approve(self) -> Post {
        Post {
            content: self.content,
        }
    }
}
```

Listagem 17-20: Um `PendingReviewPost` que é criado chamando `request_review` em `DraftPost` e um método `approve` que transforma um `PendingReviewPost` em um `Post` publicado

Os métodos `request_review` e `approve` assumem a propriedade de `self`, consumindo assim as instâncias `DraftPost` e `PendingReviewPost` e transformando-as em um `PendingReviewPost` e um `Post` publicado, respectivamente. Dessa forma, não teremos nenhuma instância `DraftPost` persistente depois de chamarmos `request_review` nelas, e assim por diante. A struct `PendingReviewPost` não tem um método `content` definido, portanto, tentar ler seu conteúdo resulta em um erro do compilador, como com `DraftPost`. Como a única maneira de obter uma instância `Post` publicada que tenha um método `content` definido é chamar o método `approve` em um `PendingReviewPost`, e a única maneira de obter um `PendingReviewPost` é chamar o método `request_review` em um `DraftPost`, agora codificamos o fluxo de trabalho da postagem do blog no sistema de tipos.

Mas também precisamos fazer algumas pequenas alterações em `main`. Os métodos `request_review` e `approve` retornam novas instâncias em vez de modificar a struct em que são chamados, então precisamos adicionar mais atribuições de sombreamento `let post =` para salvar as instâncias retornadas. Também não podemos ter as asserções sobre os conteúdos das postagens de rascunho e revisão pendente sendo strings vazias, nem precisamos delas: não podemos compilar código que tenta usar o conteúdo de postagens nesses estados. O código atualizado em `main` é mostrado na Listagem 17-21.

Nome do arquivo: `src/main.rs`

```rust
use blog::Post;

fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");

    let post = post.request_review();

    let post = post.approve();

    assert_eq!("I ate a salad for lunch today", post.content());
}
```

Listagem 17-21: Modificações em `main` para usar a nova implementação do fluxo de trabalho da postagem do blog

As alterações que precisávamos fazer em `main` para reatribuir `post` significam que essa implementação não segue mais o padrão de estado orientado a objetos: as transformações entre os estados não são mais encapsuladas inteiramente dentro da implementação `Post`. No entanto, nosso ganho é que os estados inválidos agora são impossíveis por causa do sistema de tipos e da verificação de tipos que acontece no tempo de compilação! Isso garante que certos bugs, como a exibição do conteúdo de uma postagem não publicada, sejam descobertos antes de chegarem à produção.

Experimente as tarefas sugeridas no início desta seção no crate `blog` como está após a Listagem 17-21 para ver o que você pensa sobre o design desta versão do código. Observe que algumas das tarefas podem já estar concluídas neste design.

Vimos que, embora o Rust seja capaz de implementar padrões de design orientados a objetos, outros padrões, como a codificação de estado no sistema de tipos, também estão disponíveis no Rust. Esses padrões têm diferentes compensações. Embora você possa estar muito familiarizado com padrões orientados a objetos, repensar o problema para aproveitar os recursos do Rust pode fornecer benefícios, como evitar alguns bugs no tempo de compilação. Os padrões orientados a objetos nem sempre serão a melhor solução no Rust devido a certos recursos, como propriedade, que as linguagens orientadas a objetos não possuem.
