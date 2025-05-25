# Correspondência de Intervalos de Valores com ..= (Matching Ranges of Values with ..=)

A sintaxe `..=` nos permite corresponder a um intervalo inclusivo de valores. No código a seguir, quando um padrão corresponde a qualquer um dos valores dentro do intervalo fornecido, esse braço será executado:

Nome do arquivo: `src/main.rs`

```rust
let x = 5;

match x {
    1..=5 => println!("one through five"),
    _ => println!("something else"),
}
```

Se `x` for `1`, `2`, `3`, `4` ou `5`, o primeiro braço corresponderá. Essa sintaxe é mais conveniente para múltiplos valores de correspondência do que usar o operador `|` para expressar a mesma ideia; se fôssemos usar `|`, teríamos que especificar `1 | 2 | 3 | 4 | 5`. Especificar um intervalo é muito mais curto, especialmente se quisermos corresponder, por exemplo, qualquer número entre 1 e 1.000!

O compilador verifica se o intervalo não está vazio no tempo de compilação, e como os únicos tipos para os quais o Rust pode dizer se um intervalo está vazio ou não são `char` e valores numéricos, os intervalos são permitidos apenas com valores numéricos ou `char`.

Aqui está um exemplo usando intervalos de valores `char`:

Nome do arquivo: `src/main.rs`

```rust
let x = 'c';

match x {
    'a'..='j' => println!("early ASCII letter"),
    'k'..='z' => println!("late ASCII letter"),
    _ => println!("something else"),
}
```

Rust pode dizer que `'c'` está dentro do intervalo do primeiro padrão e imprime `early ASCII letter`.
