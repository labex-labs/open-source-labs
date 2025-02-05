# 可变性

可变数据可以使用 `&mut T` 进行可变借用。这被称为**可变引用**，它为借用者提供读/写访问权限。相比之下，`&T` 通过不可变引用借用数据，借用者可以读取数据但不能修改它：

```rust
#[allow(dead_code)]
#[derive(Clone, Copy)]
struct Book {
    // `&'static str` 是对分配在只读内存中的字符串的引用
    author: &'static str,
    title: &'static str,
    year: u32,
}

// 此函数接受对一本书的引用
fn borrow_book(book: &Book) {
    println!("我不可变地借用了 {} - {} 版", book.title, book.year);
}

// 此函数接受对可变书籍的引用，并将 `year` 更改为 2014
fn new_edition(book: &mut Book) {
    book.year = 2014;
    println!("我可变地借用了 {} - {} 版", book.title, book.year);
}

fn main() {
    // 创建一个名为 `immutabook` 的不可变 Book
    let immutabook = Book {
        // 字符串字面量的类型为 `&'static str`
        author: "Douglas Hofstadter",
        title: "Gödel, Escher, Bach",
        year: 1979,
    };

    // 创建 `immutabook` 的可变副本并将其称为 `mutabook`
    let mut mutabook = immutabook;

    // 不可变地借用一个不可变对象
    borrow_book(&immutabook);

    // 不可变地借用一个可变对象
    borrow_book(&mutabook);

    // 可变地借用一个可变对象
    new_edition(&mut mutabook);

    // 错误！不能将不可变对象作为可变对象借用
    new_edition(&mut immutabook);
    // FIXME ^ 注释掉这一行
}
```
