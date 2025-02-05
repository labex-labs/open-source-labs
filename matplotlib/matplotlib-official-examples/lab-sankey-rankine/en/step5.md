# Add Labels and Formatting

We will add labels to the patches in the Sankey diagram using the `text` attribute of each patch. We will also format the text to be bold and increase the font size.

```python
diagrams = sankey.finish()
for diagram in diagrams:
    diagram.text.set_fontweight('bold')
    diagram.text.set_fontsize('10')
    for text in diagram.texts:
        text.set_fontsize('10')
```
