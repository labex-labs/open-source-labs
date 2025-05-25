# 벡터 (Vectors)

벡터는 크기 조절이 가능한 배열입니다. 슬라이스 (slice) 와 마찬가지로 컴파일 시간에 크기를 알 수 없지만, 언제든지 늘리거나 줄일 수 있습니다. 벡터는 다음 3 가지 매개변수를 사용하여 표현됩니다.

- 데이터에 대한 포인터 (pointer)
- 길이 (length)
- 용량 (capacity)

용량은 벡터에 대해 예약된 메모리의 양을 나타냅니다. 길이는 용량보다 작을 때까지 벡터가 증가할 수 있습니다. 이 임계값을 초과해야 할 경우, 벡터는 더 큰 용량으로 재할당됩니다.

```rust
fn main() {
    // Iterators can be collected into vectors
    let collected_iterator: Vec<i32> = (0..10).collect();
    println!("Collected (0..10) into: {:?}", collected_iterator);

    // The `vec!` macro can be used to initialize a vector
    let mut xs = vec![1i32, 2, 3];
    println!("Initial vector: {:?}", xs);

    // Insert new element at the end of the vector
    println!("Push 4 into the vector");
    xs.push(4);
    println!("Vector: {:?}", xs);

    // Error! Immutable vectors can't grow
    collected_iterator.push(0);
    // FIXME ^ Comment out this line

    // The `len` method yields the number of elements currently stored in a vector
    println!("Vector length: {}", xs.len());

    // Indexing is done using the square brackets (indexing starts at 0)
    println!("Second element: {}", xs[1]);

    // `pop` removes the last element from the vector and returns it
    println!("Pop last element: {:?}", xs.pop());

    // Out of bounds indexing yields a panic
    println!("Fourth element: {}", xs[3]);
    // FIXME ^ Comment out this line

    // `Vector`s can be easily iterated over
    println!("Contents of xs:");
    for x in xs.iter() {
        println!("> {}", x);
    }

    // A `Vector` can also be iterated over while the iteration
    // count is enumerated in a separate variable (`i`)
    for (i, x) in xs.iter().enumerate() {
        println!("In position {} we have value {}", i, x);
    }

    // Thanks to `iter_mut`, mutable `Vector`s can also be iterated
    // over in a way that allows modifying each value
    for x in xs.iter_mut() {
        *x *= 3;
    }
    println!("Updated vector: {:?}", xs);
}
```

더 많은 `Vec` 메서드는 `std::vec` 모듈에서 찾을 수 있습니다.
