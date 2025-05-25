# Movimentos Parciais

Dentro da \[desestruturação] de uma única variável, tanto `by-move` quanto `by-reference` pattern bindings (ligações de padrão) podem ser usados ao mesmo tempo. Fazer isso resultará em um _movimento parcial_ da variável, o que significa que partes da variável serão movidas enquanto outras partes permanecem. Em tal caso, a variável pai não pode ser usada posteriormente como um todo, no entanto, as partes que são apenas referenciadas (e não movidas) ainda podem ser usadas.

```rust
fn main() {
    #[derive(Debug)]
    struct Person {
        name: String,
        age: Box<u8>,
    }

    let person = Person {
        name: String::from("Alice"),
        age: Box::new(20),
    };

    // `name` is moved out of person, but `age` is referenced
    let Person { name, ref age } = person;

    println!("The person's age is {}", age);

    println!("The person's name is {}", name);

    // Error! borrow of partially moved value: `person` partial move occurs
    //println!("The person struct is {:?}", person);

    // `person` cannot be used but `person.age` can be used as it is not moved
    println!("The person's age from person struct is {}", person.age);
}
```

(Neste exemplo, armazenamos a variável `age` no heap (montículo) para ilustrar o movimento parcial: deletar `ref` no código acima daria um erro, pois a propriedade de `person.age` seria movida para a variável `age`. Se `Person.age` fosse armazenado na stack (pilha), `ref` não seria necessário, pois a definição de `age` copiaria os dados de `person.age` sem movê-los.)
