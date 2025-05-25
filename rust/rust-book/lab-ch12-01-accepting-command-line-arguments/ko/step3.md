# 인자 값을 변수에 저장하기 (Saving the Argument Values in Variables)

프로그램은 현재 명령줄 인자로 지정된 값에 접근할 수 있습니다. 이제 두 인자의 값을 변수에 저장하여 프로그램의 나머지 부분에서 해당 값을 사용할 수 있도록 해야 합니다. Listing 12-2 에서 그렇게 합니다.

파일 이름: `src/main.rs`

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let query = &args[1];
    let file_path = &args[2];

    println!("Searching for {}", query);
    println!("In file {}", file_path);
}
```

Listing 12-2: 검색어 인자와 파일 경로 인자를 저장할 변수 생성하기

벡터를 출력했을 때 보았듯이, 프로그램 이름은 `args[0]`에서 벡터의 첫 번째 값을 차지하므로, 인자를 인덱스 1 부터 시작합니다. `minigrep`이 받는 첫 번째 인자는 우리가 검색하려는 문자열이므로, 첫 번째 인자에 대한 참조를 변수 `query`에 넣습니다. 두 번째 인자는 파일 경로가 되므로, 두 번째 인자에 대한 참조를 변수 `file_path`에 넣습니다.

코드가 의도한 대로 작동하는지 확인하기 위해, 이러한 변수의 값을 임시로 출력합니다. `test`와 `sample.txt` 인자를 사용하여 이 프로그램을 다시 실행해 보겠습니다.

```bash
$ cargo run -- test sample.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep test sample.txt`
Searching for test
In file sample.txt
```

훌륭합니다, 프로그램이 작동합니다! 필요한 인자 값들이 올바른 변수에 저장되고 있습니다. 나중에 사용자가 인자를 제공하지 않는 경우와 같은 특정 잠재적인 오류 상황을 처리하기 위해 몇 가지 오류 처리를 추가할 것입니다. 지금은 해당 상황을 무시하고 대신 파일 읽기 기능을 추가하는 작업을 진행하겠습니다.
