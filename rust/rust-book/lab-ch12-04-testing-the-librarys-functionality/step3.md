# Writing Code to Pass the Test

Currently, our test is failing because we always return an empty vector. To fix that and implement `search`, our program needs to follow these steps:

1.  Iterate through each line of the contents.
2.  Check whether the line contains our query string.
3.  If it does, add it to the list of values we're returning.
4.  If it doesn't, do nothing.
5.  Return the list of results that match.

Let's work through each step, starting with iterating through lines.
