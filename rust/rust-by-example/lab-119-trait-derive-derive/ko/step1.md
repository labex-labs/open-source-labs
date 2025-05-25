# Derive (파생)

컴파일러는 `#[derive]` 속성을 통해 일부 트레이트에 대한 기본적인 구현을 제공할 수 있습니다. 더 복잡한 동작이 필요한 경우 이러한 트레이트를 수동으로 구현할 수도 있습니다.

다음은 파생 가능한 트레이트 목록입니다.

- 비교 트레이트: `Eq`, `PartialEq`, `Ord`, `PartialOrd`.
- `Clone`, 복사를 통해 `&T`에서 `T`를 생성합니다.
- `Copy`, '이동 의미론 (move semantics)' 대신 '복사 의미론 (copy semantics)'을 타입에 부여합니다.
- `Hash`, `&T`에서 해시를 계산합니다.
- `Default`, 데이터 타입의 빈 인스턴스를 생성합니다.
- `Debug`, `{:?}` 포매터를 사용하여 값을 형식화합니다.

```rust
// `Centimeters`, 비교 가능한 튜플 구조체
#[derive(PartialEq, PartialOrd)]
struct Centimeters(f64);

// `Inches`, 출력 가능한 튜플 구조체
#[derive(Debug)]
struct Inches(i32);

impl Inches {
    fn to_centimeters(&self) -> Centimeters {
        let &Inches(inches) = self;

        Centimeters(inches as f64 * 2.54)
    }
}

// `Seconds`, 추가 속성이 없는 튜플 구조체
struct Seconds(i32);

fn main() {
    let _one_second = Seconds(1);

    // Error: `Seconds` 는 출력할 수 없습니다; `Debug` 트레이트를 구현하지 않았습니다.
    //println!("One second looks like: {:?}", _one_second);
    // TODO ^ Try uncommenting this line

    // Error: `Seconds` 는 비교할 수 없습니다; `PartialEq` 트레이트를 구현하지 않았습니다.
    //let _this_is_true = (_one_second == _one_second);
    // TODO ^ Try uncommenting this line

    let foot = Inches(12);

    println!("One foot equals {:?}", foot);

    let meter = Centimeters(100.0);

    let cmp =
        if foot.to_centimeters() < meter {
            "smaller"
        } else {
            "bigger"
        };

    println!("One foot is {} than one meter.", cmp);
}
```
