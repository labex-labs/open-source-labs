# 배열과 슬라이스

배열은 동일한 타입 `T`의 객체들을 연속된 메모리에 저장하는 컬렉션입니다. 배열은 대괄호 `[]`를 사용하여 생성되며, 컴파일 시간에 알려진 그 길이는 타입 시그니처 `[T; length]`의 일부입니다.

슬라이스는 배열과 유사하지만, 그 길이는 컴파일 시간에 알려져 있지 않습니다. 대신, 슬라이스는 두 단어 (two-word) 객체입니다. 첫 번째 단어는 데이터에 대한 포인터이고, 두 번째 단어는 슬라이스의 길이입니다. 단어 크기는 프로세서 아키텍처에 의해 결정되는 `usize`와 동일합니다. 예를 들어, x86-64 에서는 64 비트입니다. 슬라이스는 배열의 일부분을 빌려오는 데 사용될 수 있으며, 타입 시그니처는 `&[T]`입니다.

```rust
use std::mem;

// This function borrows a slice.
fn analyze_slice(slice: &[i32]) {
    println!("First element of the slice: {}", slice[0]);
    println!("The slice has {} elements", slice.len());
}

fn main() {
    // Fixed-size array (type signature is superfluous).
    let xs: [i32; 5] = [1, 2, 3, 4, 5];

    // All elements can be initialized to the same value.
    let ys: [i32; 500] = [0; 500];

    // Indexing starts at 0.
    println!("First element of the array: {}", xs[0]);
    println!("Second element of the array: {}", xs[1]);

    // `len` returns the count of elements in the array.
    println!("Number of elements in array: {}", xs.len());

    // Arrays are stack allocated.
    println!("Array occupies {} bytes", mem::size_of_val(&xs));

    // Arrays can be automatically borrowed as slices.
    println!("Borrow the whole array as a slice.");
    analyze_slice(&xs);

    // Slices can point to a section of an array.
    // They are of the form [starting_index..ending_index].
    // `starting_index` is the first position in the slice.
    // `ending_index` is one more than the last position in the slice.
    println!("Borrow a section of the array as a slice.");
    analyze_slice(&ys[1 .. 4]);

    // Example of empty slice `&[]`:
    let empty_array: [u32; 0] = [];
    assert_eq!(&empty_array, &[]);
    assert_eq!(&empty_array, &[][..]); // Same but more verbose

    // Arrays can be safely accessed using `.get`, which returns an
    // `Option`. This can be matched as shown below, or used with
    // `.expect()` if you would like the program to exit with a nice
    // message instead of happily continue.
    for i in 0..xs.len() + 1 { // Oops, one element too far!
        match xs.get(i) {
            Some(xval) => println!("{}: {}", i, xval),
            None => println!("Slow down! {} is too far!", i),
        }
    }

    // Out of bound indexing on array causes compile time error.
    //println!("{}", xs[5]);
    // Out of bound indexing on slice causes runtime error.
    //println!("{}", xs[..][5]);
}
```
