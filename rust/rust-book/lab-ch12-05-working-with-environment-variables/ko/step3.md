# `search_case_insensitive` 함수 구현하기

Listing 12-21 에 표시된 `search_case_insensitive` 함수는 `search` 함수와 거의 동일합니다. 유일한 차이점은 입력 인수의 대소문자에 관계없이 줄에 쿼리가 포함되어 있는지 확인할 때 동일한 대소문자가 되도록 `query`와 각 `line`을 소문자로 변환한다는 것입니다.

파일 이름: `src/lib.rs`

```rust
pub fn search_case_insensitive<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
  1 let query = query.to_lowercase();
    let mut results = Vec::new();

    for line in contents.lines() {
        if 2 line.to_lowercase().contains(3 &query) {
            results.push(line);
        }
    }

    results
}
```

Listing 12-21: 쿼리와 줄을 비교하기 전에 소문자로 변환하는 `search_case_insensitive` 함수 정의

먼저 `query` 문자열을 소문자로 변환하고 동일한 이름의 그림자 변수에 저장합니다 \[1]. 쿼리에 대해 `to_lowercase`를 호출하는 것은 사용자의 쿼리가 `"rust"`, `"RUST"`, `"Rust"`, 또는 `"rUsT"`이든 상관없이 쿼리를 `"rust"`로 처리하고 대소문자를 구분하지 않도록 하기 위해 필요합니다. `to_lowercase`는 기본적인 유니코드를 처리하지만 100% 정확하지는 않습니다. 실제 애플리케이션을 작성하는 경우 여기에서 조금 더 작업하고 싶겠지만, 이 섹션은 유니코드가 아닌 환경 변수에 관한 것이므로 여기서는 이 정도로 하겠습니다.

`to_lowercase`를 호출하면 기존 데이터를 참조하는 대신 새 데이터를 생성하므로 `query`는 이제 문자열 슬라이스가 아닌 `String`입니다. 예를 들어 쿼리가 `"rUsT"`라고 가정해 보겠습니다. 해당 문자열 슬라이스에는 사용할 소문자 `u` 또는 `t`가 포함되어 있지 않으므로 `"rust"`를 포함하는 새 `String`을 할당해야 합니다. 이제 `query`를 `contains` 메서드에 인수로 전달할 때 앰퍼샌드 \[3]를 추가해야 합니다. 왜냐하면 `contains`의 시그니처는 문자열 슬라이스를 사용하도록 정의되어 있기 때문입니다.

다음으로, 각 `line`에 대해 `to_lowercase`를 호출하여 모든 문자를 소문자로 변환합니다 \[2]. 이제 `line`과 `query`를 소문자로 변환했으므로 쿼리의 대소문자에 관계없이 일치하는 항목을 찾을 수 있습니다.

이 구현이 테스트를 통과하는지 확인해 보겠습니다.

    running 2 tests
    test tests::case_insensitive ... ok
    test tests::case_sensitive ... ok

    test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

훌륭합니다! 통과했습니다. 이제 `run` 함수에서 새로운 `search_case_insensitive` 함수를 호출해 보겠습니다. 먼저 대소문자 구분 검색과 대소문자 구분 없는 검색 간을 전환하기 위해 `Config` 구조체에 구성 옵션을 추가합니다. 이 필드를 추가하면 아직 이 필드를 초기화하지 않았기 때문에 컴파일러 오류가 발생합니다.

파일 이름: `src/lib.rs`

```rust
pub struct Config {
    pub query: String,
    pub file_path: String,
    pub ignore_case: bool,
}
```

`ignore_case` 필드를 추가하여 부울 값을 저장했습니다. 다음으로, Listing 12-22 에 표시된 것처럼 `run` 함수가 `ignore_case` 필드의 값을 확인하고 이를 사용하여 `search` 함수를 호출할지 또는 `search_case_insensitive` 함수를 호출할지 결정해야 합니다. 이것은 아직 컴파일되지 않습니다.

파일 이름: `src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    let results = if config.ignore_case {
        search_case_insensitive(&config.query, &contents)
    } else {
        search(&config.query, &contents)
    };

    for line in results {
        println!("{line}");
    }

    Ok(())
}
```

Listing 12-22: `config.ignore_case`의 값에 따라 `search` 또는 `search_case_insensitive` 호출

