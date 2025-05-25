# 오류 전파를 위한 단축키: ? 연산자

Listing 9-7 은 Listing 9-6 과 동일한 기능을 가진 `read_username_from_file`의 구현을 보여주지만, 이 구현은 `?` 연산자를 사용합니다.

파일 이름: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?;
    let mut username = String::new();
    username_file.read_to_string(&mut username)?;
    Ok(username)
}
```

Listing 9-7: `?` 연산자를 사용하여 오류를 호출하는 코드에 반환하는 함수

`Result` 값 뒤에 배치된 `?`는 Listing 9-6 에서 `Result` 값을 처리하기 위해 정의한 `match` 표현식과 거의 동일한 방식으로 작동하도록 정의되어 있습니다. `Result`의 값이 `Ok`이면, `Ok` 내부의 값이 이 표현식에서 반환되고 프로그램은 계속됩니다. 값이 `Err`이면, `Err`은 전체 함수에서 `return` 키워드를 사용한 것처럼 반환되므로 오류 값이 호출하는 코드로 전파됩니다.

Listing 9-6 의 `match` 표현식과 `?` 연산자가 하는 일 사이에는 차이점이 있습니다. `?` 연산자가 호출된 오류 값은 표준 라이브러리의 `From` 트레이트에서 정의된 `from` 함수를 거칩니다. 이 함수는 한 타입의 값을 다른 타입으로 변환하는 데 사용됩니다. `?` 연산자가 `from` 함수를 호출하면, 수신된 오류 타입은 현재 함수의 반환 타입에 정의된 오류 타입으로 변환됩니다. 이는 함수가 여러 가지 이유로 실패할 수 있음에도 불구하고, 함수가 실패할 수 있는 모든 방식을 나타내기 위해 하나의 오류 타입을 반환할 때 유용합니다.

예를 들어, Listing 9-7 의 `read_username_from_file` 함수를 우리가 정의한 `OurError`라는 사용자 정의 오류 타입을 반환하도록 변경할 수 있습니다. 또한 `impl From<io::Error> for OurError`를 정의하여 `io::Error`에서 `OurError`의 인스턴스를 생성하면, `read_username_from_file` 본문에서 `?` 연산자 호출은 `from`을 호출하고 함수에 더 많은 코드를 추가할 필요 없이 오류 타입을 변환합니다.

Listing 9-7 의 컨텍스트에서, `File::open` 호출 끝에 있는 `?`는 `Ok` 내부의 값을 변수 `username_file`로 반환합니다. 오류가 발생하면, `?` 연산자는 전체 함수에서 조기에 반환하고 모든 `Err` 값을 호출하는 코드에 제공합니다. `read_to_string` 호출 끝에 있는 `?`에도 동일하게 적용됩니다.

`?` 연산자는 많은 상용구를 제거하고 이 함수의 구현을 더 간단하게 만듭니다. Listing 9-8 과 같이 `?` 다음에 메서드 호출을 바로 연결하여 이 코드를 더 짧게 만들 수도 있습니다.

파일 이름: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username = String::new();

    File::open("hello.txt")?.read_to_string(&mut username)?;

    Ok(username)
}
```

Listing 9-8: `?` 연산자 다음에 메서드 호출 연결

새로운 `String`을 `username`에 생성하는 것을 함수의 시작 부분으로 옮겼습니다. 해당 부분은 변경되지 않았습니다. 변수 `username_file`을 생성하는 대신, `read_to_string` 호출을 `File::open("hello.txt")?`의 결과에 직접 연결했습니다. `read_to_string` 호출 끝에도 여전히 `?`가 있으며, `File::open`과 `read_to_string`이 모두 성공하면 오류를 반환하는 대신 `username`을 포함하는 `Ok` 값을 반환합니다. 기능은 다시 Listing 9-6 및 Listing 9-7 과 동일합니다. 이것은 단지 다른, 더 사용하기 쉬운 방식으로 작성된 것입니다.

Listing 9-9 는 `fs::read_to_string`을 사용하여 이를 훨씬 더 짧게 만드는 방법을 보여줍니다.

파일 이름: `src/main.rs`

```rust
use std::fs;
use std::io;

fn read_username_from_file() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}
```

Listing 9-9: 파일을 열고 읽는 대신 `fs::read_to_string` 사용

파일을 문자열로 읽는 것은 매우 일반적인 작업이므로, 표준 라이브러리는 파일을 열고, 새로운 `String`을 생성하고, 파일의 내용을 읽고, 해당 `String`에 내용을 넣고, 반환하는 편리한 `fs::read_to_string` 함수를 제공합니다. 물론, `fs::read_to_string`을 사용하면 모든 오류 처리를 설명할 기회가 없으므로, 먼저 더 긴 방식을 사용했습니다.
