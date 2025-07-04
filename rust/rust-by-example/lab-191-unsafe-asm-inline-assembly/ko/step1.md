# 인라인 어셈블리

Rust 는 `asm!` 매크로를 통해 인라인 어셈블리를 지원합니다. 컴파일러가 생성하는 어셈블리 출력에 수작업으로 작성된 어셈블리를 포함시키는 데 사용할 수 있습니다. 일반적으로 이는 필요하지 않지만, 요구되는 성능이나 타이밍을 다른 방법으로 달성할 수 없는 경우에 사용될 수 있습니다. 예를 들어 커널 코드에서 하위 수준 하드웨어 원시 요소에 액세스하려면 이 기능이 필요할 수 있습니다.

> **참고**: 여기 예제는 x86/x86-64 어셈블리로 제공되지만 다른 아키텍처도 지원됩니다.

인라인 어셈블리는 다음 아키텍처에서 현재 지원됩니다.

- x86 및 x86-64
- ARM
- AArch64
- RISC-V

## 기본 사용법

가장 간단한 예제부터 시작해 보겠습니다.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

unsafe {
    asm!("nop");
}
# }
```

이것은 컴파일러가 생성하는 어셈블리에 NOP(No Operation) 명령어를 삽입합니다. 모든 `asm!` 호출은 임의의 명령어를 삽입하고 다양한 불변성을 위반할 수 있으므로 `unsafe` 블록 내에 있어야 합니다. 삽입할 명령어는 `asm!` 매크로의 첫 번째 인수로 문자열 리터럴로 나열됩니다.

## 입력 및 출력

이제 아무것도 하지 않는 명령어를 삽입하는 것은 다소 지루합니다. 실제로 데이터에 작용하는 작업을 해 보겠습니다.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let x: u64;
unsafe {
    asm!("mov {}, 5", out(reg) x);
}
assert_eq!(x, 5);
# }
```

이것은 `u64` 변수 `x`에 값 `5`를 씁니다. 명령어를 지정하기 위해 사용하는 문자열 리터럴은 실제로 템플릿 문자열입니다. Rust 형식 문자열과 동일한 규칙을 따릅니다. 그러나 템플릿에 삽입되는 인수는 익숙한 것과 약간 다릅니다. 먼저 변수가 인라인 어셈블리의 입력 또는 출력인지 지정해야 합니다. 이 경우 출력입니다. `out`을 써서 이를 선언했습니다. 또한 어셈블리가 변수를 기대하는 레지스터 유형을 지정해야 합니다. 이 경우 `reg`를 지정하여 임의의 일반 목적 레지스터에 넣습니다. 컴파일러는 템플릿에 삽입할 적절한 레지스터를 선택하고 인라인 어셈블리 실행이 끝난 후 해당 레지스터에서 변수를 읽습니다.

입력도 사용하는 또 다른 예를 살펴보겠습니다.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let i: u64 = 3;
let o: u64;
unsafe {
    asm!(
        "mov {0}, {1}",
        "add {0}, 5",
        out(reg) o,
        in(reg) i,
    );
}
assert_eq!(o, 8);
# }
```

이것은 입력 변수 `i`에 `5`를 더하고 결과를 변수 `o`에 씁니다. 이 어셈블리가 이 작업을 수행하는 특정 방법은 먼저 `i`의 값을 출력에 복사한 다음 `5`를 더하는 것입니다.

이 예제는 몇 가지 사항을 보여줍니다.

첫째, `asm!`는 여러 템플릿 문자열 인수를 허용합니다. 각각은 새 줄로 연결된 것처럼 별도의 어셈블리 코드 줄로 처리됩니다. 이렇게 하면 어셈블리 코드를 쉽게 형식화할 수 있습니다.

둘째, 입력은 `out` 대신 `in`을 써서 선언할 수 있습니다.

셋째, 모든 형식 문자열과 마찬가지로 인수 번호 또는 이름을 지정할 수 있습니다. 인라인 어셈블리 템플릿의 경우 인수가 여러 번 사용되는 경우가 많으므로 이 기능이 특히 유용합니다. 이 기능을 사용하면 가독성이 향상되고 인수 순서를 변경하지 않고도 명령어의 순서를 재정렬할 수 있습니다.

위의 예제를 더욱 개선하여 `mov` 명령어를 피할 수 있습니다.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut x: u64 = 3;
unsafe {
    asm!("add {0}, 5", inout(reg) x);
}
assert_eq!(x, 8);
# }
```

