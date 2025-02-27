# Identificadores crudos

Rust, al igual que muchos lenguajes de programación, tiene el concepto de "palabras clave". Estos identificadores tienen un significado para el lenguaje, y por lo tanto no se pueden usar en lugares como nombres de variables, nombres de funciones y otros lugares. Los identificadores crudos te permiten usar palabras clave donde normalmente no se les permitiría. Esto es particularmente útil cuando Rust introduce nuevas palabras clave, y una biblioteca que utiliza una edición anterior de Rust tiene una variable o función con el mismo nombre que una palabra clave introducida en una edición más reciente.

Por ejemplo, considere un crat (`crate`) `foo` compilado con la edición 2015 de Rust que exporta una función llamada `try`. Esta palabra clave está reservada para una nueva característica en la edición 2018, por lo que sin identificadores crudos, no tendríamos forma de nombrar la función.

```rust
extern crate foo;

fn main() {
    foo::try();
}
```

Obtendrás este error:

```plaintext
error: expected identifier, found keyword `try`
 --> src/main.rs:4:4
  |
4 | foo::try();
  |      ^^^ expected identifier, found keyword
```

Puedes escribir esto con un identificador crudo:

```rust
extern crate foo;

fn main() {
    foo::r#try();
}
```
