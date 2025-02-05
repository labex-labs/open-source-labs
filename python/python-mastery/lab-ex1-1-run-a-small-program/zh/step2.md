# 一些生成式艺术

创建以下程序并将其保存到名为 `art.py` 的文件中：

```python
# art.py

import sys
import random

chars = '\|/'

def draw(rows, columns):
    for r in range(rows):
        print(''.join(random.choice(chars) for _ in range(columns)))

if __name__ == '__main__':
    if len(sys.argv)!= 3:
        raise SystemExit("Usage: art.py rows columns")
    draw(int(sys.argv[1]), int(sys.argv[2]))
```

确保你能够从命令行或终端运行此程序。

```bash
python3 art.py 10 20
```

如果你运行上述命令，将会得到一个崩溃和回溯消息。去修复问题并再次运行程序。你应该会得到如下输出：

```bash
python3 art.py 10 20
||||/\||//\//\|||\|\
///||\/||\//|\\|\\/\
|\////|//|||\//|/\||
|//\||\/|\///|\|\|/|
|/|//|/|/|\\/\/\||//
|\/\|\//\\//\|\||\\/
|||\\\\/\\\|/||||\/|
\\||\\\|\||||////\\|
//\//|/|\\|\//\|||\/
\\\|/\\|/|\\\|/|/\/|
```

## 重要说明

在本课程的剩余部分，你能够编辑、运行和调试普通的Python程序是绝对必要的。编辑器、集成开发环境（IDE）或操作系统的选择并不重要，只要你能够进行交互式实验并创建可以从命令行执行的普通Python源文件即可。
