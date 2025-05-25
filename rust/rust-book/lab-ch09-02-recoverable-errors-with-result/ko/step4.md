# 오류 발생 시 패닉을 위한 단축키: unwrap 과 expect

`match`를 사용하는 것은 충분히 잘 작동하지만, 약간 장황할 수 있으며 항상 의도를 잘 전달하지는 않습니다. `Result<T, E>` 타입에는 다양한, 더 구체적인 작업을 수행하기 위해 정의된 많은 헬퍼 메서드가 있습니다. `unwrap` 메서드는 Listing 9-4 에서 작성한 `match` 표현식과 유사하게 구현된 단축 메서드입니다. `Result` 값이 `Ok` 변형인 경우, `unwrap`은 `Ok` 내부의 값을 반환합니다. `Result`가 `Err` 변형인 경우, `unwrap`은 우리를 위해 `panic!` 매크로를 호출합니다. 다음은 `unwrap`의 작동 예시입니다.

파일 이름: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap();
}
```

_hello.txt_ 파일 없이 이 코드를 실행하면, `unwrap` 메서드가 만드는 `panic!` 호출에서 오류 메시지가 표시됩니다.

    thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:4:49

마찬가지로, `expect` 메서드를 사용하면 `panic!` 오류 메시지도 선택할 수 있습니다. `unwrap` 대신 `expect`를 사용하고 좋은 오류 메시지를 제공하면 의도를 전달하고 패닉의 원인을 더 쉽게 추적할 수 있습니다. `expect`의 구문은 다음과 같습니다.

파일 이름: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")
        .expect("hello.txt should be included in this project");
}
```

`unwrap`과 동일한 방식으로 `expect`를 사용하여 파일 핸들을 반환하거나 `panic!` 매크로를 호출합니다. `expect`가 `panic!`을 호출할 때 사용되는 오류 메시지는 `unwrap`이 사용하는 기본 `panic!` 메시지가 아닌, `expect`에 전달하는 매개변수가 됩니다. 다음과 같습니다.

    thread 'main' panicked at 'hello.txt should be included in this project: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:5:10

프로덕션 품질의 코드에서 대부분의 Rust 개발자는 `unwrap` 대신 `expect`를 선택하고, 작업이 항상 성공할 것으로 예상되는 이유에 대한 더 많은 컨텍스트를 제공합니다. 그렇게 하면, 가정이 틀린 것으로 판명될 경우, 디버깅에 사용할 수 있는 더 많은 정보를 얻을 수 있습니다.
