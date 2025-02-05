# 理解数据类型

NumPy 支持多种与 C 编程语言紧密相关的数值类型。以下是 NumPy 中一些最常用的数据类型：

- `numpy.bool_`：布尔值（True 或 False），存储为一个字节
- `numpy.byte`：有符号字符（取决于平台）
- `numpy.ubyte`：无符号字符（取决于平台）
- `numpy.short`：短整型（取决于平台）
- `numpy.ushort`：无符号短整型（取决于平台）
- `numpy.intc`：整型（取决于平台）
- `numpy.uintc`：无符号整型（取决于平台）
- `numpy.int_`：长整型（取决于平台）
- `numpy.uint`：无符号长整型（取决于平台）
- `numpy.longlong`：长长整型（取决于平台）
- `numpy.ulonglong`：无符号长长整型（取决于平台）
- `numpy.half` / `numpy.float16`：半精度浮点数
- `numpy.single`：单精度浮点数（取决于平台）
- `numpy.double`：双精度浮点数（取决于平台）
- `numpy.longdouble`：扩展精度浮点数（取决于平台）
- `numpy.csingle`：由两个单精度浮点数表示的复数
- `numpy.cdouble`：由两个双精度浮点数表示的复数
- `numpy.clongdouble`：由两个扩展精度浮点数表示的复数

这些数据类型的定义取决于平台，但为了方便起见，NumPy 也提供了固定大小的别名。
