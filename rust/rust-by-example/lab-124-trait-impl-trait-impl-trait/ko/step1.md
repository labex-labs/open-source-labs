# `impl Trait`

`impl Trait`는 두 가지 위치에서 사용할 수 있습니다:

1.  인자 타입으로
2.  반환 타입으로

## 인자 타입으로

함수가 트레이트 (trait) 에 대해 제네릭 (generic) 하지만 특정 타입에 신경 쓰지 않는 경우, 인자의 타입으로 `impl Trait`를 사용하여 함수 선언을 단순화할 수 있습니다.

예를 들어, 다음 코드를 고려해 보세요:

```rust
fn parse_csv_document<R: std::io::BufRead>(src: R) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
        .map(|line| {
            // For each line in the source
            line.map(|line| {
                // If the line was read successfully, process it, if not, return the error
                line.split(',') // Split the line separated by commas
                    .map(|entry| String::from(entry.trim())) // Remove leading and trailing whitespace
                    .collect() // Collect all strings in a row into a Vec<String>
            })
        })
        .collect() // Collect all lines into a Vec<Vec<String>>
}
```

`parse_csv_document`는 제네릭하며, `BufReader<File>` 또는 `[u8]`과 같이 `BufRead`를 구현하는 모든 타입을 사용할 수 있습니다. 하지만 `R`의 타입이 무엇인지는 중요하지 않으며, `R`은 단지 `src`의 타입을 선언하는 데만 사용되므로, 함수는 다음과 같이 작성할 수도 있습니다:

```rust
fn parse_csv_document(src: impl std::io::BufRead) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
        .map(|line| {
            // For each line in the source
            line.map(|line| {
                // If the line was read successfully, process it, if not, return the error
                line.split(',') // Split the line separated by commas
                    .map(|entry| String::from(entry.trim())) // Remove leading and trailing whitespace
                    .collect() // Collect all strings in a row into a Vec<String>
            })
        })
        .collect() // Collect all lines into a Vec<Vec<String>>
}
```

인자 타입으로 `impl Trait`를 사용하면 함수가 어떤 형태를 사용하는지 명시적으로 지정할 수 없다는 점에 유의하세요. 즉, `parse_csv_document::<std::io::Empty>(std::io::empty())`는 두 번째 예제에서는 작동하지 않습니다.

## 반환 타입으로

함수가 `MyTrait`를 구현하는 타입을 반환하는 경우, 반환 타입을 `-> impl MyTrait`로 작성할 수 있습니다. 이는 타입 시그니처를 상당히 단순화하는 데 도움이 될 수 있습니다!

```rust
use std::iter;
use std::vec::IntoIter;

// This function combines two `Vec<i32>` and returns an iterator over it.
// Look how complicated its return type is!
fn combine_vecs_explicit_return_type(
    v: Vec<i32>,
    u: Vec<i32>,
) -> iter::Cycle<iter::Chain<IntoIter<i32>, IntoIter<i32>>> {
    v.into_iter().chain(u.into_iter()).cycle()
}

// This is the exact same function, but its return type uses `impl Trait`.
// Look how much simpler it is!
fn combine_vecs(
    v: Vec<i32>,
    u: Vec<i32>,
) -> impl Iterator<Item=i32> {
    v.into_iter().chain(u.into_iter()).cycle()
}

fn main() {
    let v1 = vec![1, 2, 3];
    let v2 = vec![4, 5];
    let mut v3 = combine_vecs(v1, v2);
    assert_eq!(Some(1), v3.next());
    assert_eq!(Some(2), v3.next());
    assert_eq!(Some(3), v3.next());
    assert_eq!(Some(4), v3.next());
    assert_eq!(Some(5), v3.next());
    println!("all done");
}
```

더 중요한 것은, 일부 Rust 타입은 명시적으로 작성할 수 없다는 것입니다. 예를 들어, 모든 클로저 (closure) 는 자체적인 이름 없는 구체적인 타입을 가지고 있습니다. `impl Trait` 구문 이전에는 클로저를 반환하기 위해 힙 (heap) 에 할당해야 했습니다. 하지만 이제 다음과 같이 모든 것을 정적으로 수행할 수 있습니다:

```rust
// Returns a function that adds `y` to its input
fn make_adder_function(y: i32) -> impl Fn(i32) -> i32 {
    let closure = move |x: i32| { x + y };
    closure
}

fn main() {
    let plus_one = make_adder_function(1);
    assert_eq!(plus_one(2), 3);
}
```

`impl Trait`를 사용하여 `map` 또는 `filter` 클로저를 사용하는 이터레이터 (iterator) 를 반환할 수도 있습니다! 이렇게 하면 `map`과 `filter`를 더 쉽게 사용할 수 있습니다. 클로저 타입은 이름이 없기 때문에, 함수가 클로저를 사용하는 이터레이터를 반환하는 경우 명시적인 반환 타입을 작성할 수 없습니다. 하지만 `impl Trait`를 사용하면 이를 쉽게 수행할 수 있습니다:

```rust
fn double_positives<'a>(numbers: &'a Vec<i32>) -> impl Iterator<Item = i32> + 'a {
    numbers
        .iter()
        .filter(|x| x > &&0)
        .map(|x| x * 2)
}

fn main() {
    let singles = vec![-3, -2, 2, 3];
    let doubles = double_positives(&singles);
    assert_eq!(doubles.collect::<Vec<i32>>(), vec![4, 6]);
}
```
