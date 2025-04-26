# 142. Linked List Cycle-II 　

- https://leetcode.com/problems/linked-list-cycle/description/

## STEP1

- 何も見ずに解いてみる

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = set()
        node = head
        while node:
            if node in visited_nodes:
                return node
            visited_nodes.add(node)
            node = node.next
        return None
```

#### 考えたこと,過程

- すでに訪れたことのあるノードを記録しておいて、繰り返しの中ですでに訪れたノードに再度訪れたらサイクルが存在するということ
- 141 Linked List Cycle と非常に似ていると感じた。違いはサイクルがある場合にはサイクルが始まる node を返す必要があることだと考えた。
- ここまでで１０分かからないくらいでした。

## STEP2

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        fast = head
        slow = head
        # サイクルが検出された時点でループ処理を終了
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        # ループが存在せず上のwhileが終了した場合
        if fast.next is None or fast.next.next is None:
            return None

        # fastを最初に移動させてもう一度追いかけることでサイクルの開始点を検出。
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
```

### プルリクやドキュメントを参照

#### 参照したもの

- https://github.com/shintaro1993/arai60/pull/5
- https://github.com/plushn/SWE-Arai60/blob/plushn-patch-1/leetcode142.md
- https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.2k4z0wt6ytf9
- https://docs.python.org/ja/3.13/library/stdtypes.html#set
- https://ttsuki.github.io/styleguide/cppguide.ja.html#General_Naming_Rules

#### 感想

- フロイドの循環検出法での実装を見たので自分でも試してみたが、step01 のほうが感覚的にわかりやすいと感じる。

## STEP3

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = set()
        node = head
        while node:
            if node in visited_nodes:
                return node
            visited_nodes.add(node)
            node = node.next
        return None
```

### 3 回ミスなく書く

- 1 回あたり約四分で完了
