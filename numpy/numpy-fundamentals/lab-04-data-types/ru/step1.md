# Понимание типов данных

NumPy поддерживает различные числовые типы, которые тесно связаны с типами в языке программирования C. Вот некоторые из наиболее часто используемых типов данных в NumPy:

- `numpy.bool_`: Логический (True или False), хранимый как байт
- `numpy.byte`: Signed char (зависит от платформы)
- `numpy.ubyte`: Unsigned char (зависит от платформы)
- `numpy.short`: Short (зависит от платформы)
- `numpy.ushort`: Unsigned short (зависит от платформы)
- `numpy.intc`: Int (зависит от платформы)
- `numpy.uintc`: Unsigned int (зависит от платформы)
- `numpy.int_`: Long (зависит от платформы)
- `numpy.uint`: Unsigned long (зависит от платформы)
- `numpy.longlong`: Long long (зависит от платформы)
- `numpy.ulonglong`: Unsigned long long (зависит от платформы)
- `numpy.half` / `numpy.float16`: Полупрецизионный float
- `numpy.single`: Single precision float (зависит от платформы)
- `numpy.double`: Double precision float (зависит от платформы)
- `numpy.longdouble`: Extended-precision float (зависит от платформы)
- `numpy.csingle`: Комплексное число, представленное двумя single-precision float
- `numpy.cdouble`: Комплексное число, представленное двумя double-precision float
- `numpy.clongdouble`: Комплексное число, представленное двумя extended-precision float

Эти типы данных имеют определения, зависящие от платформы, но NumPy также предоставляет фиксированных размеров псевдонимы для удобства.
