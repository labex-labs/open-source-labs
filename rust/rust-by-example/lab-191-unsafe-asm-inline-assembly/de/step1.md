# Inline-Assembly

Rust bietet Unterstützung für Inline-Assembly über das `asm!`-Makro. Es kann verwendet werden, um handgeschriebene Assembly-Code in die von dem Compiler generierte Assembly-Ausgabe einzubetten. Im Allgemeinen sollte dies nicht erforderlich sein, kann aber erforderlich sein, wenn die erforderliche Leistung oder Genauigkeit nicht anders erreicht werden kann. Der Zugang zu niedrigen Hardware-Primitiven, z.B. im Kernel-Code, kann auch diese Funktionalität erfordern.

> **Hinweis**: Die hier gezeigten Beispiele sind in x86/x86-64-Assembly angegeben, aber auch andere Architekturen werden unterstützt.

Inline-Assembly wird derzeit auf folgenden Architekturen unterstützt:

- x86 und x86-64
- ARM
- AArch64
- RISC-V

## Grundlegende Verwendung

Lassen Sie uns mit dem einfachsten möglichen Beispiel beginnen:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

unsafe {
    asm!("nop");
}
# }
```

Dies wird einen NOP (keine Aktion) Befehl in die von dem Compiler generierte Assembly einfügen. Beachten Sie, dass alle `asm!`-Aufrufe innerhalb eines `unsafe`-Blocks sein müssen, da sie beliebige Anweisungen einfügen können und verschiedene Invarianten brechen können. Die einzufügenden Anweisungen werden als String-Literal im ersten Argument der `asm!`-Makro aufgelistet.

## Eingaben und Ausgaben

Einen Befehl einzufügen, der nichts tut, ist ziemlich langweilig. Lassen Sie uns etwas tun, das tatsächlich auf Daten wirkt:

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

Dies wird den Wert `5` in die `u64`-Variable `x` schreiben. Sie können sehen, dass der String-Literal, den wir verwenden, um Anweisungen anzugeben, tatsächlich ein Template-String ist. Er wird von den gleichen Regeln wie Rust-Format-Strings beherrscht. Die Argumente, die in das Template eingefügt werden, sehen jedoch etwas anders aus, als Sie es vielleicht gewohnt sind. Zunächst müssen wir angeben, ob die Variable eine Eingabe oder eine Ausgabe der Inline-Assembly ist. In diesem Fall ist es eine Ausgabe. Wir haben dies durch Schreiben von `out` deklariert. Wir müssen auch angeben, in welchem Registertyp die Assembly die Variable erwartet. In diesem Fall legen wir es in einem beliebigen allgemeinen Register fest, indem wir `reg` angeben. Der Compiler wird ein passendes Register auswählen, um in das Template einzufügen, und wird die Variable danach lesen, nachdem die Inline-Assembly ausgeführt wurde.

Lassen Sie uns ein weiteres Beispiel betrachten, das auch eine Eingabe verwendet:

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

Dies wird `5` zur Eingabe in der Variable `i` addieren und das Ergebnis in die Variable `o` schreiben. Die besondere Art, wie diese Assembly dies tut, ist, dass sie zuerst den Wert von `i` in die Ausgabe kopiert und dann `5` hinzuaddiert.

Das Beispiel zeigt ein paar Dinge:

Zunächst können wir sehen, dass `asm!` mehrere Template-String-Argumente erlaubt; jedes wird als separate Zeile von Assembly-Code behandelt, als wären sie alle mit Zeilenumbrüchen dazwischen verbunden. Dies macht es einfach, Assembly-Code zu formatieren.

Zweitens können wir sehen, dass Eingaben durch Schreiben von `in` statt `out` deklariert werden.

Drittens können wir sehen, dass wir eine Argumentnummer oder einen Namen wie in jedem Format-String angeben können. Für Inline-Assembly-Templates ist dies besonders nützlich, da Argumente oft mehrmals verwendet werden. Für komplexeren Inline-Assembly wird diese Funktion im Allgemeinen empfohlen, da sie die Lesbarkeit verbessert und die Anweisungen ohne Änderung der Argumentreihenfolge neu anordnen lässt.

Wir können das obige Beispiel weiter verfeinern, um den `mov`-Befehl zu vermeiden:

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

Wir können sehen, dass `inout` verwendet wird, um ein Argument anzugeben, das sowohl Eingabe als auch Ausgabe ist. Dies unterscheidet sich davon, separate Eingaben und Ausgaben anzugeben, indem es sichergestellt ist, dass beide auf dasselbe Register zugewiesen werden.

Es ist auch möglich, unterschiedliche Variablen für die Eingabe- und Ausgabeteile eines `inout`-Operanden anzugeben:

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

## Spätausgabebetreiber

Der Rust-Compiler ist konservativ bei der Zuweisung von Operanden. Es wird angenommen, dass ein `out` zu jeder Zeit geschrieben werden kann und daher nicht seinen Speicherort mit einem anderen Argument teilen kann. Um jedoch die optimale Leistung zu gewährleisten, ist es wichtig, möglichst wenige Register zu verwenden, damit sie nicht gespeichert und neu geladen werden müssen, wenn der Inline-Assembly-Block ausgeführt wird. Um dies zu erreichen, bietet Rust einen `lateout`-Spezifizierer. Dies kann für jede Ausgabe verwendet werden, die erst nach dem Verbrauch aller Eingaben geschrieben wird. Es gibt auch eine `inlateout`-Variante dieses Spezifizierers.

Hier ist ein Beispiel, in dem `inlateout` in `release`-Modus oder anderen optimierten Fällen _nicht_ verwendet werden kann:

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

Das obige könnte in nicht optimierten Fällen (`Debug`-Modus) gut funktionieren, aber wenn Sie optimierte Leistung (`release`-Modus oder andere optimierte Fälle) möchten, könnte es nicht funktionieren.

Das liegt daran, dass im optimierten Fall der Compiler frei ist, dasselbe Register für die Eingaben `b` und `c` zuzuweisen, da er weiß, dass sie den gleichen Wert haben. Er muss jedoch ein separates Register für `a` zuweisen, da er `inout` und nicht `inlateout` verwendet. Wenn `inlateout` verwendet würde, könnten `a` und `c` auf dasselbe Register zugewiesen werden, was dazu führen würde, dass die erste Anweisung den Wert von `c` überschreibt und die Assembly-Code den falschen Wert produziert.

Das folgende Beispiel kann jedoch `inlateout` verwenden, da die Ausgabe erst nach dem Lesen aller Eingaberegister geändert wird:

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

Wie Sie sehen können, wird dieser Assembly-Fragment weiterhin korrekt funktionieren, wenn `a` und `b` auf dasselbe Register zugewiesen werden.

## Explizite Registerbetreiber

Einige Anweisungen erfordern, dass die Operanden in einem bestimmten Register sind. Daher bietet Rust Inline-Assembly einige spezifischere Einschränkungsspezifizierer. Während `reg` im Allgemeinen auf jeder Architektur verfügbar ist, sind explizite Register stark architekturspezifisch. Beispielsweise können für x86 die allgemeinen Register `eax`, `ebx`, `ecx`, `edx`, `ebp`, `esi` und `edi` unter anderen durch ihren Namen angesprochen werden.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let cmd = 0xd1;
unsafe {
    asm!("out 0x64, eax", in("eax") cmd);
}
# }
```

