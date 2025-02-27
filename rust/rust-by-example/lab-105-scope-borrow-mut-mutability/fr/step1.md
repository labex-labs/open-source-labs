# Mutabilité

Les données mutables peuvent être empruntées de manière mutable en utilisant `&mut T`. Cela s'appelle une _référence mutable_ et donne un accès lecture/écriture au preneur. En revanche, `&T` emprunte les données via une référence immuable, et le preneur peut lire les données mais ne peut pas les modifier :

```rust
#[allow(dead_code)]
#[derive(Clone, Copy)]
struct Book {
    // `&'static str` est une référence à une chaîne de caractères allouée en mémoire en lecture seule
    author: &'static str,
    title: &'static str,
    year: u32,
}

// Cette fonction prend une référence à un livre
fn borrow_book(book: &Book) {
    println!("J'ai emprunté immuablement {} - édition {}", book.title, book.year);
}

// Cette fonction prend une référence à un livre mutable et change `year` en 2014
fn new_edition(book: &mut Book) {
    book.year = 2014;
    println!("J'ai emprunté mutuellement {} - édition {}", book.title, book.year);
}

fn main() {
    // Crée un livre immuable nommé `immutabook`
    let immutabook = Book {
        // Les littéraux de chaîne ont le type `&'static str`
        author: "Douglas Hofstadter",
        title: "Gödel, Escher, Bach",
        year: 1979,
    };

    // Crée une copie mutable de `immutabook` et l'appelle `mutabook`
    let mut mutabook = immutabook;

    // Emprunte immuablement un objet immuable
    borrow_book(&immutabook);

    // Emprunte immuablement un objet mutable
    borrow_book(&mutabook);

    // Emprunte un objet mutable en tant que mutable
    new_edition(&mut mutabook);

    // Erreur! Impossible d'emprunter un objet immuable en tant que mutable
    new_edition(&mut immutabook);
    // FIXME ^ Commenter cette ligne
}
```
