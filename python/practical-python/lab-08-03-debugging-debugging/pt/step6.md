# Executar sob o depurador

Você também pode executar um programa inteiro sob o depurador.

```bash
$ python3 -m pdb someprogram.py
```

Ele entrará automaticamente no depurador antes da primeira instrução. Permitindo que você defina breakpoints (pontos de interrupção) e altere a configuração.

Comandos comuns do depurador:

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

Para breakpoints, a localização é uma das seguintes.

```code
(Pdb) b 45            # Line 45 in current file
(Pdb) b file.py:45    # Line 45 in file.py
(Pdb) b foo           # Function foo() in current file
(Pdb) b module.foo    # Function foo() in a module
```