`inout`는 입력이자 출력인 인수를 지정하는 데 사용됩니다. 이는 입력과 출력을 별도로 지정하는 것과 달리 동일한 레지스터에 할당되는 것을 보장합니다.

입력 및 출력 부분에 대해 다른 변수를 지정하는 것도 가능합니다.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let x: u64 = 3;
let y: u64;
unsafe {
    asm!("add {0}, 5", inout(reg) x => y);
}
assert_eq!(y, 8);
# }
```

## 늦은 출력 피연산자

Rust 컴파일러는 피연산자 할당에 보수적입니다. `out`은 언제든지 쓸 수 있다고 가정하므로 다른 인수와 위치를 공유할 수 없습니다. 그러나 최적의 성능을 보장하려면 가능한 한 적은 레지스터를 사용하는 것이 중요합니다. 그렇지 않으면 인라인 어셈블리 블록 주변에서 레지스터를 저장하고 다시 로드해야 합니다. 이를 달성하기 위해 Rust 는 `lateout` 지정자를 제공합니다. 이는 모든 입력이 소비된 후에만 쓰이는 모든 출력에 사용할 수 있습니다. 이 지정자의 `inlateout` 변형도 있습니다.

여기서 `inlateout`을 `release` 모드 또는 다른 최적화된 경우에 사용할 수 없는 예제가 있습니다.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut a: u64 = 4;
let b: u64 = 4;
let c: u64 = 4;
unsafe {
    asm!(
        "add {0}, {1}",
        "add {0}, {2}",
        inout(reg) a,
        in(reg) b,
        in(reg) c,
    );
}
assert_eq!(a, 12);
# }
```

위의 코드는 최적화되지 않은 경우 (`Debug` 모드) 에 잘 작동할 수 있지만 최적화된 성능 (`release` 모드 또는 다른 최적화된 경우) 을 원한다면 작동하지 않을 수 있습니다.

이는 최적화된 경우 컴파일러가 입력 `b`와 `c`에 동일한 레지스터를 할당할 수 있기 때문입니다. 컴파일러는 `inout`가 아닌 `inlateout`이기 때문에 `a`에 대해 별도의 레지스터를 할당해야 합니다. `inlateout`이 사용된 경우 `a`와 `c`에 동일한 레지스터를 할당할 수 있습니다. 이 경우 `c`의 값을 덮어쓰는 첫 번째 명령어로 인해 어셈블리 코드가 잘못된 결과를 생성합니다.

그러나 출력이 모든 입력 레지스터가 읽힌 후에만 수정되는 다음 예제는 `inlateout`을 사용할 수 있습니다.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut a: u64 = 4;
let b: u64 = 4;
unsafe {
    asm!("add {0}, {1}", inlateout(reg) a, in(reg) b);
}
assert_eq!(a, 8);
# }
```

이 어셈블리 조각은 `a`와 `b`에 동일한 레지스터가 할당된 경우에도 여전히 올바르게 작동합니다.

## 명시적인 레지스터 피연산자

일부 명령어는 피연산자가 특정 레지스터에 있어야 합니다. 따라서 Rust 인라인 어셈블리는 더 구체적인 제약 지정자를 제공합니다. `reg`는 일반적으로 모든 아키텍처에서 사용할 수 있지만 명시적인 레지스터는 아키텍처에 따라 크게 다릅니다. 예를 들어 x86 의 경우 일반 목적 레지스터 `eax`, `ebx`, `ecx`, `edx`, `ebp`, `esi` 및 `edi` 등을 이름으로 참조할 수 있습니다.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let cmd = 0xd1;
unsafe {
    asm!("out 0x64, eax", in("eax") cmd);
}
# }
```

