# Troubleshooting

To check whether you have Rust installed correctly, open a **new shell** and enter this line:

```bash
# Open a new terminal first!
rustc --version
```

You should see the version number, commit hash, and commit date for the latest stable version that has been released, in the following format:

```bash
rustc x.y.z (abcabcabc yyyy-mm-dd)
```

If you see this information, you have installed Rust successfully! If you don't see this information, check that Rust is in your `%PATH%` system variable as follows.

in Linux, use:

```bash
echo $PATH
```

If that's all correct and Rust still isn't working, there are a number of places you can get help. Find out how to get in touch with other Rustaceans (a silly nickname we call ourselves) on the community page at *https://www.rust-lang.org/community*.
