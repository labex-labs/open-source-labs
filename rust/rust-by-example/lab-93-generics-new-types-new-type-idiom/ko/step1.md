# 새로운 타입 관용구 (New Type Idiom)

`newtype` 관용구는 프로그램에 올바른 타입의 값이 제공되도록 컴파일 시점 보장을 제공합니다.

예를 들어, 연 단위 나이를 확인하는 나이 확인 함수는 반드시 `Years` 타입의 값을 받아야 합니다.

```rust
struct Years(i64);

struct Days(i64);

impl Years {
    pub fn to_days(&self) -> Days {
        Days(self.0 * 365)
    }
}


impl Days {
    /// 부분 연을 버립니다.
    pub fn to_years(&self) -> Years {
        Years(self.0 / 365)
    }
}

fn old_enough(age: &Years) -> bool {
    age.0 >= 18
}

fn main() {
    let age = Years(5);
    let age_days = age.to_days();
    println!("만 18 세 이상인가 {}", old_enough(&age));
    println!("만 18 세 이상인가 {}", old_enough(&age_days.to_years()));
    // println!("만 18 세 이상인가 {}", old_enough(&age_days));
}
```

마지막 출력문을 주석 해제하면 제공된 타입이 `Years`여야 함을 확인할 수 있습니다.

`newtype`의 값을 기본 타입으로 얻으려면 튜플 또는 구조 분해 구문을 사용할 수 있습니다.

```rust
struct Years(i64);

fn main() {
    let years = Years(42);
    let years_as_primitive_1: i64 = years.0; // 튜플
    let Years(years_as_primitive_2) = years; // 구조 분해
}
```
