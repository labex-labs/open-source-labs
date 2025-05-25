# Debug (Depuração)

Todos os tipos que desejam usar os _traits_ de formatação `std::fmt` requerem uma implementação para serem imprimíveis. Implementações automáticas são fornecidas apenas para tipos como os da biblioteca `std`. Todos os outros _devem_ ser implementados manualmente de alguma forma.

O _trait_ `fmt::Debug` torna isso muito simples. _Todos_ os tipos podem `derive` (criar automaticamente) a implementação `fmt::Debug`. Isso não é verdade para `fmt::Display`, que deve ser implementado manualmente.

```rust
// Esta estrutura não pode ser impressa nem com `fmt::Display` nem
// com `fmt::Debug`.
struct UnPrintable(i32);

// O atributo `derive` cria automaticamente a implementação
// necessária para tornar esta `struct` imprimível com `fmt::Debug`.
#[derive(Debug)]
struct DebugPrintable(i32);
```

Todos os tipos da biblioteca `std` são automaticamente imprimíveis com `{:?}` também:

```rust
// Deriva a implementação `fmt::Debug` para `Structure`. `Structure`
// é uma estrutura que contém um único `i32`.
#[derive(Debug)]
struct Structure(i32);

// Coloca uma `Structure` dentro da estrutura `Deep`. Torna-a imprimível
// também.
#[derive(Debug)]
struct Deep(Structure);

fn main() {
    // Imprimir com `{:?}` é semelhante a com `{}`.
    println!("{:?} meses em um ano.", 12);
    println!("{1:?} {0:?} é o nome do {actor:?}.",
             "Slater",
             "Christian",
             actor="ator's");

    // `Structure` é imprimível!
    println!("Agora {:?} irá imprimir!", Structure(3));

    // O problema com `derive` é que não há controle sobre como
    // os resultados aparecem. E se eu quiser que isso mostre apenas um `7`?
    println!("Agora {:?} irá imprimir!", Deep(Structure(7)));
}
```

Portanto, `fmt::Debug` definitivamente torna isso imprimível, mas sacrifica um pouco de elegância. Rust também fornece "pretty printing" (formatação elegante) com `{:#?}`.

```rust
#[derive(Debug)]
struct Person<'a> {
    name: &'a str,
    age: u8
}

fn main() {
    let name = "Peter";
    let age = 27;
    let peter = Person { name, age };

    // Pretty print (Formatação elegante)
    println!("{:#?}", peter);
}
```

Pode-se implementar manualmente `fmt::Display` para controlar a exibição.
