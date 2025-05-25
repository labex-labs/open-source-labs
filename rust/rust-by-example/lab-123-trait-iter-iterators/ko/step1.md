# 이터레이터 (Iterators)

`Iterator` 트레이트는 배열과 같은 컬렉션에 대한 이터레이터를 구현하는 데 사용됩니다.

이 트레이트는 `next` 요소에 대해 정의해야 하는 메서드만 필요하며, 이는 `impl` 블록에서 수동으로 정의하거나 자동으로 정의할 수 있습니다 (배열 및 범위에서와 같이).

일반적인 상황에 대한 편의를 위해, `for` 구문은 `.into_iter()` 메서드를 사용하여 일부 컬렉션을 이터레이터로 변환합니다.

```rust
struct Fibonacci {
    curr: u32,
    next: u32,
}

// `Fibonacci` 에 대해 `Iterator` 를 구현합니다.
// `Iterator` 트레이트는 `next` 요소에 대해 정의해야 하는 메서드만 필요합니다.
impl Iterator for Fibonacci {
    // Self::Item 을 사용하여 이 유형을 참조할 수 있습니다.
    type Item = u32;

    // 여기서 `.curr` 및 `.next` 를 사용하여 시퀀스를 정의합니다.
    // 반환 유형은 `Option<T>` 입니다.
    //     * `Iterator` 가 완료되면 `None` 이 반환됩니다.
    //     * 그렇지 않으면 다음 값이 `Some` 으로 래핑되어 반환됩니다.
    // 반환 유형에서 Self::Item 을 사용하므로
    // 함수 시그니처를 업데이트하지 않고도
    // 유형을 변경할 수 있습니다.
    fn next(&mut self) -> Option<Self::Item> {
        let current = self.curr;

        self.curr = self.next;
        self.next = current + self.next;

        // 피보나치 수열에는 끝점이 없으므로 `Iterator` 는
        // 결코 `None` 을 반환하지 않으며, 항상 `Some` 이 반환됩니다.
        Some(current)
    }
}

// 피보나치 수열 생성기를 반환합니다.
fn fibonacci() -> Fibonacci {
    Fibonacci { curr: 0, next: 1 }
}

fn main() {
    // `0..3` 은 0, 1, 2 를 생성하는 `Iterator` 입니다.
    let mut sequence = 0..3;

    println!("0..3 에 대한 연속적인 `next` 호출 4 번");
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());

    // `for` 는 `None` 을 반환할 때까지 `Iterator` 를 통해 작동합니다.
    // 각 `Some` 값은 언래핑되어 변수 (여기서는 `i`) 에 바인딩됩니다.
    println!("`for` 를 사용하여 0..3 을 반복합니다.");
    for i in 0..3 {
        println!("> {}", i);
    }

    // `take(n)` 메서드는 `Iterator` 를 처음 `n` 개의 항으로 줄입니다.
    println!("피보나치 수열의 처음 4 개 항은 다음과 같습니다: ");
    for i in fibonacci().take(4) {
        println!("> {}", i);
    }

    // `skip(n)` 메서드는 처음 `n` 개의 항을 삭제하여 `Iterator` 를 단축합니다.
    println!("피보나치 수열의 다음 4 개 항은 다음과 같습니다: ");
    for i in fibonacci().skip(4).take(4) {
        println!("> {}", i);
    }

    let array = [1u32, 3, 3, 7];

    // `iter` 메서드는 배열/슬라이스에 대한 `Iterator` 를 생성합니다.
    println!("다음 배열을 반복합니다 {:?}", &array);
    for i in array.iter() {
        println!("> {}", i);
    }
}
```
