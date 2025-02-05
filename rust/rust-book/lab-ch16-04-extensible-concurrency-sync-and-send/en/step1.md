# Extensible Concurrency with the Send and Sync Traits

Interestingly, the Rust language has _very_ few concurrency features. Almost every concurrency feature we've talked about so far in this chapter has been part of the standard library, not the language. Your options for handling concurrency are not limited to the language or the standard library; you can write your own concurrency features or use those written by others.

However, two concurrency concepts are embedded in the language: the `std::marker` traits `Send` and `Sync` .
