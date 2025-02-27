# 可変性

可変データは `&mut T` を使って可変的に借用できます。これは _可変参照_ と呼ばれ、借用者に読み書きアクセスを与えます。対照的に、`&T` は不変参照を通じてデータを借用し、借用者はデータを読むことはできますが、変更することはできません。

```rust
#[allow(dead_code)]
#[derive(Clone, Copy)]
struct Book {
    // `&'static str` は読み取り専用メモリに割り当てられた文字列への参照
    author: &'static str,
    title: &'static str,
    year: u32,
}

// この関数は本への参照を受け取ります
fn borrow_book(book: &Book) {
    println!("I immutably borrowed {} - {} edition", book.title, book.year);
}

// この関数は可変な本への参照を受け取り、`year` を 2014 に変更します
fn new_edition(book: &mut Book) {
    book.year = 2014;
    println!("I mutably borrowed {} - {} edition", book.title, book.year);
}

fn main() {
    // 不変の本 `immutabook` を作成します
    let immutabook = Book {
        // 文字列リテラルは `&'static str` 型を持ちます
        author: "Douglas Hofstadter",
        title: "Gödel, Escher, Bach",
        year: 1979,
    };

    // `immutabook` の可変コピーを作成し、`mutabook` と呼びます
    let mut mutabook = immutabook;

    // 不変オブジェクトを不変的に借用します
    borrow_book(&immutabook);

    // 可変オブジェクトを不変的に借用します
    borrow_book(&mutabook);

    // 可変オブジェクトを可変的に借用します
    new_edition(&mut mutabook);

    // エラー！不変オブジェクトを可変的に借用することはできません
    new_edition(&mut immutabook);
    // FIXME ^ この行をコメントアウトしてください
}
```
