# 여러 루프 간의 모호성을 제거하기 위한 루프 레이블

루프 안에 루프가 있는 경우 `break` 및 `continue`는 해당 시점에서 가장 안쪽 루프에 적용됩니다. 선택적으로 `break` 또는 `continue`와 함께 사용하여 해당 키워드가 가장 안쪽 루프 대신 레이블이 지정된 루프에 적용되도록 지정할 수 있는 루프에 *루프 레이블*을 지정할 수 있습니다. 루프 레이블은 작은 따옴표로 시작해야 합니다. 다음은 두 개의 중첩된 루프가 있는 예입니다.

```rust
fn main() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");
}
```

바깥쪽 루프에는 `'counting_up` 레이블이 있으며 0 에서 2 까지 카운트합니다. 레이블이 없는 안쪽 루프는 10 에서 9 까지 카운트다운합니다. 레이블을 지정하지 않는 첫 번째 `break`는 안쪽 루프만 종료합니다. `break 'counting_up;` 문은 바깥쪽 루프를 종료합니다. 이 코드는 다음을 출력합니다.

       Compiling loops v0.1.0 (file:///projects/loops)
        Finished dev [unoptimized + debuginfo] target(s) in 0.58s
         Running `target/debug/loops`
    count = 0
    remaining = 10
    remaining = 9
    count = 1
    remaining = 10
    remaining = 9
    count = 2
    remaining = 10
    End count = 2
