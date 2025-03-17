# 第1章: 準備運動 - 解説

## 問題00: 文字列の逆順
### 問題の概要
この問題では、文字列"stressed"を逆順にして"desserts"という文字列を得る処理を実装します。

### 解法のポイント
1. **Pythonでの文字列の逆順**：
   Pythonでは、スライス記法 `[::-1]` を使うと、文字列を逆順に取得できます。
   ```python
   s = "stressed"
   reversed_s = s[::-1]  # "desserts"
   ```

2. **他の方法**：
   - `reversed関数とjoinメソッドを使用`：
     ```python
     s = "stressed"
     reversed_s = ''.join(reversed(s))  # "desserts"
     ```
   - `リストに変換して逆順にしてから結合`：
     ```python
     s = "stressed"
     char_list = list(s)
     char_list.reverse()
     reversed_s = ''.join(char_list)  # "desserts"
     ```

### 実装上の注意点
- 文字列は不変（イミュータブル）なので、元の文字列を直接変更することはできません。新しい文字列を作成する必要があります。
- スライス記法 `[::-1]` が最も簡潔で効率的な方法です。

## 問題01: 「パタトクカシーー」
### 問題の概要
この問題では、「パタトクカシーー」という文字列の奇数番目の文字を取り出して、「パトカー」という文字列を作る処理を実装します。

### 解法のポイント
1. **文字列のインデックス**：
   Pythonでは、文字列の各文字にインデックスでアクセスできます。インデックスは0から始まるため、奇数番目の文字（1, 3, 5, ...）は、インデックスでは0, 2, 4, ...となります。

2. **スライスを使った方法**：
   Pythonのスライス記法 `[start:stop:step]` を使うと、特定の間隔で文字を取り出すことができます。
   ```python
   s = "パタトクカシーー"
   result = s[::2]  # "パトカー"
   ```

3. **リスト内包表記を使った方法**：
   ```python
   s = "パタトクカシーー"
   result = ''.join([s[i] for i in range(0, len(s), 2)])  # "パトカー"
   ```

### 実装上の注意点
- 日本語の文字列も、Pythonでは1文字ずつ正しく処理されます。
- インデックスの開始が0であることに注意が必要です。

## 問題02: 「パトカー」＋「タクシー」＝「パタトクカシーー」
### 問題の概要
この問題では、「パトカー」と「タクシー」という2つの文字列を交互に結合して、「パタトクカシーー」という文字列を作る処理を実装します。

### 解法のポイント
1. **zipを使った方法**：
   Pythonの `zip()` 関数を使うと、複数のイテラブルオブジェクトから要素を1つずつ取り出してタプルにまとめることができます。
   ```python
   s1 = "パトカー"
   s2 = "タクシー"
   result = ''.join(c1 + c2 for c1, c2 in zip(s1, s2))  # "パタトクカシーー"
   ```

2. **インデックスを使った方法**：
   ```python
   s1 = "パトカー"
   s2 = "タクシー"
   result = ''
   for i in range(min(len(s1), len(s2))):
       result += s1[i] + s2[i]
   # 長さが異なる場合は残りの文字を追加
   if len(s1) > len(s2):
       result += s1[len(s2):]
   elif len(s2) > len(s1):
       result += s2[len(s1):]
   ```

### 実装上の注意点
- 2つの文字列の長さが異なる場合の処理を考慮する必要があります。

## 問題03: 円周率
### 問題の概要
この問題では、"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し、各単語の（アルファベットの）文字数を先頭から順に並べたリストを作成します。

### 解法のポイント
1. **文の分割**：
   文を空白で分割して単語のリストを作成します。
   ```python
   text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
   words = text.split()
   ```

2. **文字数のカウント**：
   各単語の文字数をカウントします。ただし、カンマやピリオドなどの記号は除外します。
   ```python
   import re
   word_lengths = [len(re.sub(r'[^a-zA-Z]', '', word)) for word in words]
   ```

