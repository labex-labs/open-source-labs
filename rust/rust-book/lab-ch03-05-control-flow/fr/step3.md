# Gérer plusieurs conditions avec `else if`

Vous pouvez utiliser plusieurs conditions en combinant `if` et `else` dans une expression `else if`. Par exemple :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let number = 6;

    if number % 4 == 0 {
        println!("number est divisible par 4");
    } else if number % 3 == 0 {
        println!("number est divisible par 3");
    } else if number % 2 == 0 {
        println!("number est divisible par 2");
    } else {
        println!("number n'est pas divisible par 4, 3 ou 2");
    }
}
```

Ce programme peut suivre quatre chemins possibles. Après l'avoir exécuté, vous devriez voir la sortie suivante :

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projets/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
number est divisible par 3
```

Lorsque ce programme s'exécute, il vérifie chaque expression `if` tour à tour et exécute le premier corps pour lequel la condition est évaluée à `vraie`. Notez que bien que 6 soit divisible par 2, nous ne voyons pas la sortie `number est divisible par 2`, ni le texte `number n'est pas divisible par 4, 3 ou 2` du bloc `else`. C'est parce que Rust n'exécute le bloc que pour la première condition `vraie`, et une fois qu'il l'a trouvée, il ne vérifie même pas le reste.

L'utilisation de trop nombreuses expressions `else if` peut alourdir votre code, donc si vous en avez plus d'une, vous pouvez vouloir refactoriser votre code. Le chapitre 6 décrit une structure de branchement puissante en Rust appelée `match` pour ces cas.
