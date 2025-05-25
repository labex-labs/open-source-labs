# Múltiplos Blocos `impl`

Cada struct pode ter múltiplos blocos `impl`. Por exemplo, a Listagem 5-15 é equivalente ao código mostrado na Listagem 5-16, que tem cada método em seu próprio bloco `impl`.

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Listagem 5-16: Reescrevendo a Listagem 5-15 usando múltiplos blocos `impl`

Não há razão para separar esses métodos em múltiplos blocos `impl` aqui, mas esta é uma sintaxe válida. Veremos um caso em que múltiplos blocos `impl` são úteis no Capítulo 10, onde discutiremos tipos genéricos e traits.