### 実装上の注意点
- 単語の区切りとして空白を使用しますが、カンマやピリオドなどの記号も単語の一部として扱われる可能性があります。
- 記号を除外するために、正規表現を使用することができます。

## 問題04: 元素記号
### 問題の概要
この問題では、"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し、1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字、それ以外の単語は先頭の2文字を取り出し、取り出した文字列から単語の位置への連想配列（辞書型もしくはマップ型）を作成します。

### 解法のポイント
1. **文の分割**：
   文を空白で分割して単語のリストを作成します。

2. **指定された位置の単語の処理**：
   1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字、それ以外の単語は先頭の2文字を取り出します。
   ```python
   text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
   words = text.split()
   one_char_positions = [1, 5, 6, 7, 8, 9, 15, 16, 19]  # 1-indexed
   
   element_dict = {}
   for i, word in enumerate(words, 1):  # 1-indexedにするためにenumerate(words, 1)を使用
       if i in one_char_positions:
           element_dict[word[:1]] = i
       else:
           element_dict[word[:2]] = i
   ```

### 実装上の注意点
- 問題文では1-indexedで位置が指定されていますが、Pythonのインデックスは0から始まるため、調整が必要です。
- 単語の先頭の文字を取り出す際に、記号を除外するかどうかを考慮する必要があります。

## 問題05: n-gram
### 問題の概要
この問題では、与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を実装します。n-gramとは、対象となるシーケンスをn個の要素ごとに分割したものです。この関数を用いて、"I am an NLPer"という文から単語bi-gram、文字bi-gramを得ます。

### 解法のポイント
1. **n-gram関数の実装**：
   シーケンスとnを受け取り、n-gramのリストを返す関数を実装します。
   ```python
   def n_gram(sequence, n):
       return [sequence[i:i+n] for i in range(len(sequence)-n+1)]
   ```

2. **単語bi-gramの作成**：
   文を単語に分割し、n=2でn-gram関数を適用します。
   ```python
   text = "I am an NLPer"
   words = text.split()
   word_bigrams = n_gram(words, 2)  # [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
   ```

3. **文字bi-gramの作成**：
   文をそのままn=2でn-gram関数に渡します。
   ```python
   char_bigrams = n_gram(text, 2)  # ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
   ```

### 実装上の注意点
- 単語n-gramを作成する場合は、文を単語に分割してからn-gram関数を適用します。
- 文字n-gramを作成する場合は、文をそのままn-gram関数に渡します。
- n-gram関数は、シーケンスの長さがn未満の場合は空のリストを返します。

## 問題06: 集合
### 問題の概要
この問題では、"paraparaparadise"と"paragraph"から文字bi-gramの集合を作り、それぞれをX、Yとして、X∪Y（和集合）、X∩Y（積集合）、X−Y（差集合）を求めます。さらに、"se"という文字bi-gramがXおよびYに含まれるかどうかを調べます。

### 解法のポイント
1. **文字bi-gramの作成**：
   問題05で実装したn-gram関数を使用して、2つの文字列から文字bi-gramを作成します。
   ```python
   text1 = "paraparaparadise"
   text2 = "paragraph"
   X = set(n_gram(text1, 2))
   Y = set(n_gram(text2, 2))
   ```

2. **集合演算**：
   Pythonの集合演算を使用して、和集合、積集合、差集合を求めます。
   ```python
   union_set = X | Y  # 和集合
   intersection_set = X & Y  # 積集合
   difference_set = X - Y  # 差集合
   ```

3. **含まれるかどうかの判定**：
   `in`演算子を使用して、特定の要素が集合に含まれるかどうかを判定します。
   ```python
   is_se_in_X = "se" in X
   is_se_in_Y = "se" in Y
   ```

