
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_nums = set()
        for num in nums:
            if num in seen_nums:
                return True
            seen_nums.add(num)
        return False
"""
- Counterクラスを作ってください
- 見つけて終わりではなく､重複する数字をすべて返してください｡
- numsが､数字1T個だったらどうしますか?
   - numに適当な制約をつけると方針は変わりますか?
"""