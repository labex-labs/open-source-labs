# Option`<T>`을 사용한 매칭

이전 섹션에서 `Option<T>`를 사용할 때 `Some` 케이스에서 내부 `T` 값을 얻고 싶었습니다. `Coin` enum 에서 했던 것처럼 `match`를 사용하여 `Option<T>`를 처리할 수도 있습니다! 동전을 비교하는 대신 `Option<T>`의 변형을 비교하지만 `match` 표현식이 작동하는 방식은 동일하게 유지됩니다.

`Option<i32>`를 받아 내부에 값이 있으면 해당 값에 1 을 더하는 함수를 작성한다고 가정해 보겠습니다. 내부에 값이 없으면 함수는 `None` 값을 반환하고 어떠한 연산도 시도하지 않아야 합니다.

이 함수는 `match` 덕분에 작성하기 매우 쉬우며 Listing 6-5 와 같습니다.

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
      1 None => None,
      2 Some(i) => Some(i + 1),
    }
}

let five = Some(5);
let six = plus_one(five); 3
let none = plus_one(None); 4
```

Listing 6-5: `Option<i32>`에 `match` 표현식을 사용하는 함수

`plus_one`의 첫 번째 실행을 자세히 살펴보겠습니다. `plus_one(five)` \[3]를 호출하면 `plus_one` 본문의 변수 `x`는 값 `Some(5)`를 갖습니다. 그런 다음 각 match arm 과 비교합니다.

```rust
None => None,
```

`Some(5)` 값은 패턴 `None` \[1]과 일치하지 않으므로 다음 arm 으로 계속 진행합니다.

```rust
Some(i) => Some(i + 1),
```

`Some(5)`가 `Some(i)` \[2]와 일치합니까? 네, 그렇습니다! 동일한 변형이 있습니다. `i`는 `Some`에 포함된 값에 바인딩되므로 `i`는 값 `5`를 갖습니다. 그런 다음 match arm 의 코드가 실행되므로 `i`의 값에 1 을 더하고 총 `6`이 내부에 있는 새로운 `Some` 값을 생성합니다.

이제 Listing 6-5 에서 `x`가 `None` \[4]인 `plus_one`의 두 번째 호출을 고려해 보겠습니다. `match`에 들어가 첫 번째 arm \[1]과 비교합니다.

일치합니다! 더할 값이 없으므로 프로그램이 중지되고 `=>`의 오른쪽에 있는 `None` 값을 반환합니다. 첫 번째 arm 이 일치했으므로 다른 arm 은 비교되지 않습니다.

`match`와 enum 을 결합하는 것은 많은 상황에서 유용합니다. Rust 코드에서 이 패턴을 많이 보게 될 것입니다. enum 에 대해 `match`를 수행하고, 변수를 내부에 있는 데이터에 바인딩한 다음, 이를 기반으로 코드를 실행합니다. 처음에는 약간 까다롭지만 익숙해지면 모든 언어에서 이 기능을 사용하고 싶을 것입니다. 이는 일관되게 사용자가 가장 좋아하는 기능입니다.
