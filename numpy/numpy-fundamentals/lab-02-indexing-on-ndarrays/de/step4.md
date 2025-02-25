# Fortgeschrittenes Indexieren

Fortgeschrittenes Indexieren tritt ein, wenn das Auswahlobjekt `obj` ein nicht-Tupel-Sequenzenobjekt, ein ndarray (vom Datentyp Integer oder Bool) oder ein Tupel mit mindestens einem Sequenzenobjekt oder ndarray (vom Datentyp Integer oder Bool) ist. Es gibt zwei Arten von fortgeschrittenem Indexieren: Integer- und Boolean-Indexieren.

## Integer-Array-Indexieren

Integer-Array-Indexieren ermöglicht die Auswahl beliebiger Elemente im Array basierend auf ihrem N-dimensionalen Index. Jedes Integer-Array repräsentiert eine Anzahl von Indizes in diese Dimension.

```python
x = np.arange(10, 1, -1)
print(x[np.array([3, 3, 1, 8])])  # Ausgabe: [7, 7, 9, 2]
print(x[np.array([3, 3, -3, 8])])  # Ausgabe: [7, 7, 4, 2]
```

## Boolean-Array-Indexieren

Boolean-Array-Indexieren ermöglicht die Auswahl von Array-Elementen basierend auf einer booleschen Bedingung. Das Ergebnis ist ein neues Array, das nur die Elemente enthält, die den `True`-Werten des booleschen Arrays entsprechen.

```python
x = np.array([1., -1., -2., 3])
x[x < 0] += 20
print(x)  # Ausgabe: [ 1., 19., 18., 3.]
```
