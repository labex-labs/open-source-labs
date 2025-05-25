# 제약 조건

제네릭을 사용할 때, 타입 매개변수는 종종 트레이트를 _제약 조건_ 으로 사용하여 특정 타입이 구현하는 기능을 명시해야 합니다. 예를 들어, 다음 예제는 `Display` 트레이트를 사용하여 출력하기 때문에 `T`가 `Display`로 제약되어야 합니다. 즉, `T`는 반드시 `Display`를 구현해야 합니다.

```rust
// `Display` 트레이트를 구현해야 하는 제네릭 타입 `T` 를 받는 함수 `printer` 를 정의합니다.
fn printer<T: Display>(t: T) {
    println!("{}", t);
}
```

제약 조건은 제네릭 타입이 제약 조건에 부합하는 타입으로 제한합니다. 즉:

```rust
struct S<T: Display>(T);

// 오류! `Vec<T>` 는 `Display` 를 구현하지 않습니다. 이 특수화는 실패합니다.
let s = S(vec![1]);
```

제약 조건의 또 다른 효과는 제네릭 인스턴스가 제약 조건에 명시된 트레이트의 [메서드](methods)에 접근할 수 있도록 허용한다는 것입니다. 예를 들어:

```rust
// 출력 마커 `{:?}` 를 구현하는 트레이트.
use std::fmt::Debug;

trait HasArea {
    fn area(&self) -> f64;
}

impl HasArea for Rectangle {
    fn area(&self) -> f64 { self.length * self.height }
}

#[derive(Debug)]
struct Rectangle { length: f64, height: f64 }
#[allow(dead_code)]
struct Triangle  { length: f64, height: f64 }

// 제네릭 `T` 는 `Debug` 를 구현해야 합니다. 타입에 관계없이 제대로 작동합니다.
fn print_debug<T: Debug>(t: &T) {
    println!("{:?}", t);
}

// `T` 는 `HasArea` 를 구현해야 합니다. 제약 조건을 충족하는 모든 타입은 `HasArea` 의 함수 `area` 에 접근할 수 있습니다.
fn area<T: HasArea>(t: &T) -> f64 { t.area() }

fn main() {
    let rectangle = Rectangle { length: 3.0, height: 4.0 };
    let _triangle = Triangle  { length: 3.0, height: 4.0 };

    print_debug(&rectangle);
    println!("Area: {}", area(&rectangle));

    //print_debug(&_triangle);
    //println!("Area: {}", area(&_triangle));
    // ^ TODO: 이 부분을 주석 해제해 보세요.
    // | 오류: `Debug` 또는 `HasArea` 를 구현하지 않습니다.
}
```

추가적으로, `where` 절을 사용하여 특정 경우에 제약 조건을 적용하여 더욱 명확하게 표현할 수 있습니다.