### 実装上の注意点
- 集合を使用することで、重複する要素を自動的に除外できます。
- 集合演算は、Pythonの組み込み演算子（`|`, `&`, `-`）または集合のメソッド（`union()`, `intersection()`, `difference()`）を使用できます。

## 問題07: テンプレートによる文生成
### 問題の概要
この問題では、引数x、y、zを受け取り、「x時のyはz」という文字列を返す関数を実装します。さらに、この関数に「12」「気温」「22.4」を渡して、「12時の気温は22.4」という文字列を得ます。

### 解法のポイント
1. **テンプレート文字列の作成**：
   引数を受け取り、テンプレートに埋め込んで文字列を返す関数を実装します。
   ```python
   def template(x, y, z):
       return f"{x}時の{y}は{z}"
   ```

2. **関数の呼び出し**：
   実装した関数に引数を渡して、結果を確認します。
   ```python
   result = template("12", "気温", "22.4")  # "12時の気温は22.4"
   ```

### 実装上の注意点
- Pythonでは、f文字列（Python 3.6以降）を使用すると、変数を文字列に埋め込むことができます。
- 古いバージョンのPythonでは、`format()`メソッドや`%`演算子を使用することもできます。
  ```python
  # format()メソッドを使用
  def template(x, y, z):
      return "{}時の{}は{}".format(x, y, z)
  
  # %演算子を使用
  def template(x, y, z):
      return "%s時の%sは%s" % (x, y, z)
  ```

## 問題08: 暗号文
### 問題の概要
この問題では、与えられた文字列に対して、各文字を以下の規則で変換する関数を実装します：
- 英小文字ならば、(219 - 文字コード)の文字に置換
- その他の文字はそのまま

この関数を用いて、「Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.」を暗号化し、復号します。

### 解法のポイント
1. **暗号化関数の実装**：
   文字列を受け取り、各文字を規則に従って変換する関数を実装します。
   ```python
   def cipher(text):
       result = ""
       for char in text:
           if char.islower():  # 英小文字かどうかを判定
               result += chr(219 - ord(char))  # 文字コードを変換
           else:
               result += char  # その他の文字はそのまま
       return result
   ```

2. **暗号化と復号**：
   実装した関数を使用して、文字列を暗号化し、さらに暗号化された文字列を復号します。
   ```python
   text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
   encrypted = cipher(text)
   decrypted = cipher(encrypted)  # 同じ関数を適用することで復号できる
   ```

### 実装上の注意点
- 文字の判定には、`islower()`メソッドを使用します。
- 文字コードの変換には、`ord()`関数（文字から文字コードを取得）と`chr()`関数（文字コードから文字を取得）を使用します。
- この暗号化方法は、英小文字に対して対称的な変換を行うため、同じ関数を2回適用することで元の文字列に戻ります。

## 問題09: Typoglycemia
### 問題の概要
この問題では、スペースで区切られた単語列に対して、各単語の先頭と末尾の文字は残し、それ以外の文字の順序をランダムに並び替える関数を実装します。

### 解法のポイント
1. **単語の分割**：
   文を空白で分割して単語のリストを作成します。

2. **単語の処理**：
   各単語に対して、先頭と末尾の文字を残し、それ以外の文字の順序をランダムに並び替えます。
   ```python
   import random

   def typoglycemia(text):
       words = text.split()
       result = []
       for word in words:
           if len(word) <= 4:  # 4文字以下の単語はそのまま
               result.append(word)
           else:
               # 先頭と末尾の文字を除いた部分をランダムに並び替え
               middle_chars = list(word[1:-1])
               random.shuffle(middle_chars)
               result.append(word[0] + ''.join(middle_chars) + word[-1])
       return ' '.join(result)
   ```

### 実装上の注意点
- 単語の長さが4文字以下の場合は、そのままにすることが一般的です。
- ランダムな並び替えには、`random.shuffle()`関数を使用します。
- 先頭と末尾の文字を除いた部分をリストに変換してからシャッフルし、再度結合します。
