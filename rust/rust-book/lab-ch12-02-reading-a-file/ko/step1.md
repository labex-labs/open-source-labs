# 파일 읽기

이제 `file_path` 인수로 지정된 파일을 읽는 기능을 추가해 보겠습니다. 먼저 테스트할 샘플 파일이 필요합니다. 여러 줄에 걸쳐 약간의 텍스트와 몇 개의 반복되는 단어가 있는 파일을 사용합니다. Listing 12-3 에는 Emily Dickinson 의 시가 있는데, 잘 작동할 것입니다! 프로젝트의 루트 레벨에 *poem.txt*라는 파일을 만들고 "I'm Nobody! Who are you?"라는 시를 입력하세요.

파일 이름: poem.txt

    I'm nobody! Who are you?
    Are you nobody, too?
    Then there's a pair of us - don't tell!
    They'd banish us, you know.

    How dreary to be somebody!
    How public, like a frog
    To tell your name the livelong day
    To an admiring bog!

Listing 12-3: Emily Dickinson 의 시는 좋은 테스트 케이스가 됩니다.

텍스트를 입력한 후, `src/main.rs`를 편집하고 Listing 12-4 에 표시된 대로 파일을 읽는 코드를 추가합니다.

파일 이름: `src/main.rs`

```rust
use std::env;
1 use std::fs;

fn main() {
    --snip--
    println!("In file {}", file_path);

  2 let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

  3 println!("With text:\n{contents}");
}
```

Listing 12-4: 두 번째 인수로 지정된 파일의 내용을 읽기

먼저 `use` 문을 사용하여 표준 라이브러리의 관련 부분을 가져옵니다. 파일을 처리하려면 `std::fs`가 필요합니다 \[1].

`main`에서 새로운 문인 `fs::read_to_string`은 `file_path`를 가져와 해당 파일을 열고 파일 내용의 `std::io::Result<String>`을 반환합니다 \[2].

그 후, 파일이 읽힌 후 `contents`의 값을 출력하는 임시 `println!` 문을 다시 추가하여 프로그램이 지금까지 제대로 작동하는지 확인할 수 있습니다 \[3].

첫 번째 명령줄 인수로 임의의 문자열 (아직 검색 부분을 구현하지 않았기 때문) 과 두 번째 인수로 _poem.txt_ 파일을 사용하여 이 코드를 실행해 보겠습니다.

```bash
$ cargo run -- the poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep the poem.txt`
Searching for the
In file poem.txt
With text:
I'm nobody! Who are you?
Are you nobody, too?
Then there's a pair of us - don't tell!
They'd banish us, you know.

How dreary to be somebody!
How public, like a frog
To tell your name the livelong day
To an admiring bog!
```

훌륭합니다! 코드는 파일의 내용을 읽고 출력했습니다. 하지만 코드에는 몇 가지 결함이 있습니다. 현재 `main` 함수는 여러 책임을 가지고 있습니다. 일반적으로 함수는 각 함수가 하나의 아이디어만 담당하는 경우 더 명확하고 유지 관리하기 쉽습니다. 또 다른 문제는 오류를 제대로 처리하지 않고 있다는 것입니다. 프로그램은 아직 작아서 이러한 결함이 큰 문제는 아니지만, 프로그램이 커지면 깔끔하게 수정하기가 더 어려워질 것입니다. 프로그램을 개발할 때 초기에 리팩토링을 시작하는 것이 좋은 방법입니다. 코드가 적을 때 리팩토링하는 것이 훨씬 쉽기 때문입니다. 다음으로 그렇게 할 것입니다.
