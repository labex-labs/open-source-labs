# 테스트에서 Result\<T, E\> 사용하기

지금까지의 모든 테스트는 실패할 때 패닉합니다. `Result<T, E>`를 사용하는 테스트도 작성할 수 있습니다! 다음은 Listing 11-1 의 테스트를 `Result<T, E>`를 사용하고 패닉하는 대신 `Err`를 반환하도록 다시 작성한 것입니다.

파일 이름: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("two plus two does not equal four"))
        }
    }
}
```

`it_works` 함수는 이제 `Result<(), String>` 반환 유형을 갖습니다. 함수 본문에서 `assert_eq!` 매크로를 호출하는 대신, 테스트가 통과하면 `Ok(())`를 반환하고 테스트가 실패하면 내부의 `String`과 함께 `Err`를 반환합니다.

테스트를 작성하여 `Result<T, E>`를 반환하면 테스트 본문에서 물음표 연산자를 사용할 수 있습니다. 이는 테스트 내의 모든 연산이 `Err` 변형을 반환하는 경우 실패해야 하는 테스트를 작성하는 편리한 방법이 될 수 있습니다.

`Result<T, E>`를 사용하는 테스트에서는 `#[should_panic]` 주석을 사용할 수 없습니다. 연산이 `Err` 변형을 반환하는지 어서션 (assertion) 하려면 `Result<T, E>` 값에 물음표 연산자를 _사용하지_ 마십시오. 대신 `assert!(value.is_err())`를 사용하십시오.

이제 테스트를 작성하는 여러 가지 방법을 알았으므로, 테스트를 실행할 때 어떤 일이 발생하는지 살펴보고 `cargo test`와 함께 사용할 수 있는 다양한 옵션을 살펴보겠습니다.
