#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)

The number of times the `while` loop executes is directly related to the size of
`n`, therefore the runtime complexity is O(n).

b) O(n log n)

The for loop runs `n` number of times. Nested inside, the `while` loop then will
execute an additional number of times for each `n`.

c) O(n)

This recursive function will execute `n` number of times before reaching the
base-case.

## Exercise II

At a high-level, I would recommend using a binary search-type algorithm.

1. start at the middle floor, drop the egg.
2. if the egg cracks, calculate the next middle floor using the current floor as
   the ceiling/max
3. if the egg did not crack, calculate the next middle floor using the current
   floor as the minimum.
4. repeat steps 1 - 3 until you've reached the highest floor wherein the egg no
   longer breaks
