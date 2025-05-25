# Atualizando um Valor com Base no Valor Antigo

Outro caso de uso comum para hash maps é procurar o valor de uma chave e, em seguida, atualizá-lo com base no valor antigo. Por exemplo, a Listagem 8-25 mostra o código que conta quantas vezes cada palavra aparece em algum texto. Usamos um hash map com as palavras como chaves e incrementamos o valor para acompanhar quantas vezes vimos essa palavra. Se for a primeira vez que vemos uma palavra, primeiro inseriremos o valor `0`.

```rust
use std::collections::HashMap;

let text = "hello world wonderful world";

let mut map = HashMap::new();

for word in text.split_whitespace() {
    let count = map.entry(word).or_insert(0);
    *count += 1;
}

println!("{:?}", map);
```

Listagem 8-25: Contando ocorrências de palavras usando um hash map que armazena palavras e contagens

Este código imprimirá `{"world": 2, "hello": 1, "wonderful": 1}`. Você pode ver os mesmos pares chave-valor impressos em uma ordem diferente: lembre-se de "Acessando Valores em um Hash Map" que a iteração sobre um hash map acontece em uma ordem arbitrária.

O método `split_whitespace` retorna um iterador sobre subslices, separados por espaços em branco, do valor em `text`. O método `or_insert` retorna uma referência mutável (`&mut V`) ao valor para a chave especificada. Aqui, armazenamos essa referência mutável na variável `count`, então, para atribuir a esse valor, devemos primeiro desreferenciar `count` usando o asterisco (`*`). A referência mutável sai do escopo no final do loop `for`, então todas essas alterações são seguras e permitidas pelas regras de empréstimo (borrowing rules).
