# 사용자 정의 derive 매크로 작성 방법

`hello_macro`라는 크레이트를 생성하여 `hello_macro`라는 연관 함수가 하나 있는 `HelloMacro`라는 트레이트를 정의해 보겠습니다. 사용자가 각 타입에 대해 `HelloMacro` 트레이트를 구현하는 대신, 사용자가 `#[derive(HelloMacro)]`로 타입을 주석 처리하여 `hello_macro` 함수의 기본 구현을 얻을 수 있도록 절차적 매크로를 제공할 것입니다. 기본 구현은 `Hello, Macro! My name is` TypeName`!`을 출력합니다. 여기서 TypeName 은 이 트레이트가 정의된 타입의 이름입니다. 즉, 다른 프로그래머가 우리의 크레이트를 사용하여 Listing 19-30 과 같은 코드를 작성할 수 있도록 하는 크레이트를 작성할 것입니다.

Filename: `src/main.rs`

```rust
use hello_macro::HelloMacro;
use hello_macro_derive::HelloMacro;

#[derive(HelloMacro)]
struct Pancakes;

fn main() {
    Pancakes::hello_macro();
}
```

Listing 19-30: 우리의 크레이트 사용자가 절차적 매크로를 사용할 때 작성할 수 있는 코드

이 코드는 완료되면 `Hello, Macro! My name is Pancakes!`를 출력합니다. 첫 번째 단계는 다음과 같이 새로운 라이브러리 크레이트를 만드는 것입니다.

```bash
cargo new hello_macro --lib
```

다음으로, `HelloMacro` 트레이트와 연관 함수를 정의합니다.

Filename: `src/lib.rs`

```rust
pub trait HelloMacro {
    fn hello_macro();
}
```

트레이트와 해당 함수가 있습니다. 이 시점에서 크레이트 사용자는 원하는 기능을 달성하기 위해 트레이트를 구현할 수 있습니다.

```rust
use hello_macro::HelloMacro;

struct Pancakes;

impl HelloMacro for Pancakes {
    fn hello_macro() {
        println!("Hello, Macro! My name is Pancakes!");
    }
}

fn main() {
    Pancakes::hello_macro();
}
```

그러나 `hello_macro`와 함께 사용하려는 각 타입에 대해 구현 블록을 작성해야 합니다. 우리는 그들이 이 작업을 수행할 필요가 없도록 하고 싶습니다.

또한, 트레이트가 구현된 타입의 이름을 출력하는 기본 구현으로 `hello_macro` 함수를 아직 제공할 수 없습니다. Rust 에는 리플렉션 기능이 없으므로 런타임에 타입의 이름을 조회할 수 없습니다. 컴파일 시간에 코드를 생성하는 매크로가 필요합니다.

다음 단계는 절차적 매크로를 정의하는 것입니다. 이 글을 쓰는 시점에서 절차적 매크로는 자체 크레이트에 있어야 합니다. 결국 이 제한은 해제될 수 있습니다. 크레이트와 매크로 크레이트를 구조화하는 규칙은 다음과 같습니다. foo 라는 크레이트의 경우 사용자 정의 `derive` 절차적 매크로 크레이트는 foo`_derive`라고 합니다. `hello_macro` 프로젝트 내에서 `hello_macro_derive`라는 새 크레이트를 시작해 보겠습니다.

```bash
cargo new hello_macro_derive --lib
```

두 크레이트는 밀접하게 관련되어 있으므로 `hello_macro` 크레이트의 디렉토리 내에서 절차적 매크로 크레이트를 생성합니다. `hello_macro`에서 트레이트 정의를 변경하면 `hello_macro_derive`에서 절차적 매크로의 구현도 변경해야 합니다. 두 크레이트는 별도로 게시해야 하며, 이러한 크레이트를 사용하는 프로그래머는 둘 다 종속성으로 추가하고 둘 다 범위 내로 가져와야 합니다. 대신 `hello_macro` 크레이트가 `hello_macro_derive`를 종속성으로 사용하고 절차적 매크로 코드를 다시 내보내도록 할 수 있습니다. 그러나 우리가 프로젝트를 구조화한 방식은 프로그래머가 `derive` 기능을 원하지 않더라도 `hello_macro`를 사용할 수 있도록 합니다.

`hello_macro_derive` 크레이트를 절차적 매크로 크레이트로 선언해야 합니다. 또한 잠시 후에 보게 될 `syn` 및 `quote` 크레이트의 기능이 필요하므로 이를 종속성으로 추가해야 합니다. `hello_macro_derive`의 `Cargo.toml` 파일에 다음을 추가합니다.

Filename: `hello_macro_derive/Cargo.toml`

```toml
[lib]
proc-macro = true

[dependencies]
syn = "1.0"
quote = "1.0"
```

절차적 매크로 정의를 시작하려면 Listing 19-31 의 코드를 `hello_macro_derive` 크레이트의 `src/lib.rs` 파일에 넣습니다. `impl_hello_macro` 함수에 대한 정의를 추가할 때까지 이 코드는 컴파일되지 않습니다.

Filename: `hello_macro_derive/src/lib.rs`

