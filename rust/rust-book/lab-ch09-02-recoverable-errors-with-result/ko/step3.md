# Result\<T, E\>와 함께 match 를 사용하는 대안

`match`가 많네요! `match` 표현식은 매우 유용하지만, 또한 매우 기본적인 것입니다. 13 장에서 클로저 (closure) 에 대해 배우게 될 것입니다. 클로저는 `Result<T, E>`에 정의된 많은 메서드와 함께 사용됩니다. 이러한 메서드는 코드에서 `Result<T, E>` 값을 처리할 때 `match`를 사용하는 것보다 더 간결할 수 있습니다.

예를 들어, Listing 9-5 에 표시된 것과 동일한 로직을 작성하는 또 다른 방법은 클로저와 `unwrap_or_else` 메서드를 사용하는 것입니다.

    // src/main.rs
    use std::fs::File;
    use std::io::ErrorKind;

    fn main() {
        let greeting_file = File::open("hello.txt").unwrap_or_else(|error| {
            if error.kind() == ErrorKind::NotFound {
                File::create("hello.txt").unwrap_or_else(|error| {
                    panic!("Problem creating the file: {:?}", error);
                })
            } else {
                panic!("Problem opening the file: {:?}", error);
            }
        });
    }

이 코드는 Listing 9-5 와 동일한 동작을 하지만, `match` 표현식을 포함하지 않고 읽기 더 쉽습니다. 13 장을 읽은 후 이 예제로 돌아와서 표준 라이브러리 문서에서 `unwrap_or_else` 메서드를 찾아보세요. 오류를 처리할 때 이러한 메서드 중 많은 수가 거대한 중첩된 `match` 표현식을 정리할 수 있습니다.
