# macro_rules!

Rust fournit un puissant système de macros qui permet la métaprogrammation. Comme vous l'avez vu dans les chapitres précédents, les macros ressemblent à des fonctions, sauf que leur nom se termine par un bang `!`, mais au lieu de générer un appel de fonction, les macros sont étendues en code source qui est compilé avec le reste du programme. Cependant, contrairement aux macros en C et dans d'autres langages, les macros Rust sont étendues en arbres syntaxiques abstraits, plutôt qu'un prétraitement de chaînes, donc vous n'avez pas de bogues d'ordre de priorité inattendus.

Les macros sont créées à l'aide du macro `macro_rules!`.

```rust
// Ceci est une macro simple nommée `say_hello`.
macro_rules! say_hello {
    // `()` indique que la macro ne prend aucun argument.
    () => {
        // La macro sera étendue dans le contenu de ce bloc.
        println!("Hello!")
    };
}

fn main() {
    // Cette appel sera étendu en `println!("Hello")`
    say_hello!()
}
```

Alors pourquoi les macros sont-elles utiles?

1.  Ne pas répéter soi-même. Il y a de nombreux cas où vous pouvez avoir besoin d'une fonctionnalité similaire à plusieurs endroits, mais avec différents types. Souvent, écrire une macro est un moyen utile d'éviter de répéter le code. (Plus de détails plus tard)

2.  Langages spécifiques au domaine. Les macros vous permettent de définir une syntaxe spéciale à des fins spécifiques. (Plus de détails plus tard)

3.  Interfaces variadiques. Parfois, vous voulez définir une interface qui prend un nombre variable d'arguments. Un exemple est `println!` qui peut prendre un nombre quelconque d'arguments, selon la chaîne de formatage. (Plus de détails plus tard)
