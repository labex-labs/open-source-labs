# Converter numpy.datetime64 para data matplotlib

Objetos `numpy.datetime64` possuem precisão de microssegundos para um espaço de tempo muito maior do que objetos `.datetime`. No entanto, atualmente, o tempo Matplotlib é convertido de volta apenas para objetos datetime, que possuem resolução de microssegundos e anos que abrangem apenas de 0000 a 9999.

```python
date1 = np.datetime64('2000-01-01T00:10:00.000012')
mdate1 = mdates.date2num(date1)
```
