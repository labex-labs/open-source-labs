# Lesen von Daten mit PyArrow

PyArrow bietet die Funktionalität zum Lesen von Eingabe-/Ausgabedaten (IO), die in mehrere pandas-IO-Leser integriert wurde.

```python
# Importiere das IO-Modul
import io

# Erstelle ein StringIO-Objekt
data = io.StringIO("""a,b,c\n1,2.5,True\n3,4.5,False""")

# Lese die Daten in ein pandas-DataFrame ein, wobei PyArrow als Engine verwendet wird
df = pd.read_csv(data, engine="pyarrow")
```
