# Andere Slices

String-Slices, wie man sich denken kann, sind speziell für Strings. Es gibt jedoch auch einen allgemeineren Slice-Typ. Betrachten Sie dieses Array:

```rust
let a = [1, 2, 3, 4, 5];
```

Genau wie wir möglicherweise einen Teil eines Strings referenzieren möchten, möchten wir auch einen Teil eines Arrays referenzieren. Wir würden das so tun:

```rust
let a = [1, 2, 3, 4, 5];

let slice = &a[1..3];

assert_eq!(slice, &[2, 3]);
```

Dieser Slice hat den Typ `&[i32]`. Es funktioniert auf die gleiche Weise wie String-Slices, indem es eine Referenz auf das erste Element und eine Länge speichert. Sie werden diesen Typ von Slice für alle sorts anderer Sammlungen verwenden. Wir werden diese Sammlungen im Detail diskutieren, wenn wir in Kapitel 8 über Vektoren sprechen.
