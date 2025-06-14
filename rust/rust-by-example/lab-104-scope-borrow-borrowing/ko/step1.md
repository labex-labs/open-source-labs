# 차용 (Borrowing)

대부분의 경우, 소유권을 가져가지 않고 데이터에 접근하고 싶을 것입니다. 이를 위해 Rust 는 _차용 (borrowing)_ 메커니즘을 사용합니다. 값으로 객체를 전달하는 대신 (`T`), 객체는 참조로 전달될 수 있습니다 (`&T`).

컴파일러는 정적으로 (차용 검사기 (borrow checker) 를 통해) 참조가 _항상_ 유효한 객체를 가리키도록 보장합니다. 즉, 객체에 대한 참조가 존재하는 동안에는 객체를 파괴할 수 없습니다.

```rust
// This function takes ownership of a box and destroys it
fn eat_box_i32(boxed_i32: Box<i32>) {
    println!("Destroying box that contains {}", boxed_i32);
}

// This function borrows an i32
fn borrow_i32(borrowed_i32: &i32) {
    println!("This int is: {}", borrowed_i32);
}

fn main() {
    // Create a boxed i32, and a stacked i32
    let boxed_i32 = Box::new(5_i32);
    let stacked_i32 = 6_i32;

    // Borrow the contents of the box. Ownership is not taken,
    // so the contents can be borrowed again.
    borrow_i32(&boxed_i32);
    borrow_i32(&stacked_i32);

    {
        // Take a reference to the data contained inside the box
        let _ref_to_i32: &i32 = &boxed_i32;

        // Error!
        // Can't destroy `boxed_i32` while the inner value is borrowed later in scope.
        eat_box_i32(boxed_i32);
        // FIXME ^ Comment out this line

        // Attempt to borrow `_ref_to_i32` after inner value is destroyed
        borrow_i32(_ref_to_i32);
        // `_ref_to_i32` goes out of scope and is no longer borrowed.
    }

    // `boxed_i32` can now give up ownership to `eat_box` and be destroyed
    eat_box_i32(boxed_i32);
}
```
