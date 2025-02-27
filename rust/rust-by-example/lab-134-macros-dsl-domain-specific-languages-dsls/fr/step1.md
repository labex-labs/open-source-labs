# Domain Specific Languages (DSLs)

Un DSL est un mini "langage" intégré dans une macro Rust. C'est complètement du Rust valide car le système de macros se développe en constructions Rust normales, mais il ressemble à un petit langage. Cela vous permet de définir une syntaxe concise ou intuitive pour une certaine fonctionnalité spécifique (dans des limites).

Supposons que je veuille définir une petite API de calculatrice. Je voudrais fournir une expression et avoir la sortie imprimée dans la console.

```rust
macro_rules! calculate {
    (eval $e:expr) => {
        {
            let val: usize = $e; // Forcer les types à être des entiers
            println!("{} = {}", stringify!{$e}, val);
        }
    };
}

fn main() {
    calculate! {
        eval 1 + 2 // hehehe `eval` n'est _pas_ un mot clé Rust!
    }

    calculate! {
        eval (1 + 2) * (3 / 4)
    }
}
```

Sortie :

```txt
1 + 2 = 3
(1 + 2) * (3 / 4) = 0
```

C'était un exemple très simple.

Notez également les deux paires d'accolades dans la macro. Les accolades externes sont une partie de la syntaxe de `macro_rules!`, en plus de `()` ou `[]`.
