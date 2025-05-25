# Codificando Estados e Comportamento como Tipos

Mostraremos como repensar o padrão de estado para obter um conjunto diferente de compensações. Em vez de encapsular os estados e transições completamente para que o código externo não tenha conhecimento deles, codificaremos os estados em tipos diferentes. Consequentemente,, o sistema de verificação de tipos do Rust impedirá tentativas de usar postagens de rascunho onde apenas postagens publicadas são permitidas, emitindo um erro do compilador.

Vamos considerar a primeira parte de `main` na Listagem 17-11:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");
    assert_eq!("", post.content());
}
```

Ainda permitimos a criação de novas postagens no estado de rascunho usando `Post::new` e a capacidade de adicionar texto ao conteúdo da postagem. Mas, em vez de ter um método `content` em uma postagem de rascunho que retorna uma string vazia, faremos com que as postagens de rascunho não tenham o método `content` de forma alguma. Dessa forma, se tentarmos obter o conteúdo de uma postagem de rascunho, receberemos um erro do compilador informando que o método não existe. Como resultado, será impossível para nós exibir acidentalmente o conteúdo da postagem de rascunho em produção, porque esse código nem mesmo compilará. A Listagem 17-19 mostra a definição de uma struct `Post` e uma struct `DraftPost`, bem como métodos em cada uma.

Nome do arquivo: `src/lib.rs`

```rust
pub struct Post {
    content: String,
}

pub struct DraftPost {
    content: String,
}

impl Post {
  1 pub fn new() -> DraftPost {
        DraftPost {
            content: String::new(),
        }
    }

  2 pub fn content(&self) -> &str {
        &self.content
    }
}

impl DraftPost {
  3 pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

Listagem 17-19: Um `Post` com um método `content` e um `DraftPost` sem um método `content`

Tanto as structs `Post` quanto `DraftPost` têm um campo `content` privado que armazena o texto da postagem do blog. As structs não têm mais o campo `state` porque estamos movendo a codificação do estado para os tipos das structs. A struct `Post` representará uma postagem publicada e tem um método `content` que retorna o `content` \[2].

Ainda temos uma função `Post::new`, mas em vez de retornar uma instância de `Post`, ela retorna uma instância de `DraftPost` \[1]. Como `content` é privado e não há funções que retornem `Post`, não é possível criar uma instância de `Post` no momento.

A struct `DraftPost` tem um método `add_text`, então podemos adicionar texto a `content` como antes \[3], mas observe que `DraftPost` não tem um método `content` definido! Portanto, agora o programa garante que todas as postagens comecem como postagens de rascunho, e as postagens de rascunho não têm seu conteúdo disponível para exibição. Qualquer tentativa de contornar essas restrições resultará em um erro do compilador.