마지막으로, 환경 변수를 확인해야 합니다. 환경 변수 작업에 대한 함수는 표준 라이브러리의 `env` 모듈에 있으므로 해당 모듈을 `src/lib.rs`의 맨 위에 범위로 가져옵니다. 그런 다음 `env` 모듈의 `var` 함수를 사용하여 Listing 12-23 에 표시된 것처럼 `IGNORE_CASE`라는 환경 변수에 값이 설정되었는지 확인합니다.

파일 이름: `src/lib.rs`

```rust
use std::env;
--snip--

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

Listing 12-23: `IGNORE_CASE`라는 환경 변수에 값이 있는지 확인

여기에서 새 변수 `ignore_case`를 만듭니다. 해당 값을 설정하기 위해 `env::var` 함수를 호출하고 `IGNORE_CASE` 환경 변수의 이름을 전달합니다. `env::var` 함수는 환경 변수가 임의의 값으로 설정된 경우 환경 변수의 값을 포함하는 성공적인 `Ok` 변형이 될 `Result`를 반환합니다. 환경 변수가 설정되지 않은 경우 `Err` 변형을 반환합니다.

`Result`에서 `is_ok` 메서드를 사용하여 환경 변수가 설정되었는지 확인하고 있습니다. 즉, 프로그램은 대소문자를 구분하지 않는 검색을 수행해야 합니다. `IGNORE_CASE` 환경 변수가 아무것도 설정되지 않은 경우 `is_ok`는 `false`를 반환하고 프로그램은 대소문자를 구분하는 검색을 수행합니다. 환경 변수의 *값*은 중요하지 않고 설정되었는지 여부만 중요하므로 `unwrap`, `expect` 또는 `Result`에서 본 다른 메서드를 사용하는 대신 `is_ok`를 확인하고 있습니다.

`ignore_case` 변수의 값을 `Config` 인스턴스에 전달하여 `run` 함수가 해당 값을 읽고 Listing 12-22 에서 구현한 것처럼 `search_case_insensitive` 또는 `search`를 호출할지 결정할 수 있도록 합니다.

한번 시도해 봅시다! 먼저 환경 변수를 설정하지 않고 쿼리 `to`를 사용하여 프로그램을 실행합니다. 그러면 소문자 *to*라는 단어가 포함된 모든 줄이 일치해야 합니다.

```bash
$ cargo run -- to poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep to poem.txt`
Are you nobody, too?
How dreary to be somebody!
```

여전히 작동하는 것 같습니다! 이제 `IGNORE_CASE`를 `1`로 설정하고 동일한 쿼리 `to`를 사용하여 프로그램을 실행해 보겠습니다.

```bash
IGNORE_CASE=1 cargo run -- to poem.txt
```

PowerShell 을 사용하는 경우 환경 변수를 설정하고 프로그램을 별도의 명령으로 실행해야 합니다.

```rust
PS> $Env:IGNORE_CASE=1; cargo run -- to poem.txt
```

이렇게 하면 `IGNORE_CASE`가 셸 세션의 나머지 기간 동안 유지됩니다. `Remove-Item` cmdlet 을 사용하여 설정을 해제할 수 있습니다.

```rust
PS> Remove-Item Env:IGNORE_CASE
```

대문자가 포함된 *to*가 포함된 줄을 얻어야 합니다.

    Are you nobody, too?
    How dreary to be somebody!
    To tell your name the livelong day
    To an admiring bog!

훌륭합니다. *To*가 포함된 줄도 얻었습니다! 이제 `minigrep` 프로그램은 환경 변수에 의해 제어되는 대소문자 구분 없는 검색을 수행할 수 있습니다. 이제 명령줄 인수 또는 환경 변수를 사용하여 설정된 옵션을 관리하는 방법을 알았습니다.

일부 프로그램은 동일한 구성에 대해 인수 _및_ 환경 변수를 허용합니다. 이러한 경우 프로그램은 하나 또는 다른 하나가 우선한다고 결정합니다. 스스로 다른 연습을 위해 명령줄 인수 또는 환경 변수를 통해 대소문자 구분을 제어해 보십시오. 프로그램이 대소문자를 구분하는 것으로 설정된 것과 대소문자를 무시하도록 설정된 것으로 실행되는 경우 명령줄 인수 또는 환경 변수가 우선해야 하는지 결정합니다.

`std::env` 모듈에는 환경 변수를 처리하기 위한 더 많은 유용한 기능이 포함되어 있습니다. 사용 가능한 기능을 확인하려면 해당 문서를 확인하십시오.
