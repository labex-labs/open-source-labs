# Escopo e Sombreamento

As ligações de variáveis têm um escopo e estão limitadas a viver em um _bloco_. Um bloco é uma coleção de instruções delimitadas por chaves `{}`.

```rust
fn main() {
    // Esta ligação vive na função principal
    let long_lived_binding = 1;

    // Este é um bloco, e tem um escopo menor que a função principal
    {
        // Esta ligação só existe neste bloco
        let short_lived_binding = 2;

        println!("inner short: {}", short_lived_binding);
    }
    // Fim do bloco

    // Erro! `short_lived_binding` não existe neste escopo
    println!("outer short: {}", short_lived_binding);
    // FIXME ^ Comente esta linha

    println!("outer long: {}", long_lived_binding);
}
```

Também é permitido o sombreamento de variáveis.

```rust
fn main() {
    let shadowed_binding = 1;

    {
        println!("antes de ser sombreado: {}", shadowed_binding);

        // Esta ligação *sombreia* a externa
        let shadowed_binding = "abc";

        println!("sombreado no bloco interno: {}", shadowed_binding);
    }
    println!("fora do bloco interno: {}", shadowed_binding);

    // Esta ligação *sombreia* a ligação anterior
    let shadowed_binding = 2;
    println!("sombreado no bloco externo: {}", shadowed_binding);
}
```
