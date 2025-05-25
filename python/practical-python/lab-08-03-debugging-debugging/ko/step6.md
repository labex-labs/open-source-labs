# 디버거에서 실행하기

전체 프로그램을 디버거에서 실행할 수도 있습니다.

```bash
$ python3 -m pdb someprogram.py
```

첫 번째 문장 전에 자동으로 디버거에 진입합니다. 중단점을 설정하고 구성을 변경할 수 있습니다.

일반적인 디버거 명령어:

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

중단점의 위치는 다음 중 하나입니다.

```code
(Pdb) b 45            # Line 45 in current file
(Pdb) b file.py:45    # Line 45 in file.py
(Pdb) b foo           # Function foo() in current file
(Pdb) b module.foo    # Function foo() in a module
```
