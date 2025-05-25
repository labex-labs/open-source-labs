# Result 를 사용한 복구 가능한 오류

대부분의 오류는 프로그램이 완전히 중단될 정도로 심각하지 않습니다. 때로는 함수가 실패하는 이유가 쉽게 해석하고 대응할 수 있는 경우도 있습니다. 예를 들어, 파일을 열려고 시도했는데 파일이 존재하지 않아 해당 작업이 실패하면 프로세스를 종료하는 대신 파일을 생성할 수 있습니다.

"Result 를 사용한 잠재적 실패 처리"에서 기억하듯이, `Result` 열거형은 다음과 같이 `Ok`와 `Err`의 두 가지 변형을 갖도록 정의됩니다.

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

`T`와 `E`는 제네릭 타입 매개변수입니다. 제네릭에 대해서는 10 장에서 자세히 논의할 것입니다. 지금 알아야 할 것은 `T`가 `Ok` 변형 내에서 성공 사례에서 반환될 값의 타입을 나타내고, `E`가 `Err` 변형 내에서 실패 사례에서 반환될 오류의 타입을 나타낸다는 것입니다. `Result`는 이러한 제네릭 타입 매개변수를 가지므로, 반환하려는 성공 값과 오류 값이 다를 수 있는 다양한 상황에서 `Result` 타입과 해당 타입에 정의된 함수를 사용할 수 있습니다.

함수가 실패할 수 있으므로 `Result` 값을 반환하는 함수를 호출해 보겠습니다. Listing 9-3 에서는 파일을 열려고 시도합니다.

파일 이름: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");
}
```

Listing 9-3: 파일 열기

`File::open`의 반환 타입은 `Result<T, E>`입니다. 제네릭 매개변수 `T`는 성공 값의 타입인 `std::fs::File`로 `File::open`의 구현에 의해 채워졌습니다. 이는 파일 핸들입니다. 오류 값에 사용되는 `E`의 타입은 `std::io::Error`입니다. 이 반환 타입은 `File::open` 호출이 성공하여 읽거나 쓸 수 있는 파일 핸들을 반환할 수 있음을 의미합니다. 또한 함수 호출이 실패할 수도 있습니다. 예를 들어, 파일이 존재하지 않거나 파일에 액세스할 권한이 없을 수 있습니다. `File::open` 함수는 성공했는지 실패했는지 알려주는 동시에 파일 핸들 또는 오류 정보를 제공할 수 있어야 합니다. 이 정보가 바로 `Result` 열거형이 전달하는 것입니다.

`File::open`이 성공하는 경우, 변수 `greeting_file_result`의 값은 파일 핸들을 포함하는 `Ok`의 인스턴스가 됩니다. 실패하는 경우, `greeting_file_result`의 값은 발생한 오류 종류에 대한 추가 정보를 포함하는 `Err`의 인스턴스가 됩니다.

Listing 9-3 의 코드에 `File::open`이 반환하는 값에 따라 다른 작업을 수행하도록 추가해야 합니다. Listing 9-4 는 6 장에서 논의한 기본 도구인 `match` 표현식을 사용하여 `Result`를 처리하는 한 가지 방법을 보여줍니다.

파일 이름: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => {
            panic!("Problem opening the file: {:?}", error);
        }
    };
}
```

Listing 9-4: 반환될 수 있는 `Result` 변형을 처리하기 위해 `match` 표현식 사용

`Option` 열거형과 마찬가지로, `Result` 열거형과 해당 변형은 prelude 에 의해 범위 내로 가져왔으므로, `match` arm 에서 `Ok`와 `Err` 변형 앞에 `Result::`를 지정할 필요가 없습니다.

결과가 `Ok`인 경우, 이 코드는 `Ok` 변형에서 내부 `file` 값을 반환하고, 해당 파일 핸들 값을 변수 `greeting_file`에 할당합니다. `match` 이후에는 파일 핸들을 사용하여 읽거나 쓸 수 있습니다.

`match`의 다른 arm 은 `File::open`에서 `Err` 값을 얻는 경우를 처리합니다. 이 예제에서는 `panic!` 매크로를 호출하도록 선택했습니다. 현재 디렉토리에 *hello.txt*라는 파일이 없고 이 코드를 실행하면 `panic!` 매크로에서 다음 출력을 볼 수 있습니다.

    thread 'main' panicked at 'Problem opening the file: Os { code:
     2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:8:23

평소와 같이, 이 출력은 정확히 무엇이 잘못되었는지 알려줍니다.
