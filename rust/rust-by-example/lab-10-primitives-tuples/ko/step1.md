# 튜플 (Tuples)

튜플은 서로 다른 타입의 값들을 묶어 놓은 컬렉션입니다. 튜플은 괄호 `()`를 사용하여 생성되며, 각 튜플 자체는 타입 시그니처 (type signature) `(T1, T2, ...)`를 갖는 값입니다. 여기서 `T1`, `T2`는 멤버들의 타입입니다. 함수는 튜플을 사용하여 여러 값을 반환할 수 있는데, 튜플은 임의의 수의 값을 담을 수 있기 때문입니다.

```rust
// 튜플은 함수 인자 (argument) 및 반환 값으로 사용될 수 있습니다.
fn reverse(pair: (i32, bool)) -> (bool, i32) {
    // `let` 은 튜플의 멤버들을 변수에 바인딩 (bind) 하는 데 사용될 수 있습니다.
    let (int_param, bool_param) = pair;

    (bool_param, int_param)
}

// 다음 구조체는 활동을 위한 것입니다.
#[derive(Debug)]
struct Matrix(f32, f32, f32, f32);

fn main() {
    // 다양한 타입들을 가진 튜플.
    let long_tuple = (1u8, 2u16, 3u32, 4u64,
                      -1i8, -2i16, -3i32, -4i64,
                      0.1f32, 0.2f64,
                      'a', true);

    // 튜플 인덱싱 (tuple indexing) 을 사용하여 튜플에서 값을 추출할 수 있습니다.
    println!("Long tuple first value: {}", long_tuple.0);
    println!("Long tuple second value: {}", long_tuple.1);

    // 튜플은 튜플 멤버가 될 수 있습니다.
    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // 튜플은 출력 가능합니다.
    println!("tuple of tuples: {:?}", tuple_of_tuples);

    // 하지만 긴 튜플 (12 개 이상의 요소) 은 출력할 수 없습니다.
    //let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);
    //println!("Too long tuple: {:?}", too_long_tuple);
    // TODO ^ 컴파일러 오류를 보려면 위의 2 줄의 주석을 해제하세요.

    let pair = (1, true);
    println!("Pair is {:?}", pair);

    println!("The reversed pair is {:?}", reverse(pair));

    // 단일 요소 튜플을 생성하려면 쉼표가 필요하며, 괄호로 묶인 리터럴과 구별합니다.
    println!("One element tuple: {:?}", (5u32,));
    println!("Just an integer: {:?}", (5u32));

    // 튜플은 바인딩 (binding) 을 생성하기 위해 분해 (destructure) 될 수 있습니다.
    let tuple = (1, "hello", 4.5, true);

    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("{:?}", matrix);
}
```

## 활동

1.  _복습_: 위의 예제에서 `Matrix` 구조체에 `fmt::Display` 트레이트 (trait) 를 추가하여 디버그 형식 `{:?}`에서 표시 형식 `{}`으로 전환하면 다음과 같은 출력이 나타나도록 합니다.

    ```plaintext
    ( 1.1 1.2 )
    ( 2.1 2.2 )
    ```

    출력 표시 예제를 다시 참조할 수 있습니다.

2.  `reverse` 함수를 템플릿으로 사용하여 `transpose` 함수를 추가합니다. 이 함수는 매트릭스를 인자로 받아 두 요소를 교환한 매트릭스를 반환합니다. 예를 들어:

    ```rust
    println!("Matrix:\n{}", matrix);
    println!("Transpose:\n{}", transpose(matrix));
    ```

    결과는 다음과 같습니다.

    ```plaintext
    Matrix:
    ( 1.1 1.2 )
    ( 2.1 2.2 )
    Transpose:
    ( 1.1 2.1 )
    ( 1.2 2.2 )
    ```
