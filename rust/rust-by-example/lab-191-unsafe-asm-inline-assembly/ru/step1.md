# Встроенный ассемблер

Rust поддерживает встроенный ассемблер с помощью макроса `asm!`. Его можно использовать для встраивания ручного ассемблера в выходной код, сгенерированный компилятором. Как правило, этого не нужно, но это может быть полезно, когда требуемая производительность или точность времени не могут быть достигнуты иным способом. Доступ к низкоуровневым примитивам аппаратуры, например, в коде ядра, также может требовать этой функциональности.

> **Примечание**: примеры здесь даны в ассемблере x86/x86-64, но другие архитектуры также поддерживаются.

Встроенный ассемблер в настоящее время поддерживается на следующих архитектурах:

- x86 и x86-64
- ARM
- AArch64
- RISC-V

## Базовое использование

Начнем с самого простого примера:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

unsafe {
    asm!("nop");
}
# }
```

Это вставит инструкцию NOP (no operation) в ассемблерный код, сгенерированный компилятором. Обратите внимание, что все вызовы `asm!` должны быть внутри блока `unsafe`, так как они могут вставлять произвольные инструкции и нарушать различные инварианты. Инструкции, которые нужно вставить, перечисляются в первом аргументе макроса `asm!` в виде строкового литерала.

## Входы и выходы

Теперь вставлять инструкцию, которая ничего не делает, довольно скучно. Давайте что-нибудь сделаем, что будет действовать на данные:

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

Это запишет значение `5` в переменную `u64` `x`. Можно увидеть, что строковый литерал, который мы используем для указания инструкций, на самом деле является шаблонной строкой. Он подчиняется тем же правилам, что и строки форматирования Rust. Однако аргументы, которые вставляются в шаблон, выглядят немного по-другому, чем вы, возможно, привыкли. Во-первых, нужно указать, является ли переменная входом или выходом встроенного ассемблера. В этом случае это выход. Мы объявили это, написав `out`. Также нужно указать, в каком типе регистра ассемблер ожидает переменную. В этом случае мы поместили ее в произвольный общийPurpose register, указав `reg`. Компилятор выберет подходящий регистр для вставки в шаблон и прочитает переменную из него после завершения выполнения встроенного ассемблера.

Давайте рассмотрим еще один пример, который также использует вход:

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

Это добавит `5` к входу в переменной `i` и запишет результат в переменную `o`. Особый способ, которым этот ассемблер делает это, заключается в том, что сначала копирует значение из `i` в выход, а затем добавляет `5` к нему.

Пример показывает несколько вещей:

Во-первых, можно увидеть, что `asm!` позволяет использовать несколько аргументов шаблонной строки; каждый из них обрабатывается как отдельная строка ассемблерного кода, как будто они все были объединены с помощью переводов строки между ними. Это делает форматирование ассемблерного кода удобным.

Во-вторых, можно увидеть, что входы объявляются с помощью `in` вместо `out`.

В-третьих, можно увидеть, что можно указать номер аргумента или имя, как в любой строке форматирования. Для шаблонов встроенного ассемблера это особенно полезно, так как аргументы часто используются более одного раза. Для более сложного встроенного ассемблера обычно рекомендуется использовать эту возможность, так как это улучшает читаемость и позволяет переупорядочивать инструкции без изменения порядка аргументов.

Мы можем дальнейшим образом усовершенствовать вышеуказанный пример, чтобы избежать инструкции `mov`:

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

Можно увидеть, что `inout` используется для указания аргумента, который является и входом, и выходом. Это отличается от отдельного указания входа и выхода тем, что гарантируется, что оба будут присвоены тому же регистру.

Также можно указать разные переменные для входной и выходной частей операнда `inout`:

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

## Операнды позднего вывода

Компилятор Rust консервативен при распределении операндов. Предполагается, что `out` может быть записан в любое время, и поэтому не может делиться своим расположением с любым другим аргументом. Однако, чтобы гарантировать оптимальную производительность, важно использовать как можно меньше регистров, чтобы не приходилось сохранять и перезагружать их вокруг блока встроенного ассемблера. Для этого Rust предоставляет спецификатор `lateout`. Его можно использовать для любого вывода, который записывается только после того, как все входы будут обработаны. Также есть вариант `inlateout` этого спецификатора.

Вот пример, где `inlateout` _не может_ быть использован в режиме `release` или других оптимизированных случаях:

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

Вышеописанный пример может хорошо работать в неоптимизированных случаях (`Debug`-режим), но если вы хотите получить оптимизированную производительность (`release`-режим или другие оптимизированные случаи), он может не работать.

Это происходит потому, что в оптимизированных случаях компилятор может свободно распределить один и тот же регистр для входов `b` и `c`, так как он знает, что они имеют одинаковые значения. Однако он должен выделить отдельный регистр для `a`, так как он использует `inout`, а не `inlateout`. Если бы использовался `inlateout`, то `a` и `c` могли бы быть выделены в один и тот же регистр, в этом случае первая инструкция, которая перезаписывает значение `c`, и при этом приводит к тому, что ассемблерный код будет выдавать неправильный результат.

Однако следующий пример может использовать `inlateout`, так как выход модифицируется только после того, как все входные регистры будут прочитаны:

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

Как можно видеть, этот фрагмент ассемблера по-прежнему будет работать правильно, если `a` и `b` будут присвоены одному и тому же регистру.

## Явные операнды регистров

Некоторые инструкции требуют, чтобы операнды были в определенном регистре. Поэтому встроенный ассемблер Rust предоставляет несколько более специфических спецификаторов ограничений. Хотя `reg` обычно доступен на любой архитектуре, явные регистры зависят от архитектуры. Например, для x86 общиеPurpose регистры `eax`, `ebx`, `ecx`, `edx`, `ebp`, `esi` и `edi` могут быть адресованы по имени.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let cmd = 0xd1;
unsafe {
    asm!("out 0x64, eax", in("eax") cmd);
}
# }
```