이 예제에서는 `out` 명령어를 호출하여 `cmd` 변수의 내용을 포트 `0x64`로 출력합니다. `out` 명령어는 `eax` (및 하위 레지스터) 만 피연산자로 허용하므로 `eax` 제약 지정자를 사용해야 했습니다.

> **참고**: 다른 피연산자 유형과 달리 명시적인 레지스터 피연산자는 템플릿 문자열에서 사용할 수 없습니다. `{}`를 사용할 수 없으며 대신 레지스터 이름을 직접 작성해야 합니다. 또한 다른 모든 피연산자 유형 뒤에 피연산자 목록의 끝에 나타나야 합니다.

x86 `mul` 명령어를 사용하는 다음 예제를 고려하십시오.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

fn mul(a: u64, b: u64) -> u128 {
    let lo: u64;
    let hi: u64;

    unsafe {
        asm!(
            // x86 mul 명령어는 rax 를 암시적 입력으로 사용하고
            // 곱셈의 128 비트 결과를 rax:rdx 에 씁니다.
            "mul {}",
            in(reg) a,
            inlateout("rax") b => lo,
            lateout("rdx") hi
        );
    }

    ((hi as u128) << 64) + lo as u128
}
# }
```

이것은 두 개의 64 비트 입력을 128 비트 결과로 곱하는 데 `mul` 명령어를 사용합니다. 유일한 명시적 피연산자는 변수 `a`에서 채우는 레지스터입니다. 두 번째 피연산자는 암시적이며 `rax` 레지스터여야 합니다. 이 레지스터는 변수 `b`에서 채웁니다. 결과의 하위 64 비트는 `rax`에 저장되며, 이를 통해 변수 `lo`를 채웁니다. 상위 64 비트는 `rdx`에 저장되며, 이를 통해 변수 `hi`를 채웁니다.

## 덮어쓰기 레지스터

많은 경우 인라인 어셈블리는 출력으로 필요하지 않은 상태를 수정합니다. 일반적으로 어셈블리에서 스크래치 레지스터를 사용해야 하거나 명령어가 더 이상 검사할 필요가 없는 상태를 수정하기 때문입니다. 이 상태는 일반적으로 "덮어쓰기"라고 합니다. 컴파일러는 인라인 어셈블리 블록 주변에서 이 상태를 저장하고 복원해야 할 수 있으므로 컴파일러에게 이에 대해 알려야 합니다.

```rust
use std::arch::asm;

# #[cfg(target_arch = "x86_64")]
fn main() {
    // 네 바이트씩 세 개의 항목
    let mut name_buf = [0_u8; 12];
    // 문자열은 ebx, edx, ecx 순서로 ascii 로 저장됩니다.
    // ebx 가 예약되어 있으므로 asm 은 그 값을 유지해야 합니다.
    // 따라서 주요 asm 주변에서 push 및 pop 합니다.
    // 64 비트 프로세서에서 64 비트 모드는
    // ebx 와 같은 32 비트 레지스터를 push/pop할 수 없습니다. 따라서 확장된 rbx 레지스터를 대신 사용해야 합니다.

    unsafe {
        asm!(
            "push rbx",
            "cpuid",
            "mov [rdi], ebx",
            "mov [rdi + 4], edx",
            "mov [rdi + 8], ecx",
            "pop rbx",
            // 값을 저장하기 위해 포인터 배열을 사용합니다.
            // 이는 몇 개의 asm 명령어를 더 사용하는 비용으로 Rust 코드를 단순화합니다.
            // 그러나 asm 이 작동하는 방식에 대해 더 명시적입니다.
            // `out("ecx") val`와 같은 명시적인 레지스터 출력과 달리
            // *포인터 자체*는 여러 개의 asm 명령어를 사용하더라도 입력일 뿐입니다.
            in("rdi") name_buf.as_mut_ptr(),
            // cpuid 0 선택, eax 도 덮어쓰기로 지정
            inout("eax") 0 => _,
            // cpuid 는 이 레지스터도 덮어씁니다.
            out("ecx") _,
            out("edx") _,
        );
    }

    let name = core::str::from_utf8(&name_buf).unwrap();
    println!("CPU 제조업체 ID: {}", name);
}

