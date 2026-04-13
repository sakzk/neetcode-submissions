from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def _normalize_dict(d: dict) -> str:            
            return frozenset(d.items())
            # return frozendict(d.items())
            # https://docs.python.org/3.15/library/stdtypes.html#frozendict:~:text=A%20frozendict%20can%20be%20hashed%20with%20hash(frozendict)%20if%20all%20keys%20and%20values%20can%20be%20hashed.
            # A frozendict can be hashed with hash(frozendict) if all keys and values can be hashed.
            # Added in version 3.15.

        char_to_count_to_words = dict()
        for word in strs:
            char_to_count = Counter(word)
            char_to_count_normalized = _normalize_dict(char_to_count)
            if char_to_count_normalized not in char_to_count_to_words:
                char_to_count_to_words[char_to_count_normalized] = []
            char_to_count_to_words[char_to_count_normalized].append(word)
        return list(char_to_count_to_words.values())

    # normalize_dict未実装: 迷彩が辛い｡
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     def _normalize_dict(d: dict) -> str:
    #         return tuple()

    #     char_to_count_to_words = dict()
    #     for word in strs:
    #         char_to_count = Counter(word)
    #         char_to_count_normalized = _normalize_dict(char_to_count)
    #         if char_to_count_normalized not in char_to_count_to_words:
    #             char_to_count_to_words[char_to_count_normalized] = []
    #         char_to_count_to_words[char_to_count_normalized].append(word)
    #     print(char_to_count_to_words)
    #     return []
    #     return char_to_count_to_words
        # [list(char_to_count_to_words.values())]
"""
迷彩になっていてつらい｡
char_to_count_to_words
-> anagrams_gouped_by_pattern?
-> anagrams_group[count_to_char].append(word) から逆算して考えるとよかった｡
char_to_countからスタートしたので､char_to_count_words になってしまって､これは迷彩｡

デバッグしやすい書き方
- normalized_dictを取り出す
- normalized_dict を固定値にして､_wordsが同じになるか見る｡
"""

'''
- dict_to_something で､dictをキーにしたいことってあるはずだよなー｡pythonのイディオムがあるはず｡

- frozendict の PEP と仕様への取り込みを調べてみる
    - neetcode の処理系は､3.14.2
    - document は3.15から｡

- 辞書の同一性チェック
- もとの単語を保持しておきたい
- char_to_count_to_words がほしいな～｡
- char_to_count_to_word

- dict.values() に .cpoy() しようとして出ているエラー｡  
- []と､dict.values() の違いについて調べよう｡
return [char_to_count_to_words.values()]
```Error
Traceback (most recent call last):
  File "/box/main.py", line 61, in process_input
    output_copy = [l.copy() for l in output]
                   ^^^^^^
AttributeError: 'dict_values' object has no attribute 'copy'
```
'''