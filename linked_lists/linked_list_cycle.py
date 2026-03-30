from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False


if __name__ == "__main__":
    first = ListNode(3)
    second = ListNode(2)
    third = ListNode(0)
    fourth = ListNode(-4)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = second

    solution = Solution()
    print(solution.has_cycle(first))
