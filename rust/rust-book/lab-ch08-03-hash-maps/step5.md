# Updating a Hash Map

Although the number of key and value pairs is growable, each unique key can
only have one value associated with it at a time (but not vice versa: for
example, both the Blue team and the Yellow team could have the value `10`
stored in the `scores` hash map).

When you want to change the data in a hash map, you have to decide how to
handle the case when a key already has a value assigned. You could replace the
old value with the new value, completely disregarding the old value. You could
keep the old value and ignore the new value, only adding the new value if the
key _doesn’t_ already have a value. Or you could combine the old value and the
new value. Let’s look at how to do each of these!