```rust
use proc_macro::TokenStream;
use quote::quote;
use syn;

#[proc_macro_derive(HelloMacro)]
pub fn hello_macro_derive(input: TokenStream) -> TokenStream {
    // Construct a representation of Rust code as a syntax tree
    // that we can manipulate
    let ast = syn::parse(input).unwrap();

    // Build the trait implementation
    impl_hello_macro(&ast)
}
```

Listing 19-31: 대부분의 절차적 매크로 크레이트가 Rust 코드를 처리하는 데 필요한 코드

`TokenStream`을 구문 분석하는 역할을 하는 `hello_macro_derive` 함수와 구문 트리를 변환하는 역할을 하는 `impl_hello_macro` 함수로 코드를 분할했음을 알 수 있습니다. 이렇게 하면 절차적 매크로를 더 편리하게 작성할 수 있습니다. 외부 함수 (이 경우 `hello_macro_derive`) 의 코드는 거의 모든 절차적 매크로 크레이트에서 동일합니다. 내부 함수 (이 경우 `impl_hello_macro`) 의 본문에 지정하는 코드는 절차적 매크로의 목적에 따라 다릅니다.

`proc_macro`, `syn`(*https://crates.io/crates/syn*에서 사용 가능) 및 `quote`(*https://crates.io/crates/quote*에서 사용 가능) 의 세 가지 새로운 크레이트를 소개했습니다. `proc_macro` 크레이트는 Rust 와 함께 제공되므로 `Cargo.toml`의 종속성에 추가할 필요가 없었습니다. `proc_macro` 크레이트는 코드에서 Rust 코드를 읽고 조작할 수 있도록 하는 컴파일러의 API 입니다.

`syn` 크레이트는 문자열에서 Rust 코드를 구문 분석하여 작업을 수행할 수 있는 데이터 구조로 변환합니다. `quote` 크레이트는 `syn` 데이터 구조를 다시 Rust 코드로 변환합니다. 이러한 크레이트는 처리하려는 모든 종류의 Rust 코드를 구문 분석하는 것을 훨씬 더 간단하게 만듭니다. Rust 코드에 대한 전체 파서를 작성하는 것은 간단한 작업이 아닙니다.

우리 라이브러리의 사용자가 타입에 `#[derive(HelloMacro)]`를 지정하면 `hello_macro_derive` 함수가 호출됩니다. 이는 `hello_macro_derive` 함수에 `proc_macro_derive`를 주석 처리하고 트레이트 이름과 일치하는 `HelloMacro` 이름을 지정했기 때문에 가능합니다. 이것이 대부분의 절차적 매크로가 따르는 규칙입니다.

`hello_macro_derive` 함수는 먼저 `input`을 `TokenStream`에서 우리가 해석하고 작업을 수행할 수 있는 데이터 구조로 변환합니다. 이것이 `syn`이 사용되는 곳입니다. `syn`의 `parse` 함수는 `TokenStream`을 가져와 구문 분석된 Rust 코드를 나타내는 `DeriveInput` 구조체를 반환합니다. Listing 19-32 는 `struct Pancakes;` 문자열을 구문 분석하여 얻은 `DeriveInput` 구조체의 관련 부분을 보여줍니다.

    DeriveInput {
        --snip--

        ident: Ident {
            ident: "Pancakes",
            span: #0 bytes(95..103)
        },
        data: Struct(
            DataStruct {
                struct_token: Struct,
                fields: Unit,
                semi_token: Some(
                    Semi
                )
            }
        )
    }

Listing 19-32: Listing 19-30 에서 매크로의 속성이 있는 코드를 구문 분석할 때 얻는 `DeriveInput` 인스턴스

이 구조체의 필드는 구문 분석한 Rust 코드가 `Pancakes`의 `ident`(_식별자_, 즉 이름) 를 가진 unit struct 임을 보여줍니다. 모든 종류의 Rust 코드를 설명하는 이 구조체에는 더 많은 필드가 있습니다. 자세한 내용은 *https://docs.rs/syn/1.0/syn/struct.DeriveInput.html*에서 `DeriveInput`에 대한 `syn` 문서를 확인하십시오.

곧 포함하려는 새로운 Rust 코드를 빌드할 `impl_hello_macro` 함수를 정의할 것입니다. 그러나 그 전에 `derive` 매크로의 출력도 `TokenStream`임을 기억하십시오. 반환된 `TokenStream`은 크레이트 사용자가 작성하는 코드에 추가되므로 크레이트를 컴파일할 때 수정된 `TokenStream`에서 제공하는 추가 기능을 얻게 됩니다.

`syn::parse` 함수에 대한 호출이 실패하면 `hello_macro_derive` 함수가 패닉을 발생시키기 위해 `unwrap`을 호출하고 있음을 알 수 있습니다. `proc_macro_derive` 함수는 절차적 매크로 API 를 준수하기 위해 `Result`가 아닌 `TokenStream`을 반환해야 하므로 절차적 매크로가 오류 시 패닉을 발생시키는 것이 필요합니다. `unwrap`을 사용하여 이 예제를 단순화했습니다. 프로덕션 코드에서는 `panic!` 또는 `expect`를 사용하여 무엇이 잘못되었는지에 대한 더 구체적인 오류 메시지를 제공해야 합니다.

이제 주석 처리된 Rust 코드를 `TokenStream`에서 `DeriveInput` 인스턴스로 변환하는 코드가 있으므로 Listing 19-33 에 표시된 대로 주석 처리된 타입에 대해 `HelloMacro` 트레이트를 구현하는 코드를 생성해 보겠습니다.

Filename: `hello_macro_derive/src/lib.rs`

```rust
fn impl_hello_macro(ast: &syn::DeriveInput) -> TokenStream {
    let name = &ast.ident;
    let gen = quote! {
        impl HelloMacro for #name {
            fn hello_macro() {
                println!(
                    "Hello, Macro! My name is {}!",
                    stringify!(#name)
                );
            }
        }
    };
    gen.into()
}
```

Listing 19-33: 구문 분석된 Rust 코드를 사용하여 `HelloMacro` 트레이트 구현

`ast.ident`를 사용하여 주석 처리된 타입의 이름 (식별자) 을 포함하는 `Ident` 구조체 인스턴스를 가져옵니다. Listing 19-32 의 구조체는 Listing 19-30 의 코드에서 `impl_hello_macro` 함수를 실행하면 얻는 `ident`가 `"Pancakes"`의 값을 가진 `ident` 필드를 갖게 됨을 보여줍니다. 따라서 Listing 19-33 의 `name` 변수는 출력 시 Listing 19-30 의 구조체 이름인 문자열 `"Pancakes"`가 될 `Ident` 구조체 인스턴스를 포함합니다.

`quote!` 매크로를 사용하면 반환하려는 Rust 코드를 정의할 수 있습니다. 컴파일러는 `quote!` 매크로 실행의 직접적인 결과와 다른 것을 예상하므로 이를 `TokenStream`으로 변환해야 합니다. `into` 메서드를 호출하여 이 중간 표현을 사용하고 필요한 `TokenStream` 타입의 값을 반환하여 이를 수행합니다.

`quote!` 매크로는 또한 매우 멋진 템플릿 메커니즘을 제공합니다. `#name`을 입력할 수 있으며 `quote!`는 이를 `name` 변수의 값으로 대체합니다. 일반 매크로가 작동하는 방식과 유사한 반복도 수행할 수 있습니다. 자세한 소개는 *https://docs.rs/quote*에서 `quote` 크레이트의 문서를 확인하십시오.

사용자가 주석 처리한 타입에 대해 `HelloMacro` 트레이트의 구현을 생성하도록 절차적 매크로를 원합니다. 이는 `#name`을 사용하여 얻을 수 있습니다. 트레이트 구현에는 우리가 제공하려는 기능, 즉 `Hello, Macro! My name is`를 출력한 다음 주석 처리된 타입의 이름을 포함하는 하나의 함수 `hello_macro`가 있습니다.

여기서 사용된 `stringify!` 매크로는 Rust 에 내장되어 있습니다. `1 + 2`와 같은 Rust 표현식을 가져와 컴파일 시간에 해당 표현식을 `"1 + 2"`와 같은 문자열 리터럴로 변환합니다. 이것은 표현식을 평가한 다음 결과를 `String`으로 변환하는 `format!` 또는 `println!` 매크로와 다릅니다. `#name` 입력이 문자 그대로 출력할 표현식일 가능성이 있으므로 `stringify!`를 사용합니다. `stringify!`를 사용하면 컴파일 시간에 `#name`을 문자열 리터럴로 변환하여 할당을 절약할 수도 있습니다.

이 시점에서 `cargo build`는 `hello_macro`와 `hello_macro_derive` 모두에서 성공적으로 완료되어야 합니다. Listing 19-30 의 코드에 이러한 크레이트를 연결하여 절차적 매크로가 작동하는 것을 살펴보겠습니다! `project` 디렉토리에서 `cargo new pancakes`를 사용하여 새 바이너리 프로젝트를 만듭니다. `pancakes` 크레이트의 `Cargo.toml`에 `hello_macro`와 `hello_macro_derive`를 종속성으로 추가해야 합니다. `hello_macro`와 `hello_macro_derive`의 버전을 *https://crates.io*에 게시하는 경우 일반 종속성이 됩니다. 그렇지 않은 경우 다음과 같이 `path` 종속성으로 지정할 수 있습니다.

    [dependencies]
    hello_macro = { path = "../hello_macro" }
    hello_macro_derive = { path = "../hello_macro/hello_macro_derive" }

Listing 19-30 의 코드를 `src/main.rs`에 넣고 `cargo run`을 실행합니다. `Hello, Macro! My name is Pancakes!`가 출력되어야 합니다. 절차적 매크로에서 `HelloMacro` 트레이트의 구현은 `pancakes` 크레이트가 이를 구현할 필요 없이 포함되었습니다. `#[derive(HelloMacro)]`는 트레이트 구현을 추가했습니다.

다음으로, 다른 종류의 절차적 매크로가 사용자 정의 `derive` 매크로와 어떻게 다른지 살펴보겠습니다.
