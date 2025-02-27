# `From` et `Into`

Les traits [`From`](#from) et [`Into`](#into) sont intrinsèquement liés, et c'est en fait une partie de leur implémentation. Si vous êtes capable de convertir le type A à partir du type B, alors il devrait être facile de croire que nous devrions être capables de convertir le type B en type A.

## `From`

Le trait [`From`](#from) permet à un type de définir comment se créer lui-même à partir d'un autre type, offrant ainsi un mécanisme très simple pour convertir entre plusieurs types. Il existe de nombreuses implémentations de ce trait dans la bibliothèque standard pour la conversion de types primitifs et courants.

Par exemple, nous pouvons facilement convertir une `str` en une `String`

```rust
let my_str = "hello";
let my_string = String::from(my_str);
```

Nous pouvons faire de même pour définir une conversion pour notre propre type.

```rust
use std::convert::From;

#[derive(Debug)]
struct Number {
    value: i32,
}

impl From<i32> for Number {
    fn from(item: i32) -> Self {
        Number { value: item }
    }
}

fn main() {
    let num = Number::from(30);
    println!("My number is {:?}", num);
}
```

## `Into`

Le trait [`Into`](#into) est simplement le réciproque du trait `From`. C'est-à-dire que si vous avez implémenté le trait `From` pour votre type, `Into` l'appellera si nécessaire.

Utiliser le trait `Into` nécessitera généralement de spécifier le type de conversion car le compilateur est incapable de le déterminer la plupart du temps. Cependant, c'est un petit compromis compte tenu que nous obtenons cette fonctionnalité gratuitement.

```rust
use std::convert::Into;

#[derive(Debug)]
struct Number {
    value: i32,
}

impl Into<Number> for i32 {
    fn into(self) -> Number {
        Number { value: self }
    }
}

fn main() {
    let int = 5;
    // Essayez de supprimer l'annotation de type
    let num: Number = int.into();
    println!("My number is {:?}", num);
}
```
