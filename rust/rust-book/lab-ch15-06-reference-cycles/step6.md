# Visualizing Changes to strong_count and weak_count

Let’s look at how the `strong_count` and `weak_count` values of the `Rc<Node>`
instances change by creating a new inner scope and moving the creation of
`branch` into that scope. By doing so, we can see what happens when `branch` is
created and then dropped when it goes out of scope. The modifications are shown
in Listing 15-29.

Filename: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

  1 println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );

  2 {
        let branch = Rc::new(Node {
            value: 5,
            parent: RefCell::new(Weak::new()),
            children: RefCell::new(vec![Rc::clone(&leaf)]),
        });

        *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

      3 println!(
            "branch strong = {}, weak = {}",
            Rc::strong_count(&branch),
            Rc::weak_count(&branch),
        );

      4 println!(
            "leaf strong = {}, weak = {}",
            Rc::strong_count(&leaf),
            Rc::weak_count(&leaf),
        );
  5 }

  6 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );
  7 println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );
}
```

Listing 15-29: Creating `branch` in an inner scope and examining strong and
weak reference counts

After `leaf` is created, its `Rc<Node>` has a strong count of 1 and a weak
count of 0 [1]. In the inner scope [2], we create `branch` and associate it
with `leaf`, at which point when we print the counts [3], the `Rc<Node>` in
`branch` will have a strong count of 1 and a weak count of 1 (for `leaf.parent`
pointing to `branch` with a `Weak<Node>`). When we print the counts in `leaf`
[4], we’ll see it will have a strong count of 2 because `branch` now has a
clone of the `Rc<Node>` of `leaf` stored in `branch.children`, but will still
have a weak count of 0.

When the inner scope ends [5], `branch` goes out of scope and the strong count
of the `Rc<Node>` decreases to 0, so its `Node` is dropped. The weak count of 1
from `leaf.parent` has no bearing on whether or not `Node` is dropped, so we
don’t get any memory leaks!

If we try to access the parent of `leaf` after the end of the scope, we’ll get
`None` again [6]. At the end of the program [7], the `Rc<Node>` in `leaf` has a
strong count of 1 and a weak count of 0 because the variable `leaf` is now the
only reference to the `Rc<Node>` again.

All of the logic that manages the counts and value dropping is built into
`Rc<T>` and `Weak<T>` and their implementations of the `Drop` trait. By
specifying that the relationship from a child to its parent should be a
`Weak<T>` reference in the definition of `Node`, you’re able to have parent
nodes point to child nodes and vice versa without creating a reference cycle
and memory leaks.
