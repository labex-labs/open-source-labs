# 반복자를 사용하여 clone 제거하기

Listing 12-6 에서, `String` 값의 슬라이스를 받아 슬라이스에서 인덱싱하고 값을 복제하여 `Config` 구조체의 인스턴스를 생성하는 코드를 추가했습니다. 이를 통해 `Config` 구조체가 해당 값을 소유할 수 있었습니다. Listing 13-17 에서는 `Config::build` 함수의 구현을 Listing 12-23 과 동일하게 재현했습니다.

파일 이름: `src/lib.rs`

```rust
impl Config {
    pub fn build(
        args: &[String]
    ) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

Listing 13-17: Listing 12-23 의 `Config::build` 함수 재현

당시에는 비효율적인 `clone` 호출에 대해 나중에 제거할 것이라고 말씀드렸습니다. 이제 그 시간이 왔습니다!

여기서 `clone`이 필요했던 이유는 매개변수 `args`에 `String` 요소의 슬라이스가 있지만, `build` 함수는 `args`를 소유하지 않기 때문입니다. `Config` 인스턴스의 소유권을 반환하기 위해, `Config` 인스턴스가 자체 값을 소유할 수 있도록 `Config`의 `query` 및 `filename` 필드에서 값을 복제해야 했습니다.

반복자에 대한 새로운 지식을 바탕으로, `build` 함수가 슬라이스를 빌리는 대신 반복자의 소유권을 인수로 받도록 변경할 수 있습니다. 슬라이스의 길이를 확인하고 특정 위치를 인덱싱하는 코드 대신 반복자 기능을 사용할 것입니다. 반복자가 값에 접근하므로 `Config::build` 함수가 무엇을 하는지 명확해질 것입니다.

`Config::build`가 반복자의 소유권을 가져가고 빌리는 인덱싱 작업을 중단하면, `clone`을 호출하고 새로운 할당을 하는 대신 반복자에서 `String` 값을 `Config`로 이동할 수 있습니다.
