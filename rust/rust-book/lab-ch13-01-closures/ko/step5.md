# 클로저에서 캡처된 값 이동 및 Fn 트레이트

클로저가 클로저가 정의된 환경에서 참조를 캡처하거나 값의 소유권을 캡처한 후 (따라서 클로저 _안으로_ 이동하는 모든 것에 영향을 미침), 클로저 본문의 코드는 클로저가 나중에 평가될 때 참조 또는 값에 어떤 일이 발생하는지 정의합니다 (따라서 클로저 _밖으로_ 이동하는 모든 것에 영향을 미침).

클로저 본문은 다음 중 하나를 수행할 수 있습니다. 캡처된 값을 클로저 밖으로 이동, 캡처된 값을 변경, 값을 이동하거나 변경하지 않음, 또는 처음부터 환경에서 아무것도 캡처하지 않음.

클로저가 환경에서 값을 캡처하고 처리하는 방식은 클로저가 구현하는 트레이트에 영향을 미치며, 트레이트는 함수와 구조체가 사용할 수 있는 클로저의 종류를 지정할 수 있는 방법입니다. 클로저는 클로저의 본문이 값을 처리하는 방식에 따라 이러한 `Fn` 트레이트 중 하나, 두 개 또는 세 개 모두를 부가적인 방식으로 자동으로 구현합니다.

- `FnOnce`는 한 번 호출할 수 있는 클로저에 적용됩니다. 모든 클로저는 최소한 이 트레이트를 구현합니다. 왜냐하면 모든 클로저를 호출할 수 있기 때문입니다. 본문에서 캡처된 값을 이동하는 클로저는 다른 `Fn` 트레이트가 아닌 `FnOnce`만 구현합니다. 왜냐하면 한 번만 호출할 수 있기 때문입니다.
- `FnMut`는 본문에서 캡처된 값을 이동하지 않지만 캡처된 값을 변경할 수 있는 클로저에 적용됩니다. 이러한 클로저는 두 번 이상 호출할 수 있습니다.
- `Fn`은 본문에서 캡처된 값을 이동하지 않고 캡처된 값을 변경하지 않으며, 환경에서 아무것도 캡처하지 않는 클로저에 적용됩니다. 이러한 클로저는 환경을 변경하지 않고 두 번 이상 호출할 수 있으며, 이는 클로저를 여러 번 동시에 호출하는 경우와 같은 경우에 중요합니다.

Listing 13-1 에서 사용한 `Option<T>`의 `unwrap_or_else` 메서드의 정의를 살펴보겠습니다.

```rust
impl<T> Option<T> {
    pub fn unwrap_or_else<F>(self, f: F) -> T
    where
        F: FnOnce() -> T
    {
        match self {
            Some(x) => x,
            None => f(),
        }
    }
}
```

`T`는 `Option`의 `Some` 변형에 있는 값의 타입을 나타내는 제네릭 타입임을 기억하십시오. 해당 타입 `T`는 또한 `unwrap_or_else` 함수의 반환 타입입니다. 예를 들어, `Option<String>`에서 `unwrap_or_else`를 호출하는 코드는 `String`을 얻게 됩니다.

다음으로, `unwrap_or_else` 함수에는 추가적인 제네릭 타입 매개변수 `F`가 있습니다. `F` 타입은 `f`라는 매개변수의 타입이며, 이는 `unwrap_or_else`를 호출할 때 제공하는 클로저입니다.

제네릭 타입 `F`에 지정된 트레이트 바운드는 `FnOnce() -> T`이며, 이는 `F`가 한 번 호출할 수 있고, 인수를 받지 않으며, `T`를 반환할 수 있어야 함을 의미합니다. 트레이트 바운드에서 `FnOnce`를 사용하면 `unwrap_or_else`가 `f`를 최대 한 번만 호출한다는 제약 조건을 표현합니다. `unwrap_or_else`의 본문에서 `Option`이 `Some`인 경우 `f`가 호출되지 않는다는 것을 알 수 있습니다. `Option`이 `None`인 경우 `f`가 한 번 호출됩니다. 모든 클로저가 `FnOnce`를 구현하므로 `unwrap_or_else`는 가장 다양한 클로저를 허용하며 최대한 유연합니다.

> 참고: 함수도 세 가지 `Fn` 트레이트 모두를 구현할 수 있습니다. 우리가 하려는 작업이 환경에서 값을 캡처할 필요가 없는 경우, `Fn` 트레이트 중 하나를 구현하는 것이 필요한 곳에서 클로저 대신 함수의 이름을 사용할 수 있습니다. 예를 들어, `Option<Vec<T>>` 값에서 `unwrap_or_else(Vec::new)`를 호출하여 값이 `None`인 경우 새 빈 벡터를 얻을 수 있습니다.

