# Capturando o Ambiente com Closures

Primeiramente, examinaremos como podemos usar closures para capturar valores do ambiente em que são definidas para uso posterior. Aqui está o cenário: de vez em quando, nossa empresa de camisetas oferece uma camiseta exclusiva de edição limitada para alguém em nossa lista de e-mail como uma promoção. As pessoas na lista de e-mail podem opcionalmente adicionar sua cor favorita ao seu perfil. Se a pessoa escolhida para uma camiseta grátis tiver sua cor favorita definida, ela receberá a camiseta dessa cor. Se a pessoa não especificou uma cor favorita, ela receberá a cor que a empresa tem em maior quantidade no momento.

Existem muitas maneiras de implementar isso. Para este exemplo, vamos usar um enum chamado `ShirtColor` que tem as variantes `Red` e `Blue` (limitando o número de cores disponíveis para simplificar). Representamos o inventário da empresa com uma struct `Inventory` que tem um campo chamado `shirts` que contém um `Vec<ShirtColor>` representando as cores das camisetas atualmente em estoque. O método `giveaway` definido em `Inventory` obtém a preferência opcional de cor da camiseta do vencedor e retorna a cor da camiseta que a pessoa receberá. Essa configuração é mostrada na Listagem 13-1.

Nome do arquivo: `src/main.rs`

```rust
#[derive(Debug, PartialEq, Copy, Clone)]
enum ShirtColor {
    Red,
    Blue,
}

struct Inventory {
    shirts: Vec<ShirtColor>,
}

impl Inventory {
    fn giveaway(
        &self,
        user_preference: Option<ShirtColor>,
    ) -> ShirtColor {
      1 user_preference.unwrap_or_else(|| self.most_stocked())
    }

    fn most_stocked(&self) -> ShirtColor {
        let mut num_red = 0;
        let mut num_blue = 0;

        for color in &self.shirts {
            match color {
                ShirtColor::Red => num_red += 1,
                ShirtColor::Blue => num_blue += 1,
            }
        }
        if num_red > num_blue {
            ShirtColor::Red
        } else {
            ShirtColor::Blue
        }
    }
}

fn main() {
    let store = Inventory {
      2 shirts: vec![
            ShirtColor::Blue,
            ShirtColor::Red,
            ShirtColor::Blue,
        ],
    };

    let user_pref1 = Some(ShirtColor::Red);
  3 let giveaway1 = store.giveaway(user_pref1);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref1, giveaway1
    );

    let user_pref2 = None;
  4 let giveaway2 = store.giveaway(user_pref2);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref2, giveaway2
    );
}
```

Listagem 13-1: Situação de sorteio da empresa de camisetas

A `store` definida em `main` tem duas camisetas azuis e uma camiseta vermelha restantes para distribuir para esta promoção de edição limitada \[2\]. Chamamos o método `giveaway` para um usuário com preferência por uma camiseta vermelha \[3] e um usuário sem nenhuma preferência \[4].

Novamente, este código poderia ser implementado de muitas maneiras e, aqui, para focar em closures, nos apegamos a conceitos que você já aprendeu, exceto pelo corpo do método `giveaway` que usa uma closure. No método `giveaway`, obtemos a preferência do usuário como um parâmetro do tipo `Option<ShirtColor>` e chamamos o método `unwrap_or_else` em `user_preference` \[1]. O método `unwrap_or_else` em `Option<T>` é definido pela biblioteca padrão. Ele recebe um argumento: uma closure sem nenhum argumento que retorna um valor `T` (o mesmo tipo armazenado na variante `Some` do `Option<T>`, neste caso `ShirtColor`). Se o `Option<T>` for a variante `Some`, `unwrap_or_else` retorna o valor de dentro do `Some`. Se o `Option<T>` for a variante `None`, `unwrap_or_else` chama a closure e retorna o valor retornado pela closure.

Especificamos a expressão de closure `|| self.most_stocked()` como o argumento para `unwrap_or_else`. Esta é uma closure que não recebe nenhum parâmetro (se a closure tivesse parâmetros, eles apareceriam entre as duas barras verticais). O corpo da closure chama `self.most_stocked()`. Estamos definindo a closure aqui, e a implementação de `unwrap_or_else` avaliará a closure mais tarde, se o resultado for necessário.

A execução deste código imprime o seguinte:

```rust
The user with preference Some(Red) gets Red
The user with preference None gets Blue
```

Um aspecto interessante aqui é que passamos uma closure que chama `self.most_stocked()` na instância `Inventory` atual. A biblioteca padrão não precisou saber nada sobre os tipos `Inventory` ou `ShirtColor` que definimos, ou a lógica que queremos usar neste cenário. A closure captura uma referência imutável para a instância `self` `Inventory` e a passa com o código que especificamos para o método `unwrap_or_else`. Funções, por outro lado, não são capazes de capturar seu ambiente dessa maneira.
