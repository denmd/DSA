
https://leetcode.com/problems/next-permutation/description/




- two pointer
- generally to dinf a next perumuattaion of array is 
- Identify the longest non-increasing suffix: Start from the end of the array and move backwards to find the first element that is not in increasing order. This element is the pivot.

- Find the rightmost element greater than the pivot: Once you've identified the pivot, look to the right of this element and find the smallest element that is larger than the pivot.

- Swap the pivot with this element: Swap the pivot element with the smallest element that is larger than the pivot found in the previous step.

- Reverse the suffix: Finally, reverse the order of the elements to the right of the original pivot's position (which is now the position of the element it was swapped with).