# #[cfg(not(target_arch = "x86_64"))]
# fn main() {}
```

위의 예제에서는 `cpuid` 명령어를 사용하여 CPU 제조업체 ID 를 읽습니다. 이 명령어는 `eax`에 최대 지원 `cpuid` 인수와 `ebx`, `edx`, `ecx`에 CPU 제조업체 ID 를 ASCII 바이트 순서대로 씁니다.

`eax`가 결코 읽히지 않더라도 컴파일러가 asm 이전에 이러한 레지스터에 있던 모든 값을 저장할 수 있도록 컴파일러에게 레지스터가 수정되었음을 알려야 합니다. 이는 출력 변수 대신 `_`를 사용하여 출력 값이 버려질 것을 나타내는 출력으로 선언하여 수행됩니다.

이 코드는 LLVM 에서 `ebx`가 예약된 레지스터라는 제한 사항을 우회합니다. 즉, LLVM 은 레지스터에 대한 완전한 제어권을 가정하고 asm 블록을 종료하기 전에 레지스터를 원래 상태로 복원해야 하므로 일반 레지스터 클래스 (예: `in(reg)`) 를 충족하는 데 사용할 수 없습니다. 이로 인해 예약된 레지스터를 사용할 때 `reg` 피연산자가 위험해집니다. 컴파일러가 이를 사용하여 일반 레지스터 클래스를 충족하는 경우를 제외하고는 입력 또는 출력을 알지 못하고 손상시킬 수 있습니다.

이를 우회하기 위해 `rdi`를 출력 배열의 포인터에 저장하고 `push`를 통해 `ebx`를 저장하고 asm 블록 내에서 `ebx`에서 배열로 읽고 `pop`을 통해 `ebx`를 원래 상태로 복원합니다. `push` 및 `pop`은 레지스터 전체를 저장하도록 64 비트 `rbx` 버전의 레지스터를 사용합니다. 32 비트 대상에서는 코드가 대신 `push`/`pop`에서 `ebx`를 사용합니다.

이를 일반 레지스터 클래스와 함께 사용하여 asm 코드 내에서 스크래치 레지스터를 얻을 수도 있습니다.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

// x 를 6 으로 곱합니다.
let mut x: u64 = 4;
unsafe {
    asm!(
        "mov {tmp}, {x}",
        "shl {tmp}, 1",
        "shl {x}, 2",
        "add {x}, {tmp}",
        x = inout(reg) x,
        tmp = out(reg) _,
    );
}
assert_eq!(x, 4 * 6);
# }
```

## 심볼 피연산자 및 ABI 덮어쓰기

기본적으로 `asm!`는 출력으로 지정되지 않은 모든 레지스터의 내용이 어셈블리 코드에 의해 보존될 것이라고 가정합니다. `asm!`의 `[clobber_abi]` 인수는 지정된 호출 규약 ABI 에 따라 필요한 덮어쓰기 피연산자를 자동으로 삽입하도록 컴파일러에게 알립니다. 해당 ABI 에서 완전히 보존되지 않는 레지스터는 덮어쓰기로 처리됩니다. 여러 `clobber_abi` 인수를 제공할 수 있으며 모든 지정된 ABI 의 모든 덮어쓰기가 삽입됩니다.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

extern "C" fn foo(arg: i32) -> i32 {
    println!("arg = {}", arg);
    arg * 2
}

