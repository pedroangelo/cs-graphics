> move data pointer (dp) one cell to the right
< move dp one cell to the left
+ increment the byte stored in the cell pointed by dp by 1 bit
- decrement the byte stored in the cell pointed by dp by 1 bit
[ if value at dp is 0 then jump to matching closed bracket
] if value at dp is not 0 then jump back to the open bracket
. output byte stored in cell pointed by dp as a character
, store ASCII representation of input char in cell pointed by dp
