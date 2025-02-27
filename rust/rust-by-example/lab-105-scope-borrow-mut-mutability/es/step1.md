# Mutabilidad

Los datos mutables pueden ser prestados mutablesmente usando `&mut T`. Esto se llama una _referencia mutable_ y otorga acceso de lectura/escritura al prestatario. En contraste, `&T` presta los datos a través de una referencia inmutable, y el prestatario puede leer los datos pero no modificarlos:

```rust
#[allow(dead_code)]
#[derive(Clone, Copy)]
struct Book {
    // `&'static str` es una referencia a una cadena almacenada en memoria de solo lectura
    author: &'static str,
    title: &'static str,
    year: u32,
}

// Esta función toma una referencia a un libro
fn borrow_book(book: &Book) {
    println!("I immutably borrowed {} - {} edition", book.title, book.year);
}

// Esta función toma una referencia a un libro mutable y cambia `year` a 2014
fn new_edition(book: &mut Book) {
    book.year = 2014;
    println!("I mutably borrowed {} - {} edition", book.title, book.year);
}

fn main() {
    // Crea un libro inmutable llamado `immutabook`
    let immutabook = Book {
        // los literales de cadena tienen el tipo `&'static str`
        author: "Douglas Hofstadter",
        title: "Gödel, Escher, Bach",
        year: 1979,
    };

    // Crea una copia mutable de `immutabook` y llámala `mutabook`
    let mut mutabook = immutabook;

    // Presta inmutablemente un objeto inmutable
    borrow_book(&immutabook);

    // Presta inmutablemente un objeto mutable
    borrow_book(&mutabook);

    // Presta un objeto mutable como mutable
    new_edition(&mut mutabook);

    // Error! No se puede prestar un objeto inmutable como mutable
    new_edition(&mut immutabook);
    // FIXME ^ Comenta esta línea
}
```
