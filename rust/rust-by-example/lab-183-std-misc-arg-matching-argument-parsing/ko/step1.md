# 인수 분석

매칭을 사용하여 간단한 인수를 분석할 수 있습니다.

```rust
use std::env;

fn increase(number: i32) {
    println!("{}", number + 1);
}

fn decrease(number: i32) {
    println!("{}", number - 1);
}

fn help() {
    println!("usage:
match_args <문자열>
    주어진 문자열이 답인지 확인합니다.
match_args {{증가 | 감소}} <정수>
    주어진 정수를 1 씩 증가 또는 감소시킵니다.");
}

fn main() {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        // 인수가 전달되지 않음
        1 => {
            println!("제 이름은 'match_args'입니다. 몇 가지 인수를 전달해 보세요!");
        },
        // 하나의 인수가 전달됨
        2 => {
            match args[1].parse() {
                Ok(42) => println!("정답입니다!"),
                _ => println!("정답이 아닙니다."),
            }
        },
        // 하나의 명령과 하나의 인수가 전달됨
        3 => {
            let cmd = &args[1];
            let num = &args[2];
            // 숫자를 구문 분석
            let number: i32 = match num.parse() {
                Ok(n) => {
                    n
                },
                Err(_) => {
                    eprintln!("오류: 두 번째 인수가 정수가 아닙니다.");
                    help();
                    return;
                },
            };
            // 명령을 구문 분석
            match &cmd[..] {
                "increase" => increase(number),
                "decrease" => decrease(number),
                _ => {
                    eprintln!("오류: 잘못된 명령입니다.");
                    help();
                },
            }
        },
        // 다른 모든 경우
        _ => {
            // 도움말 메시지 표시
            help();
        }
    }
}
```

```shell
$ ./match_args Rust
정답이 아닙니다.
$ ./match_args 42
정답입니다!
$ ./match_args do something
오류: 두 번째 인수가 정수가 아닙니다.
usage:
match_args <문자열>
    주어진 문자열이 답인지 확인합니다.
match_args {증가 | 감소} <정수>
    주어진 정수를 1 씩 증가 또는 감소시킵니다.
$ ./match_args do 42
오류: 잘못된 명령입니다.
usage:
match_args <문자열>
    주어진 문자열이 답인지 확인합니다.
match_args {증가 | 감소} <정수>
    주어진 정수를 1 씩 증가 또는 감소시킵니다.
$ ./match_args increase 42
43
```