В этом примере мы вызываем инструкцию `out` для вывода содержимого переменной `cmd` в порт `0x64`. Поскольку инструкция `out` принимает только `eax` (и его подрегистры) в качестве операнда, мы должны были использовать спецификатор ограничений `eax`.

> **Примечание**: в отличие от других типов операндов, явные операнды регистров не могут быть использованы в шаблонной строке: нельзя использовать `{}` и нужно вместо этого писать имя регистра напрямую. Также они должны появляться в конце списка операндов после всех других типов операндов.

Рассмотрим этот пример, который использует инструкцию `mul` x86:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

fn mul(a: u64, b: u64) -> u128 {
    let lo: u64;
    let hi: u64;

    unsafe {
        asm!(
            // Инструкция mul x86 принимает rax в качестве неявного входа и записывает
            // 128-битный результат умножения в rax:rdx.
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

Это использует инструкцию `mul` для умножения двух 64-битных входов с 128-битным результатом. Единственный явный операнд - это регистр, который мы заполняем из переменной `a`. Второй операнд неявный и должен быть регистром `rax`, который мы заполняем из переменной `b`. Нижние 64 бита результата хранятся в `rax`, из которого мы заполняем переменную `lo`. Верхние 64 бита хранятся в `rdx`, из которого мы заполняем переменную `hi`.

## Замаскированные регистры

В многих случаях встроенный ассемблер будет модифицировать состояние, которое не нужно в качестве вывода. Обычно это происходит потому, что мы должны использовать временный регистр в ассемблере или потому, что инструкции модифицируют состояние, которое мы не хотим дальнейшим образом исследовать. Это состояние обычно называется "замаскированным". Мы должны сообщить компилятору об этом, так как он может потребовать сохранить и восстановить это состояние вокруг блока встроенного ассемблера.

```rust
use std::arch::asm;

# #[cfg(target_arch = "x86_64")]
fn main() {
    // Три записи по четыре байта каждый
    let mut name_buf = [0_u8; 12];
    // Строка хранится в виде ASCII в ebx, edx, ecx в этом порядке
    // Поскольку ebx зарезервирован, ассемблер должен сохранить значение его.
    // Поэтому мы помещаем его на стек и извлекаем перед основным ассемблером.
    // 64-битный режим на 64-битных процессорах не позволяет помещать/извлекать
    // 32-битные регистры (как ebx), поэтому мы должны использовать расширенный регистр rbx вместо этого.

    unsafe {
        asm!(
            "push rbx",
            "cpuid",
            "mov [rdi], ebx",
            "mov [rdi + 4], edx",
            "mov [rdi + 8], ecx",
            "pop rbx",
            // Мы используем указатель на массив для хранения значений, чтобы упростить
            // Rust-код, в代价 более длинного ассемблерного кода
            // Это более явно показывает, как работает ассемблер, в отличие от
            // явных регистровых выводов, таких как `out("ecx") val`
            // Сам *указатель* является только входом, хотя он записывается позже
            in("rdi") name_buf.as_mut_ptr(),
            // Выбираем cpuid 0, также указываем eax как замаскированный
            inout("eax") 0 => _,
            // cpuid также замаскирует эти регистры
            out("ecx") _,
            out("edx") _,
        );
    }

    let name = core::str::from_utf8(&name_buf).unwrap();
    println!("CPU Manufacturer ID: {}", name);
}

# #[cfg(not(target_arch = "x86_64"))]
# fn main() {}
```

В приведенном выше примере мы используем инструкцию `cpuid` для чтения идентификатора производителя CPU. Эта инструкция записывает в `eax` максимально поддерживаемый аргумент `cpuid` и в `ebx`, `edx` и `ecx` идентификатор производителя CPU в виде ASCII-байтов в этом порядке.

Даже если `eax` никогда не читается, мы по-прежнему должны сообщить компилятору, что регистр был модифицирован, чтобы компилятор мог сохранить любые значения, которые были в этих регистрах до выполнения ассемблера. Это делается путем объявления его как вывод, но с `_` вместо имени переменной, что означает, что значение вывода должно быть проигнорировано.

Этот код также обходит ограничение, что `ebx` является зарезервированным регистром в LLVM. Это означает, что LLVM предполагает, что имеет полный контроль над регистром и его состояние должно быть восстановлено до исходного перед выходом из блока ассемблера, поэтому его нельзя использовать в качестве входа или выхода **за исключением** случаев, когда компилятор использует его для заполнения общего класса регистров (например, `in(reg)`). Это делает операнды `reg` опасными при использовании зарезервированных регистров, так как мы можем неосознанно повредить наш вход или выход, так как они используют один и тот же регистр.

Чтобы обойти это, мы используем `rdi` для хранения указателя на выходной массив, сохраняем `ebx` с помощью `push`, читаем из `ebx` внутри блока ассемблера в массив и затем восстанавливаем `ebx` до исходного состояния с помощью `pop`. `push` и `pop` используют полноразмерную 64-битную версию регистра `rbx`, чтобы гарантировать сохранение всего регистра. На 32-битных целевых платформах код вместо этого использовал бы `ebx` в `push`/`pop`.

Это также можно использовать с общим классом регистров, чтобы получить временный регистр для использования внутри ассемблерного кода:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

// Умножаем x на 6 с использованием сдвигов и сложений
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

## Операнды символов и ABI-замаскировки

По умолчанию `asm!` предполагает, что любой регистр, не указанный в качестве вывода, будет иметь свои содержимое сохраненным ассемблерным кодом. Аргумент \[`clobber_abi`\] для `asm!` сообщает компилятору автоматически вставлять необходимые операнды замаскировки в соответствии с заданным соглашением вызова ABI: любой регистр, который не полностью сохраняется в этом ABI, будет считаться замаскированным. Можно указать несколько аргументов `clobber_abi`, и все замаскировки из всех указанных ABIs будут вставлены.

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
            // Указатель на функцию для вызова
            in(reg) foo,
            // Первый аргумент в rdi
            in("rdi") arg,
            // Возвращаемое значение в rax
            out("rax") result,
            // Отметить все регистры, которые не сохраняются в соответствии с
            // соглашением вызова "C" как замаскированные.
            clobber_abi("C"),
        );
        result
    }
}
# }
```

## Модификаторы шаблонов регистров

В некоторых случаях требуется точный контроль над тем, как имя регистра форматируется при вставке в шаблонную строку. Это нужно, когда ассемблерный язык архитектуры имеет несколько имен для одного и того же регистра, каждый из которых обычно представляет собой "представление" над подмножеством регистра (например, нижние 32 бита 64-битного регистра).

По умолчанию компилятор всегда выбирает имя, которое относится к полному размеру регистра (например, `rax` на x86-64, `eax` на x86 и т.д.).

Это значение по умолчанию можно переопределить с помощью модификаторов на операндах шаблонной строки, точно так же, как это делается с строками форматирования:

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

В этом примере мы используем класс регистров `reg_abcd` для ограничения аллокатора регистров до 4 старых регистров x86 (`ax`, `bx`, `cx`, `dx`), из которых первые два байта можно адресовать отдельно.

Предположим, что аллокатор регистров выбрал для хранения `x` регистр `ax`. Модификатор `h` выведет имя регистра для верхнего байта этого регистра, а модификатор `l` выведет имя регистра для нижнего байта. Ассемблерный код будет таким образом развернут в `mov ah, al`, что копирует нижний байт значения в верхний байт.

Если вы используете более мелкий тип данных (например, `u16`) с операндом и забываете использовать модификаторы шаблонов, компилятор выдаст предупреждение и предложит правильный модификатор для использования.

## Операнды адресов памяти

Иногда инструкции ассемблера требуют операндов, передаваемых через адреса памяти/локации памяти. Вам нужно вручную использовать синтаксис адреса памяти, заданный целевой архитектурой. Например, на x86/x86_64 при использовании синтаксиса Intel ассемблера вы должны заключать входы/выходы в `[]`, чтобы показать, что они являются операндами памяти:

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

## Метки

Любая повторная используемость именованной метки, локальной или другой, может привести к ошибке сборщика ассемблера или линкера или может вызвать другое странное поведение. Повторная используемость именованной метки может произойти различными способами, включая:

- явно: использование метки более одного раза в одном блоке `asm!` или несколько раз в разных блоках.
- неявно через инлайн: компилятор может создавать несколько копий блока `asm!`, например, когда функция, содержащая его, инлайнируется в нескольких местах.
- неявно через LTO: LTO может привести к тому, что код из _других крейтов_ будет помещен в одну единицу генерации кода, и поэтому может принести произвольные метки.

В результате вы должны использовать только **числовые** \[локальные метки\] GNU-ассемблера внутри встроенного ассемблерного кода. Определение символов в ассемблерном коде может привести к ошибкам сборщика ассемблера и/или линкера из-за дублирования определений символов.

Помимо этого, на x86 при использовании стандартного синтаксиса Intel, из-за \[бага LLVM\], вы не должны использовать метки, состоящие только из цифр `0` и `1`, например, `0`, `11` или `101010`, так как они могут окажется интерпретируемыми как бинарные значения. Использование `options(att_syntax)` избавит от любых двусмыслений, но это повлияет на синтаксис _целого_ блока `asm!`. (см. [Options](#options), ниже, для более подробной информации о `options`.)

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

Это уменьшит значение регистра `{0}` от 10 до 3, затем добавит 2 и сохранит его в `a`.

Этот пример показывает несколько вещей:

- Во-первых, что одно и то же число можно использовать в качестве метки несколько раз в одном и том же встроенном блоке.
- Во-вторых, что когда числовая метка используется в качестве ссылки (например, в качестве операнда инструкции), к числовой метке должны быть добавлены суффиксы "b" ("назад") или "f" ("вперед"). Затем она будет ссылаться на ближайшую метку, определенную этим числом в этом направлении.

## Параметры

По умолчанию блок встроенного ассемблера обрабатывается так же, как вызов внешней функции FFI с пользовательским соглашением вызова: он может читать/записывать память, иметь заметные побочные эффекты и т.д. Однако, в многих случаях желательно дать компилятору больше информации о том, что на самом деле делает ассемблерный код, чтобы он мог лучше оптимизировать.

Возьмем наш предыдущий пример с инструкцией `add`:

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

Параметры можно указать в качестве необязательного последнего аргумента для макроса `asm!`. Мы указали здесь три параметра:

- `pure` означает, что ассемблерный код не имеет заметных побочных эффектов и что его вывод зависит только от его входов. Это позволяет оптимизатору компилятора вызывать встроенный ассемблер реже или даже полностью избавиться от него.
- `nomem` означает, что ассемблерный код не читает или не записывает в память. По умолчанию компилятор предполагает, что встроенный ассемблер может читать или записать любой адрес памяти, доступный для него (например, через указатель, переданный в качестве операнда, или глобальную переменную).
- `nostack` означает, что ассемблерный код не помещает никаких данных на стек. Это позволяет компилятору использовать оптимизации, такие как зона безопасности стека на x86-64, чтобы избежать调整 стека.

Это позволяет компилятору лучше оптимизировать код с использованием `asm!`, например, путем удаления чистых блоков `asm!`, вывод которых не нужен.

см. [справочник](https://doc.rust-lang.org/stable/reference/inline-assembly.html) для полного списка доступных параметров и их эффектов.
