# 함수 매개변수

함수 매개변수도 패턴이 될 수 있습니다. Listing 18-6 의 코드는 `i32` 타입의 `x`라는 매개변수 하나를 받는 `foo`라는 함수를 선언하며, 이제 익숙해 보일 것입니다.

```rust
fn foo(x: i32) {
    // code goes here
}
```

Listing 18-6: 매개변수에서 패턴을 사용하는 함수 시그니처

`x` 부분은 패턴입니다! `let`과 마찬가지로, 함수의 인수에 있는 튜플을 패턴과 일치시킬 수 있습니다. Listing 18-7 은 튜플을 함수에 전달할 때 튜플의 값을 분할합니다.

파일 이름: `src/main.rs`

```rust
fn print_coordinates(&(x, y): &(i32, i32)) {
    println!("Current location: ({x}, {y})");
}

fn main() {
    let point = (3, 5);
    print_coordinates(&point);
}
```

Listing 18-7: 튜플을 destructure 하는 매개변수가 있는 함수

이 코드는 `Current location: (3, 5)`를 출력합니다. 값 `&(3, 5)`는 패턴 `&(x, y)`와 일치하므로 `x`는 값 `3`이고 `y`는 값 `5`입니다.

13 장에서 논의했듯이 클로저는 함수와 유사하므로 함수 매개변수 목록과 동일한 방식으로 클로저 매개변수 목록에서도 패턴을 사용할 수 있습니다.

지금까지 패턴을 사용하는 몇 가지 방법을 살펴보았지만, 패턴은 사용할 수 있는 모든 곳에서 동일하게 작동하지 않습니다. 어떤 곳에서는 패턴이 irrefutable(부정할 수 없는) 해야 하고, 다른 상황에서는 refutable(부정할 수 있는) 할 수 있습니다. 다음에서 이 두 가지 개념에 대해 논의하겠습니다.