fn call_foo(arg: i32) -> i32 {
    unsafe {
        let result;
        asm!(
            "call {}",
            // 호출할 함수 포인터
            in(reg) foo,
            // 첫 번째 인수는 rdi
            in("rdi") arg,
            // 반환 값은 rax
            out("rax") result,
            // "C" 호출 규약에 의해 보존되지 않는 모든 레지스터를 덮어쓰기로 표시합니다.
            clobber_abi("C"),
        );
        result
    }
}
# }
```

## 레지스터 템플릿 수정자

일부 경우 레지스터 이름이 템플릿 문자열에 삽입되는 방식에 대한 세부 제어가 필요합니다. 이는 아키텍처의 어셈블리 언어에 동일한 레지스터에 대한 여러 이름이 있고 각각 일반적으로 레지스터의 하위 집합에 대한 "뷰"(예: 64 비트 레지스터의 하위 32 비트) 인 경우에 필요합니다.

기본적으로 컴파일러는 항상 전체 레지스터 크기를 참조하는 이름 (예: x86-64 의 `rax`, x86 의 `eax` 등) 을 선택합니다.

이 기본값은 템플릿 문자열 피연산자에 수정자를 사용하여 재정의할 수 있습니다. 형식 문자열과 마찬가지입니다.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut x: u16 = 0xab;

unsafe {
    asm!("mov {0:h}, {0:l}", inout(reg_abcd) x);
}

assert_eq!(x, 0xabab);
# }
```

이 예제에서는 `reg_abcd` 레지스터 클래스를 사용하여 레지스터 할당기를 4 개의 레거시 x86 레지스터 (`ax`, `bx`, `cx`, `dx`) 로 제한합니다. 이 레지스터의 첫 두 바이트는 독립적으로 참조할 수 있습니다.

레지스터 할당기가 `ax` 레지스터에 `x`를 할당했다고 가정합니다. `h` 수정자는 해당 레지스터의 상위 바이트에 대한 레지스터 이름을 생성하고 `l` 수정자는 하위 바이트에 대한 레지스터 이름을 생성합니다. 따라서 asm 코드는 `mov ah, al`로 확장되어 값의 하위 바이트를 상위 바이트로 복사합니다.

작은 데이터 유형 (예: `u16`) 을 피연산자와 함께 사용하고 템플릿 수정자를 사용하지 않으면 컴파일러가 경고를 표시하고 사용할 올바른 수정자를 제안합니다.

## 메모리 주소 피연산자

때로는 어셈블리 명령어에 메모리 주소/메모리 위치를 통해 전달되는 피연산자가 필요합니다. 대상 아키텍처에서 지정한 메모리 주소 구문을 수동으로 사용해야 합니다. 예를 들어 x86/x86_64에서 Intel 어셈블리 구문을 사용하는 경우 입력/출력을 `[]`로 묶어 메모리 피연산자임을 나타내야 합니다.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

fn load_fpu_control_word(control: u16) {
    unsafe {
        asm!("fldcw [{}]", in(reg) &control, options(nostack));
    }
}
# }
```

## 레이블

명시적이든 지역적이든 이름이 지정된 레이블의 재사용은 어셈블러 또는 링커 오류를 발생시키거나 다른 이상한 동작을 유발할 수 있습니다. 이름이 지정된 레이블의 재사용은 다음과 같은 다양한 방법으로 발생할 수 있습니다.

- 명시적으로: 하나의 `asm!` 블록에서 레이블을 여러 번 사용하거나 여러 블록에서 여러 번 사용합니다.
- 인라인을 통해 암시적으로: 컴파일러는 함수가 여러 곳에서 인라인될 수 있으므로 `asm!` 블록의 여러 복사본을 인스턴스화할 수 있습니다.
- LTO 를 통해 암시적으로: LTO 는 다른 크레이트의 코드를 동일한 코드 생성 단위에 배치할 수 있으므로 임의의 레이블을 가져올 수 있습니다.

따라서 인라인 어셈블리 코드 내에서 GNU 어셈블러 **숫자** \[로컬 레이블]만 사용해야 합니다. 어셈블리 코드에서 심볼을 정의하면 중복 심볼 정의로 인해 어셈블러 및/또는 링커 오류가 발생할 수 있습니다.

또한 x86 에서 기본 Intel 구문을 사용하는 경우 \[LLVM 버그]로 인해 `0`, `11` 또는 `101010`와 같이 `0`과 `1` 자릿수로만 구성된 레이블을 사용해서는 안 됩니다. 이러한 레이블은 이진 값으로 해석될 수 있습니다. `options(att_syntax)`를 사용하면 모호성을 피할 수 있지만 이는 _전체_ `asm!` 블록의 구문에 영향을 미칩니다. (옵션에 대한 자세한 내용은 아래 옵션을 참조하십시오.)

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut a = 0;
unsafe {
    asm!(
        "mov {0}, 10",
        "2:",
        "sub {0}, 1",
        "cmp {0}, 3",
        "jle 2f",
        "jmp 2b",
        "2:",
        "add {0}, 2",
        out(reg) a
    );
}
assert_eq!(a, 5);
# }
```

