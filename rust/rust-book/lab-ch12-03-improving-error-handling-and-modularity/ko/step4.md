# 구성 값 그룹화

`parse_config` 함수를 더욱 개선하기 위해 또 다른 작은 단계를 수행할 수 있습니다. 현재 튜플을 반환하지만, 즉시 해당 튜플을 다시 개별 부분으로 나눕니다. 이는 아직 올바른 추상화가 없을 수 있다는 신호입니다.

개선할 여지가 있음을 보여주는 또 다른 지표는 `parse_config`의 `config` 부분입니다. 이는 반환하는 두 값이 관련되어 있으며 모두 하나의 구성 값의 일부임을 의미합니다. 현재 두 값을 튜플로 그룹화하는 것 외에는 데이터 구조에서 이러한 의미를 전달하지 않습니다. 대신 두 값을 하나의 구조체에 넣고 각 구조체 필드에 의미 있는 이름을 지정합니다. 이렇게 하면 이 코드의 향후 유지 관리자가 서로 다른 값이 어떻게 관련되어 있는지, 그리고 그 목적이 무엇인지 이해하기가 더 쉬워집니다.

목록 12-6 은 `parse_config` 함수에 대한 개선 사항을 보여줍니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = parse_config(&args);

    println!("Searching for {}", 2 config.query);
    println!("In file {}", 3 config.file_path);

    let contents = fs::read_to_string(4 config.file_path)
        .expect("Should have been able to read the file");

    --snip--
}

5 struct Config {
    query: String,
    file_path: String,
}

6 fn parse_config(args: &[String]) -> Config {
  7 let query = args[1].clone();
  8 let file_path = args[2].clone();

    Config { query, file_path }
}
```

목록 12-6: `Config` 구조체의 인스턴스를 반환하도록 `parse_config` 리팩토링

`query` 및 `file_path`라는 필드를 갖도록 정의된 `Config`라는 구조체를 추가했습니다 \[5]. 이제 `parse_config`의 시그니처는 `Config` 값을 반환함을 나타냅니다 \[6]. `parse_config`의 본문에서 `args`의 `String` 값을 참조하는 문자열 슬라이스를 반환했던 곳에서 이제 소유된 `String` 값을 포함하도록 `Config`를 정의합니다. `main`의 `args` 변수는 인수 값의 소유자이며 `parse_config` 함수가 이를 빌리도록 허용할 뿐입니다. 즉, `Config`가 `args`의 값을 소유하려고 하면 Rust 의 빌림 규칙을 위반하게 됩니다.

`String` 데이터를 관리할 수 있는 여러 가지 방법이 있습니다. 가장 쉬운 방법은 다소 비효율적이지만, 값에 대해 `clone` 메서드를 호출하는 것입니다 \[7] \[8]. 이렇게 하면 `Config` 인스턴스가 소유할 데이터의 전체 복사본이 생성되므로 문자열 데이터에 대한 참조를 저장하는 것보다 더 많은 시간과 메모리가 소요됩니다. 그러나 데이터를 복제하면 참조의 수명을 관리할 필요가 없으므로 코드도 매우 간단해집니다. 이러한 상황에서는 약간의 성능을 포기하여 단순성을 얻는 것이 가치 있는 절충안입니다.

> **`clone` 사용의 절충점**
>
> 많은 Rust 개발자들은 런타임 비용 때문에 소유권 문제를 해결하기 위해 `clone`을 사용하는 것을 피하는 경향이 있습니다. 13 장에서 이러한 유형의 상황에서 더 효율적인 메서드를 사용하는 방법을 배우게 됩니다. 하지만 지금은 파일 경로와 쿼리 문자열이 매우 작기 때문에 몇 개의 문자열을 복사하여 계속 진행하는 것이 괜찮습니다. 처음부터 코드를 과도하게 최적화하려고 하는 것보다 약간 비효율적인 작동하는 프로그램을 갖는 것이 더 좋습니다. Rust 에 대한 경험이 많아지면 가장 효율적인 솔루션으로 시작하는 것이 더 쉬워지지만, 지금은 `clone`을 호출하는 것이 완벽하게 허용됩니다.

`parse_config`에서 반환된 `Config`의 인스턴스를 `config`라는 변수에 넣도록 `main`을 업데이트했으며 \[1], 이전에 별도의 `query` 및 `file_path` 변수를 사용했던 코드를 업데이트하여 이제 `Config` 구조체의 필드를 대신 사용하도록 했습니다 \[2] \[3] \[4].

이제 코드는 `query`와 `file_path`가 관련되어 있으며 그 목적이 프로그램이 작동하는 방식을 구성하는 것임을 더 명확하게 전달합니다. 이러한 값을 사용하는 모든 코드는 해당 목적에 맞게 명명된 필드의 `config` 인스턴스에서 해당 값을 찾을 수 있습니다.
