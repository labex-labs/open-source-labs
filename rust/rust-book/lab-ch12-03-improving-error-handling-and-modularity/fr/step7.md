# Improving the Error Message

Dans le Listing 12-8, nous ajoutons une vérification dans la fonction `new` qui vérifiera que la tranche est suffisamment longue avant d'accéder à l'index 1 et index 2. Si la tranche n'est pas suffisamment longue, le programme génère une panique et affiche un message d'erreur meilleur.

Nom du fichier : `src/main.rs`

```rust
--snip--
fn new(args: &[String]) -> Config {
    if args.len() < 3 {
        panic!("not enough arguments");
    }
    --snip--
```

Listing 12-8 : Ajout d'une vérification pour le nombre d'arguments

Ce code est similaire à la fonction `Guess::new` que nous avons écrite dans le Listing 9-13, où nous appelions `panic!` lorsque l'argument `value` était en dehors de la plage de valeurs valides. Au lieu de vérifier une plage de valeurs ici, nous vérifions que la longueur de `args` est au moins `3` et le reste de la fonction peut fonctionner en supposant que cette condition est remplie. Si `args` a moins de trois éléments, cette condition sera `true`, et nous appelons la macro `panic!` pour terminer immédiatement le programme.

Avec ces quelques lignes de code supplémentaires dans `new`, exécutons le programme sans arguments à nouveau pour voir à quoi ressemble l'erreur maintenant :

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep`
thread'main' panicked at 'not enough arguments',
src/main.rs:26:13
note: run with `RUST_BACKTRACE=1` environment variable to display
a backtrace
```

Cette sortie est meilleure : nous avons maintenant un message d'erreur raisonnable. Cependant, nous avons également des informations superflues que nous ne voulons pas donner à nos utilisateurs. Peut-être que la technique que nous avons utilisée dans le Listing 9-13 n'est pas la meilleure à utiliser ici : un appel à `panic!` est plus approprié pour un problème de programmation qu'un problème d'utilisation, comme discuté au chapitre 9. Au lieu de cela, nous utiliserons l'autre technique que vous avez apprise au chapitre 9 --- renvoyer un `Result` qui indique soit un succès soit une erreur.
