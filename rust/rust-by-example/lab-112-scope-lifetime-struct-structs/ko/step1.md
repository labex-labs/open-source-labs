# 구조체 (Structs)

구조체에서 라이프타임 (Lifetimes) 의 주석 (Annotation) 도 함수와 유사합니다.

```rust
// `i32` 에 대한 참조를 담는 `Borrowed` 타입.
// `i32` 에 대한 참조는 `Borrowed` 보다 오래 지속되어야 합니다.
#[derive(Debug)]
struct Borrowed<'a>(&'a i32);

// 마찬가지로, 여기 있는 두 참조 모두 이 구조체보다 오래 지속되어야 합니다.
#[derive(Debug)]
struct NamedBorrowed<'a> {
    x: &'a i32,
    y: &'a i32,
}

// `i32` 이거나 이에 대한 참조인 열거형 (enum).
#[derive(Debug)]
enum Either<'a> {
    Num(i32),
    Ref(&'a i32),
}

fn main() {
    let x = 18;
    let y = 15;

    let single = Borrowed(&x);
    let double = NamedBorrowed { x: &x, y: &y };
    let reference = Either::Ref(&x);
    let number    = Either::Num(y);

    println!("x is borrowed in {:?}", single);
    println!("x and y are borrowed in {:?}", double);
    println!("x is borrowed in {:?}", reference);
    println!("y is *not* borrowed in {:?}", number);
}
```
