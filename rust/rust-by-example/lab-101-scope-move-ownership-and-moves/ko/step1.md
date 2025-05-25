# 소유권과 이동 (moves)

변수는 자체 리소스를 해제하는 역할을 하므로, **리소스는 하나의 소유자만 가질 수 있습니다**. 이는 또한 리소스가 두 번 이상 해제되는 것을 방지합니다. 모든 변수가 리소스를 소유하는 것은 아닙니다 (예: \[참조 (references)]).

할당 (`let x = y`) 을 수행하거나 함수 인수를 값으로 전달 (`foo(x)`) 할 때 리소스의 *소유권*이 이전됩니다. Rust 에서는 이를 *이동 (move)*이라고 합니다.

리소스를 이동한 후에는 이전 소유자를 더 이상 사용할 수 없습니다. 이는 댕글링 포인터 (dangling pointer) 생성을 방지합니다.

```rust
// This function takes ownership of the heap allocated memory
fn destroy_box(c: Box<i32>) {
    println!("Destroying a box that contains {}", c);

    // `c` is destroyed and the memory freed
}

fn main() {
    // _Stack_ allocated integer
    let x = 5u32;

    // *Copy* `x` into `y` - no resources are moved
    let y = x;

    // Both values can be independently used
    println!("x is {}, and y is {}", x, y);

    // `a` is a pointer to a _heap_ allocated integer
    let a = Box::new(5i32);

    println!("a contains: {}", a);

    // *Move* `a` into `b`
    let b = a;
    // The pointer address of `a` is copied (not the data) into `b`.
    // Both are now pointers to the same heap allocated data, but
    // `b` now owns it.

    // Error! `a` can no longer access the data, because it no longer owns the
    // heap memory
    //println!("a contains: {}", a);
    // TODO ^ Try uncommenting this line

    // This function takes ownership of the heap allocated memory from `b`
    destroy_box(b);

    // Since the heap memory has been freed at this point, this action would
    // result in dereferencing freed memory, but it's forbidden by the compiler
    // Error! Same reason as the previous Error
    //println!("b contains: {}", b);
    // TODO ^ Try uncommenting this line
}
```
