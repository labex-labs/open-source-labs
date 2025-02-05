# Understanding Zorder

The `zorder` attribute in Matplotlib is a floating point number that determines the drawing order of artists. Artists with higher `zorder` are drawn on top of those with lower `zorder`. The default value of `zorder` depends on the type of the artist. For example, images have a default `zorder` of 0, while patches have a default `zorder` of 1.
