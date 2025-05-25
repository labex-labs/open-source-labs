# Compreendendo os Tipos de Dados

NumPy suporta uma variedade de tipos numéricos que estão intimamente ligados aos da linguagem de programação C. Aqui estão alguns dos tipos de dados mais comumente usados no NumPy:

- `numpy.bool_`: Booleano (True ou False) armazenado como um byte
- `numpy.byte`: Char com sinal (definido pela plataforma)
- `numpy.ubyte`: Char sem sinal (definido pela plataforma)
- `numpy.short`: Short (definido pela plataforma)
- `numpy.ushort`: Short sem sinal (definido pela plataforma)
- `numpy.intc`: Int (definido pela plataforma)
- `numpy.uintc`: Int sem sinal (definido pela plataforma)
- `numpy.int_`: Long (definido pela plataforma)
- `numpy.uint`: Long sem sinal (definido pela plataforma)
- `numpy.longlong`: Long long (definido pela plataforma)
- `numpy.ulonglong`: Long long sem sinal (definido pela plataforma)
- `numpy.half` / `numpy.float16`: Float de meia precisão
- `numpy.single`: Float de precisão simples (definido pela plataforma)
- `numpy.double`: Float de dupla precisão (definido pela plataforma)
- `numpy.longdouble`: Float de precisão estendida (definido pela plataforma)
- `numpy.csingle`: Número complexo representado por dois floats de precisão simples
- `numpy.cdouble`: Número complexo representado por dois floats de dupla precisão
- `numpy.clongdouble`: Número complexo representado por dois floats de precisão estendida

Esses tipos de dados têm definições dependentes da plataforma, mas NumPy também fornece aliases de tamanho fixo para conveniência.
