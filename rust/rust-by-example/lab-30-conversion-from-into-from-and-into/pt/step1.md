# `From` e `Into`

Os traits [`From`](#from) e [`Into`](#into) estão intrinsecamente ligados, e isto faz parte da sua implementação. Se for possível converter o tipo A a partir do tipo B, então é de esperar que seja possível converter o tipo B para o tipo A.

## `From`

O trait [`From`](#from) permite que um tipo defina como criar a si próprio a partir de outro tipo, fornecendo assim um mecanismo simples para converter entre vários tipos. Existem inúmeras implementações deste trait na biblioteca padrão para conversão de tipos primitivos e comuns.

Por exemplo, podemos facilmente converter um `str` num `String`:

```rust
let my_str = "hello";
let my_string = String::from(my_str);
```

Podemos fazer algo semelhante para definir uma conversão para o nosso próprio tipo.

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

O trait [`Into`](#into) é simplesmente o recíproco do trait `From`. Ou seja, se tiver implementado o trait `From` para o seu tipo, `Into` irá chamá-lo quando necessário.

Utilizar o trait `Into` normalmente requer a especificação do tipo para conversão, uma vez que o compilador geralmente não consegue determiná-lo. No entanto, este é um pequeno custo considerando que obtemos a funcionalidade gratuitamente.

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
    // Tente remover a anotação de tipo
    let num: Number = int.into();
    println!("My number is {:?}", num);
}
```
