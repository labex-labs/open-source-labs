# Em Definições de Métodos

Podemos implementar métodos em structs e enums (como fizemos no Capítulo 5) e usar tipos genéricos em suas definições também. A Listagem 10-9 mostra a struct `Point<T>` que definimos na Listagem 10-6 com um método chamado `x` implementado nela.

Nome do arquivo: `src/main.rs`

```rust
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

fn main() {
    let p = Point { x: 5, y: 10 };

    println!("p.x = {}", p.x());
}
```

Listagem 10-9: Implementando um método chamado `x` na struct `Point<T>` que retornará uma referência ao campo `x` do tipo `T`

Aqui, definimos um método chamado `x` em `Point<T>` que retorna uma referência aos dados no campo `x`.

Observe que temos que declarar `T` logo após `impl` para que possamos usar `T` para especificar que estamos implementando métodos no tipo `Point<T>`. Ao declarar `T` como um tipo genérico após `impl`, o Rust pode identificar que o tipo nos colchetes angulares em `Point` é um tipo genérico em vez de um tipo concreto. Poderíamos ter escolhido um nome diferente para este parâmetro genérico do que o parâmetro genérico declarado na definição da struct, mas usar o mesmo nome é convencional. Métodos escritos dentro de um `impl` que declara o tipo genérico serão definidos em qualquer instância do tipo, não importa qual tipo concreto acabe substituindo o tipo genérico.

Também podemos especificar restrições em tipos genéricos ao definir métodos no tipo. Poderíamos, por exemplo, implementar métodos apenas em instâncias `Point<f32>` em vez de em instâncias `Point<T>` com qualquer tipo genérico. Na Listagem 10-10, usamos o tipo concreto `f32`, o que significa que não declaramos nenhum tipo após `impl`.

Nome do arquivo: `src/main.rs`

```rust
impl Point<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}
```

Listagem 10-10: Um bloco `impl` que se aplica apenas a uma struct com um tipo concreto específico para o parâmetro de tipo genérico `T`

Este código significa que o tipo `Point<f32>` terá um método `distance_from_origin`; outras instâncias de `Point<T>` onde `T` não é do tipo `f32` não terão este método definido. O método mede a distância do nosso ponto em relação à origem (0.0, 0.0) e usa operações matemáticas que estão disponíveis apenas para tipos de ponto flutuante.

Parâmetros de tipo genérico em uma definição de struct nem sempre são os mesmos que você usa nas assinaturas de método da mesma struct. A Listagem 10-11 usa os tipos genéricos `X1` e `Y1` para a struct `Point` e `X2` `Y2` para a assinatura do método `mixup` para tornar o exemplo mais claro. O método cria uma nova instância `Point` com o valor `x` do `Point` `self` (do tipo `X1`) e o valor `y` do `Point` passado (do tipo `Y2`).

Nome do arquivo: `src/main.rs`

```rust
struct Point<X1, Y1> {
    x: X1,
    y: Y1,
}

1 impl<X1, Y1> Point<X1, Y1> {
  2 fn mixup<X2, Y2>(
        self,
        other: Point<X2, Y2>,
    ) -> Point<X1, Y2> {
        Point {
            x: self.x,
            y: other.y,
        }
    }
}

fn main() {
  3 let p1 = Point { x: 5, y: 10.4 };
  4 let p2 = Point { x: "Hello", y: 'c' };

  5 let p3 = p1.mixup(p2);

  6 println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
}
```

Listagem 10-11: Um método que usa tipos genéricos diferentes da definição de sua struct

Em `main`, definimos um `Point` que tem um `i32` para `x` (com o valor `5`) e um `f64` para `y` (com o valor `10.4` \[3]). A variável `p2` é uma struct `Point` que tem uma fatia de string para `x` (com o valor `"Hello"`) e um `char` para `y` (com o valor `c` \[4]). Chamar `mixup` em `p1` com o argumento `p2` nos dá `p3` \[5], que terá um `i32` para `x` porque `x` veio de `p1`. A variável `p3` terá um `char` para `y` porque `y` veio de `p2`. A chamada de macro `println!` \[6] imprimirá `p3.x = 5, p3.y = c`.

O objetivo deste exemplo é demonstrar uma situação em que alguns parâmetros genéricos são declarados com `impl` e alguns são declarados com a definição do método. Aqui, os parâmetros genéricos `X1` e `Y1` são declarados após `impl` \[1] porque eles vão com a definição da struct. Os parâmetros genéricos `X2` e `Y2` são declarados após `fn mixup` \[2] porque são relevantes apenas para o método.