이제 슬라이스에 정의된 표준 라이브러리 메서드 `sort_by_key`를 살펴보고 `unwrap_or_else`와 어떻게 다른지, 그리고 `sort_by_key`가 트레이트 바운드에 대해 `FnOnce` 대신 `FnMut`를 사용하는 이유를 살펴보겠습니다. 클로저는 고려 중인 슬라이스의 현재 항목에 대한 참조 형태의 인수를 하나 받아서 정렬할 수 있는 타입 `K`의 값을 반환합니다. 이 함수는 각 항목의 특정 속성으로 슬라이스를 정렬하려는 경우에 유용합니다. Listing 13-7 에서 `Rectangle` 인스턴스 목록이 있으며 `sort_by_key`를 사용하여 `width` 속성별로 낮은 값에서 높은 값으로 정렬합니다.

파일 이름: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    list.sort_by_key(|r| r.width);
    println!("{:#?}", list);
}
```

Listing 13-7: `sort_by_key`를 사용하여 너비별로 사각형 정렬

이 코드는 다음을 출력합니다.

    [
        Rectangle {
            width: 3,
            height: 5,
        },
        Rectangle {
            width: 7,
            height: 12,
        },
        Rectangle {
            width: 10,
            height: 1,
        },
    ]

`sort_by_key`가 `FnMut` 클로저를 사용하도록 정의된 이유는 슬라이스의 각 항목에 대해 한 번씩 클로저를 여러 번 호출하기 때문입니다. 클로저 `|r| r.width`는 환경에서 아무것도 캡처, 변경 또는 이동하지 않으므로 트레이트 바운드 요구 사항을 충족합니다.

반대로, Listing 13-8 은 환경에서 값을 이동하기 때문에 `FnOnce` 트레이트만 구현하는 클로저의 예제를 보여줍니다. 컴파일러는 이 클로저를 `sort_by_key`와 함께 사용하도록 허용하지 않습니다.

파일 이름: `src/main.rs`

```rust
--snip--

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    let mut sort_operations = vec![];
    let value = String::from("by key called");

    list.sort_by_key(|r| {
        sort_operations.push(value);
        r.width
    });
    println!("{:#?}", list);
}
```

Listing 13-8: `sort_by_key`와 함께 `FnOnce` 클로저를 사용하려는 시도

이것은 `list`를 정렬할 때 `sort_by_key`가 호출되는 횟수를 (작동하지 않는) 억지로 세는, 엉성하고 복잡한 방법입니다. 이 코드는 클로저의 환경에서 `String`인 `value`를 `sort_operations` 벡터로 푸시하여 이 카운팅을 시도합니다. 클로저는 `value`를 캡처한 다음 `value`의 소유권을 `sort_operations` 벡터로 전송하여 `value`를 클로저 밖으로 이동합니다. 이 클로저는 한 번 호출할 수 있습니다. 두 번째로 호출하려고 하면 `value`가 다시 `sort_operations`에 푸시될 환경에 더 이상 없기 때문에 작동하지 않습니다! 따라서 이 클로저는 `FnOnce`만 구현합니다. 이 코드를 컴파일하려고 하면 클로저가 `FnMut`를 구현해야 하므로 `value`를 클로저 밖으로 이동할 수 없다는 오류가 발생합니다.

```bash
error[E0507]: cannot move out of `value`, a captured variable in an `FnMut`
closure
  --> src/main.rs:18:30
   |
15 |       let value = String::from("by key called");
   |           ----- captured outer variable
16 |
17 |       list.sort_by_key(|r| {
   |  ______________________-
18 | |         sort_operations.push(value);
   | |                              ^^^^^ move occurs because `value` has
type `String`, which does not implement the `Copy` trait
19 | |         r.width
20 | |     });
   | |_____- captured by this `FnMut` closure
```

오류는 클로저 본문에서 `value`를 환경 밖으로 이동하는 줄을 가리킵니다. 이 문제를 해결하려면 환경에서 값을 이동하지 않도록 클로저 본문을 변경해야 합니다. 환경에서 카운터를 유지하고 클로저 본문에서 해당 값을 증가시키는 것이 `sort_by_key`가 호출되는 횟수를 세는 더 간단한 방법입니다. Listing 13-9 의 클로저는 `sort_by_key`와 함께 작동합니다. 왜냐하면 `num_sort_operations` 카운터에 대한 가변 참조만 캡처하고 두 번 이상 호출할 수 있기 때문입니다.

파일 이름: `src/main.rs`

```rust
--snip--

fn main() {
    --snip--

    let mut num_sort_operations = 0;
    list.sort_by_key(|r| {
        num_sort_operations += 1;
        r.width
    });
    println!(
        "{:#?}, sorted in {num_sort_operations} operations",
        list
    );
}
```

Listing 13-9: `sort_by_key`와 함께 `FnMut` 클로저를 사용하는 것이 허용됩니다.

`Fn` 트레이트는 클로저를 사용하는 함수 또는 타입을 정의하거나 사용할 때 중요합니다. 다음 섹션에서는 반복자에 대해 논의합니다. 많은 반복자 메서드는 클로저 인수를 사용하므로 계속 진행하면서 이러한 클로저 세부 정보를 염두에 두십시오!
