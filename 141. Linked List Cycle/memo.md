# 141. Linked List Cycle 　

- https://leetcode.com/problems/linked-list-cycle/description/

## STEP1

- 何も見ずに解いてみる

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        while head:
            if head in visited_nodes:
                return True
            visited_nodes.add(head)
            head = head.next
        return False
```

#### 考えたこと,過程

- すでに訪れたことのあるノードを記録しておいて、繰り返しの中ですでに訪れたノードに再度訪れたらサイクルが存在するということ
- 全部の連結リストのノードを見てもサイクルが内容であればその旨メッセージで出してあげたほうが良いかも
- 最初、head を for で回し、辞書に格納してすでに訪れたかを調べようとしたが、ListNode が**iter**を持っておらずイテラブルでないため,set() を使用
- 詰まって答えを見た

## STEP2

```python

```

### プルリクやドキュメントを参照

#### 参照したもの

- https://discord.com/channels/1084280443945353267/1195700948786491403/1195944696665604156
- https://github.com/myzn0806/leetcode-2/pull/1
- https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.2k4z0wt6ytf9
- https://docs.python.org/ja/3.13/library/stdtypes.html#set

#### ドキュメント等

- set()の実装を確認
  - https://github.com/python/cpython/blob/main/Objects/setobject.c
- C の構造がわからずコードリーディングが進まない。step03 までやったあとに詳しく見ようと思うが、どれくらいの時間でどれくらいの理解ができているのが常識なのかが気になった。

- とりあえず 30 分で読めたもの
  - set_lookkey 関数の動作
  - python で簡易的に実装された set()の実装を読んだ
    - https://github.com/fuga-98/arai60/blob/141-Linked-List-Cycle/141LinkedListCycle.md
- set_lookkey 関数
  - 作成した set(集合)内で特定の要素が存在するか検索し、存在する場合は存在するメモリ上の場所を返し、存在しない場合は空いているメモリ上の場所を返すという理解

#### 感想

- 他の人の PR へのコメントで head が動いているのが分かりづらいというのがあった。node という名前のほうがわかりやすいと思われる。
- 別の解法が存在するらしいが常識の範囲でもないらしい？
  - https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.2k4z0wt6ytf9

## STEP3

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        node = head
        while node:
            if node in visited_nodes:
                return True
            visited_nodes.add(node)
            node = node.next
        return False

```

### 3 回ミスなく書く

- 1 回あたり約四分
