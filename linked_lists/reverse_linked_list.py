from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current is not None:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt

        return previous


def build_list(values):
    dummy = ListNode(0)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def to_list(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    solution = Solution()
    head = build_list([1, 2, 3, 4, 5])
    reversed_head = solution.reverse_list(head)
    print(to_list(reversed_head))
