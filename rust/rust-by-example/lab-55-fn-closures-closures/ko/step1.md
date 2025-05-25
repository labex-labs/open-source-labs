# 클로저

클로저는 외부 환경을 포착할 수 있는 함수입니다. 예를 들어, `x` 변수를 포착하는 클로저는 다음과 같습니다.

```rust
|val| val + x
```

클로저의 구문과 기능은 즉석 사용에 매우 편리하게 만듭니다. 클로저를 호출하는 것은 함수를 호출하는 것과 정확히 같습니다. 그러나 입력 및 반환 형식은 _추론될 수 있으며_, 입력 변수 이름은 _반드시_ 지정되어야 합니다.

클로저의 다른 특징은 다음과 같습니다.

- 입력 변수 주변에 `()` 대신 `||`를 사용합니다.
- 단일 표현식에 대한 본문 구분 (`{}`) 은 선택 사항입니다 (그렇지 않으면 필수).
- 외부 환경 변수를 포착할 수 있습니다.

```rust
fn main() {
    let outer_var = 42;

    // 일반 함수는 외부 환경의 변수를 참조할 수 없습니다.
    //fn function(i: i32) -> i32 { i + outer_var }
    // TODO: 위의 줄을 주석 해제하고 컴파일러 오류를 확인하십시오. 컴파일러는 대신 클로저를 정의하도록 제안합니다.

    // 클로저는 익명이며, 여기서는 참조에 바인딩합니다.
    // 주석은 함수 주석과 동일하지만 선택 사항입니다.
    // 본문을 감싸는 `{}` 도 마찬가지입니다. 이러한 이름 없는 함수는 적절한 이름의 변수에 할당됩니다.
    let closure_annotated = |i: i32| -> i32 { i + outer_var };
    let closure_inferred  = |i     |          i + outer_var  ;

    // 클로저를 호출합니다.
    println!("closure_annotated: {}", closure_annotated(1));
    println!("closure_inferred: {}", closure_inferred(1));
    // 클로저의 형식이 추론된 후에는 다른 형식으로 다시 추론할 수 없습니다.
    //println!("cannot reuse closure_inferred with another type: {}", closure_inferred(42i64));
    // TODO: 위의 줄을 주석 해제하고 컴파일러 오류를 확인하십시오.

    // 인수를 받지 않고 `i32` 를 반환하는 클로저.
    // 반환 형식은 추론됩니다.
    let one = || 1;
    println!("closure returning one: {}", one());

}
```
