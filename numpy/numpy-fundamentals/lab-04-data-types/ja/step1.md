# データ型の理解

NumPy は、C 言語におけるものと密接に関連したさまざまな数値型をサポートしています。以下は、NumPy で最も一般的に使用されるデータ型のいくつかです。

- `numpy.bool_`: バイトとして格納されるブール型 (True または False)
- `numpy.byte`: 符号付き char (プラットフォームに依存)
- `numpy.ubyte`: 符号なし char (プラットフォームに依存)
- `numpy.short`: ショート (プラットフォームに依存)
- `numpy.ushort`: 符号なしショート (プラットフォームに依存)
- `numpy.intc`: int (プラットフォームに依存)
- `numpy.uintc`: 符号なし int (プラットフォームに依存)
- `numpy.int_`: long (プラットフォームに依存)
- `numpy.uint`: 符号なし long (プラットフォームに依存)
- `numpy.longlong`: long long (プラットフォームに依存)
- `numpy.ulonglong`: 符号なし long long (プラットフォームに依存)
- `numpy.half` / `numpy.float16`: 半精度浮動小数点数
- `numpy.single`: 単精度浮動小数点数 (プラットフォームに依存)
- `numpy.double`: 倍精度浮動小数点数 (プラットフォームに依存)
- `numpy.longdouble`: 拡張精度浮動小数点数 (プラットフォームに依存)
- `numpy.csingle`: 2 つの単精度浮動小数点数で表される複素数
- `numpy.cdouble`: 2 つの倍精度浮動小数点数で表される複素数
- `numpy.clongdouble`: 2 つの拡張精度浮動小数点数で表される複素数

これらのデータ型はプラットフォームに依存する定義を持っていますが、NumPy は便利さのために固定サイズのエイリアスも提供しています。
