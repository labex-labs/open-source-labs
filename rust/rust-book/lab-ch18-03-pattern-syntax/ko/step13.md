# 중첩된 \_로 값의 일부 무시하기 (Parts of a Value with a Nested \_)

또한 다른 패턴 내에서 `_`를 사용하여 값의 일부만 무시할 수 있습니다. 예를 들어, 값의 일부만 테스트하고 싶지만 실행하려는 해당 코드에서 다른 부분은 사용할 필요가 없는 경우입니다. Listing 18-18 은 설정 값을 관리하는 코드를 보여줍니다. 비즈니스 요구 사항은 사용자가 설정의 기존 사용자 지정을 덮어쓸 수 없지만, 설정이 현재 설정되지 않은 경우 설정을 해제하고 값을 지정할 수 있어야 한다는 것입니다.

파일 이름: `src/main.rs`

```rust
let mut setting_value = Some(5);
let new_setting_value = Some(10);

match (setting_value, new_setting_value) {
    (Some(_), Some(_)) => {
        println!("Can't overwrite an existing customized value");
    }
    _ => {
        setting_value = new_setting_value;
    }
}

println!("setting is {:?}", setting_value);
```

Listing 18-18: `Some` variant 내의 값을 사용할 필요가 없을 때 `Some` variant 와 일치하는 패턴 내에서 밑줄 사용하기

이 코드는 `Can't overwrite an existing customized value`를 출력한 다음 `setting is Some(5)`를 출력합니다. 첫 번째 match arm 에서 `Some` variant 내의 값을 일치시키거나 사용할 필요는 없지만, `setting_value`와 `new_setting_value`가 모두 `Some` variant 인 경우를 테스트해야 합니다. 이 경우 `setting_value`를 변경하지 않는 이유를 출력하고, 변경되지 않습니다.

두 번째 arm 의 `_` 패턴으로 표현된 다른 모든 경우 ( `setting_value` 또는 `new_setting_value`가 `None`인 경우) 에는 `new_setting_value`가 `setting_value`가 되도록 허용합니다.

또한 하나의 패턴 내에서 여러 위치에 밑줄을 사용하여 특정 값을 무시할 수 있습니다. Listing 18-19 는 5 개의 항목으로 구성된 튜플에서 두 번째 및 네 번째 값을 무시하는 예제를 보여줍니다.

파일 이름: `src/main.rs`

```rust
let numbers = (2, 4, 8, 16, 32);

match numbers {
    (first, _, third, _, fifth) => {
        println!("Some numbers: {first}, {third}, {fifth}");
    }
}
```

Listing 18-19: 튜플의 여러 부분 무시하기

이 코드는 `Some numbers: 2, 8, 32`를 출력하고, 값 `4`와 `16`은 무시됩니다.
