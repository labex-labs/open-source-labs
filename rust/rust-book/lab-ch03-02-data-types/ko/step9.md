# 튜플 타입 (The Tuple Type)

*튜플*은 다양한 타입의 여러 값을 하나의 복합 타입으로 묶는 일반적인 방법입니다. 튜플은 고정된 길이를 가집니다: 선언되면 크기가 커지거나 줄어들 수 없습니다.

괄호 안에 쉼표로 구분된 값 목록을 작성하여 튜플을 생성합니다. 튜플의 각 위치에는 타입이 있으며, 튜플 내의 서로 다른 값의 타입이 동일할 필요는 없습니다. 이 예제에서는 선택적 타입 어노테이션 (type annotations) 을 추가했습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
}
```

변수 `tup`는 전체 튜플에 바인딩됩니다. 튜플은 단일 복합 요소로 간주되기 때문입니다. 튜플에서 개별 값을 가져오려면 패턴 매칭 (pattern matching) 을 사용하여 튜플 값을 분해 (destructure) 할 수 있습니다. 다음과 같습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let tup = (500, 6.4, 1);

    let (x, y, z) = tup;

    println!("The value of y is: {y}");
}
```

이 프로그램은 먼저 튜플을 생성하고 이를 변수 `tup`에 바인딩합니다. 그런 다음 `let`과 함께 패턴을 사용하여 `tup`을 가져와 세 개의 개별 변수 `x`, `y`, `z`로 변환합니다. 이것은 단일 튜플을 세 부분으로 나누기 때문에 *분해 (destructuring)*라고 합니다. 마지막으로, 프로그램은 `y`의 값인 `6.4`를 출력합니다.

마침표 (`.`) 다음에 접근하려는 값의 인덱스를 사용하여 튜플 요소를 직접 접근할 수도 있습니다. 예를 들어:

파일 이름: `src/main.rs`

```rust
fn main() {
    let x: (i32, f64, u8) = (500, 6.4, 1);

    let five_hundred = x.0;

    let six_point_four = x.1;

    let one = x.2;
}
```

이 프로그램은 튜플 `x`를 생성한 다음 각 요소의 인덱스를 사용하여 튜플의 각 요소에 접근합니다. 대부분의 프로그래밍 언어와 마찬가지로 튜플의 첫 번째 인덱스는 0 입니다.

값이 없는 튜플은 *유닛 (unit)*이라는 특별한 이름을 갖습니다. 이 값과 해당 타입은 모두 `()`로 작성되며 빈 값 또는 빈 반환 타입을 나타냅니다. 다른 값을 반환하지 않으면 표현식은 암시적으로 유닛 값을 반환합니다.
