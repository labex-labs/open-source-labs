# Armazenando o Texto do Conteúdo da Postagem

Vimos na Listagem 17-11 que queremos ser capazes de chamar um método chamado `add_text` e passar a ele um `&str` que é então adicionado como o conteúdo de texto da postagem do blog. Implementamos isso como um método, em vez de expor o campo `content` como `pub`, para que, mais tarde, possamos implementar um método que controlará como os dados do campo `content` são lidos. O método `add_text` é bastante simples, então vamos adicionar a implementação na Listagem 17-13 ao bloco `impl Post`.

Nome do arquivo: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

Listagem 17-13: Implementando o método `add_text` para adicionar texto ao `content` de uma postagem

O método `add_text` recebe uma referência mutável a `self` porque estamos alterando a instância `Post` na qual estamos chamando `add_text`. Em seguida, chamamos `push_str` na `String` em `content` e passamos o argumento `text` para adicionar ao `content` salvo. Este comportamento não depende do estado em que a postagem está, portanto, não faz parte do padrão de estado. O método `add_text` não interage com o campo `state` em absoluto, mas faz parte do comportamento que queremos suportar.
