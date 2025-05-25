# 파이썬 타입 매개변수

파이썬 타입 매개변수는 런타임에는 나타나지 않지만 컴파일 시점에만 정적으로 검사되는 매개변수입니다.

데이터 유형은 추가적인 제네릭 타입 매개변수를 사용하여 컴파일 시점에 마커 역할을 하거나 타입 검사를 수행할 수 있습니다. 이러한 추가 매개변수는 저장 값을 가지지 않으며 런타임 동작이 없습니다.

다음 예제에서는 `std::marker::PhantomData`를 파이썬 타입 매개변수 개념과 결합하여 서로 다른 데이터 유형을 포함하는 튜플을 만듭니다.

```rust
use std::marker::PhantomData;

// `A` 에 대한 제네릭이고 숨겨진 매개변수 `B` 를 가진 파이썬 튜플 구조체.
#[derive(PartialEq)] // 이 유형에 대한 동등성 테스트를 허용합니다.
struct PhantomTuple<A, B>(A, PhantomData<B>);

// `A` 에 대한 제네릭이고 숨겨진 매개변수 `B` 를 가진 파이썬 타입 구조체.
#[derive(PartialEq)] // 이 유형에 대한 동등성 테스트를 허용합니다.
struct PhantomStruct<A, B> { first: A, phantom: PhantomData<B> }

// 참고: 제네릭 타입 `A` 에 대한 저장 공간은 할당되지만 `B` 에 대한 저장 공간은 할당되지 않습니다.
// 따라서 `B` 는 계산에 사용될 수 없습니다.

fn main() {
    // 여기서 `f32` 와 `f64` 는 숨겨진 매개변수입니다.
    // PhantomTuple 타입은 `<char, f32>`로 지정됩니다.
    let _tuple1: PhantomTuple<char, f32> = PhantomTuple('Q', PhantomData);
    // PhantomTuple 타입은 `<char, f64>`로 지정됩니다.
    let _tuple2: PhantomTuple<char, f64> = PhantomTuple('Q', PhantomData);

    // 타입은 `<char, f32>`로 지정됩니다.
    let _struct1: PhantomStruct<char, f32> = PhantomStruct {
        first: 'Q',
        phantom: PhantomData,
    };
    // 타입은 `<char, f64>`로 지정됩니다.
    let _struct2: PhantomStruct<char, f64> = PhantomStruct {
        first: 'Q',
        phantom: PhantomData,
    };

    // 컴파일 시 오류! 타입 불일치로 인해 비교할 수 없습니다.
    // println!("_tuple1 == _tuple2 yields: {}",
    //           _tuple1 == _tuple2);

    // 컴파일 시 오류! 타입 불일치로 인해 비교할 수 없습니다.
    // println!("_struct1 == _struct2 yields: {}",
    //           _struct1 == _struct2);
}
```
