# 가변성 (Mutability)

가변 데이터는 `&mut T`를 사용하여 가변적으로 빌릴 수 있습니다. 이것을 _가변 참조 (mutable reference)_ 라고 하며, 빌린 사람에게 읽기/쓰기 접근 권한을 부여합니다. 반대로, `&T`는 불변 참조를 통해 데이터를 빌리며, 빌린 사람은 데이터를 읽을 수 있지만 수정할 수는 없습니다.

```rust
#[allow(dead_code)]
#[derive(Clone, Copy)]
struct Book {
    // `&'static str`은 읽기 전용 메모리에 할당된 문자열에 대한 참조입니다.
    author: &'static str,
    title: &'static str,
    year: u32,
}

// 이 함수는 책에 대한 참조를 받습니다.
fn borrow_book(book: &Book) {
    println!("I immutably borrowed {} - {} edition", book.title, book.year);
}

// 이 함수는 가변 책에 대한 참조를 받아 `year` 를 2014 로 변경합니다.
fn new_edition(book: &mut Book) {
    book.year = 2014;
    println!("I mutably borrowed {} - {} edition", book.title, book.year);
}

fn main() {
    // `immutabook` 이라는 불변 Book 을 생성합니다.
    let immutabook = Book {
        // 문자열 리터럴은 `&'static str` 타입을 가집니다.
        author: "Douglas Hofstadter",
        title: "Gödel, Escher, Bach",
        year: 1979,
    };

    // `immutabook` 의 가변 복사본을 생성하고 `mutabook` 이라고 부릅니다.
    let mut mutabook = immutabook;

    // 불변 객체를 불변적으로 빌립니다.
    borrow_book(&immutabook);

    // 가변 객체를 불변적으로 빌립니다.
    borrow_book(&mutabook);

    // 가변 객체를 가변적으로 빌립니다.
    new_edition(&mut mutabook);

    // 오류! 불변 객체를 가변적으로 빌릴 수 없습니다.
    new_edition(&mut immutabook);
    // FIXME ^ 이 줄을 주석 처리하세요.
}
```
