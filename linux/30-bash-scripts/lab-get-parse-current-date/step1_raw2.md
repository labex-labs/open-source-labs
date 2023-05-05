# Get Parse Current Date

## Introduction

In Bash scripting, you can use the `date` command to get the current system date and time value. This challenge will guide you on how to parse the different parts of the date and time value using the `date` command.

## Problem

Create a Bash script named `date_parse.sh` that will separate the day, month, year, hour, minute, and second values of the current system date and time. The script should output the current date and time in the format `DD-MM-YYYY` and `HH:MM:SS`, respectively.

## Requirements

- The Bash script should be named `date_parse.sh`.
- The script should use the `date` command to get the current system date and time value.
- The script should parse the day, month, year, hour, minute, and second values using the `date` command.
- The script should output the current date and time in the format `DD-MM-YYYY` and `HH:MM:SS`, respectively.

## Solution

Add the following code to `date_parse.sh`:

```bash
#!/bin/bash
Year=$(date +%Y)
Month=$(date +%m)
Day=$(date +%d)
Hour=$(date +%H)
Minute=$(date +%M)
Second=$(date +%S)
echo $(date)
echo "Current Date is: $Day-$Month-$Year"
echo "Current Time is: $Hour:$Minute:$Second"
```

Save the file and run it with the following command:

```bash
bash date_parse.sh
```

The output should be similar to the following:

```bash
Tue Aug 31 14:30:00 PDT 2021
Current Date is: 31-08-2021
Current Time is: 14:30:00
```

## Summary

In this Bash challenge, you learned how to parse the different parts of the current system date and time value using the `date` command. You created a Bash script that separated the day, month, year, hour, minute, and second values and outputted the current date and time in the desired format.
