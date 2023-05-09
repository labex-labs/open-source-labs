# Solution

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
