# `abort` et `unwind`

La section précédente illustre le mécanisme de gestion d'erreurs `panic`. Différents chemins de code peuvent être compilés conditionnellement en fonction du paramètre de panique. Les valeurs disponibles actuellement sont `unwind` et `abort`.

En partant de l'exemple de limonade précédent, nous utilisons explicitement la stratégie de panique pour tester différentes parties de code.

```rust
fn drink(beverage: &str) {
   // Vous ne devriez pas boire trop de boissons sucrées.
    if beverage == "lemonade" {
        if cfg!(panic="abort"){ println!("This is not your party. Run!!!!");}
        else{ println!("Spit it out!!!!");}
    }
    else{ println!("Some refreshing {} is all I need.", beverage); }
}

fn main() {
    drink("water");
    drink("lemonade");
}
```

Voici un autre exemple qui se concentre sur la réécriture de `drink()` et utilise explicitement le mot clé `unwind`.

```rust
#[cfg(panic = "unwind")]
fn ah(){ println!("Spit it out!!!!");}

#[cfg(not(panic="unwind"))]
fn ah(){ println!("This is not your party. Run!!!!");}

fn drink(beverage: &str){
    if beverage == "lemonade"{ ah();}
    else{println!("Some refreshing {} is all I need.", beverage);}
}

fn main() {
    drink("water");
    drink("lemonade");
}
```

La stratégie de panique peut être définie à partir de la ligne de commande en utilisant `abort` ou `unwind`.

```console
rustc lemonade.rs -C panic=abort
```
