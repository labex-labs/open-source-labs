# Storing UTF-8 Encoded Text with Strings

We talked about strings in Chapter 4, but we’ll look at them in more depth now.
New Rustaceans commonly get stuck on strings for a combination of three
reasons: Rust’s propensity for exposing possible errors, strings being a more
complicated data structure than many programmers give them credit for, and
UTF-8. These factors combine in a way that can seem difficult when you’re
coming from other programming languages.

We discuss strings in the context of collections because strings are
implemented as a collection of bytes, plus some methods to provide useful
functionality when those bytes are interpreted as text. In this section, we’ll
talk about the operations on `String` that every collection type has, such as
creating, updating, and reading. We’ll also discuss the ways in which `String`
is different from the other collections, namely how indexing into a `String` is
complicated by the differences between how people and computers interpret
`String` data.
