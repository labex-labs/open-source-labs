# Desambiguação de _traits_ sobrepostos

Um tipo pode implementar muitos _traits_ diferentes. E se dois _traits_ exigirem o mesmo nome? Por exemplo, muitos _traits_ podem ter um método chamado `get()`. Eles podem até ter diferentes tipos de retorno!

Boas notícias: porque cada implementação de _trait_ recebe seu próprio bloco `impl`, fica claro qual método `get` do _trait_ você está implementando.

Mas e quando chega a hora de _chamar_ esses métodos? Para desambiguá-los, precisamos usar a Sintaxe Totalmente Qualificada (Fully Qualified Syntax).

```rust
trait UsernameWidget {
    // Get the selected username out of this widget
    fn get(&self) -> String;
}

trait AgeWidget {
    // Get the selected age out of this widget
    fn get(&self) -> u8;
}

// A form with both a UsernameWidget and an AgeWidget
struct Form {
    username: String,
    age: u8,
}

impl UsernameWidget for Form {
    fn get(&self) -> String {
        self.username.clone()
    }
}

impl AgeWidget for Form {
    fn get(&self) -> u8 {
        self.age
    }
}

fn main() {
    let form = Form {
        username: "rustacean".to_owned(),
        age: 28,
    };

    // If you uncomment this line, you'll get an error saying
    // "multiple `get` found". Because, after all, there are multiple methods
    // named `get`.
    // println!("{}", form.get());

    let username = <Form as UsernameWidget>::get(&form);
    assert_eq!("rustacean".to_owned(), username);
    let age = <Form as AgeWidget>::get(&form);
    assert_eq!(28, age);
}
```
