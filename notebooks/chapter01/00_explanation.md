# 問題00: 文字列の逆順 - 解説

## 問題の概要
この問題では、文字列"stressed"を逆順にして"desserts"という文字列を得る処理を実装します。

## 解法のポイント

### 1. Pythonでの文字列の逆順
Pythonでは、文字列をスライスを使って逆順にすることができます。スライス記法 `[::-1]` を使うと、文字列を逆順に取得できます。

```python
s = "stressed"
reversed_s = s[::-1]  # "desserts"
```

### 2. 他の方法
他にも以下のような方法があります：

1. **reversed関数とjoinメソッドを使用**：
   ```python
   s = "stressed"
   reversed_s = ''.join(reversed(s))  # "desserts"
   ```

2. **リストに変換して逆順にしてから結合**：
   ```python
   s = "stressed"
   char_list = list(s)
   char_list.reverse()
   reversed_s = ''.join(char_list)  # "desserts"
   ```

## 実装上の注意点
- 文字列は不変（イミュータブル）なので、元の文字列を直接変更することはできません。新しい文字列を作成する必要があります。
- スライス記法 `[::-1]` が最も簡潔で効率的な方法です。

## 発展的な内容
この問題は単純ですが、文字列操作の基本を学ぶための良い導入です。文字列の逆順は、回文（前から読んでも後ろから読んでも同じ文字列）の判定などで使われます。

```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
```
