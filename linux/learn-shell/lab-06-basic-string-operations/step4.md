# Simple Data Extraction Example

Here's an example that demonstrates data extraction using substring operations:

```bash
DATARECORD="last=Clifford,first=Johnny Boy,state=CA"
COMMA1=$(expr index "$DATARECORD" ',') # 14 (position of first comma)
CHOP1FIELD=${DATARECORD:$COMMA1}       #
COMMA2=$(expr index "$CHOP1FIELD" ',')
LENGTH=$(expr $COMMA2 - 6 - 1)
FIRSTNAME=${CHOP1FIELD:6:$LENGTH} # "Johnny Boy"
echo $FIRSTNAME
```

Execute the script:

```bash
./string-operations.sh
```
