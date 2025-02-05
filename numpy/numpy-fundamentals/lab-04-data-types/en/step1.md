# Understanding Data Types

NumPy supports a variety of numerical types that are closely tied to those in the C programming language. Here are some of the most commonly used data types in NumPy:

- `numpy.bool_`: Boolean (True or False) stored as a byte
- `numpy.byte`: Signed char (platform-defined)
- `numpy.ubyte`: Unsigned char (platform-defined)
- `numpy.short`: Short (platform-defined)
- `numpy.ushort`: Unsigned short (platform-defined)
- `numpy.intc`: Int (platform-defined)
- `numpy.uintc`: Unsigned int (platform-defined)
- `numpy.int_`: Long (platform-defined)
- `numpy.uint`: Unsigned long (platform-defined)
- `numpy.longlong`: Long long (platform-defined)
- `numpy.ulonglong`: Unsigned long long (platform-defined)
- `numpy.half` / `numpy.float16`: Half precision float
- `numpy.single`: Single precision float (platform-defined)
- `numpy.double`: Double precision float (platform-defined)
- `numpy.longdouble`: Extended-precision float (platform-defined)
- `numpy.csingle`: Complex number represented by two single-precision floats
- `numpy.cdouble`: Complex number represented by two double-precision floats
- `numpy.clongdouble`: Complex number represented by two extended-precision floats

These data types have platform-dependent definitions, but NumPy also provides fixed-size aliases for convenience.
