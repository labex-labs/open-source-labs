# Emprunt

La plupart du temps, nous souhaitons accéder aux données sans prendre la propriété d'elles. Pour y arriver, Rust utilise un mécanisme d'_emprunt_. Au lieu de passer les objets par valeur (`T`), les objets peuvent être passés par référence (`&T`).

Le compilateur garantit statiquement (via son vérificateur d'emprunt) que les références _pointent toujours_ vers des objets valides. C'est-à-dire que tant que des références à un objet existent, l'objet ne peut pas être détruit.

```rust
// Cette fonction prend la propriété d'un box et le détruit
fn eat_box_i32(boxed_i32: Box<i32>) {
    println!("Destroying box that contains {}", boxed_i32);
}

// Cette fonction emprunte un i32
fn borrow_i32(borrowed_i32: &i32) {
    println!("This int is: {}", borrowed_i32);
}

fn main() {
    // Crée un boxed i32 et un stacked i32
    let boxed_i32 = Box::new(5_i32);
    let stacked_i32 = 6_i32;

    // Emprunte le contenu du box. La propriété n'est pas prise,
    // donc le contenu peut être emprunté à nouveau.
    borrow_i32(&boxed_i32);
    borrow_i32(&stacked_i32);

    {
        // Prend une référence à la donnée contenue dans le box
        let _ref_to_i32: &i32 = &boxed_i32;

        // Erreur!
        // Ne peut pas détruire `boxed_i32` tandis que la valeur interne est empruntée plus tard dans la portée.
        eat_box_i32(boxed_i32);
        // FIXME ^ Commenter cette ligne

        // Tente d'emprunter `_ref_to_i32` après que la valeur interne a été détruite
        borrow_i32(_ref_to_i32);
        // `_ref_to_i32` sort de portée et n'est plus emprunté.
    }

    // `boxed_i32` peut maintenant céder la propriété à `eat_box` et être détruit
    eat_box_i32(boxed_i32);
}
```
