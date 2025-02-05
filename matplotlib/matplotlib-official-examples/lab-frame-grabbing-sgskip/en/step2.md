# Set up the writer

We need to set up the writer that will be used to write the frames to a file. We set the frames per second (fps) and add metadata such as the title, artist, and comment.

```python
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)
```
