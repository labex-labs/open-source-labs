# A Use Case for Interior Mutability: Mock Objects

Sometimes during testing a programmer will use a type in place of another type,
in order to observe particular behavior and assert that it’s implemented
correctly. This placeholder type is called a _test double_. Think of it in the
sense of a stunt double in filmmaking, where a person steps in and substitutes
for an actor to do a particularly tricky scene. Test doubles stand in for other
types when we’re running tests. _Mock objects_ are specific types of test
doubles that record what happens during a test so you can assert that the
correct actions took place.

Rust doesn’t have objects in the same sense as other languages have objects,
and Rust doesn’t have mock object functionality built into the standard library
as some other languages do. However, you can definitely create a struct that
will serve the same purposes as a mock object.

Here’s the scenario we’ll test: we’ll create a library that tracks a value
against a maximum value and sends messages based on how close to the maximum
value the current value is. This library could be used to keep track of a
user’s quota for the number of API calls they’re allowed to make, for example.

Our library will only provide the functionality of tracking how close to the
maximum a value is and what the messages should be at what times. Applications
that use our library will be expected to provide the mechanism for sending the
messages: the application could put a message in the application, send an
email, send a text message, or do something else. The library doesn’t need to
know that detail. All it needs is something that implements a trait we’ll
provide called `Messenger`. Listing 15-20 shows the library code.

Filename: `src/lib.rs`

```rust
pub trait Messenger {
  1 fn send(&self, msg: &str);
}

pub struct LimitTracker<'a, T: Messenger> {
    messenger: &'a T,
    value: usize,
    max: usize,
}

impl<'a, T> LimitTracker<'a, T>
where
    T: Messenger,
{
    pub fn new(
        messenger: &'a T,
        max: usize
    ) -> LimitTracker<'a, T> {
        LimitTracker {
            messenger,
            value: 0,
            max,
        }
    }

  2 pub fn set_value(&mut self, value: usize) {
        self.value = value;

        let percentage_of_max =
            self.value as f64 / self.max as f64;

        if percentage_of_max >= 1.0 {
            self.messenger
                .send("Error: You are over your quota!");
        } else if percentage_of_max >= 0.9 {
            self.messenger
                .send("Urgent: You're at 90% of your quota!");
        } else if percentage_of_max >= 0.75 {
            self.messenger
                .send("Warning: You're at 75% of your quota!");
        }
    }
}
```

Listing 15-20: A library to keep track of how close a value is to a maximum
value and warn when the value is at certain levels

One important part of this code is that the `Messenger` trait has one method
called `send` that takes an immutable reference to `self` and the text of the
message [1]. This trait is the interface our mock object needs to implement so
that the mock can be used in the same way a real object is. The other important
part is that we want to test the behavior of the `set_value` method on the
`LimitTracker` [2]. We can change what we pass in for the `value` parameter,
but `set_value` doesn’t return anything for us to make assertions on. We want
to be able to say that if we create a `LimitTracker` with something that
implements the `Messenger` trait and a particular value for `max`, when we pass
different numbers for `value` the messenger is told to send the appropriate
messages.

We need a mock object that, instead of sending an email or text message when we
call `send`, will only keep track of the messages it’s told to send. We can
create a new instance of the mock object, create a `LimitTracker` that uses the
mock object, call the `set_value` method on `LimitTracker`, and then check that
the mock object has the messages we expect. Listing 15-21 shows an attempt to
implement a mock object to do just that, but the borrow checker won’t allow it.

