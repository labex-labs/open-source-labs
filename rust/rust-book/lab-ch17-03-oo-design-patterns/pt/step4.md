# Garantindo que o Conteúdo de uma Postagem em Rascunho esteja Vazio

Mesmo depois de chamarmos `add_text` e adicionarmos algum conteúdo à nossa postagem, ainda queremos que o método `content` retorne uma fatia de string vazia porque a postagem ainda está no estado de rascunho, conforme mostrado em \[3] na Listagem 17-11. Por enquanto, vamos implementar o método `content` com a coisa mais simples que atenderá a este requisito: sempre retornando uma fatia de string vazia. Mudaremos isso mais tarde, uma vez que implementarmos a capacidade de alterar o estado de uma postagem para que ela possa ser publicada. Até agora, as postagens só podem estar no estado de rascunho, então o conteúdo da postagem deve sempre estar vazio. A Listagem 17-14 mostra esta implementação de espaço reservado.

Nome do arquivo: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn content(&self) -> &str {
        ""
    }
}
```

Listagem 17-14: Adicionando uma implementação de espaço reservado para o método `content` em `Post` que sempre retorna uma fatia de string vazia

Com este método `content` adicionado, tudo na Listagem 17-11 até a linha em \[3] funciona como pretendido.
