from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None


class Solution:
    def add_two_numbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:
            value_1 = l1.val if l1 is not None else 0
            value_2 = l2.val if l2 is not None else 0

            total = value_1 + value_2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return dummy.next


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
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    print(to_list(solution.add_two_numbers(l1, l2)))
