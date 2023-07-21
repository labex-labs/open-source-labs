# Discussion

Something very powerful just happened here. You moved an interesting iteration pattern
(reading lines at the end of a file) into its own little function. The `follow()` function
is now this completely general purpose utility that you can use in any program. For
example, you could use it to watch server logs, debugging logs, and other similar data sources.
That's kind of cool.
