# `create`

`create` 함수는 파일을 쓰기 전용 모드로 엽니다. 파일이 이미 존재하면 기존 내용이 삭제되고, 그렇지 않으면 새 파일이 생성됩니다.

```rust
static LOREM_IPSUM: &str =
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
";

use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    let path = Path::new("lorem_ipsum.txt");
    let display = path.display();

    // 쓰기 전용 모드로 파일을 엽니다. `io::Result<File>` 를 반환합니다.
    let mut file = match File::create(&path) {
        Err(why) => panic!("{} 생성 실패: {}", display, why),
        Ok(file) => file,
    };

    // `LOREM_IPSUM` 문자열을 `file` 에 씁니다. `io::Result<()>` 를 반환합니다.
    match file.write_all(LOREM_IPSUM.as_bytes()) {
        Err(why) => panic!("{}에 쓰기 실패: {}", display, why),
        Ok(_) => println!("{}에 성공적으로 썼습니다", display),
    }
}
```

예상 성공 출력:

```shell
$ rustc create.rs && ./create
lorem_ipsum.txt에 성공적으로 썼습니다
$ cat lorem_ipsum.txt
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

(이전 예제와 마찬가지로, 실패 조건에서도 이 예제를 테스트하는 것이 좋습니다.)

파일을 여는 방법을 구성하려면 `OpenOptions` 구조체를 사용할 수 있습니다.
