# 기본 요소 (Primitives)

Rust 는 다양한 `primitives`에 대한 접근을 제공합니다. 샘플은 다음과 같습니다.

## 스칼라 타입 (Scalar Types)

- 부호 있는 정수: `i8`, `i16`, `i32`, `i64`, `i128` 및 `isize` (포인터 크기)
- 부호 없는 정수: `u8`, `u16`, `u32`, `u64`, `u128` 및 `usize` (포인터 크기)
- 부동 소수점: `f32`, `f64`
- `char` 유니코드 스칼라 값, 예: `'a'`, `'α'` 및 `'∞'` (각 4 바이트)
- `bool`은 `true` 또는 `false`
- 유닛 타입 `()`, 유일한 가능한 값은 빈 튜플: `()`

유닛 타입의 값이 튜플임에도 불구하고, 여러 값을 포함하지 않기 때문에 복합 타입으로 간주되지 않습니다.

## 복합 타입 (Compound Types)

- `[1, 2, 3]`과 같은 배열 (Arrays)
- `(1, true)`와 같은 튜플 (Tuples)

변수는 항상 *타입 주석 (type annotated)*을 사용할 수 있습니다. 숫자는 _접미사 (suffix)_ 또는 *기본값 (by default)*을 통해 추가로 주석 처리될 수 있습니다. 정수는 기본적으로 `i32`이고 부동 소수점은 `f64`입니다. Rust 는 컨텍스트에서 타입을 추론할 수도 있습니다.

```rust
fn main() {
    // Variables can be type annotated.
    let logical: bool = true;

    let a_float: f64 = 1.0;  // Regular annotation
    let an_integer   = 5i32; // Suffix annotation

    // Or a default will be used.
    let default_float   = 3.0; // `f64`
    let default_integer = 7;   // `i32`

    // A type can also be inferred from context.
    let mut inferred_type = 12; // Type i64 is inferred from another line.
    inferred_type = 4294967296i64;

    // A mutable variable's value can be changed.
    let mut mutable = 12; // Mutable `i32`
    mutable = 21;

    // Error! The type of a variable can't be changed.
    mutable = true;

    // Variables can be overwritten with shadowing.
    let mutable = true;
}
```
