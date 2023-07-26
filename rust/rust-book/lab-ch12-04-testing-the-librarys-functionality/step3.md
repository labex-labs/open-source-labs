# Writing Code to Pass the Test

Currently, our test is failing because we always return an empty vector. To fix
that and implement `search`, our program needs to follow these steps:

1. Iterate through each line of the contents.
1. Check whether the line contains our query string.
1. If it does, add it to the list of values we’re returning.
1. If it doesn’t, do nothing.
1. Return the list of results that match.

Let’s work through each step, starting with iterating through lines.
