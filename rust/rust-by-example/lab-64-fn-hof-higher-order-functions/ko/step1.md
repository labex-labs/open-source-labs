# 고차 함수

Rust 는 고차 함수 (HOF) 를 제공합니다. 이 함수들은 하나 이상의 함수를 받아들여 또는 더 유용한 함수를 생성하는 함수입니다. HOF 와 지연 반복자는 Rust 에 함수형 스타일을 부여합니다.

```rust
fn is_odd(n: u32) -> bool {
    n % 2 == 1
}

fn main() {
    println!("1000 미만의 모든 제곱 홀수의 합을 구합니다.");
    let upper = 1000;

    // 명령형 접근 방식
    // 누산기 변수 선언
    let mut acc = 0;
    // 반복: 0, 1, 2, ... 무한대까지
    for n in 0.. {
        // 숫자 제곱
        let n_squared = n * n;

        if n_squared >= upper {
            // 상한을 초과하면 루프 종료
            break;
        } else if is_odd(n_squared) {
            // 홀수이면 값 누적
            acc += n_squared;
        }
    }
    println!("명령형 스타일: {}", acc);

    // 함수형 접근 방식
    let sum_of_squared_odd_numbers: u32 =
        (0..).map(|n| n * n)                             // 모든 자연수 제곱
             .take_while(|&n_squared| n_squared < upper) // 상한 이하
             .filter(|&n_squared| is_odd(n_squared))     // 홀수인 것만
             .sum();                                     // 합계
    println!("함수형 스타일: {}", sum_of_squared_odd_numbers);
}
```

Option 과 Iterator 는 고차 함수를 상당 부분 구현합니다.
