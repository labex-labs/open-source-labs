# Min Heap

Problem: Implement a min heap with extract_min and insert methods.

## Requirements

- Can we assume the inputs are ints?
  - Yes
- Can we assume this fits memory?
  - Yes

## Example Usage

- Extract min of an empty tree
- Extract min general case
- Insert into an empty tree
- Insert general case (left and right insert)

<pre>
          _5_
        /     \
       20     15
      / \    /  \
     22  40 25
     
extract_min(): 5

          _15_
        /      \
       20      25
      / \     /  \
     22  40 

insert(2):

          _2_
        /     \
       20      5
      / \     / \
     22  40  25  15
</pre>
