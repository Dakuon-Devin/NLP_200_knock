# 問題21: カテゴリ名を含む行を抽出 - 解説

## 問題の概要
この問題では、Wikipediaの記事から、カテゴリ名を表す行を抽出する処理を実装します。Wikipediaのカテゴリは、`[[Category:カテゴリ名]]`という形式で記述されています。

## 解法のポイント

### 1. 正規表現を使用したパターンマッチング
Pythonの`re`モジュールを使用して、カテゴリ行を抽出します。

```python
import re

pattern = r'\[\[Category:(.+?)(?:\|.*)?\]\]'
for line in article.split('\n'):
    match = re.search(pattern, line)
    if match:
        print(line)
```

### 2. 正規表現パターンの解説
- `\[\[Category:`: `[[Category:`という文字列にマッチします（`[`は正規表現では特殊文字なので、エスケープが必要）
- `(.+?)`: カテゴリ名にマッチします（非貪欲マッチング）
- `(?:\|.*)?`: オプションのパイプ記号とそれに続く文字列にマッチします（キャプチャしない）
- `\]\]`: `]]`という文字列にマッチします

### 3. 単純な文字列検索を使用する方法
正規表現を使わずに、単純な文字列検索でも実装できます。

```python
for line in article.split('\n'):
    if '[[Category:' in line:
        print(line)
```

## 実装上の注意点

1. **カテゴリ名の抽出**：
   問題では行全体を抽出していますが、カテゴリ名だけを抽出したい場合は、正規表現のキャプチャグループを使用します。

   ```python
   import re

   pattern = r'\[\[Category:(.+?)(?:\|.*)?\]\]'
   for line in article.split('\n'):
       match = re.search(pattern, line)
       if match:
           category_name = match.group(1)
           print(category_name)
   ```

2. **複数のカテゴリ**：
   1行に複数のカテゴリが記述されている可能性があります。その場合は、`re.findall()`を使用して全てのカテゴリを抽出します。

   ```python
   import re

   pattern = r'\[\[Category:(.+?)(?:\|.*)?\]\]'
   for line in article.split('\n'):
       categories = re.findall(pattern, line)
       for category in categories:
           print(category)
   ```

3. **大文字小文字の区別**：
   Wikipediaでは通常、「Category」は大文字で始まりますが、念のため大文字小文字を区別しない検索（`re.IGNORECASE`フラグを使用）も考慮すると良いでしょう。

## 発展的な内容
この問題は、正規表現を使った基本的なパターンマッチングの例です。Wikipediaの記事には、カテゴリ以外にも様々なマークアップが使用されています。例えば：

- リンク：`[[リンク先]]`または`[[リンク先|表示テキスト]]`
- テンプレート：`{{テンプレート名|パラメータ}}`
- 見出し：`==見出しテキスト==`

これらのマークアップも、同様の正規表現技術を使って抽出・解析することができます。
