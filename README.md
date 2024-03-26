# PASS_W5
Welcome to week 5's coding activity
- Note: you're not allowed to use in-built lists, sets and dictionaries
- To run tests, open terminal then:
```sh
python3 run_tests.py # and follow command line instructions
```

- If you encounter errors with the above, make sure that at least python runs on terminal
```sh
python3
```

- You may be directed to Microsoft Store (Windows), if so install python from there
- For mac see this: https://docs.python-guide.org/starting/install3/osx/

---

### Q1: Remove Second Half of Linked List
You are given a `Linked List`, `list1`.

Return a Linked List after removing the second half.

*Examples*

Input: Linked List: 1 -> 0 -> 0 -> 8 -> 2 -> 0 -> 8 -> 5
Output: Linked List: 1 -> 0 -> 0 -> 8 


---
### Q2: Kth smallest element 

You are given an unsorted list (`nums`) and a list of positive integers, (`queries`) of length `m`

You are to return a `List` of length `m` where `List[i]` is the `queries[i]`th smallest number

*Examples*

Input: nums = [1, 8, 2, 0, 5, 4, 7], queries = [4, 2, 1, 7]
Output: [4,1,0,8]
- i = 0: k = queries[0] = 4, the 4th smallest number in `nums` is 4, hence, output[0] = 4
- i = 1: k = queries[1] = 2, the 2nd smallest number in `nums` is 1, hence, output[1] = 1
- i = 2: k = queries[2] = 1, the 1st smallest number in `nums` is 0, hence, output[2] = 0
- i = 3: k = queries[3] = 7, the 7th smallest number in `nums` is 8, hence, output[3] = 8

Assume Each k in `queries` is valid (i.e. `1 <= k <= n` where `n` is the length of `nums`)

<details>
<summary>Hint</summary>
Think of a Data structure that stores the order of elements
</details>
