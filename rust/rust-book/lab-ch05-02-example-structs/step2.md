# Refactoring with Tuples

Listing 5-9 shows another version of our program that uses tuples.

Filename: `src/main.rs`

```rust
fn main() {
    let rect1 = (30, 50);

    println!(
        "The area of the rectangle is {} square pixels.",
      1 area(rect1)
    );
}

fn area(dimensions: (u32, u32)) -> u32 {
  2 dimensions.0 * dimensions.1
}
```

Listing 5-9: Specifying the width and height of the rectangle with a tuple

In one way, this program is better. Tuples let us add a bit of structure, and we're now passing just one argument \[1\]. But in another way, this version is less clear: tuples don't name their elements, so we have to index into the parts of the tuple \[2\], making our calculation less obvious.

Mixing up the width and height wouldn't matter for the area calculation, but if we want to draw the rectangle on the screen, it would matter! We would have to keep in mind that `width` is the tuple index `0` and `height` is the tuple index `1`. This would be even harder for someone else to figure out and keep in mind if they were to use our code. Because we haven't conveyed the meaning of our data in our code, it's now easier to introduce errors.
