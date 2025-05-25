# `open`

`open` 함수는 읽기 전용 모드로 파일을 열기 위해 사용할 수 있습니다.

`File` 객체는 파일 디스크립터와 같은 리소스를 소유하고, `drop`될 때 파일을 자동으로 닫습니다.

```rust
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    // 원하는 파일의 경로를 만듭니다.
    let path = Path::new("hello.txt");
    let display = path.display();

    // 읽기 전용 모드로 경로를 엽니다. `io::Result<File>` 를 반환합니다.
    let mut file = match File::open(&path) {
        Err(why) => panic!("{} 열기 실패: {}", display, why),
        Ok(file) => file,
    };

    // 파일 내용을 문자열로 읽습니다. `io::Result<usize>` 를 반환합니다.
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("{} 읽기 실패: {}", display, why),
        Ok(_) => print!("{}에는 다음과 같은 내용이 있습니다:\n{}", display, s),
    }

    // `file` 객체가 범위를 벗어나면서 "hello.txt" 파일이 닫힙니다.
}
```

예상 성공적인 출력은 다음과 같습니다.

```shell
$ echo "Hello World!" > hello.txt
$ rustc open.rs && ./open
hello.txt에는 다음과 같은 내용이 있습니다:
Hello World!
```

(다양한 실패 조건 (예: `hello.txt` 파일이 존재하지 않거나 읽을 수 없는 경우 등) 에서 위의 예제를 테스트해 보는 것을 권장합니다.)