이렇게 하면 `{0}` 레지스터 값을 10 에서 3 으로 감소시킨 다음 2 를 더하고 `a`에 저장합니다.

이 예제는 몇 가지 사항을 보여줍니다.

- 동일한 숫자를 동일한 인라인 블록에서 여러 번 레이블로 사용할 수 있습니다.
- 숫자 레이블이 참조로 사용될 때 (예: 명령어 피연산자로) 접미사 "b"("역방향") 또는 "f"("정방향") 를 숫자 레이블에 추가해야 합니다. 그러면 이 방향의 이 숫자로 정의된 가장 가까운 레이블을 참조합니다.

## 옵션

기본적으로 인라인 어셈블리 블록은 사용자 지정 호출 규약이 있는 외부 FFI 함수 호출과 동일하게 처리됩니다. 메모리를 읽거나 쓸 수 있고 관찰 가능한 부작용이 있을 수 있습니다. 그러나 많은 경우 컴파일러가 어셈블리 코드가 실제로 수행하는 작업에 대한 더 많은 정보를 제공하여 최적화를 개선하는 것이 바람직합니다.

`add` 명령어의 이전 예제를 살펴보겠습니다.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut a: u64 = 4;
let b: u64 = 4;
unsafe {
    asm!(
        "add {0}, {1}",
        inlateout(reg) a, in(reg) b,
        options(pure, nomem, nostack),
    );
}
assert_eq!(a, 8);
# }
```

옵션은 `asm!` 매크로에 선택적 마지막 인수로 제공할 수 있습니다. 여기서 세 가지 옵션을 지정했습니다.

- `pure`는 asm 코드에 관찰 가능한 부작용이 없고 출력이 입력에만 의존한다는 것을 의미합니다. 이를 통해 컴파일러 최적화기는 인라인 asm 을 덜 호출하거나 완전히 제거할 수 있습니다.
- `nomem`은 asm 코드가 메모리를 읽거나 쓰지 않는다는 것을 의미합니다. 기본적으로 컴파일러는 인라인 어셈블리가 피연산자로 전달된 포인터 또는 전역을 통해 액세스할 수 있는 모든 메모리 주소를 읽거나 쓸 수 있다고 가정합니다.
- `nostack`은 asm 코드가 스택에 데이터를 푸시하지 않는다는 것을 의미합니다. 이를 통해 컴파일러는 x86-64 의 스택 레드 존과 같은 최적화를 사용하여 스택 포인터 조정을 피할 수 있습니다.

이러한 옵션을 통해 컴파일러는 `asm!`를 사용하는 코드를 더 잘 최적화할 수 있습니다. 예를 들어 출력이 필요하지 않은 순수 `asm!` 블록을 제거할 수 있습니다.

사용 가능한 옵션 및 효과에 대한 전체 목록은 참조를 참조하십시오.
