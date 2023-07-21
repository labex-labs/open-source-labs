# Run under debugger

You can also run an entire program under debugger.

```bash
$ python3 -m pdb someprogram.py
```

It will automatically enter the debugger before the first
statement. Allowing you to set breakpoints and change the
configuration.

Common debugger commands:

```code
(Pdb) help            # Get help
(Pdb) w(here)         # Print stack trace
(Pdb) d(own)          # Move down one stack level
(Pdb) u(p)            # Move up one stack level
(Pdb) b(reak) loc     # Set a breakpoint
(Pdb) s(tep)          # Execute one instruction
(Pdb) c(ontinue)      # Continue execution
(Pdb) l(ist)          # List source code
(Pdb) a(rgs)          # Print args of current function
(Pdb) !statement      # Execute statement
```

For breakpoints location is one of the following.

```code
(Pdb) b 45            # Line 45 in current file
(Pdb) b file.py:45    # Line 45 in file.py
(Pdb) b foo           # Function foo() in current file
(Pdb) b module.foo    # Function foo() in a module
```
