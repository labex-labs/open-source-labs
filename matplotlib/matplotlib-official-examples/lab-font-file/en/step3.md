# Set the font path

We set the font path by using the `mpl.get_data_path()` method to get the path of the data directory and then append the path of the font file `cmr10.ttf` to it using `Path()` method from the `pathlib` module.

```python
from pathlib import Path

fpath = Path(mpl.get_data_path(), "fonts/ttf/cmr10.ttf")
```
