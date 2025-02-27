# Movimientos parciales

Dentro de la \[desestructuración\] de una variable única, se pueden utilizar enlaces de patrón `by-move` y `by-reference` al mismo tiempo. Hacer esto resultará en un _movimiento parcial_ de la variable, lo que significa que partes de la variable se moverán mientras que otras partes permanecerán. En tal caso, la variable padre no se puede utilizar después como un todo, sin embargo las partes que solo se refieren (y no se mueven) todavía se pueden utilizar.

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

    // `name` se mueve fuera de person, pero `age` se referencia
    let Person { name, ref age } = person;

    println!("La edad de la persona es {}", age);

    println!("El nombre de la persona es {}", name);

    // Error! préstamo de valor parcialmente movido: `person` se produce un movimiento parcial
    //println!("La estructura de persona es {:?}", person);

    // `person` no se puede utilizar pero `person.age` se puede utilizar ya que no se mueve
    println!("La edad de la persona de la estructura de persona es {}", person.age);
}
```

(En este ejemplo, almacenamos la variable `age` en el montón para ilustrar el movimiento parcial: eliminar `ref` en el código anterior generaría un error ya que la propiedad de `person.age` se movería a la variable `age`. Si `Person.age` se almacenara en la pila, no se requeriría `ref` ya que la definición de `age` copiaría los datos de `person.age` sin moverlos.)
