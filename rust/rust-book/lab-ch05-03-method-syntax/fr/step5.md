# Plusieurs blocs impl

Chaque structure est autorisée à avoir plusieurs blocs `impl`. Par exemple, la Liste 5-15 est équivalente au code montré dans la Liste 5-16, qui a chaque méthode dans son propre bloc `impl`.

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

Liste 5-16 : Reprise de la Liste 5-15 en utilisant plusieurs blocs `impl`

Il n'y a pas de raison de séparer ces méthodes en plusieurs blocs `impl` ici, mais c'est une syntaxe valide. Nous verrons un cas où plusieurs blocs `impl` sont utiles au Chapitre 10, où nous discuterons des types génériques et des traits.
