# `read_lines`

## 단순한 방법

파일에서 라인을 읽는 초보자의 첫 번째 구현에 대한 합리적인 첫 시도일 수 있습니다.

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}
```

`lines()` 메서드는 파일의 라인에 대한 반복자를 반환하므로, 인라인 매핑을 수행하고 결과를 수집하여 더 간결하고 유창한 표현을 얻을 수도 있습니다.

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap()  // 파일 읽기 오류 발생 시 즉시 종료
        .lines()  // 문자열을 문자열 슬라이스 반복자로 분할
        .map(String::from)  // 각 슬라이스를 문자열로 변환
        .collect()  // 벡터에 모음
}
```

위의 두 예제에서 `lines()`가 반환하는 `&str` 참조를 각각 `.to_string()` 및 `String::from`을 사용하여 소유형 `String`으로 변환해야 함에 유의하십시오.

## 더 효율적인 방법

여기서는 열린 `File`의 소유권을 `BufReader` 구조체에 전달합니다. `BufReader`는 내부 버퍼를 사용하여 중간 할당을 줄입니다.

또한 `read_lines`를 업데이트하여 각 라인에 대한 메모리에 새로운 `String` 객체를 할당하는 대신 반복자를 반환합니다.

```rust
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    // hosts.txt 파일이 현재 경로에 있어야 합니다.
    if let Ok(lines) = read_lines("./hosts.txt") {
        // 반복자를 소비하고 (선택적) 문자열을 반환합니다.
        for line in lines {
            if let Ok(ip) = line {
                println!("{}", ip);
            }
        }
    }
}

// 출력은 오류 일치를 허용하기 위해 Result 로 감싸져 있습니다.
// 파일의 라인의 Reader 에 대한 반복자를 반환합니다.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
```

이 프로그램을 실행하면 각 라인이 개별적으로 출력됩니다.

```shell
$ echo -e "127.0.0.1\n192.168.0.1\n" > hosts.txt
$ rustc read_lines.rs && ./read_lines
127.0.0.1
192.168.0.1
```

(`File::open`이 제네릭 `AsRef<Path>`를 인수로 예상하기 때문에 `where` 키워드를 사용하여 동일한 제네릭 제약 조건을 가진 제네릭 `read_lines()` 메서드를 정의했습니다.)

이 프로세스는 파일의 모든 내용으로 메모리에 `String`을 만드는 것보다 더 효율적입니다. 이는 특히 큰 파일을 처리할 때 성능 문제를 일으킬 수 있습니다.
