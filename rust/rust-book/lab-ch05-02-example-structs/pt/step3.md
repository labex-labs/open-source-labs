# Refatorando com Structs: Adicionando Mais Significado

Usamos structs para adicionar significado rotulando os dados. Podemos transformar a tupla que estamos usando em uma struct com um nome para o todo, bem como nomes para as partes, conforme mostrado na Listagem 5-10.

Nome do arquivo: `src/main.rs`

```rust
1 struct Rectangle {
  2 width: u32,
    height: u32,
}

fn main() {
  3 let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        area(&rect1)
    );
}

4 fn area(rectangle: &Rectangle) -> u32 {
  5 rectangle.width * rectangle.height
}
```

Listagem 5-10: Definindo uma struct `Rectangle`

Aqui, definimos uma struct e a nomeamos `Rectangle` \[1]. Dentro das chaves, definimos os campos como `width` e `height`, ambos do tipo `u32` \[2]. Então, em `main`, criamos uma instância específica de `Rectangle` que tem uma largura de `30` e uma altura de `50` \[3].

Nossa função `area` agora é definida com um parâmetro, que nomeamos `rectangle`, cujo tipo é um empréstimo imutável de uma instância da struct `Rectangle` \[4]. Como mencionado no Capítulo 4, queremos emprestar a struct em vez de assumir a propriedade dela. Dessa forma, `main` retém sua propriedade e pode continuar usando `rect1`, que é a razão pela qual usamos o `&` na assinatura da função e onde chamamos a função.

A função `area` acessa os campos `width` e `height` da instância `Rectangle` \[5] (observe que acessar campos de uma instância de struct emprestada não move os valores dos campos, e é por isso que você frequentemente vê empréstimos de structs). Nossa assinatura de função para `area` agora diz exatamente o que queremos dizer: calcular a área de `Rectangle`, usando seus campos `width` e `height`. Isso transmite que a largura e a altura estão relacionadas entre si e dá nomes descritivos aos valores em vez de usar os valores de índice de tupla `0` e `1`. Isso é uma vitória para a clareza.
