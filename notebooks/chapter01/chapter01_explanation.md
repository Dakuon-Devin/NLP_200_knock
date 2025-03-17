# 第1章: 準備運動 - 解説

## 問題00: 文字列の逆順
### 問題の概要
この問題では、文字列「stressed」を逆順にして「desserts」という文字列を得る処理を実装します。

### 解法のポイント
Pythonでは、文字列のスライス操作を使用して簡単に文字列を逆順にすることができます。
```python
s = "stressed"
reversed_s = s[::-1]  # スライス操作で逆順にする
print(reversed_s)  # "desserts"が出力される
```

スライス操作の`[::-1]`は、文字列の最初から最後までを-1ステップで（つまり逆順に）取得することを意味します。

### 実装上の注意点
- Pythonの文字列は不変（immutable）なので、新しい文字列が生成されます。
- 他の方法としては、`reversed()`関数を使用して文字列を逆順にし、`join()`メソッドで結合する方法もあります：
  ```python
  s = "stressed"
  reversed_s = ''.join(reversed(s))
  print(reversed_s)  # "desserts"が出力される
  ```

## 問題01: 「パタトクカシーー」
### 問題の概要
この問題では、「パタトクカシーー」という文字列の奇数番目の文字を取り出して、「パトカー」という文字列を得る処理を実装します。

### 解法のポイント
Pythonでは、文字列のスライス操作を使用して、特定の間隔で文字を取り出すことができます。
```python
s = "パタトクカシーー"
result = s[::2]  # 偶数インデックス（0から始まるため、奇数番目の文字）を取り出す
print(result)  # "パトカー"が出力される
```

スライス操作の`[::2]`は、文字列の最初から最後までを2ステップごとに取得することを意味します。

### 実装上の注意点
- Pythonのインデックスは0から始まるため、奇数番目の文字は偶数インデックスになります。
- 日本語の文字（全角文字）も1文字としてカウントされます。

## 問題02: 「パトカー」＋「タクシー」＝「パタトクカシーー」
### 問題の概要
この問題では、「パトカー」と「タクシー」という2つの文字列を交互に結合して、「パタトクカシーー」という文字列を得る処理を実装します。

### 解法のポイント
Pythonでは、`zip()`関数を使用して2つの文字列を要素ごとに組み合わせることができます。
```python
s1 = "パトカー"
s2 = "タクシー"
result = ''.join(c1 + c2 for c1, c2 in zip(s1, s2))
print(result)  # "パタトクカシーー"が出力される
```

`zip(s1, s2)`は、2つの文字列の対応する文字のペアを生成します。その後、各ペアを結合して1つの文字列にします。

### 実装上の注意点
- `zip()`関数は、短い方の文字列の長さに合わせてペアを生成します。この問題では、両方の文字列の長さが同じなので問題ありません。
- 文字列の長さが異なる場合は、`itertools.zip_longest()`を使用して、不足している部分を指定した値（例えば空文字）で埋めることができます。

## 問題03: 円周率
### 問題の概要
この問題では、「Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.」という文を単語に分解し、各単語の文字数を順に並べると、円周率の最初の15桁になることを確認します。

### 解法のポイント
Pythonでは、文字列の`split()`メソッドを使用して文を単語に分割し、各単語の長さを取得することができます。
```python
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# カンマとピリオドを除去してから単語に分割
words = text.replace(',', '').replace('.', '').split()
# 各単語の文字数を取得
word_lengths = [len(word) for word in words]
print(word_lengths)  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]が出力される
```

### 実装上の注意点
- カンマやピリオドなどの句読点を除去するか、それらを含めるかによって結果が変わります。この問題では、句読点を除去してから単語の長さを数えています。
- 実際の円周率の最初の15桁は「3.14159265358979」ですが、小数点を除くと「314159265358979」となります。単語の長さのリストを見ると、「3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9」となり、円周率の桁と一致していることがわかります。

## 問題04: 元素記号
### 問題の概要
この問題では、「Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.」という文を単語に分解し、1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字、それ以外の単語は先頭の2文字を取り出し、それを単語の位置（先頭から何番目の単語か）に対応する辞書を作成します。

