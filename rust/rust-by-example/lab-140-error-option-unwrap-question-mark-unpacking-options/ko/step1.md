# `?`를 사용하여 옵션 언패킹하기

`match` 문을 사용하여 `Option`을 언패킹할 수 있지만, `?` 연산자를 사용하는 것이 더 쉬운 경우가 많습니다. `x`가 `Option`인 경우, `x?`를 평가하면 `x`가 `Some`인 경우 기본 값을 반환하고, 그렇지 않으면 실행 중인 모든 함수를 종료하고 `None`을 반환합니다.

```rust
fn next_birthday(current_age: Option<u8>) -> Option<String> {
    // If `current_age` is `None`, this returns `None`.
    // If `current_age` is `Some`, the inner `u8` gets assigned to `next_age`
    let next_age: u8 = current_age? + 1;
    Some(format!("Next year I will be {}", next_age))
}
```

코드를 훨씬 더 읽기 쉽게 만들기 위해 여러 개의 `?`를 함께 연결할 수 있습니다.

```rust
struct Person {
    job: Option<Job>,
}

#[derive(Clone, Copy)]
struct Job {
    phone_number: Option<PhoneNumber>,
}

#[derive(Clone, Copy)]
struct PhoneNumber {
    area_code: Option<u8>,
    number: u32,
}

impl Person {

    // Gets the area code of the phone number of the person's job, if it exists.
    fn work_phone_area_code(&self) -> Option<u8> {
        // This would need many nested `match` statements without the `?` operator.
        // It would take a lot more code - try writing it yourself and see which
        // is easier.
        self.job?.phone_number?.area_code
    }
}

fn main() {
    let p = Person {
        job: Some(Job {
            phone_number: Some(PhoneNumber {
                area_code: Some(61),
                number: 439222222,
            }),
        }),
    };

    assert_eq!(p.work_phone_area_code(), Some(61));
}
```
