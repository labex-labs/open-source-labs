# 함수 추출을 통한 중복 제거

제네릭 (generics) 을 사용하면 특정 타입을 여러 타입을 나타내는 자리 표시자로 대체하여 코드 중복을 제거할 수 있습니다. 제네릭 구문에 대해 자세히 알아보기 전에, 먼저 제네릭 타입을 사용하지 않고 특정 값을 여러 값을 나타내는 자리 표시자로 대체하는 함수를 추출하여 중복을 제거하는 방법을 살펴보겠습니다. 그런 다음 동일한 기술을 적용하여 제네릭 함수를 추출할 것입니다! 함수로 추출할 수 있는 중복된 코드를 인식하는 방법을 살펴보면, 제네릭을 사용할 수 있는 중복된 코드를 인식하기 시작할 것입니다.

먼저 목록에서 가장 큰 숫자를 찾는 Listing 10-1 의 짧은 프로그램부터 시작합니다.

파일 이름: `src/main.rs`

```rust
fn main() {
  1 let number_list = vec![34, 50, 25, 100, 65];

  2 let mut largest = &number_list[0];

  3 for number in &number_list {
      4 if number > largest {
          5 largest = number;
        }
    }

    println!("The largest number is {largest}");
}
```

Listing 10-1: 숫자 목록에서 가장 큰 숫자 찾기

`number_list` 변수 \[1]에 정수 목록을 저장하고, 목록의 첫 번째 숫자에 대한 참조를 `largest`라는 변수 \[2]에 넣습니다. 그런 다음 목록의 모든 숫자를 반복하고 \[3], 현재 숫자가 `largest`에 저장된 숫자보다 크면 \[4], 해당 변수의 참조를 대체합니다 \[5]. 그러나 현재 숫자가 지금까지 본 가장 큰 숫자보다 작거나 같으면 변수는 변경되지 않고 코드는 목록의 다음 숫자로 이동합니다. 목록의 모든 숫자를 고려한 후, `largest`는 가장 큰 숫자, 즉 이 경우 100 을 참조해야 합니다.

이제 두 개의 서로 다른 숫자 목록에서 가장 큰 숫자를 찾는 작업이 주어졌습니다. 이를 위해 Listing 10-1 의 코드를 복제하고 프로그램의 두 다른 위치에서 동일한 로직을 사용할 수 있습니다. Listing 10-2 에 나와 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let mut largest = &number_list[0];

    for number in &number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("The largest number is {largest}");

    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];

    let mut largest = &number_list[0];

    for number in &number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("The largest number is {largest}");
}
```

Listing 10-2: _두 개의_ 숫자 목록에서 가장 큰 숫자를 찾는 코드

이 코드는 작동하지만, 코드를 복제하는 것은 지루하고 오류가 발생하기 쉽습니다. 또한 코드를 변경하려는 경우 여러 위치에서 코드를 업데이트해야 한다는 것을 기억해야 합니다.

이 중복을 제거하기 위해 매개변수로 전달된 모든 정수 목록에 대해 작동하는 함수를 정의하여 추상화를 만들 것입니다. 이 솔루션은 코드를 더 명확하게 만들고 목록에서 가장 큰 숫자를 찾는 개념을 추상적으로 표현할 수 있게 해줍니다.

Listing 10-3 에서 가장 큰 숫자를 찾는 코드를 `largest`라는 함수로 추출합니다. 그런 다음 함수를 호출하여 Listing 10-2 의 두 목록에서 가장 큰 숫자를 찾습니다. 앞으로 있을 수 있는 다른 `i32` 값 목록에서도 함수를 사용할 수 있습니다.

파일 이름: `src/main.rs`

```rust
fn largest(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {result}");

    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];

    let result = largest(&number_list);
    println!("The largest number is {result}");
}
```

Listing 10-3: 두 목록에서 가장 큰 숫자를 찾기 위한 추상화된 코드

`largest` 함수에는 `list`라는 매개변수가 있는데, 이 매개변수는 함수에 전달할 수 있는 모든 구체적인 `i32` 값 슬라이스를 나타냅니다. 결과적으로 함수를 호출하면 코드는 전달하는 특정 값에 대해 실행됩니다.

요약하면, Listing 10-2 의 코드를 Listing 10-3 으로 변경하기 위해 수행한 단계는 다음과 같습니다.

1.  중복된 코드를 식별합니다.
2.  중복된 코드를 함수의 본문으로 추출하고, 해당 코드의 입력 및 반환 값을 함수 시그니처 (signature) 에 지정합니다.
3.  함수를 호출하도록 중복된 코드의 두 인스턴스를 업데이트합니다.

다음으로, 제네릭을 사용하여 코드 중복을 줄이기 위해 동일한 단계를 사용합니다. 함수 본문이 특정 값 대신 추상적인 `list`에 대해 작동할 수 있는 방식과 마찬가지로, 제네릭을 사용하면 코드가 추상 타입에 대해 작동할 수 있습니다.

예를 들어, `i32` 값 슬라이스에서 가장 큰 항목을 찾는 함수와 `char` 값 슬라이스에서 가장 큰 항목을 찾는 함수가 있다고 가정해 보겠습니다. 어떻게 그 중복을 제거할 수 있을까요? 알아보겠습니다!
