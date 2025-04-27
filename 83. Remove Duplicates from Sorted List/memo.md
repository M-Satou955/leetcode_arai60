# 83. Remove Duplicates from Sorted List

- https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/?envType=problem-list-v2&envId=xo2bgr0r

## STEP1

- 何も見ずに解いてみる

```python
class Solution:
    #  この状態でどうすればいいかわからなくなり答えをみた。
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return node
```

#### 考えたこと,過程

- LinkedList の要素の重複を削除するとのことだったので、要素を head からすべて辿って配列に格納して、set()で重複を削除することをまず考えた。
- 上記のアプローチだと返却するデータの構造を配列からもう一度 ListNode に変換する必要があり、変換のやり方が思いつかない＆非効率そうなことに気づき断念（ここまでで 13 分ほど）
- 今、ポインターが指している node とその次の node を比較して、値が同じなら次の node を飛ばすという処理を繰り返して終端まで行き、飛ばされなかった値のみの内容を返却する？
- 変数を通して LinkedList を操作しているので変数を返却することで、飛ばされなかった値をのみの LinkedList を返却できると考えたが、うまくいかず他の人のコードを見る
- データ構造に対する理解度が低いと感じる。

## STEP2

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head
```

> https://github.com/garunitule/coding_practice/blob/83/LinkedList/83/memo.md

- 二重のループを使用する方法もあるので実装してみる

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            while node.next is not None and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head
```

### プルリクやドキュメントを参照

#### 参照したもの

- https://github.com/atomina1/Arai60_review/pull/2
- https://github.com/Yoshiki-Iwasa/Arai60/pull/1#discussion_r1640835379
- https://github.com/garunitule/coding_practice/blob/83/LinkedList/83/memo.md
- https://github.com/tokuhirat/LeetCode/pull/3

#### 感想

- head が指しているリンクリストのスタート地点のポインタ情報を node に代入し、node のポインタ情報をもとにリンクリスト自体を操作しているという理解。
- head の情報があればリンクリストの終端まで辿れるため、head を返却することで重複を削除したリンクリストが返却されるといる理解。
- ポインターが指しているノードの値が現在地、次で重複していたら、ポインタのつなぎ先を現在地ー次から、現在地ー次の次に変えるということだと思う。
- `while node and node.next:`より`while node is not None:`のほうが素直だと思うので書き直す。

## STEP3

二重ループを使用したやり方のほうが現在の node が指す値の重複をなくすまで処理を続けるという意図が汲み取りやすい気がするので、二重ループの書き方で step03 を実施。

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node is not None:
            while node.next is not None and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head
```

### 3 回ミスなく書く

1 回目５分
2 回目３分
3 回目３分
