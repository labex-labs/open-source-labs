# Métodos com Mais Parâmetros

Vamos praticar o uso de métodos implementando um segundo método na struct `Rectangle`. Desta vez, queremos que uma instância de `Rectangle` receba outra instância de `Rectangle` e retorne `true` se o segundo `Rectangle` puder caber completamente dentro de `self` (o primeiro `Rectangle`); caso contrário, deve retornar `false`. Ou seja, depois de definirmos o método `can_hold`, queremos ser capazes de escrever o programa mostrado na Listagem 5-14.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    let rect2 = Rectangle {
        width: 10,
        height: 40,
    };
    let rect3 = Rectangle {
        width: 60,
        height: 45,
    };

    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));
}
```

Listagem 5-14: Usando o método `can_hold`, ainda não escrito

A saída esperada seria semelhante à seguinte, porque ambas as dimensões de `rect2` são menores que as dimensões de `rect1`, mas `rect3` é mais largo que `rect1`:

```rust
Can rect1 hold rect2? true
Can rect1 hold rect3? false
```

Sabemos que queremos definir um método, então ele estará dentro do bloco `impl Rectangle`. O nome do método será `can_hold`, e ele receberá um empréstimo imutável de outro `Rectangle` como parâmetro. Podemos dizer qual será o tipo do parâmetro olhando para o código que chama o método: `rect1.can_hold(&rect2)` passa `&rect2`, que é um empréstimo imutável para `rect2`, uma instância de `Rectangle`. Isso faz sentido porque só precisamos ler `rect2` (em vez de escrever, o que significaria que precisaríamos de um empréstimo mutável), e queremos que `main` mantenha a propriedade de `rect2` para que possamos usá-lo novamente após chamar o método `can_hold`. O valor de retorno de `can_hold` será um booleano, e a implementação verificará se a largura e a altura de `self` são maiores que a largura e a altura do outro `Rectangle`, respectivamente. Vamos adicionar o novo método `can_hold` ao bloco `impl` da Listagem 5-13, mostrado na Listagem 5-15.

Nome do arquivo: `src/main.rs`

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Listagem 5-15: Implementando o método `can_hold` em `Rectangle` que recebe outra instância de `Rectangle` como parâmetro

Quando executamos este código com a função `main` na Listagem 5-14, obteremos a saída desejada. Os métodos podem receber múltiplos parâmetros que adicionamos à assinatura após o parâmetro `self`, e esses parâmetros funcionam como parâmetros em funções.
