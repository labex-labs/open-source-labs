# Usando Box`<T>` Como uma Referência

Podemos reescrever o código na Listagem 15-6 para usar um `Box<T>` em vez de uma referência; o operador de desreferenciação usado no `Box<T>` na Listagem 15-7 funciona da mesma forma que o operador de desreferenciação usado na referência na Listagem 15-6.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let x = 5;
  1 let y = Box::new(x);

    assert_eq!(5, x);
  2 assert_eq!(5, *y);
}
```

Listagem 15-7: Usando o operador de desreferenciação em um `Box<i32>`

A principal diferença entre a Listagem 15-7 e a Listagem 15-6 é que aqui definimos `y` como uma instância de uma box apontando para um valor copiado de `x`, em vez de uma referência apontando para o valor de `x` \[1]. Na última asserção \[2], podemos usar o operador de desreferenciação para seguir o ponteiro da box da mesma forma que fizemos quando `y` era uma referência. Em seguida, exploraremos o que é especial sobre `Box<T>` que nos permite usar o operador de desreferenciação, definindo nosso próprio tipo de box.
