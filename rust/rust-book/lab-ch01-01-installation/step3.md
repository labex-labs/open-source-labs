# Installing rustup on Windows

On Windows, go to *https://www.rust-lang.org/tools/install* and follow the
instructions for installing Rust. At some point in the installation, you’ll
receive a message explaining that you’ll also need the MSVC build tools for
Visual Studio 2013 or later.

To acquire the build tools, you’ll need to install Visual Studio 2022 from
*https://visualstudio.microsoft.com/downloads*. When asked which workloads to
install, include:

- “Desktop Development with C++”
- The Windows 10 or 11 SDK
- The English language pack component, along with any other language pack of
  your choosing

The rest of this book uses commands that work in both _cmd.exe_ and PowerShell.
If there are specific differences, we’ll explain which to use.
