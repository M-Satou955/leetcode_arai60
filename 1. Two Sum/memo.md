# 1. Two Sum

- https://leetcode.com/problems/two-sum/solutions/127810/two-sum/?envType=problem-list-v2&envId=xo2bgr0r

## STEP1

- 何も見ずに解いてみる

```python
# Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j]

        return []

# Hash Map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [i, prevMap[diff]]

            prevMap[n] = i

        return

```

#### 考えたこと

- まず思いつくのは与えられた値のすべての組み合わせをチェックして合計が targe の値になるか確認する方法
- target の値になる組み合わせが見つかるまでループするので n \* n の時間がかかりそう

#### 過程

- 二重の for 文でできそうなので for i in range(len(nums))で最初の要素、内側のループで 2 個目から先の要素から targe の値になる組み合わせを確認していく。

## STEP2

- 解説を見て HashMap の解法を知ったのでこちらも実装してみる。
- ハッシュを使用するという選択肢が頭になかった（Hash の使い方や存在が頭に定着していないため選択肢に加えられていなかったと思う）。

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in prevMap:
                return [i, prevMap[complement]]
            prevMap[n] = i
```

### プルリクやドキュメントを参照

#### 参照したもの

- https://youtu.be/KLlXCFG5TnA?si=JsWaRkUQoPetWPWQ
- https://leetcode.com/problems/two-sum/solutions/127810/two-sum/?envType=problem-list-v2&envId=xo2bgr0r
- https://discord.com/channels/1084280443945353267/1239148130679783424/1346473543063441488
- https://discord.com/channels/1084280443945353267/1239148130679783424/1351813815565553696
- https://discord.com/channels/1084280443945353267/1239148130679783424/1349402191512866918
- https://discord.com/channels/1084280443945353267/1239148130679783424/1346123432802390076
- https://discord.com/channels/1084280443945353267/1239148130679783424/1344573190369972255

#### ドキュメント等

- https://docs.python.org/ja/3.13/library/functions.html#enumerate

#### 感想

- エラー処理を意識していなかったが、実際にプロダクトで使われるコードだと考えればエラーメッセージがあったほうが良いという視点がなかったことに気づく。
- 型ヒントが大文字からスタートで記述しなくて良くなったことを知る。
- VSC に python 用の拡張機能をいれた。
- index と value を取得しておいたほうが便利なので dict に格納するほうが良い。
- enumerate を使用することで value と index が同時に扱えるのが便利に感じた。

## STEP3

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in prevMap:
                return [prevMap[complement], i]
            prevMap[n] = i
        raise ValueError('No valid pair of numbers found in the input list')
```

### 3 回ミスなく書く

- 9 分で 3 回 AC
- タイピングが遅いことがわかった
