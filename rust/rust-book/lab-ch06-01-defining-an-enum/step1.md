# Defining an Enum

Where structs give you a way of grouping together related fields and data, like
a `Rectangle` with its `width` and `height`, enums give you a way of saying a
value is one of a possible set of values. For example, we may want to say that
`Rectangle` is one of a set of possible shapes that also includes `Circle` and
`Triangle`. To do this, Rust allows us to encode these possibilities as an enum.

Let’s look at a situation we might want to express in code and see why enums
are useful and more appropriate than structs in this case. Say we need to work
with IP addresses. Currently, two major standards are used for IP addresses:
version four and version six. Because these are the only possibilities for an
IP address that our program will come across, we can _enumerate_ all possible
variants, which is where enumeration gets its name.

Any IP address can be either a version four or a version six address, but not
both at the same time. That property of IP addresses makes the enum data
structure appropriate because an enum value can only be one of its variants.
Both version four and version six addresses are still fundamentally IP
addresses, so they should be treated as the same type when the code is handling
situations that apply to any kind of IP address.

We can express this concept in code by defining an `IpAddrKind` enumeration and
listing the possible kinds an IP address can be, `V4` and `V6`. These are the
variants of the enum:

```rust
enum IpAddrKind {
    V4,
    V6,
}
```

`IpAddrKind` is now a custom data type that we can use elsewhere in our code.
