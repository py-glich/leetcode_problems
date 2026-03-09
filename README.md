#📌 Two Sum Implementation Errors (Python)
❌ Common Errors in This Code
1. Constructor Usage Error

👉 Wrong:

obj = Solution

👉 Correct:

obj = Solution()

✅ Always create class objects using parentheses.

2. Incorrect Complement Formula

❌ Wrong:

complement = num[i] - target

✅ Correct:

complement = target - num[i]

👉 Two Sum rule:

target = current_number + complement
3. Method Calling Error

❌ Wrong:

obj.twoSum(num,target)

(if object is not created properly)

✅ Correct flow:

Create Object → Call Method → Print Result

Example:

obj = Solution()
result = obj.twoSum(num, target)
print(result)
4. Class Initialization Confusion

❌ Avoid putting logic inside:

__init__()

👉 Use separate solving methods.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

#📌 Common Errors in Add Two Numbers Code
✅ 1. Using total Before Assignment (Very Common Bug)

❌ Wrong order:

carry = total // 10   # total not defined yet
total = val1 + val2 + carry

✅ Correct order:

total = val1 + val2 + carry
carry = total // 10

👉 Python throws:

UnboundLocalError
✅ 2. Missing ListNode Class

If you use:

ListNode()

without defining:

class ListNode:

You will get:

NameError: ListNode is not defined
✅ 3. Pointer Movement Error

These lines are important:

current.next = ListNode(total % 10)
current = current.next

If you forget:

current = current.next

👉 Linked list will not grow.

✅ 4. Dummy Node Mistake

Always return:

return dummy.next

❌ Not:

return dummy

Because dummy is only a helper node.

✅ 5. Loop Condition Error

Correct loop:

while l1 or l2 or carry:

Wrong loop may stop early.

⭐ Most Dangerous Beginner Mistake

This one:

val1 = l1.val

Without checking:

if l1 else 0

Fix:

val1 = l1.val if l1 else 0

Otherwise program crashes when list ends.

📌 Add Two Numbers Problem Type

Linked List Traversal

Carry Propagation Arithmetic

Pointer Manipulation

Time Complexity:

O(max(n, m))

Space Complexity:

O(max(n, m))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#📌 Substring vs Subsequence – Quick Study Notes
1. Definitions

Substring

A substring is a continuous block of characters taken from a string.

You cannot skip any characters.

Order is always preserved.

Subsequence

A subsequence is a set of characters taken from a string in the same order, but you can skip some characters.

Order must be preserved, but continuity is not required.

2. Key Differences
Feature	Substring	Subsequence
Continuity	✅ Must be continuous	❌ Can skip characters
Order	✅ Must preserve original order	✅ Must preserve original order
Skipping letters	❌ Not allowed	✅ Allowed
Example from "PWWKEW"	"WKE"	"PKE", "PWKE"
3. How to Identify

Substring → pick a block of letters without gaps.

Subsequence → pick letters in order, skip letters if needed.

Remember:

Substring → letters are together

Subsequence → letters can be apart

4. Why They Matter

Substring problems: sliding window techniques, longest substring without repeating characters.

Subsequence problems: dynamic programming, longest common subsequence, pattern matching, DNA analysis, file comparison.

Benefit of subsequences: detect patterns even if extra or irrelevant letters appear.

Benefit of substrings: detect continuous patterns without interruption.

5. Quick Visual Example

String: "PWWKEW"

Substring examples (continuous, no repeat):

PW, WKE, KEW

Subsequence examples (order preserved, can skip):

PKE, PWKE, WKE

Rule to remember:

Substring → no skips, continuous
Subsequence → can skip, order preserved

✅ Memory Tip:

Think Substring = solid block, Subsequence = arrows skipping letters.

When solving problems, check whether continuity is required (substring) or skipping is allowed (subsequence).

#Wrong Duplicate Check 

Issue in Code:

if char in seen and seen[char] <= left:
    left = seen[char] + 1

❌ Using <= left is incorrect

Correct Version:

if char in seen and seen[char] >= left:
    left = seen[char] + 1

Explanation:

Move left only when the duplicate character is inside the current window.

This ensures the sliding window always contains unique characters.
