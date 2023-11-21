---
date: 2022-07-01
title: Mastering Common Patterns to Solve Leetcode Problems
postSlug: leetcode-patterns
featured: false
ogImage: ""
categories:
  - leetcode
  - interview
  - algorithms
description: Knowing these patterns can help you solve most of the problems in leetcode.
---

In this post, I will introduce you to 14 important patterns that can help you solve most of the problems on Leetcode. I will provide a template for each pattern to help you quickly apply it to a problem, as well as a list of important problems to practice with. By the end of this post, you will have a powerful set of tools to enhance your problem-solving skills on Leetcode and beyond. Let's get started!

## 1. Sliding Window

The sliding window pattern is a common technique used to solve problems involving arrays or strings. It involves using a fixed-size "window" that slides through the array or string, and performs some operation on each sub-array or sub-string that it covers. This allows you to perform the operation on each possible sub-array or sub-string without having to create a new array or string for each one.

Here is a simple template in Python that you can use to solve any problem that uses the sliding window pattern:

**Template**

```python
# initialize the window
window_start = 0
window_end = 0

# initialize any other variables you need
result = 0

# loop until the window_end reaches the end of the array/string
while window_end < len(arr):
  # perform the operation on the current sub-array/sub-string
  result = update_result(arr[window_start:window_end+1], result)

  # move the window to the right
  window_start += 1
  window_end += 1

# return the final result
return result
```

To use this template, you just need to define the update_result() function, which should take in the current sub-array/sub-string and the current result, and return an updated result.

**Practise**

Here are some important problems on leetcode that can be solved using the sliding window pattern:

- [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/): This problem involves finding the longest substring in a string that does not contain any repeating characters. The sliding window pattern can be used to efficiently search for this substring.
- [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/): This problem involves finding the smallest subarray in an array that has a given sum. The sliding window pattern can be used to efficiently search for this subarray.
- [Permutation in String](https://leetcode.com/problems/permutation-in-string/): This problem involves checking whether one string is a permutation of another string. The sliding window pattern can be used to efficiently compare the two strings and check for a permutation.
- [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) 💰: This problem involves finding the longest substring in a string that contains at most two distinct characters. The sliding window pattern can be used to efficiently search for this substring.
- [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/): This problem involves finding the smallest substring in a string that contains all of the characters in another string. The sliding window pattern can be used to efficiently search for this substring.

## 2. Two pointers

The two pointers pattern is a common technique used to solve problems involving arrays or strings. It involves using two "pointers" that point to different elements in the array or string, and moving them in a specific way to perform some operation on the sub-array or sub-string they cover. This allows you to perform the operation on each possible sub-array or sub-string without having to create a new array or string for each one.

Here is a simple template in Python that you can use to solve any problem that uses the two pointers pattern:

**Template**

```python
# initialize the pointers
pointer1 = 0
pointer2 = 0

# initialize any other variables you need
result = 0

# loop until the pointers reach the end of the array/string
while pointer1 < len(arr) and pointer2 < len(arr):
  # perform the operation on the current sub-array/sub-string
  result = update_result(arr[pointer1:pointer2+1], result)

  # move the pointers according to the specific rules of the pattern
  pointer1, pointer2 = move_pointers(pointer1, pointer2)

# return the final result
return result
```

To use this template, you just need to define the move_pointers() and update_result() functions. The move_pointers() function should take in the current values of the pointers, and return updated values for the pointers according to the specific rules of the pattern. The update_result() function should take in the current sub-array/sub-string and the current result, and return an updated result.

**Practise**

Here are some important problems on leetcode that can be solved using the two pointers pattern:

- [Two Sum](https://leetcode.com/problems/two-sum/): This problem involves finding two numbers in an array that add up to a given target number. The two pointers pattern can be used to efficiently search for these numbers by moving the pointers in opposite directions.
- [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/): This problem involves removing duplicate elements from a sorted array. The two pointers pattern can be used to efficiently remove the duplicates by comparing the elements at each pointer and moving them as necessary.
- [Container With Most Water](https://leetcode.com/problems/container-with-most-water/): This problem involves finding the maximum area of a container formed by two lines on a graph. The two pointers pattern can be used to efficiently search for the maximum area by moving the pointers in opposite directions.
- [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/): This problem involves finding the amount of rainwater that can be trapped between bars on a histogram. The two pointers pattern can be used to efficiently calculate the trapped water by moving the pointers inwards from the ends of the array.

## 3. Fast and slow pointers

The fast and slow pointers pattern is a common technique used to solve problems involving linked lists. It involves using two pointers that traverse the linked list at different speeds. The "slow" pointer moves one step at a time, while the "fast" pointer moves two steps at a time. This allows the fast pointer to "lap" the slow pointer, and makes it possible to detect when the two pointers are pointing to the same node (i.e., they have "collided").

**Template**

```python
# initialize the pointers
slow_pointer = linked_list.head
fast_pointer = linked_list.head

# initialize any other variables you need
result = 0

# loop until the pointers reach the end of the linked list
while fast_pointer is not None and fast_pointer.next is not None:
  # perform the operation on the current nodes
  result = update_result(slow_pointer, fast_pointer, result)

  # move the pointers according to the specific rules of the pattern
  slow_pointer = slow_pointer.next
  fast_pointer = fast_pointer.next.next

  # check if the pointers have collided
  if slow_pointer == fast_pointer:
    break

# return the final result
return result
```

To use this template, you just need to define the update_result() function, which should take in the current values of the slow and fast pointers, and the current result, and return an updated result.

**Practise**

Here are some important problems on leetcode that can be solved using the fast and slow pointers pattern:

- [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/): This problem involves detecting whether a linked list contains a cycle. The fast and slow pointers pattern can be used to efficiently detect the cycle by moving the pointers at different speeds and checking for overlap.
- [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/): This problem involves finding the middle element of a linked list. The fast and slow pointers pattern can be used to efficiently find the middle element by moving the pointers at different speeds and stopping when the fast pointer reaches the end of the list.
- [Happy Number](https://leetcode.com/problems/happy-number/): This problem involves determining whether a number is a happy number. The fast and slow pointers pattern can be used to efficiently check for happiness by moving the pointers at different speeds and checking for a cycle.
  Reorder List: This problem involves reordering the elements of a linked list in a specific way. The fast and slow pointers pattern can be used to efficiently reorder the elements by moving the pointers at different speeds and rearranging the elements as necessary.
- [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/): This problem involves checking whether a linked list is a palindrome. The fast and slow pointers pattern can be used to efficiently check for palindromicity by moving the pointers at different speeds and comparing the elements at each pointer.

## 4. Merge Intervals

The merge intervals pattern is a common technique used to solve problems involving sets of intervals. It involves sorting the intervals by their start time, and then merging any intervals that overlap. This allows you to take a set of potentially overlapping intervals and convert it into a set of non-overlapping intervals.

Here is a simple template in Python that you can use to solve any problem that uses the merge intervals pattern:

**Template**

```python

# sort the intervals by their start time
intervals = sorted(intervals, key=lambda x: x[0])

# initialize the result list with the first interval
result = [intervals[0]]

# loop through the remaining intervals
for i in range(1, len(intervals)):
  # get the last interval in the result list
  last_interval = result[-1]

  # check if the current interval overlaps with the last interval
  if intervals[i][0] <= last_interval[1]:
    # if it does, merge the current interval with the last interval
    result[-1] = (last_interval[0], max(last_interval[1], intervals[i][1]))
  else:
    # if it doesn't, add the current interval to the result list
    result.append(intervals[i])

# return the final result
return result
```

To use this template, you just need to provide a list of intervals (in the form of tuples of start and end times), and the template will return a list of non-overlapping intervals.

**Practise**

Here are some important problems on leetcode that can be solved using the merge intervals pattern:

-[Merge Intervals](https://leetcode.com/problems/merge-intervals): This problem involves merging a list of intervals that may overlap.

- [Insert Interval](https://leetcode.com/problems/insert-interval): This problem involves inserting a new interval into a list of intervals that may overlap.
- [Meeting Rooms](https://leetcode.com/problems/meeting-rooms): This problem involves checking whether it is possible to attend all of the meetings in a list of intervals.
- [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii): This problem involves finding the minimum number of rooms needed to hold all of the meetings in a list of intervals.
- [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons): This problem involves finding the minimum number of arrows needed to burst a given set of balloons.

## 5. Cyclic sort

Cyclic sort is a technique used to sort a list of numbers that are in a certain range, but not necessarily in the correct order. It involves looping through the list and "cycling" the numbers into the correct positions. For example, if the list is [3, 1, 5, 4, 2] and the range is 1 to 5, the first step would be to put the 1 in its correct position at index 0, the second step would be to put the 2 in its correct position at index 1, and so on.

**Template**

```python
# initialize the current index and the number of items to sort
current_index = 0
num_to_sort = len(arr)

# loop until all items have been sorted
while num_to_sort > 0:
  # get the correct value for the current index
  correct_value = current_index + 1

  # check if the current value is already correct
  if arr[current_index] == correct_value:
    # if it is, move on to the next index
    current_index += 1
    num_to_sort -= 1
  else:
    # if it isn't, swap the current value with the correct value
    arr[current_index], arr[arr[current_index] - 1] = arr[arr[current_index] - 1], arr[current_index]

# return the sorted array
return arr
```

To use this template, you just need to provide a list of numbers that are in a certain range, and the template will return the sorted list.

**Practise**

Here are some important problems on leetcode that can be solved using the cyclic sort pattern:

- [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number): This problem involves finding the duplicate element in an array of numbers that are in the range 1 to n.
- [Find the Missing Number](https://leetcode.com/problems/find-the-missing-number): This problem involves finding the missing element in an array of numbers that are in the range 1 to n.
- [First Missing Positive](https://leetcode.com/problems/first-missing-positive/): This problem involves finding the smallest missing positive number in an array of numbers.
- [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array): This problem involves finding all of the duplicate elements in an array of numbers.

## 6. In-place reversal of linked-list

"In-place reversal of a linked list" refers to a technique for reversing the order of the nodes in a linked list without using any additional data structures. This is done by changing the links between the nodes in the linked list so that the nodes are connected in the opposite order.

**Template**

```python
# initialize the previous, current, and next nodes
prev_node = None
curr_node = linked_list.head
next_node = None

# loop until the current node is None
while curr_node is not None:
  # store the next node
  next_node = curr_node.next

  # reverse the link between the current and previous nodes
  curr_node.next = prev_node

  # move the previous and current nodes forward
  prev_node = curr_node
  curr_node = next_node

# set the head of the linked list to the new start node
linked_list.head = prev_node
```

To use this template, you just need to provide a linked list object and the template will reverse the order of the nodes in the linked list.

**Practise**

Here are some important problems on leetcode that can be solved using the in-place reversal of linked list pattern:

- [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list): This problem involves reversing the order of elements in a linked list.
- [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii): This problem involves reversing a portion of a linked list.
- [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list): This problem involves checking whether a linked list is a palindrome.
- [Reorder List](https://leetcode.com/problems/reorder-list): This problem involves reordering the elements of a linked list in a specific way.
- [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs): This problem involves swapping the nodes in a linked list in pairs.

## 7. Tree BFS

The tree BFS (Breadth-First Search) pattern is a technique used to traverse the nodes of a tree in a level-by-level order. In the case of a binary tree (i.e., a tree in which each node has at most two children), the tree BFS algorithm can be implemented as follows:

**Template**

```python
# initialize the queue with the root node
queue = [root]

# initialize any other variables you need
result = []

# loop until the queue is empty
while len(queue) > 0:
  # get the next node from the queue
  current_node = queue.pop(0)

  # perform the operation on the current node
  result = update_result(current_node, result)

  # add the left and right child nodes of the current node to the queue
  if current_node.left is not None:
    queue.append(current_node.left)
  if current_node.right is not None:
    queue.append(current_node.right)

# return the final result
return result
```

To use this template, you just need to provide the root node of the binary tree and define the update_result() function, which should take in the current node and the current result, and return an updated result.

**Practise**

Here are some important problems on leetcode that can be solved using the tree BFS pattern:

- [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal): This problem involves performing a level-order traversal of a binary tree.
- [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree): This problem involves finding the minimum depth of a binary tree.
- [Symmetric Tree](https://leetcode.com/problems/symmetric-tree): This problem involves checking whether a binary tree is symmetric.
- [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal): This problem involves performing a zigzag-level-order traversal of a binary tree.
- [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree): This problem involves serializing and deserializing a binary tree.

## 8. Tree DFS

The tree DFS (Depth-First Search) pattern is a technique used to traverse the nodes of a tree in a depth-first manner. In the case of a binary tree (i.e., a tree in which each node has at most two children), the tree DFS algorithm can be implemented as follows:

**Template**

```python
# initialize any other variables you need
result = []

# perform the DFS traversal on the root node
traverse(root, result)

# return the final result
return result

def traverse(node, result):
  # perform the operation on the current node
  result = update_result(node, result)

  # recursively traverse the left and right child nodes of the current node
  if node.left is not None:
    traverse(node.left, result)
  if node.right is not None:
    traverse(node.right, result)
```

To use this template, you just need to provide the root node of the binary tree and define the update_result() function, which should take in the current node and the current result, and return an updated result.

**Practise**

Here are some important problems on leetcode that can be solved using the tree DFS pattern:

- [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal): This problem involves performing a preorder traversal of a binary tree.
- [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree): This problem involves checking whether a binary tree is a valid binary search tree.
- [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree): This problem involves finding the maximum depth of a binary tree.

## 9. Two heaps

The "two heaps" pattern is a common technique used to solve problems involving sets of numbers. It involves using two heaps (i.e., data structures that provide efficient ways to insert and remove items, and to find the minimum or maximum item) to store the numbers in the set. This allows you to efficiently maintain certain properties of the numbers in the set, and to quickly perform operations on the numbers when needed.

**Template**

```python
import heapq

# initialize the two heaps
heap1 = []
heap2 = []

# initialize any other variables you need

# loop through the numbers in the set
for num in nums:
  # insert the number into the appropriate heap
  if condition1:
    heapq.heappush(heap1, num)
  else:
    heapq.heappush(heap2, num)

  # balance the heaps if necessary
  if condition2:
    heapq.heappush(heap2, heapq.heappop(heap1))
  elif condition3:
    heapq.heappush(heap1, heapq.heappop(heap2))

  # update any other variables you need
  update_variables(num)

# return the final result
return result
```

To use this template, you just need to provide a list of numbers and define the condition1, condition2, condition3, and update_variables() functions. These functions should determine which heap to insert the current number into, whether the heaps need to be balanced, and how to update any other variables you need.

For example, if you want to use the two heaps pattern to find the median of a set of numbers, you could define the following functions:

```python
# insert the number into the smaller_half heap if it is smaller than the current median,
# or into the larger_half heap if it is larger or equal to the current median
def condition1(num, median):
  return num < median

# balance the heaps if the size difference between them is greater than 1
def condition2(smaller_half, larger_half):
  return len(smaller_half) > len(larger_half) + 1

# balance the heaps if the size difference between them is greater than 1
def condition3(smaller_half, larger_half):
  return len(larger_half) > len(smaller_half) + 1

# update the median if the size of the two heaps is equal, or if one heap is larger than the other
def update_variables(num, median, smaller_half, larger_half):
  if len(smaller_half) == len(larger_half):
    median = (-smaller_half[0] + larger_half[0]) / 2
  elif len(smaller_half) > len(larger_half):
    median = -smaller_half[0]
  else:
    median = larger_half[0]
```

**Practise**

Here are some important problems on leetcode that can be solved using the two heaps pattern:

- [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array): This problem involves finding the kth largest element in an array.
- [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays): This problem involves finding the median of two sorted arrays.
- [Sliding Window Median](https://leetcode.com/problems/sliding-window-median): This problem involves finding the median of the elements in a sliding window of an array.
- [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements): This problem involves finding the k most frequent elements in an array.
- [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix): This problem involves finding the kth smallest element in a sorted matrix.

## 10. Subsets

The "subsets" pattern is a common technique used to solve problems involving sets of numbers. It involves generating all possible subsets of the set and then performing some operation on each subset to find the desired result. This allows you to consider all possible combinations of numbers in the set and to efficiently compute the result for each combination.

**Template 1**

```python
# initialize the result
result = []

# generate all possible subsets of the set
for subset in itertools.combinations(nums, r) for r in range(len(nums)+1):
  # perform the operation on the current subset
  result = update_result(subset, result)

# return the final result
return result
```

**Template 2**

```python
# initialize the result
result = []

# generate all possible subsets of the set
for i in range(1, 2**len(nums)):
  # convert the binary representation of i to a list of indices
  indices = [j for j in range(len(nums)) if i & (1 << j)]

  # generate the current subset
  subset = [nums[j] for j in indices]

  # perform the operation on the current subset
  result = update_result(subset, result)

# return the final result
return result
```

It uses a single loop and binary operations to generate the subsets. It converts the binary representation of each number in the range 1..2^len(nums) to a list of indices, and then uses those indices to select the elements of the set that are included in the current subset.

**Practise**

Here are some important problems on leetcode that can be solved using the subsets pattern:

- [Subsets](https://leetcode.com/problems/subsets): This problem involves generating all of the subsets of a given set of elements.
- [Subsets II](https://leetcode.com/problems/subsets-ii): This problem involves generating all of the subsets of a given set of elements, allowing for duplicates.
- [Permutations](https://leetcode.com/problems/permutations): This problem involves generating all of the permutations of a given set of elements.
- [Permutations II](https://leetcode.com/problems/permutations-ii): This problem involves generating all of the permutations of a given set of elements, allowing for duplicates.
- [Combination Sum](https://leetcode.com/problems/combination-sum): This problem involves finding all of the combinations of a given set of elements that add up to a specific target sum.

## 11. Modified Binary Search

The "modified binary search" pattern is a common technique used to solve problems involving a sorted array of numbers. It is similar to regular binary search, but it allows you to modify the condition used to determine whether to search the left or right half of the array. This can be useful if the problem you're trying to solve involves finding the position of an element in the array that satisfies a certain condition, or if the array has duplicate elements and you need to find the first or last occurrence of a given element.

**Template**

```python
# initialize the left and right pointers
left = 0
right = len(nums) - 1

# search the array until the left and right pointers meet
while left < right:
  # calculate the middle index
  mid = left + (right - left) // 2

  # modify the condition used to determine which half of the array to search
  if condition(nums[mid]):
    right = mid
  else:
    left = mid + 1

# return the final result
return left
```

If you want to use the modified binary search pattern to find the first occurrence of a given element in an array, you could define the following condition() function:

```python
def condition(num):
  return num == target and (mid == 0 or nums[mid-1] != target)
```

This function checks whether the current element is equal to the target element and whether it is the first occurrence of that element in the array (i.e., whether the element before it is not equal to the target). If both of these conditions are satisfied, then the function returns True, indicating that the left pointer should be updated to the current index. Otherwise, it returns False, indicating that the right pointer should be updated to the current index.

**Practise**

Here are some important problems on leetcode that can be solved using the modified binary search pattern:

- [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array): This problem involves searching for an element in a rotated sorted array.
- [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array): This problem involves finding the minimum element in a rotated sorted array.
- [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii): This problem involves searching for an element in a rotated sorted array that may contain duplicates.
- [Find Peak Element](https://leetcode.com/problems/find-peak-element): This problem involves finding a peak element in an array.
- [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements): This problem involves finding the k closest elements to a given target in an array.

## 12. Top K elements

The "top k elements" pattern is a common technique used to solve problems involving a large set of numbers. It involves finding the largest or smallest k elements in the set and then performing some operation on those elements to find the desired result. This allows you to efficiently select the most important elements from the set and to compute the result using only those elements.

**Template**

```python
# initialize the heap with the first k elements of the set
heap = nums[:k]

# heapify the heap
heapq.heapify(heap)

# loop through the remaining elements of the set
for num in nums[k:]:
  # insert the current element into the heap if it is larger than the smallest element in the heap
  if num > heap[0]:
    heapq.heappushpop(heap, num)

# return the final result
return operation(heap)
```

For example, if you want to use the top k elements pattern to find the sum of the largest k elements in a set, you could define the following operation() function:

```python
def operation(heap):
  return sum(heap)
```

This function simply returns the sum of all the elements in the heap, which are the largest k elements in the set

**Practise**

Here are some important problems on leetcode that can be solved using the top k elements pattern:

- [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array): This problem involves finding the kth largest element in an array.
- [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements): This problem involves finding the k most frequent elements in an array.
- [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix): This problem involves finding the kth smallest element in a sorted matrix.
- [Sort Colors](https://leetcode.com/problems/sort-colors): This problem involves sorting an array of colors (represented as numbers) in place.
- [Minimum Cost to Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers): This problem involves finding the minimum cost to hire k workers, given their wage and productivity.

## 13. K-way Merge (using heap)

The k-way merge pattern using a heap is a common technique used to merge k sorted arrays into a single sorted array. It involves using a heap data structure to efficiently select the smallest element from the k arrays and to add it to the result. This allows you to efficiently combine the k arrays into a single sorted array and to perform further operations on that array.

**Template**

```python
# initialize the result and the heap with the first elements of the k arrays
result = []
heap = [(arrays[i][0], i) for i in range(k)]

# heapify the heap
heapq.heapify(heap)

# loop until all the arrays have been merged
while heap:
  # get the smallest element from the heap
  min_element, min_index = heapq.heappop(heap)

  # add the smallest element to the result
  result.append(min_element)

  # insert the next element from the array where the smallest element was found into the heap
  if min_index < len(arrays[min_index]) - 1:
    heapq.heappush(heap, (arrays[min_index][min_index+1], min_index))

# return the final result
return result
```

**Practise**

Here are some important problems on leetcode that can be solved using the k-way merge (using heap) pattern:

- [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists): This problem involves merging k sorted linked lists into a single sorted linked list.
- [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem): This problem involves finding the skyline of a set of buildings.
- [Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks): This problem involves connecting a set of sticks with minimum total cost.
- [Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended): This problem involves finding the maximum number of events that a person can attend, given a list of events with start and end times.

## 14. Topological Sort

Topological sort is an algorithm that is used to arrange the vertices of a directed acyclic graph (DAG) in a linear order such that, for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. This is useful for problems where a certain set of dependencies must be satisfied, such as scheduling tasks or determining the order in which to assemble a product.

To perform a topological sort, we first identify all of the vertices with no incoming edges (i.e., no dependencies) and put them in a queue. We then remove these vertices from the graph and repeat the process until the queue is empty. At each step, we add the vertices we remove to a list, which will eventually give us the topological ordering of the vertices.

Topological sort is commonly used to solve problems on LeetCode, such as "Course Schedule" and "Alien Dictionary". It can also be useful for solving other problems that involve dependencies between objects or tasks.

**Template**

```python
from collections import deque

def topological_sort(vertices, edges):
    # Create a list to store the topological ordering of the vertices
    top_order = []

    # Create a queue to keep track of the vertices with no incoming edges
    queue = deque()

    # Create a dictionary to store the indegrees of each vertex
    indegrees = {vertex: 0 for vertex in vertices}

    # Create a dictionary to store the adjacency list for each vertex
    adj_list = {vertex: [] for vertex in vertices}

    # Populate the indegrees dictionary and adjacency list
    for edge in edges:
        u, v = edge
        indegrees[v] += 1
        adj_list[u].append(v)

    # Add all vertices with no incoming edges to the queue
    for vertex, indegree in indegrees.items():
        if indegree == 0:
            queue.append(vertex)

    # Perform the topological sort
    while queue:
        # Remove a vertex from the queue
        vertex = queue.popleft()

        # Add the vertex to the topological ordering
        top_order.append(vertex)

        # Decrement the indegree of each of its neighbors
        for neighbor in adj_list[vertex]:
            indegrees[neighbor] -= 1

            # If the indegree of a neighbor becomes 0, add it to the queue
            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    # If there are any vertices left in the graph, then the original graph was not a DAG
    if len(top_order) != len(vertices):
        return []

    return top_order
```

**Practise**

Here are some important problems on leetcode that can be solved using the topological sort pattern:

- [Course Schedule](https://leetcode.com/problems/course-schedule): This problem involves checking whether a given set of courses can be completed, given the dependencies between the courses.
- [Course Schedule II](https://leetcode.com/problems/course-schedule-ii): This problem involves finding the order in which the courses should be taken in order to complete them all.
- [Alien Dictionary](https://leetcode.com/problems/alien-dictionary): This problem involves reconstructing the order of the letters in an alien language, given a list of words.
- [Sequence Reconstruction](https://leetcode.com/problems/sequence-reconstruction): This problem involves checking whether a given sequence can be reconstructed from a given set of subsequences.
- [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees): This problem involves finding the root(s) of a tree with minimum height.

# References

- [Grokking the Coding Interview: Patterns for Coding Questions](https://designgurus.org/link/pvL2Ws?url=https%3A%2F%2Fdesigngurus.org%2Fcourse%3Fcourseid%3Dgrokking-the-coding-interview)

  This is structured course for understanding every pattern step by step using visual walk-through.

  **\*Disclaimer**: It's an affiliate link. If you would like to thank me for this post, please purchase via that link. If you do not want to use that link for some reason, [here](https://designgurus.org/course/grokking-the-coding-interview) is a clean link.\* :)

- [14 patterns to ace any coding interview question](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)

  This blog post is a fork of this post. I would recommend checking it out.
  It's an overview of the [Grokking course](https://designgurus.org/link/pvL2Ws?url=https%3A%2F%2Fdesigngurus.org%2Fcourse%3Fcourseid%3Dgrokking-the-coding-interview) shared above.

- [emre.me #coding patterns](https://emre.me/categories/#coding-patterns)

  Excellent post about how to identify the patterns. Highly recommended.
