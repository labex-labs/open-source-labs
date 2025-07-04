# 스택 전용 데이터: Copy

아직 이야기하지 않은 또 다른 문제가 있습니다. 정수를 사용하는 이 코드 (일부 내용은 목록 4-2 에 표시됨) 는 작동하며 유효합니다.

```rust
let x = 5;
let y = x;

println!("x = {x}, y = {y}");
```

그러나 이 코드는 방금 배운 내용과 모순되는 것처럼 보입니다. `clone` 호출이 없지만 `x`는 여전히 유효하고 `y`로 이동되지 않았습니다.

그 이유는 컴파일 시간에 크기가 알려진 정수와 같은 타입은 전체적으로 스택에 저장되므로 실제 값의 복사본을 빠르게 만들 수 있기 때문입니다. 즉, 변수 `y`를 생성한 후 `x`가 유효하지 않도록 할 이유가 없습니다. 즉, 여기서는 깊은 복사와 얕은 복사 사이에 차이가 없으므로 `clone`을 호출해도 일반적인 얕은 복사와 다른 작업이 수행되지 않으며 생략할 수 있습니다.

Rust 에는 컴파일 시간에 크기가 알려진 정수와 같이 스택에 저장되는 타입에 적용할 수 있는 `Copy` 트레이트 (trait) 라는 특별한 어노테이션이 있습니다 (10 장에서 트레이트에 대해 자세히 설명합니다). 타입이 `Copy` 트레이트를 구현하는 경우, 이를 사용하는 변수는 이동하지 않고 간단하게 복사되므로 다른 변수에 할당된 후에도 여전히 유효합니다.

Rust 는 타입 또는 해당 타입의 일부가 `Drop` 트레이트를 구현한 경우 해당 타입에 `Copy`를 어노테이션할 수 없도록 합니다. 값이 범위를 벗어날 때 특별한 일이 발생해야 하고 해당 타입에 `Copy` 어노테테이션을 추가하면 컴파일 타임 오류가 발생합니다. 트레이트를 구현하기 위해 타입에 `Copy` 어노테이션을 추가하는 방법에 대한 자세한 내용은 "Derivable Traits"를 참조하십시오.

그렇다면 어떤 타입이 `Copy` 트레이트를 구현할까요? 확실히 하려면 주어진 타입에 대한 문서를 확인할 수 있지만, 일반적으로 간단한 스칼라 값의 모든 그룹은 `Copy`를 구현할 수 있으며, 할당이 필요하거나 어떤 형태의 리소스인 것은 `Copy`를 구현할 수 없습니다. 다음은 `Copy`를 구현하는 몇 가지 타입입니다.

- `u32`와 같은 모든 정수 타입.
- `true` 및 `false` 값을 가진 부울 타입 `bool`.
- `f64`와 같은 모든 부동 소수점 타입.
- 문자 타입 `char`.
- 튜플은 `Copy`를 구현하는 타입만 포함하는 경우. 예를 들어, `(i32, i32)`는 `Copy`를 구현하지만 `(i32, String)`은 그렇지 않습니다.
