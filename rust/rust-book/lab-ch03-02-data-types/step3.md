# Integer Types

An _integer_ is a number without a fractional component. We used one integer type in Chapter 2, the `u32` type. This type declaration indicates that the value it's associated with should be an unsigned integer (signed integer types start with `i` instead of `u`) that takes up 32 bits of space. Table 3-1 shows the built-in integer types in Rust. We can use any of these variants to declare the type of an integer value.

Table 3-1: Integer Types in Rust

Length Signed Unsigned

---

8-bit `i8` `u8`
16-bit `i16` `u16`
32-bit `i32` `u32`
64-bit `i64` `u64`
128-bit `i128` `u128`
arch `isize` `usize`

Each variant can be either signed or unsigned and has an explicit size. _Signed_ and _unsigned_ refer to whether it's possible for the number to be negative---in other words, whether the number needs to have a sign with it (signed) or whether it will only ever be positive and can therefore be represented without a sign (unsigned). It's like writing numbers on paper: when the sign matters, a number is shown with a plus sign or a minus sign; however, when it's safe to assume the number is positive, it's shown with no sign. Signed numbers are stored using two's complement representation.

Each signed variant can store numbers from -(2`<sup>`{=html}n - 1`</sup>`{=html}) to 2`<sup>`{=html}n - 1`</sup>`{=html} - 1 inclusive, where _n_ is the number of bits that variant uses. So an `i8` can store numbers from -(2`<sup>`{=html}7`</sup>`{=html}) to 2`<sup>`{=html}7`</sup>`{=html} - 1, which equals -128 to 127. Unsigned variants can store numbers from 0 to 2`<sup>`{=html}n`</sup>`{=html} - 1, so a `u8` can store numbers from 0 to 2`<sup>`{=html}8`</sup>`{=html} - 1, which equals 0 to 255.

Additionally, the `isize` and `usize` types depend on the architecture of the computer your program is running on, which is denoted in the table as "arch": 64 bits if you're on a 64-bit architecture and 32 bits if you're on a 32-bit architecture.

You can write integer literals in any of the forms shown in Table 3-2. Note that number literals that can be multiple numeric types allow a type suffix, such as `57u8`, to designate the type. Number literals can also use `_` as a visual separator to make the number easier to read, such as `1_000`, which will have the same value as if you had specified `1000`.

Table 3-2: Integer Literals in Rust

Number literals Example

---

Decimal `98_222`
Hex `0xff`
Octal `0o77`
Binary `0b1111_0000`
Byte (`u8` only) `b'A'`

So how do you know which type of integer to use? If you're unsure, Rust's defaults are generally good places to start: integer types default to `i32`. The primary situation in which you'd use `isize` or `usize` is when indexing some sort of collection.

> **Integer Overflow**
>
> Let's say you have a variable of type `u8` that can hold values between 0 and 255. If you try to change the variable to a value outside that range, such as 256, _integer overflow_ will occur, which can result in one of two behaviors. When you're compiling in debug mode, Rust includes checks for integer overflow that cause your program to _panic_ at runtime if this behavior occurs. Rust uses the term _panicking_ when a program exits with an error; we'll discuss panics in more depth in "Unrecoverable Errors with panic!" on page XX.
>
> When you're compiling in release mode with the `--release` flag, Rust does _not_ include checks for integer overflow that cause panics. Instead, if overflow occurs, Rust performs _two's complement wrapping_. In short, values greater than the maximum value the type can hold "wrap around" to the minimum of the values the type can hold. In the case of a `u8`, the value 256 becomes 0, the value 257 becomes 1, and so on. The program won't panic, but the variable will have a value that probably isn't what you were expecting it to have. Relying on integer overflow's wrapping behavior is considered an error.
>
> To explicitly handle the possibility of overflow, you can use these families of methods provided by the standard library for primitive numeric types:
>
> - Wrap in all modes with the `wrapping_*` methods, such as `wrapping_add`.
> - Return the `None` value if there is overflow with the `checked_*` methods.
> - Return the value and a boolean indicating whether there was overflow with the `overflowing_*` methods.
> - Saturate at the value's minimum or maximum values with the `saturating_*` methods.