In diesem Beispiel rufen wir den `out`-Befehl auf, um den Inhalt der `cmd`-Variable an Port `0x64` auszugeben. Da der `out`-Befehl nur `eax` (und seine Unterregister) als Operand akzeptiert, mussten wir den `eax`-Einschränkungsspezifizierer verwenden.

> **Hinweis**: Anders als bei anderen Operandentypen können explizite Registerbetreiber nicht im Template-String verwendet werden: Sie können nicht `{}` verwenden und sollten stattdessen den Registernamen direkt schreiben. Außerdem müssen sie am Ende der Operandenliste nach allen anderen Operandentypen erscheinen.

Betrachten Sie dieses Beispiel, das die x86 `mul`-Anweisung verwendet:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

fn mul(a: u64, b: u64) -> u128 {
    let lo: u64;
    let hi: u64;

    unsafe {
        asm!(
            // Die x86 mul-Anweisung nimmt rax als implizite Eingabe und schreibt
            // das 128-Bit-Ergebnis der Multiplikation in rax:rdx.
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

Dies verwendet die `mul`-Anweisung, um zwei 64-Bit-Eingaben mit einem 128-Bit-Ergebnis zu multiplizieren. Der einzige explizite Operand ist ein Register, das wir aus der Variable `a` füllen. Der zweite Operand ist implizit und muss das `rax`-Register sein, das wir aus der Variable `b` füllen. Die unteren 64 Bits des Ergebnisses werden in `rax` gespeichert, aus dem wir die Variable `lo` füllen. Die höheren 64 Bits werden in `rdx` gespeichert, aus dem wir die Variable `hi` füllen.

## Belegte Register

In vielen Fällen wird die Inline-Assembly den Zustand ändern, der nicht als Ausgabe benötigt wird. Normalerweise liegt dies daran, dass wir in der Assembly ein Zwischenregister verwenden müssen oder dass Anweisungen den Zustand ändern, den wir nicht weiter untersuchen müssen. Dieser Zustand wird im Allgemeinen als "belegt" bezeichnet. Wir müssen dem Compiler davon erzählen, da er möglicherweise diesen Zustand um die Inline-Assembly-Block herum speichern und wiederherstellen muss.

```rust
use std::arch::asm;

# #[cfg(target_arch = "x86_64")]
fn main() {
    // drei Einträge zu je vier Bytes
    let mut name_buf = [0_u8; 12];
    // Die Zeichenkette wird als ASCII in ebx, edx, ecx in dieser Reihenfolge gespeichert
    // Da ebx reserviert ist, muss die asm den Wert von ebx beibehalten.
    // Daher pushen und popen wir es um die Haupt-asm herum.
    // 64-Bit-Modus auf 64-Bit-Prozessoren erlaubt nicht das Pushen/Popen von
    // 32-Bit-Registern (wie ebx), daher müssen wir das erweiterte rbx-Register verwenden.

    unsafe {
        asm!(
            "push rbx",
            "cpuid",
            "mov [rdi], ebx",
            "mov [rdi + 4], edx",
            "mov [rdi + 8], ecx",
            "pop rbx",
            // Wir verwenden einen Zeiger auf ein Array zum Speichern der Werte, um
            // den Rust-Code zu vereinfachen
            // Dies hat den Preis von ein paar zusätzlichen asm-Anweisungen
            // Dies ist jedoch expliziter, wie die asm funktioniert, im Gegensatz
            // zu expliziten Registerausgaben wie `out("ecx") val`
            // Der *Zeiger selbst* ist nur eine Eingabe, auch wenn er hinter
            // geschrieben wird
            in("rdi") name_buf.as_mut_ptr(),
            // Wählen Sie cpuid 0, geben Sie auch eax als belegte an
            inout("eax") 0 => _,
            // cpuid belegt auch diese Register
            out("ecx") _,
            out("edx") _,
        );
    }

    let name = core::str::from_utf8(&name_buf).unwrap();
    println!("CPU-Hersteller-ID: {}", name);
}

# #[cfg(not(target_arch = "x86_64"))]
# fn main() {}
```

Im obigen Beispiel verwenden wir die `cpuid`-Anweisung, um die CPU-Hersteller-ID zu lesen. Dieser Befehl schreibt in `eax` mit dem maximal unterstützten `cpuid`-Argument und in `ebx`, `edx` und `ecx` mit der CPU-Hersteller-ID als ASCII-Bytes in dieser Reihenfolge.

Auch wenn `eax` nie gelesen wird, müssen wir dem Compiler trotzdem mitteilen, dass das Register geändert wurde, damit der Compiler alle Werte, die in diesen Registern waren, vor der asm speichern kann. Dies wird dadurch erreicht, dass es als Ausgabe deklariert wird, aber mit `_` statt eines Variablennamens, was angibt, dass der Ausgabewert verworfen werden soll.

Dieser Code umgeht auch die Einschränkung, dass `ebx` ein reserviertes Register von LLVM ist. Das bedeutet, dass LLVM annimmt, dass es volle Kontrolle über das Register hat und es vor dem Verlassen des asm-Blocks in seinen ursprünglichen Zustand wiederhergestellt werden muss, daher kann es nicht als Eingabe oder Ausgabe verwendet werden **außer** wenn der Compiler es verwendet, um eine allgemeine Registerklasse zu erfüllen (z.B. `in(reg)`). Dies macht `reg`-Operanden gefährlich, wenn reservierte Register verwendet werden, da wir ungewollt unseren Eingaben oder Ausgaben schaden könnten, da sie das gleiche Register teilen.

Um dies zu umgehen, verwenden wir `rdi` zum Speichern des Zeigers auf das Ausgabearray, speichern `ebx` über `push`, lesen von `ebx` innerhalb des asm-Blocks in das Array und stellen dann `ebx` in seinen ursprünglichen Zustand über `pop` wieder her. Die `push` und `pop` verwenden die volle 64-Bit-Version des Registers `rbx`, um sicherzustellen, dass das gesamte Register gespeichert wird. Auf 32-Bit-Zielen würde der Code stattdessen `ebx` in der `push`/`pop` verwenden.

Dies kann auch mit einer allgemeinen Registerklasse verwendet werden, um ein Zwischenregister für die Verwendung innerhalb des asm-Codes zu erhalten:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

// Multiplizieren Sie x mit 6 mithilfe von Schieben und Addieren
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

## Symboloperanden und ABI-Belege

Standardmäßig nimmt `asm!` an, dass der Inhalt jedes Registers, das nicht als Ausgabe angegeben ist, durch den Assembly-Code beibehalten wird. Der \[`clobber_abi`\]-Parameter von `asm!`告诉编译器，根据给定的调用约定 ABI 自动插入必要的覆盖操作数：在该 ABI 中未完全保留的任何寄存器将被视为已覆盖。可以提供多个`clobber_abi`参数，并且将插入所有指定 ABI 的所有覆盖。

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
            // Funktionszeiger auf aufzurufende Funktion
            in(reg) foo,
            // 1. Argument in rdi
            in("rdi") arg,
            // Rückgabewert in rax
            out("rax") result,
            // Markieren Sie alle Register, die nicht durch die "C"-Aufrufkonvention
            // beibehalten werden, als belegte.
            clobber_abi("C"),
        );
        result
    }
}
# }
```

## Registervorlagenmodifizierer

In einigen Fällen ist eine feine Kontrolle über die Art und Weise erforderlich, wie ein Registername im Template-String formatiert wird, wenn er eingefügt wird. Dies ist erforderlich, wenn die Assembly-Sprache einer Architektur mehrere Namen für dasselbe Register hat, wobei jeder normalerweise eine "Ansicht" über einen Teil des Registers ist (z.B. die unteren 32 Bits eines 64-Bit-Registers).

Standardmäßig wird der Compiler immer den Namen wählen, der auf die volle Registergröße verweist (z.B. `rax` auf x86-64, `eax` auf x86 usw.).

Dieser Standard kann durch die Verwendung von Modifizierern auf den Template-String-Operanden überschrieben werden, genauso wie bei Format-Strings:

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

In diesem Beispiel verwenden wir die `reg_abcd`-Registerklasse, um den Registerzuweisungsalgorithmus auf die 4 legacy x86-Registern (`ax`, `bx`, `cx`, `dx`) zu beschränken, von denen die ersten beiden Bytes unabhängig angesprochen werden können.

Angenommen, der Registerzuweisungsalgorithmus hat entschieden, `x` im `ax`-Register zuzuweisen. Der `h`-Modifizierer wird den Registernamen für das obere Byte dieses Registers ausgeben und der `l`-Modifizierer wird den Registernamen für das untere Byte ausgeben. Der asm-Code wird daher wie folgt erweitert: `mov ah, al`, was das untere Byte des Werts in das obere Byte kopiert.

Wenn Sie einen kleineren Datentyp (z.B. `u16`) mit einem Operanden verwenden und vergessen, Template-Modifizierer zu verwenden, wird der Compiler eine Warnung ausgeben und den richtigen Modifizierer vorschlagen, der verwendet werden soll.

## Speicheradressbetreiber

Manchmal erfordern Assembly-Anweisungen Operanden, die über Speicheradressen/Speicherorte übergeben werden. Sie müssen manuell die von der Zielarchitektur angegebene Speicheradress-Syntax verwenden. Beispielsweise bei x86/x86_64 mit Intel-Assembly-Syntax sollten Sie Eingaben/Ausgaben in `[]` einschließen, um anzuzeigen, dass es sich um Speicheroperanden handelt:

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

## Labels

Jede Wiederverwendung eines benannten Labels, lokal oder anderswo, kann zu einem Assembler- oder Linkerfehler führen oder kann auch andere seltsame Verhaltensweisen verursachen. Die Wiederverwendung eines benannten Labels kann auf verschiedene Weise passieren, einschließlich:

- explizit: Verwendung eines Labels mehrmals in einem `asm!`-Block oder mehrmals in verschiedenen Blöcken.
- implizit über Inlining: Der Compiler ist berechtigt, mehrere Kopien eines `asm!`-Blocks zu instanziieren, z.B. wenn die Funktion, die ihn enthält, an mehreren Stellen inlined wird.
- implizit über LTO: LTO kann dazu führen, dass Code aus _anderen Crates_ in die gleiche Codegenerierungs-Einheit platziert wird und daher beliebige Labels mitbringen kann.

Als Ergebnis sollten Sie nur GNU-Assembler **numerische** \[lokale Labels\] innerhalb des Inline-Assembly-Codes verwenden. Das Definieren von Symbolen im Assembly-Code kann aufgrund doppelter Symboldefinitionen zu Assembler- und/oder Linkerfehlern führen.

Außerdem bei x86, wenn die standardmäßige Intel-Syntax verwendet wird, aufgrund eines \[LLVM-Bugs\] sollten Sie keine Labels verwenden, die ausschließlich aus `0` und `1` Ziffern bestehen, z.B. `0`, `11` oder `101010`, da sie möglicherweise als binäre Werte interpretiert werden. Die Verwendung von `options(att_syntax)` vermeidet jede Mehrdeutigkeit, aber das wirkt sich auf die Syntax des gesamten `asm!`-Blocks aus. (Siehe [Optionen](#optionen), unten, für mehr Informationen zu `optionen`.)

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

Dies wird den Wert des `{0}`-Registers von 10 auf 3 dekrementieren, dann 2 hinzufügen und ihn in `a` speichern.

Dieses Beispiel zeigt ein paar Dinge:

- Erstens, dass die gleiche Zahl als Label mehrmals im selben Inline-Block verwendet werden kann.
- Zweitens, dass wenn ein numerisches Label als Referenz verwendet wird (z.B. als Anweisungsoperand), den Suffixen "b" ("rückwärts") oder "f" ("vorwärts") zum numerischen Label hinzugefügt werden sollte. Es wird dann auf das nächste von dieser Zahl definierte Label in diese Richtung verweisen.

## Optionen

Standardmäßig wird ein Inline-Assembly-Block auf die gleiche Weise behandelt wie ein externer FFI-Funktionsaufruf mit einer benutzerdefinierten Aufrufkonvention: es kann Speicher lesen/schreiben, beobachtbare Seiteneffekte haben usw. In vielen Fällen ist es jedoch wünschenswert, dem Compiler mehr Informationen über das zu geben, was der Assembly-Code tatsächlich tut, damit er besser optimieren kann.

Nehmen wir unser vorheriges Beispiel eines `add`-Befehls:

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

Optionen können als optionaler letzter Parameter an das `asm!`-Makro übergeben werden. Wir haben hier drei Optionen angegeben:

- `pure` bedeutet, dass der asm-Code keine beobachtbaren Seiteneffekte hat und dass seine Ausgabe ausschließlich von seinen Eingaben abhängt. Dies ermöglicht es dem Compiler-Optimierer, den Inline-asm weniger oft aufzurufen oder ihn sogar vollständig zu eliminieren.
- `nomem` bedeutet, dass der asm-Code nicht auf Speicher liest oder schreibt. Standardmäßig wird der Compiler annehmen, dass Inline-Assembly beliebige Speicheradressen lesen oder schreiben kann, auf die es zugreifen kann (z.B. über einen als Operand übergebenen Zeiger oder eine globale Variable).
- `nostack` bedeutet, dass der asm-Code keine Daten auf den Stapel pusht. Dies ermöglicht es dem Compiler, Optimierungen wie die Stack-Red-Zone auf x86-64 zu verwenden, um Stack-Zeiger-Anpassungen zu vermeiden.

Diese ermöglichen es dem Compiler, den Code mit `asm!` besser zu optimieren, z.B. indem er reine `asm!`-Blöcke eliminieren kann, deren Ausgabe nicht benötigt wird.

Siehe die [Referenz](https://doc.rust-lang.org/stable/reference/inline-assembly.html) für die vollständige Liste der verfügbaren Optionen und ihrer Auswirkungen.
