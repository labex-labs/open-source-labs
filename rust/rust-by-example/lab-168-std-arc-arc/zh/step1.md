# Arc

当线程之间需要共享所有权时，可以使用`Arc`（原子引用计数）。通过`Clone`实现，这个结构体可以为内存堆中某个值的位置创建一个引用指针，同时增加引用计数器。由于它在线程之间共享所有权，所以当指向某个值的最后一个引用指针超出作用域时，该变量就会被释放。

```rust
use std::time::Duration;
use std::sync::Arc;
use std::thread;

fn main() {
    // 这个变量声明指定了它的值。
    let apple = Arc::new("the same apple");

    for _ in 0..10 {
        // 这里没有指定值，因为它是指向内存堆中一个引用的指针。
        let apple = Arc::clone(&apple);

        thread::spawn(move || {
            // 由于使用了Arc，所以可以使用Arc变量指针位置处分配的值来创建线程。
            println!("{:?}", apple);
        });
    }

    // 确保所有从创建的线程中打印出的Arc实例都已输出。
    thread::sleep(Duration::from_secs(1));
}
```
