# Introducing Pipelines

Now, let's start using pipelines to process this information. A pipeline is created using the `|` (pipe) symbol between commands. It takes the output of the command on the left and feeds it as input to the command on the right.

We'll use the `grep` command to filter the output for specific information. The `grep` command searches for patterns in text.

Let's find all lines containing "model name":

```bash
cat /proc/cpuinfo | grep "model name"
```

This pipeline first reads the contents of `/proc/cpuinfo`, then passes that output to `grep`, which filters for lines containing "model name".

You should see one line for each CPU core, showing the model of your processor(s).
