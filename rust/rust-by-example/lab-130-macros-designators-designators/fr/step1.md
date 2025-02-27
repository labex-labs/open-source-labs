# Désignateurs

Les arguments d'une macro sont préfixés par un signe dollar `$` et annotés avec un _désignateur_ :

```rust
macro_rules! create_function {
    // Cette macro prend un argument de désignateur `ident` et
    // crée une fonction nommée `$func_name`.
    // Le désignateur `ident` est utilisé pour les noms de variables / fonctions.
    ($func_name:ident) => {
        fn $func_name() {
            // La macro `stringify!` convertit un `ident` en chaîne de caractères.
            println!("You called {:?}()",
                     stringify!($func_name));
        }
    };
}

// Crée des fonctions nommées `foo` et `bar` avec la macro ci-dessus.
create_function!(foo);
create_function!(bar);

macro_rules! print_result {
    // Cette macro prend une expression de type `expr` et l'affiche
    // sous forme de chaîne de caractères avec son résultat.
    // Le désignateur `expr` est utilisé pour les expressions.
    ($expression:expr) => {
        // `stringify!` convertira l'expression *telle quelle* en chaîne de caractères.
        println!("{:?} = {:?}",
                 stringify!($expression),
                 $expression);
    };
}

fn main() {
    foo();
    bar();

    print_result!(1u32 + 1);

    // Rappelez-vous que les blocs sont également des expressions!
    print_result!({
        let x = 1u32;

        x * x + 2 * x - 1
    });
}
```

Voici quelques-uns des désignateurs disponibles :

- `block`
- `expr` est utilisé pour les expressions
- `ident` est utilisé pour les noms de variables / fonctions
- `item`
- `literal` est utilisé pour les constantes littérales
- `pat` (_motif_)
- `path`
- `stmt` (_instruction_)
- `tt` (_arbre de jetons_)
- `ty` (_type_)
- `vis` (_qualificateur de visibilité_)

Pour obtenir une liste complète, consultez la \[Rust Reference\].
