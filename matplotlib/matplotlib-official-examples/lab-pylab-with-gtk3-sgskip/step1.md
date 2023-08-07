# Import Libraries

First, we need to import the necessary libraries. We will be using Matplotlib, GTK3, and the Gtk module from the gi.repository.

```python
import matplotlib
matplotlib.use('GTK3Agg')  # or 'GTK3Cairo'
import gi
import matplotlib.pyplot as plt
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
```