### 解法のポイント
Pythonでは、辞書（dictionary）を使用して、単語の位置と元素記号を対応付けることができます。
```python
text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# カンマとピリオドを除去してから単語に分割
words = text.replace(',', '').replace('.', '').split()
# 1文字を取り出す単語の位置（0から始まるインデックスに変換）
one_char_positions = [0, 4, 5, 6, 7, 8, 14, 15, 18]
# 単語の位置と元素記号を対応付ける辞書を作成
element_symbols = {}
for i, word in enumerate(words):
    if i in one_char_positions:
        element_symbols[i+1] = word[0]  # 1文字目を取得
    else:
        element_symbols[i+1] = word[:2]  # 1-2文字目を取得
print(element_symbols)
```

### 実装上の注意点
- Pythonのインデックスは0から始まるため、問題文の「1, 5, 6, 7, 8, 9, 15, 16, 19番目」は、0から始まるインデックスでは「0, 4, 5, 6, 7, 8, 14, 15, 18」になります。
- 辞書のキーとして単語の位置（1から始まる）を使用し、値として元素記号を格納しています。

## 問題05: n-gram
### 問題の概要
この問題では、与えられた文字列から文字n-gramと単語n-gramを生成する関数を実装します。

### 解法のポイント
n-gramとは、連続するn個の要素（文字や単語）のシーケンスのことです。Pythonでは、スライス操作を使用して簡単にn-gramを生成することができます。

```python
def character_ngram(text, n):
    """文字n-gramを生成する関数"""
    # 空白や句読点を除去
    text = text.replace(' ', '').replace(',', '').replace('.', '')
    return [text[i:i+n] for i in range(len(text) - n + 1)]

def word_ngram(text, n):
    """単語n-gramを生成する関数"""
    # 単語に分割
    words = text.replace(',', '').replace('.', '').split()
    return [tuple(words[i:i+n]) for i in range(len(words) - n + 1)]

# 例
text = "I am an NLPer"
print(character_ngram(text, 2))  # 文字バイグラム
print(word_ngram(text, 2))  # 単語バイグラム
```

### 実装上の注意点
- 文字n-gramでは、空白や句読点を含めるか除去するかによって結果が変わります。この実装では、空白や句読点を除去しています。
- 単語n-gramでは、単語のリストからn個ずつの部分リストを生成します。タプル（tuple）を使用することで、不変のシーケンスとして扱うことができます。

## 問題06: 集合
### 問題の概要
この問題では、「paraparaparadise」と「paragraph」から文字バイグラムを生成し、それらの和集合、積集合、差集合を求めます。また、「se」というバイグラムがそれぞれの集合に含まれるかどうかを調べます。

### 解法のポイント
Pythonでは、集合（set）を使用して、和集合、積集合、差集合を簡単に計算することができます。

```python
def character_bigram(text):
    """文字バイグラムを生成する関数"""
    return [text[i:i+2] for i in range(len(text) - 1)]

# 文字バイグラムを生成
X = set(character_bigram("paraparaparadise"))
Y = set(character_bigram("paragraph"))

# 和集合
union_set = X | Y  # または X.union(Y)

# 積集合
intersection_set = X & Y  # または X.intersection(Y)

# 差集合
difference_set = X - Y  # または X.difference(Y)

# 「se」の有無
se_in_X = "se" in X
se_in_Y = "se" in Y

print(f"和集合: {union_set}")
print(f"積集合: {intersection_set}")
print(f"差集合: {difference_set}")
print(f"'se' in X: {se_in_X}")
print(f"'se' in Y: {se_in_Y}")
```

### 実装上の注意点
- 集合は重複する要素を持たないため、バイグラムの頻度情報は失われます。頻度情報も保持したい場合は、`collections.Counter`を使用することができます。
- 集合演算子（`|`, `&`, `-`）を使用すると、より直感的に集合演算を表現できます。

