# Test des fonctions privées

Il existe un débat dans la communauté des tests sur le fait que les fonctions privées devraient ou non être testées directement, et d'autres langages rendent difficile voire impossible de tester les fonctions privées. Indépendamment de l'idéologie de test à laquelle vous adhérez, les règles de confidentialité de Rust vous permettent effectivement de tester les fonctions privées. Considérez le code de la Liste 11-12 avec la fonction privée `internal_adder`.

Nom de fichier : `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    internal_adder(a, 2)
}

fn internal_adder(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn internal() {
        assert_eq!(4, internal_adder(2, 2));
    }
}
```

Liste 11-12 : Test d'une fonction privée

Remarquez que la fonction `internal_adder` n'est pas marquée `pub`. Les tests sont simplement du code Rust, et le module `tests` n'est qu'un autre module. Comme nous l'avons discuté dans "Chemins pour faire référence à un élément dans l'arborescence de modules", les éléments dans les modules enfants peuvent utiliser les éléments de leurs modules ancêtres. Dans ce test, nous mettons tous les éléments du parent du module `test` dans la portée avec `use super::*`, et ensuite le test peut appeler `internal_adder`. Si vous ne pensez pas que les fonctions privées devraient être testées, rien en Rust ne vous forcera à le faire.
