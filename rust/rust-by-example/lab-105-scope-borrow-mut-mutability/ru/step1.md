# Изменяемость

Изменяемые данные можно взять в изменяемом долге с использованием `&mut T`. Это называется _изменяемой ссылкой_ и дает доступ на чтение и запись для заемщика. В отличие от этого, `&T` берет данные в неизменяемом долге, и заемщик может читать данные, но не модифицировать их:

```rust
#[allow(dead_code)]
#[derive(Clone, Copy)]
struct Book {
    // `&'static str` - это ссылка на строку, выделенную в памяти с атрибутом read only
    author: &'static str,
    title: &'static str,
    year: u32,
}

// Эта функция принимает ссылку на книгу
fn borrow_book(book: &Book) {
    println!("Я взял в неизменяемом долге {} - {} издание", book.title, book.year);
}

// Эта функция принимает ссылку на изменяемую книгу и изменяет `year` на 2014
fn new_edition(book: &mut Book) {
    book.year = 2014;
    println!("Я взял в изменяемом долге {} - {} издание", book.title, book.year);
}

fn main() {
    // Создаем неизменяемую книгу под названием `immutabook`
    let immutabook = Book {
        // литералы строк имеют тип `&'static str`
        author: "Douglas Hofstadter",
        title: "Gödel, Escher, Bach",
        year: 1979,
    };

    // Создаем изменяемую копию `immutabook` и называем ее `mutabook`
    let mut mutabook = immutabook;

    // Взять в неизменяемом долге неизменяемый объект
    borrow_book(&immutabook);

    // Взять в неизменяемом долге изменяемый объект
    borrow_book(&mutabook);

    // Взять изменяемый объект в изменяемом долге
    new_edition(&mut mutabook);

    // Ошибка! Нельзя брать неизменяемый объект в изменяемом долге
    new_edition(&mut immutabook);
    // FIXME ^ Закомментируйте эту строку
}
```