## 問題07: テンプレートによる文生成
### 問題の概要
この問題では、「x時のyはz」という文を生成する関数を実装します。この関数は、x, y, zを引数として受け取り、それらを組み合わせた文を返します。

### 解法のポイント
Pythonでは、文字列のフォーマット機能を使用して、テンプレート文を生成することができます。

```python
def generate_sentence(x, y, z):
    """「x時のyはz」という文を生成する関数"""
    return f"{x}時の{y}は{z}"

# 例
result = generate_sentence(12, "気温", "22.4")
print(result)  # "12時の気温は22.4"が出力される
```

### 実装上の注意点
- f文字列（Python 3.6以降）を使用すると、変数を直接文字列内に埋め込むことができ、コードが読みやすくなります。
- 古いバージョンのPythonでは、`format()`メソッドや`%`演算子を使用することもできます：
  ```python
  # format()メソッドを使用
  return "{}時の{}は{}".format(x, y, z)
  
  # %演算子を使用
  return "%s時の%sは%s" % (x, y, z)
  ```

## 問題08: 暗号文
### 問題の概要
この問題では、与えられた文字列に対して、各文字を暗号化する関数と、暗号化された文字列を復号する関数を実装します。暗号化のルールは、英小文字ならば(219 - 文字コード)の文字に置換し、それ以外の文字はそのまま出力するというものです。

### 解法のポイント
Pythonでは、文字のASCII値を取得するには`ord()`関数を、ASCII値から文字を取得するには`chr()`関数を使用します。

```python
def cipher(text):
    """文字列を暗号化する関数"""
    result = ""
    for char in text:
        if char.islower():  # 英小文字かどうかを判定
            # 219 - 文字コードの文字に置換
            result += chr(219 - ord(char))
        else:
            # それ以外の文字はそのまま
            result += char
    return result

def decipher(encrypted_text):
    """暗号化された文字列を復号する関数"""
    # 暗号化と同じ処理を適用すると復号できる
    return cipher(encrypted_text)

# 例
original_text = "Hello, World!"
encrypted_text = cipher(original_text)
decrypted_text = decipher(encrypted_text)

print(f"元の文字列: {original_text}")
print(f"暗号化された文字列: {encrypted_text}")
print(f"復号された文字列: {decrypted_text}")
```

### 実装上の注意点
- 英小文字のASCII値は97（'a'）から122（'z'）までです。例えば、'a'の場合、219 - 97 = 122となり、これは'z'のASCII値です。つまり、'a'は'z'に、'b'は'y'に、...、'z'は'a'に置換されます。
- この暗号化方式は対称的なので、同じ関数を使って暗号化と復号を行うことができます。

## 問題09: Typoglycemia
### 問題の概要
この問題では、スペースで区切られた単語列に対して、各単語の先頭と末尾の文字は残し、それ以外の文字の順序をランダムに並び替える関数を実装します。ただし、長さが4以下の単語は並び替えません。

### 解法のポイント
Pythonでは、`random`モジュールの`shuffle()`関数を使用して、リストの要素をランダムに並び替えることができます。

```python
import random

def typoglycemia(text):
    """Typoglycemiaを適用する関数"""
    words = text.split()
    result = []
    
    for word in words:
        if len(word) <= 4:
            # 長さが4以下の単語はそのまま
            result.append(word)
        else:
            # 先頭と末尾の文字を除いた部分をランダムに並び替え
            middle_chars = list(word[1:-1])
            random.shuffle(middle_chars)
            shuffled_word = word[0] + ''.join(middle_chars) + word[-1]
            result.append(shuffled_word)
    
    return ' '.join(result)

# 例
text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
result = typoglycemia(text)
print(result)
```

### 実装上の注意点
- `random.shuffle()`関数は、リストを直接変更します（in-place操作）。そのため、文字列を一度リストに変換してから操作する必要があります。
- 単語の長さが1や2の場合、先頭と末尾の文字だけで単語全体を構成することになるため、並び替えは行われません。
- 実行するたびに異なる結果が得られますが、先頭と末尾の文字は常に同じ位置に保たれます。
