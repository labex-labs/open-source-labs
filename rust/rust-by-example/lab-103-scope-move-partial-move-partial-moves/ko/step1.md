# 부분 이동 (Partial moves)

단일 변수의 \[구조 분해 (destructuring)] 내에서 `by-move` 및 `by-reference` 패턴 바인딩을 동시에 사용할 수 있습니다. 이렇게 하면 변수의 *부분 이동 (partial move)*이 발생하며, 이는 변수의 일부가 이동하는 동안 다른 부분은 유지됨을 의미합니다. 이러한 경우, 부모 변수는 이후에 전체로 사용할 수 없지만, 참조만 되고 (이동되지 않은) 부분은 여전히 사용할 수 있습니다.

```rust
fn main() {
    #[derive(Debug)]
    struct Person {
        name: String,
        age: Box<u8>,
    }

    let person = Person {
        name: String::from("Alice"),
        age: Box::new(20),
    };

    // `name` is moved out of person, but `age` is referenced
    let Person { name, ref age } = person;

    println!("The person's age is {}", age);

    println!("The person's name is {}", name);

    // Error! borrow of partially moved value: `person` partial move occurs
    //println!("The person struct is {:?}", person);

    // `person` cannot be used but `person.age` can be used as it is not moved
    println!("The person's age from person struct is {}", person.age);
}
```

(이 예제에서는 부분 이동을 설명하기 위해 `age` 변수를 힙에 저장합니다. 위의 코드에서 `ref`를 삭제하면 `person.age`의 소유권이 `age` 변수로 이동하므로 오류가 발생합니다. `Person.age`가 스택에 저장된 경우, `age`의 정의가 `person.age`에서 데이터를 이동하지 않고 복사하므로 `ref`가 필요하지 않습니다.)
