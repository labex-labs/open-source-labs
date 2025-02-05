# Exception Best Practices

Don't catch exceptions. Fail fast and loud. If it's important, someone else will take care of the problem. Only catch an exception if you are _that_ someone. That is, only catch errors where you can recover and sanely keep going.
