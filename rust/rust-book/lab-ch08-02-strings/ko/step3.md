# 새로운 문자열 생성하기

`String`은 실제로 몇 가지 추가적인 보장, 제한 및 기능을 갖춘 바이트 벡터의 래퍼로 구현되기 때문에, `Vec<T>`에서 사용할 수 있는 많은 동일한 연산이 `String`에서도 사용 가능합니다. `Vec<T>`와 `String`에서 동일하게 작동하는 함수의 예는 Listing 8-11 에 표시된 인스턴스를 생성하는 `new` 함수입니다.

```rust
let mut s = String::new();
```

Listing 8-11: 새로운 빈 `String` 생성하기

이 줄은 `s`라는 새로운 빈 문자열을 생성하며, 여기에 데이터를 로드할 수 있습니다. 종종, 문자열을 시작하려는 초기 데이터가 있을 것입니다. 이를 위해, 문자열 리터럴과 같이 `Display` 트레이트를 구현하는 모든 타입에서 사용할 수 있는 `to_string` 메서드를 사용합니다. Listing 8-12 는 두 가지 예를 보여줍니다.

```rust
let data = "initial contents";

let s = data.to_string();

// the method also works on a literal directly:
let s = "initial contents".to_string();
```

Listing 8-12: 문자열 리터럴로부터 `String`을 생성하기 위해 `to_string` 메서드 사용하기

이 코드는 `initial contents`를 포함하는 문자열을 생성합니다.

또한 `String::from` 함수를 사용하여 문자열 리터럴로부터 `String`을 생성할 수 있습니다. Listing 8-13 의 코드는 `to_string`을 사용하는 Listing 8-12 의 코드와 동일합니다.

```rust
let s = String::from("initial contents");
```

Listing 8-13: 문자열 리터럴로부터 `String`을 생성하기 위해 `String::from` 함수 사용하기

문자열은 매우 많은 용도로 사용되기 때문에, 우리는 문자열에 대해 다양한 제네릭 API 를 사용할 수 있으며, 이는 우리에게 많은 옵션을 제공합니다. 그 중 일부는 중복되어 보일 수 있지만, 모두 나름의 자리가 있습니다! 이 경우, `String::from`과 `to_string`은 동일한 작업을 수행하므로, 어떤 것을 선택할지는 스타일과 가독성의 문제입니다.

문자열은 UTF-8 로 인코딩되므로, Listing 8-14 에 표시된 것처럼 적절하게 인코딩된 모든 데이터를 포함할 수 있습니다.

```rust
let hello = String::from("السلام عليكم");
let hello = String::from("Dobrý den");
let hello = String::from("Hello");
let hello = String::from("שָׁלוֹם");
let hello = String::from("नमस्ते");
let hello = String::from("こんにちは");
let hello = String::from("안녕하세요");
let hello = String::from("你好");
let hello = String::from("Olá");
let hello = String::from("Здравствуйте");
let hello = String::from("Hola");
```

Listing 8-14: 다양한 언어로 된 인사를 문자열에 저장하기

이 모든 것은 유효한 `String` 값입니다.
