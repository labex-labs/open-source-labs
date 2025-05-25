# Implementando o Trait

Agora, adicionaremos alguns tipos que implementam o trait `Draw`. Forneceremos o tipo `Button`. Novamente, a implementação real de uma biblioteca GUI está além do escopo deste livro, então o método `draw` não terá nenhuma implementação útil em seu corpo. Para imaginar como a implementação pode ser, uma struct `Button` pode ter campos para `width`, `height` e `label`, conforme mostrado no Listing 17-7.

Nome do arquivo: `src/lib.rs`

```rust
pub struct Button {
    pub width: u32,
    pub height: u32,
    pub label: String,
}

impl Draw for Button {
    fn draw(&self) {
        // code to actually draw a button
    }
}
```

Listing 17-7: Uma struct `Button` que implementa o trait `Draw`

Os campos `width`, `height` e `label` em `Button` serão diferentes dos campos em outros componentes; por exemplo, um tipo `TextField` pode ter os mesmos campos mais um campo `placeholder`. Cada um dos tipos que queremos desenhar na tela implementará o trait `Draw`, mas usará código diferente no método `draw` para definir como desenhar esse tipo específico, como `Button` tem aqui (sem o código GUI real, como mencionado). O tipo `Button`, por exemplo, pode ter um bloco `impl` adicional contendo métodos relacionados ao que acontece quando um usuário clica no botão. Esses tipos de métodos não se aplicarão a tipos como `TextField`.

Se alguém que usa nossa biblioteca decidir implementar uma struct `SelectBox` que tenha campos `width`, `height` e `options`, eles também implementariam o trait `Draw` no tipo `SelectBox`, conforme mostrado no Listing 17-8.

Nome do arquivo: `src/main.rs`

```rust
use gui::Draw;

struct SelectBox {
    width: u32,
    height: u32,
    options: Vec<String>,
}

impl Draw for SelectBox {
    fn draw(&self) {
        // code to actually draw a select box
    }
}
```

Listing 17-8: Outra crate usando `gui` e implementando o trait `Draw` em uma struct `SelectBox`

O usuário da nossa biblioteca agora pode escrever sua função `main` para criar uma instância `Screen`. Para a instância `Screen`, eles podem adicionar um `SelectBox` e um `Button` colocando cada um em um `Box<T>` para se tornar um objeto trait. Eles podem então chamar o método `run` na instância `Screen`, que chamará `draw` em cada um dos componentes. O Listing 17-9 mostra esta implementação.

Nome do arquivo: `src/main.rs`

```rust
use gui::{Button, Screen};

fn main() {
    let screen = Screen {
        components: vec![
            Box::new(SelectBox {
                width: 75,
                height: 10,
                options: vec![
                    String::from("Yes"),
                    String::from("Maybe"),
                    String::from("No"),
                ],
            }),
            Box::new(Button {
                width: 50,
                height: 10,
                label: String::from("OK"),
            }),
        ],
    };

    screen.run();
}
```

Listing 17-9: Usando objetos trait para armazenar valores de diferentes tipos que implementam o mesmo trait

Quando escrevemos a biblioteca, não sabíamos que alguém poderia adicionar o tipo `SelectBox`, mas nossa implementação `Screen` foi capaz de operar no novo tipo e desenhá-lo porque `SelectBox` implementa o trait `Draw`, o que significa que ele implementa o método `draw`.

Este conceito - de se preocupar apenas com as mensagens às quais um valor responde, em vez do tipo concreto do valor - é semelhante ao conceito de _duck typing_ em linguagens de tipagem dinâmica: se anda como um pato e grasna como um pato, então deve ser um pato! Na implementação de `run` em `Screen` no Listing 17-5, `run` não precisa saber qual é o tipo concreto de cada componente. Ele não verifica se um componente é uma instância de um `Button` ou um `SelectBox`, ele apenas chama o método `draw` no componente. Ao especificar `Box<dyn Draw>` como o tipo dos valores no vetor `components`, definimos que `Screen` precisa de valores nos quais podemos chamar o método `draw`.

A vantagem de usar objetos trait e o sistema de tipos do Rust para escrever código semelhante ao código que usa duck typing é que nunca precisamos verificar se um valor implementa um método específico em tempo de execução ou nos preocupar em obter erros se um valor não implementar um método, mas o chamarmos de qualquer maneira. O Rust não compilará nosso código se os valores não implementarem os traits que os objetos trait precisam.

Por exemplo, o Listing 17-10 mostra o que acontece se tentarmos criar um `Screen` com uma `String` como um componente.

Nome do arquivo: `src/main.rs`

```rust
use gui::Screen;

fn main() {
    let screen = Screen {
        components: vec![Box::new(String::from("Hi"))],
    };

    screen.run();
}
```

Listing 17-10: Tentando usar um tipo que não implementa o trait do objeto trait

Obteremos este erro porque `String` não implementa o trait `Draw`:

```bash
error[E0277]: the trait bound `String: Draw` is not satisfied
 --> src/main.rs:5:26
  |
5 |         components: vec![Box::new(String::from("Hi"))],
  |                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ the trait `Draw` is
not implemented for `String`
  |
  = note: required for the cast to the object type `dyn Draw`
```

Este erro nos informa que estamos passando algo para `Screen` que não pretendíamos passar e, portanto, devemos passar um tipo diferente, ou devemos implementar `Draw` em `String` para que `Screen` possa chamar `draw` nele.
