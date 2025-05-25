# Laços `for`

Em um laço `for`, o valor que segue diretamente a palavra-chave `for` é um padrão. Por exemplo, em `for x in y`, o `x` é o padrão. A Listagem 18-3 demonstra como usar um padrão em um laço `for` para _desestruturar_ (destructure), ou quebrar, uma tupla como parte do laço `for`.

Nome do arquivo: `src/main.rs`

```rust
let v = vec!['a', 'b', 'c'];

for (index, value) in v.iter().enumerate() {
    println!("{value} is at index {index}");
}
```

Listagem 18-3: Usando um padrão em um laço `for` para desestruturar uma tupla

O código na Listagem 18-3 imprimirá o seguinte:

    a is at index 0
    b is at index 1
    c is at index 2

Adaptamos um iterador usando o método `enumerate` para que ele produza um valor e o índice para esse valor, colocados em uma tupla. O primeiro valor produzido é a tupla `(0, 'a')`. Quando esse valor é correspondido ao padrão `(index, value)`, `index` será `0` e `value` será `'a'`, imprimindo a primeira linha da saída.
