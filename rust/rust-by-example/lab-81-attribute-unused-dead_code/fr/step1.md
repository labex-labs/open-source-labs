# `dead_code`

Le compilateur fournit un avertissement (`lint`) `dead_code` qui signale les fonctions non utilisées. Un _attribut_ peut être utilisé pour désactiver cet avertissement.

```rust
fn used_function() {}

// `#[allow(dead_code)]` est un attribut qui désactive l'avertissement `dead_code`
#[allow(dead_code)]
fn unused_function() {}

fn noisy_unused_function() {}
// FIXME ^ Ajoutez un attribut pour supprimer l'avertissement

fn main() {
    used_function();
}
```

Notez que dans les programmes réels, vous devriez éliminer le code mort (dead code). Dans ces exemples, nous autorisons le code mort à certains endroits en raison de la nature interactive des exemples.
