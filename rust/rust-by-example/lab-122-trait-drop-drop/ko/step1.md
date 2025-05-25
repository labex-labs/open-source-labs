# Drop

`Drop` 트레이트는 `drop`이라는 하나의 메서드만 가지고 있으며, 이 메서드는 객체가 스코프 밖으로 벗어날 때 자동으로 호출됩니다. `Drop` 트레이트의 주요 사용 목적은 구현자 인스턴스가 소유한 리소스를 해제하는 것입니다.

`Box`, `Vec`, `String`, `File`, 그리고 `Process`는 리소스를 해제하기 위해 `Drop` 트레이트를 구현하는 몇 가지 예시입니다. `Drop` 트레이트는 또한 모든 사용자 정의 데이터 타입에 대해 수동으로 구현될 수 있습니다.

다음 예제는 `drop` 함수에 콘솔 출력을 추가하여 호출 시점을 알립니다.

```rust
struct Droppable {
    name: &'static str,
}

// This trivial implementation of `drop` adds a print to console.
impl Drop for Droppable {
    fn drop(&mut self) {
        println!("> Dropping {}", self.name);
    }
}

fn main() {
    let _a = Droppable { name: "a" };

    // block A
    {
        let _b = Droppable { name: "b" };

        // block B
        {
            let _c = Droppable { name: "c" };
            let _d = Droppable { name: "d" };

            println!("Exiting block B");
        }
        println!("Just exited block B");

        println!("Exiting block A");
    }
    println!("Just exited block A");

    // Variable can be manually dropped using the `drop` function
    drop(_a);
    // TODO ^ Try commenting this line

    println!("end of the main function");

    // `_a` *won't* be `drop`ed again here, because it already has been
    // (manually) `drop`ed
}
```
