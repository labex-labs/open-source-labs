# 환경을 캡처하는 클로저 사용하기

많은 반복자 어댑터는 클로저를 인수로 사용하며, 일반적으로 반복자 어댑터에 대한 인수로 지정할 클로저는 환경을 캡처하는 클로저가 될 것입니다.

이 예제에서는 클로저를 인수로 사용하는 `filter` 메서드를 사용합니다. 클로저는 반복자에서 항목을 가져와 `bool`을 반환합니다. 클로저가 `true`를 반환하면 해당 값은 `filter`에 의해 생성된 반복에 포함됩니다. 클로저가 `false`를 반환하면 해당 값은 포함되지 않습니다.

Listing 13-16 에서 `Shoe` 구조체 인스턴스 모음을 반복하기 위해 환경에서 `shoe_size` 변수를 캡처하는 클로저와 함께 `filter`를 사용합니다. 지정된 크기의 신발만 반환합니다.

파일 이름: `src/lib.rs`

```rust
#[derive(PartialEq, Debug)]
struct Shoe {
    size: u32,
    style: String,
}

fn shoes_in_size(shoes: Vec<Shoe>, shoe_size: u32) -> Vec<Shoe> {
    shoes.into_iter().filter(|s| s.size == shoe_size).collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn filters_by_size() {
        let shoes = vec![
            Shoe {
                size: 10,
                style: String::from("sneaker"),
            },
            Shoe {
                size: 13,
                style: String::from("sandal"),
            },
            Shoe {
                size: 10,
                style: String::from("boot"),
            },
        ];

        let in_my_size = shoes_in_size(shoes, 10);

        assert_eq!(
            in_my_size,
            vec![
                Shoe {
                    size: 10,
                    style: String::from("sneaker")
                },
                Shoe {
                    size: 10,
                    style: String::from("boot")
                },
            ]
        );
    }
}
```

Listing 13-16: `shoe_size`를 캡처하는 클로저와 함께 `filter` 메서드 사용하기

`shoes_in_size` 함수는 신발 벡터와 신발 크기를 매개변수로 소유권을 가져옵니다. 지정된 크기의 신발만 포함하는 벡터를 반환합니다.

`shoes_in_size`의 본문에서 `into_iter`를 호출하여 벡터의 소유권을 가져가는 반복자를 생성합니다. 그런 다음 `filter`를 호출하여 해당 반복자를 클로저가 `true`를 반환하는 요소만 포함하는 새로운 반복자로 변환합니다.

클로저는 환경에서 `shoe_size` 매개변수를 캡처하고 해당 값을 각 신발의 크기와 비교하여 지정된 크기의 신발만 유지합니다. 마지막으로, `collect`를 호출하여 어댑터된 반복자가 반환한 값을 함수가 반환하는 벡터로 수집합니다.

테스트는 `shoes_in_size`를 호출하면 지정한 값과 동일한 크기의 신발만 반환받는다는 것을 보여줍니다.
