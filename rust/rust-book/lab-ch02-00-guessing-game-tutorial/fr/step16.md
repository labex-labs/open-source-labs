# Quitter après avoir deviné correctement

Programmons le jeu pour qu'il quitte lorsque l'utilisateur gagne en ajoutant une instruction `break` :

Nom de fichier : `src/main.rs`

```rust
--snip--

match guess.cmp(&secret_number) {
    Ordering::Less => println!("Too small!"),
    Ordering::Greater => println!("Too big!"),
    Ordering::Equal => {
        println!("You win!");
        break;
    }
}
```

Ajouter la ligne `break` après `You win!` fait en sorte que le programme sorte de la boucle lorsque l'utilisateur devine correctement le nombre secret. Sortir de la boucle signifie également sortir du programme, car la boucle est la dernière partie de `main`.
