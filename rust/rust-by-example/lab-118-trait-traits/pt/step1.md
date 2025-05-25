# _Traits_

Um _trait_ é uma coleção de métodos definidos para um tipo desconhecido: `Self`. Eles podem acessar outros métodos declarados no mesmo _trait_.

_Traits_ podem ser implementados para qualquer tipo de dado. No exemplo abaixo, definimos `Animal`, um grupo de métodos. O _trait_ `Animal` é então implementado para o tipo de dado `Sheep`, permitindo o uso de métodos de `Animal` com um `Sheep`.

```rust
struct Sheep { naked: bool, name: &'static str }

trait Animal {
    // Assinatura de função associada; `Self` refere-se ao tipo implementador.
    fn new(name: &'static str) -> Self;

    // Assinaturas de métodos; estes retornarão uma string.
    fn name(&self) -> &'static str;
    fn noise(&self) -> &'static str;

    // Traits podem fornecer definições de métodos padrão.
    fn talk(&self) {
        println!("{} says {}", self.name(), self.noise());
    }
}

impl Sheep {
    fn is_naked(&self) -> bool {
        self.naked
    }

    fn shear(&mut self) {
        if self.is_naked() {
            // Métodos do implementador podem usar os métodos do trait do implementador.
            println!("{} is already naked...", self.name());
        } else {
            println!("{} gets a haircut!", self.name);

            self.naked = true;
        }
    }
}

// Implementa o trait `Animal` para `Sheep`.
impl Animal for Sheep {
    // `Self` é o tipo implementador: `Sheep`.
    fn new(name: &'static str) -> Sheep {
        Sheep { name: name, naked: false }
    }

    fn name(&self) -> &'static str {
        self.name
    }

    fn noise(&self) -> &'static str {
        if self.is_naked() {
            "baaaaah?"
        } else {
            "baaaaah!"
        }
    }

    // Métodos de trait padrão podem ser substituídos.
    fn talk(&self) {
        // Por exemplo, podemos adicionar alguma contemplação silenciosa.
        println!("{} pauses briefly... {}", self.name, self.noise());
    }
}

fn main() {
    // A anotação de tipo é necessária neste caso.
    let mut dolly: Sheep = Animal::new("Dolly");
    // TODO ^ Tente remover as anotações de tipo.

    dolly.talk();
    dolly.shear();
    dolly.talk();
}
```
