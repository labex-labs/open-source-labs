# Es wird einfacher zu wählen

Ein Problem bei der Verwendung von Vererbung ist die erhöhte Komplexität beim Auswählen der unterschiedlichen Klassen, die verwendet werden sollen (z. B. das Erinnern an die Namen, das Verwenden der richtigen `import`-Anweisungen usw.). Eine Fabrikfunktion kann dies vereinfachen. Fügen Sie eine Funktion `create_formatter()` zur Datei `tableformat.py` hinzu, die es einem Benutzer ermöglicht, einen Formatter einfacher zu erstellen, indem er ein Format wie `'text'`, `'csv'` oder `'html'` angibt. Beispielsweise:

```python
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('html')
>>> print_table(portfolio, ['name','shares','price'], formatter)
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
>>>
```

**Diskussion**

Die `TableFormatter`-Klasse in dieser Übung ist ein Beispiel für etwas, das als „abstrakte Basisklasse“ bekannt ist. Sie ist nicht für die direkte Verwendung gedacht. Stattdessen dient sie als Art von Schnittstellenspezifikation für einen Programmbereich – in diesem Fall die verschiedenen Ausgabeformate. Im Wesentlichen wird der Code, der die Tabelle erzeugt, gegen die abstrakte Basisklasse programmiert, mit der Erwartung, dass ein Benutzer eine geeignete Implementierung liefert. Solange alle erforderlichen Methoden implementiert wurden, sollte alles einfach „funktionieren“ (kreuzt die Finger).
