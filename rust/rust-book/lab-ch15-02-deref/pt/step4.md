# Definindo Nosso Próprio Ponteiro Inteligente

Vamos construir um ponteiro inteligente semelhante ao tipo `Box<T>` fornecido pela biblioteca padrão para experimentar como os ponteiros inteligentes se comportam de forma diferente das referências por padrão. Em seguida, veremos como adicionar a capacidade de usar o operador de desreferenciação.

O tipo `Box<T>` é, em última análise, definido como uma struct de tupla com um elemento, então a Listagem 15-8 define um tipo `MyBox<T>` da mesma maneira. Também definiremos uma função `new` para corresponder à função `new` definida em `Box<T>`.

Nome do arquivo: `src/main.rs`

```rust
 1 struct MyBox<T>(T);

impl<T> MyBox<T> {
  2 fn new(x: T) -> MyBox<T> {
      3 MyBox(x)
    }
}
```

Listagem 15-8: Definindo um tipo `MyBox<T>`

Definimos uma struct chamada `MyBox` e declaramos um parâmetro genérico `T` \[1] porque queremos que nosso tipo contenha valores de qualquer tipo. O tipo `MyBox` é uma struct de tupla com um elemento do tipo `T`. A função `MyBox::new` recebe um parâmetro do tipo `T` \[2] e retorna uma instância `MyBox` que contém o valor passado \[3].

Vamos tentar adicionar a função `main` na Listagem 15-7 à Listagem 15-8 e alterá-la para usar o tipo `MyBox<T>` que definimos em vez de `Box<T>`. O código na Listagem 15-9 não compilará porque o Rust não sabe como desreferenciar `MyBox`.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}
```

Listagem 15-9: Tentando usar `MyBox<T>` da mesma forma que usamos referências e `Box<T>`

Aqui está o erro de compilação resultante:

```bash
error[E0614]: type `MyBox<{integer}>` cannot be dereferenced
  --> src/main.rs:14:19
   |
14 |     assert_eq!(5, *y);
   |                   ^^
```

Nosso tipo `MyBox<T>` não pode ser desreferenciado porque não implementamos essa capacidade em nosso tipo. Para habilitar a desreferenciação com o operador `*`, implementamos o trait `Deref`.
