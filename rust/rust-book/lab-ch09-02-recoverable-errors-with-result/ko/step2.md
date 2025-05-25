# 다른 오류에 대한 매칭

Listing 9-4 의 코드는 `File::open`이 실패한 이유에 관계없이 `panic!`을 발생시킵니다. 그러나 서로 다른 실패 이유에 대해 서로 다른 작업을 수행하려고 합니다. `File::open`이 파일이 존재하지 않아서 실패한 경우, 파일을 생성하고 새 파일에 대한 핸들을 반환하려고 합니다. `File::open`이 다른 이유로 실패한 경우 (예: 파일을 열 권한이 없는 경우) 에도 Listing 9-4 에서와 마찬가지로 코드가 `panic!`을 발생시키도록 하려고 합니다. 이를 위해 Listing 9-5 에 표시된 내부 `match` 표현식을 추가합니다.

파일 이름: `src/main.rs`

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => {
                match File::create("hello.txt") {
                    Ok(fc) => fc,
                    Err(e) => panic!(
                        "Problem creating the file: {:?}",
                        e
                    ),
                }
            }
            other_error => {
                panic!(
                    "Problem opening the file: {:?}",
                    other_error
                );
            }
        },
    };
}
```

Listing 9-5: 서로 다른 방식으로 서로 다른 종류의 오류 처리

`File::open`이 `Err` 변형 내에서 반환하는 값의 타입은 표준 라이브러리에서 제공하는 구조체인 `io::Error`입니다. 이 구조체에는 `io::ErrorKind` 값을 얻기 위해 호출할 수 있는 `kind` 메서드가 있습니다. `io::ErrorKind` 열거형은 표준 라이브러리에서 제공되며, `io` 작업으로 인해 발생할 수 있는 다양한 종류의 오류를 나타내는 변형을 갖습니다. 우리가 사용하려는 변형은 `ErrorKind::NotFound`로, 열려고 하는 파일이 아직 존재하지 않음을 나타냅니다. 따라서 `greeting_file_result`에 대해 매칭하지만, `error.kind()`에 대한 내부 매칭도 있습니다.

내부 match 에서 확인하려는 조건은 `error.kind()`에서 반환된 값이 `ErrorKind` 열거형의 `NotFound` 변형인지 여부입니다. 그렇다면 `File::create`로 파일을 생성하려고 시도합니다. 그러나 `File::create`도 실패할 수 있으므로 내부 `match` 표현식에 두 번째 arm 이 필요합니다. 파일을 생성할 수 없는 경우 다른 오류 메시지가 인쇄됩니다. 외부 `match`의 두 번째 arm 은 동일하게 유지되므로, 프로그램은 파일 누락 오류 외의 모든 오류에 대해 패닉을 발생시킵니다.
