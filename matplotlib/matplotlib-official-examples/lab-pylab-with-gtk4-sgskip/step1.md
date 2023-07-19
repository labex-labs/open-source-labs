# Import the required libraries

```python
import matplotlib
matplotlib.use('GTK4Agg')
import gi
import matplotlib.pyplot as plt

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
```

We import the required libraries including `matplotlib`, `gi`, `pyplot`, and `Gtk`. We set the backend of matplotlib to use GTK4.
