class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_profit = 0
        least_price = prices[0]
        for price in prices:
            max_profit = max(max_profit, price - least_price)
            least_price = min(least_price, price)
        return max_profit
"""
- 配列を前から後ろに見ていく
    - これまでの最安値を覚えておく
    - 最安値と現在の価格から､今日達成できる利益を出す
    - 今日達成できる利益と､これまでの最大利益を比較して､大きい方で最大利益を更新
- 不要(初期化する値で不要にできる):最終的に得られる最大利益がマイナスなら0を返す
- O(N) time complexity, O(1) space complexity

実装･デバッグ:
- max_profix の初期値をどうするか? -> 0 これを0にしておくと､最大利益が0のケースに対応できる｡

拡張:
複数回売り買いする制約だとどうなるか?

評価
- prices の 1回目のループは何もしていない(max_profit, least_priceいずれも更新されない)が､初期化･ループの開始が複雑になるのを避けるため､
  price = prices[0] となる何もしないループを許容する｡
  パフォーマンス上もほぼ影響しないはず｡
"""