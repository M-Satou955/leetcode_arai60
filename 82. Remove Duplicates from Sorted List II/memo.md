## 取り組み方

- step1: 5 分考えて分からなかったら答えを見る。答えを理解したら、答えを隠して書く。筆が進まず 5 分立ったら答えを見る。答えを送信して正解するまで step01 を繰り返す。
- step2: コードを読みやすく整える。動くコードになったら終了。
- step3: 時間を計りながら書く。10 分以内に 3 回連続で AC されるまで書く。

## step1

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 重複を削除する場合先頭の削除ができないので先頭に0を挿入
        dummy_list = ListNode(0, head)
        pred = dummy_list
        while head is not None:
            if head.next is not None and head.val == head.next.val:
                while head.next is not None and head.val == head.next.val:
                    head = head.next
                # ポインターの示す先を重複を削除したheadに
                dummy_list.next = head.next
            else:
                dummy_list = dummy_list.next
            head = head.next
        return pred.next
```

- 82 と同じような考え方だが、重複があった値はすべて削除するのが違いだと考えた
- [1,1,2,3,4,5]のようなパターンの場合、82 のような形で重複を取り除くやり方が思いつかず、先頭に 0 を挿入し[0,1,1,12,3,4,5]のような形にしてから ListNode を操作するようにしたが力技感がある。

## step2

```


```

### 他の PR コメント見る

## step3
