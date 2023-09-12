# Exercise

In this exercise, you need to create a string, an integer, and a complex variable using command substitution.

- The string should be named `BIRTHDATE` and should contain the text "Jan 1, 2000".
- The integer should be named `Presents` and should contain the number 10.
- The complex variable should be named `BIRTHDAY` and should contain the full weekday name of the day matching the date in variable `BIRTHDATE`.

You can use the `date` command to convert a date format into a different date format. For example, to convert a date value `date1` to the day of the week of `date1`, use the following command:

```bash
date -d "$date1" +%A
```

> **Note:** The `-d` option is used to specify the date to be converted. The `+%A` option is used to specify the output format.

## Tasks

- Modify the `~/project/birthdate.sh` script to create the variables as described above.

## Results

- Run the script and verify the output.

```bash
cd ~/project
chmod +x birthdate.sh
./birthdate.sh
```

```text
Jan 1, 2000
10
Saturday
```
