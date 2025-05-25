# Alias

A declaração `type` pode ser usada para dar um novo nome a um tipo existente. Os tipos devem ter nomes em `UpperCamelCase`, caso contrário, o compilador emitirá um aviso. A exceção a esta regra são os tipos primitivos: `usize`, `f32`, etc.

```rust
// `NanoSecond`, `Inch`, e `U64` são novos nomes para `u64`.
type NanoSecond = u64;
type Inch = u64;
type U64 = u64;

fn main() {
    // `NanoSecond` = `Inch` = `U64` = `u64`.
    let nanoseconds: NanoSecond = 5 as U64;
    let inches: Inch = 2 as U64;

    // Note que os aliases de tipo *não* fornecem segurança de tipo adicional, porque
    // os aliases *não* são novos tipos
    println!("{} nanosegundos + {} polegadas = {} unidade?",
             nanoseconds,
             inches,
             nanoseconds + inches);
}
```

O principal uso dos aliases é reduzir a repetição; por exemplo, o tipo `io::Result<T>` é um alias para o tipo `Result<T, io::Error>`.