Filename: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

  1 struct MockMessenger {
      2 sent_messages: Vec<String>,
    }

    impl MockMessenger {
      3 fn new() -> MockMessenger {
            MockMessenger {
                sent_messages: vec![],
            }
        }
    }

  4 impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
          5 self.sent_messages.push(String::from(message));
        }
    }

    #[test]
  6 fn it_sends_an_over_75_percent_warning_message() {
        let mock_messenger = MockMessenger::new();
        let mut limit_tracker = LimitTracker::new(
            &mock_messenger,
            100
        );

        limit_tracker.set_value(80);

        assert_eq!(mock_messenger.sent_messages.len(), 1);
    }
}
```

Listing 15-21: An attempt to implement a `MockMessenger` that isn’t allowed by
the borrow checker

This test code defines a `MockMessenger` struct [1] that has a `sent_messages`
field with a `Vec` of `String` values [2] to keep track of the messages it’s
told to send. We also define an associated function `new` [3] to make it
convenient to create new `MockMessenger` values that start with an empty list
of messages. We then implement the `Messenger` trait for `MockMessenger` [4] so
we can give a `MockMessenger` to a `LimitTracker`. In the definition of the
`send` method [5], we take the message passed in as a parameter and store it in
the `MockMessenger` list of `sent_messages`.

In the test, we’re testing what happens when the `LimitTracker` is told to set
`value` to something that is more than 75 percent of the `max` value [6]. First
we create a new `MockMessenger`, which will start with an empty list of
messages. Then we create a new `LimitTracker` and give it a reference to the
new `MockMessenger` and a `max` value of `100`. We call the `set_value` method
on the `LimitTracker` with a value of `80`, which is more than 75 percent of 100. Then we assert that the list of messages that the `MockMessenger` is
keeping track of should now have one message in it.

However, there’s one problem with this test, as shown here:

```bash
error[E0596]: cannot borrow `self.sent_messages` as mutable, as it is behind a
`&` reference
  --> src/lib.rs:58:13
   |
2  |     fn send(&self, msg: &str);
   |             ----- help: consider changing that to be a mutable reference:
`&mut self`
...
58 |             self.sent_messages.push(String::from(message));
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `self` is a
`&` reference, so the data it refers to cannot be borrowed as mutable
```

We can’t modify the `MockMessenger` to keep track of the messages because the
`send` method takes an immutable reference to `self`. We also can’t take the
suggestion from the error text to use `&mut self` instead because then the
signature of `send` wouldn’t match the signature in the `Messenger` trait
definition (feel free to try it and see what error message you get).

This is a situation in which interior mutability can help! We’ll store the
`sent_messages` within a `RefCell<T>`, and then the `send` method will be able
to modify `sent_messages` to store the messages we’ve seen. Listing 15-22 shows
what that looks like.

Filename: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;
    use std::cell::RefCell;

    struct MockMessenger {
      1 sent_messages: RefCell<Vec<String>>,
    }

    impl MockMessenger {
        fn new() -> MockMessenger {
            MockMessenger {
              2 sent_messages: RefCell::new(vec![]),
            }
        }
    }

    impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
            self.sent_messages
              3 .borrow_mut()
                .push(String::from(message));
        }
    }

    #[test]
    fn it_sends_an_over_75_percent_warning_message() {
        --snip--

        assert_eq!(
          4 mock_messenger.sent_messages.borrow().len(),
            1
        );
    }
}
```

Listing 15-22: Using `RefCell<T>` to mutate an inner value while the outer
value is considered immutable

The `sent_messages` field is now of type `RefCell<Vec<String>>` [1] instead of
`Vec<String>`. In the `new` function, we create a new `RefCell<Vec<String>>`
instance around the empty vector [2].

For the implementation of the `send` method, the first parameter is still an
immutable borrow of `self`, which matches the trait definition. We call
`borrow_mut` on the `RefCell<Vec<String>>` in `self.sent_messages` [3] to get a
mutable reference to the value inside the `RefCell<Vec<String>>`, which is the
vector. Then we can call `push` on the mutable reference to the vector to keep
track of the messages sent during the test.

The last change we have to make is in the assertion: to see how many items are
in the inner vector, we call `borrow` on the `RefCell<Vec<String>>` to get an
immutable reference to the vector [4].

Now that you’ve seen how to use `RefCell<T>`, let’s dig into how it works!
