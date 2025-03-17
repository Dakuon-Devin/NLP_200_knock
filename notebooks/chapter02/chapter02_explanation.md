# 第2章: UNIXコマンド - 解説

## 問題10: 行数のカウント
### 問題の概要
この問題では、行数をカウントするプログラムを実装します。

### 解法のポイント
1. **ファイルの読み込み**：
   Pythonでファイルを読み込み、行数をカウントします。
   ```python
   with open('popular-names.txt', 'r') as f:
       line_count = sum(1 for _ in f)
   print(line_count)
   ```

2. **UNIXコマンドとの比較**：
   UNIXコマンドでは、`wc -l`を使用して行数をカウントします。
   ```bash
   wc -l popular-names.txt
   ```

### 実装上の注意点
- Pythonでファイルを読み込む際は、`with`文を使用することで、ファイルを確実に閉じることができます。
- 大きなファイルの場合、メモリ効率を考慮して、1行ずつ読み込んでカウントする方法が適しています。

## 問題11: タブをスペースに置換
### 問題の概要
この問題では、タブ文字をスペースに置換するプログラムを実装します。

### 解法のポイント
1. **ファイルの読み込みと置換**：
   Pythonでファイルを読み込み、タブ文字をスペースに置換します。
   ```python
   with open('popular-names.txt', 'r') as f:
       content = f.read()
   
   # タブをスペースに置換
   content_replaced = content.replace('\t', ' ')
   
   # 結果を出力
   print(content_replaced)
   ```

2. **UNIXコマンドとの比較**：
   UNIXコマンドでは、`tr`や`sed`を使用してタブをスペースに置換します。
   ```bash
   tr '\t' ' ' < popular-names.txt
   # または
   sed 's/\t/ /g' popular-names.txt
   ```

### 実装上の注意点
- Pythonの`replace`メソッドは、すべての一致を置換します。
- 大きなファイルの場合、メモリ効率を考慮して、1行ずつ読み込んで処理する方法が適しています。

## 問題12: 1列目をcol1.txtに，2列目をcol2.txtに保存
### 問題の概要
この問題では、ファイルの1列目をcol1.txtに、2列目をcol2.txtに保存するプログラムを実装します。

### 解法のポイント
1. **ファイルの読み込みと列の抽出**：
   Pythonでファイルを読み込み、各行をタブで分割して1列目と2列目を抽出します。
   ```python
   col1 = []
   col2 = []
   
   with open('popular-names.txt', 'r') as f:
       for line in f:
           fields = line.strip().split('\t')
           if len(fields) >= 2:
               col1.append(fields[0])
               col2.append(fields[1])
   
   # col1.txtに1列目を保存
   with open('col1.txt', 'w') as f:
       f.write('\n'.join(col1))
   
   # col2.txtに2列目を保存
   with open('col2.txt', 'w') as f:
       f.write('\n'.join(col2))
   ```

2. **UNIXコマンドとの比較**：
   UNIXコマンドでは、`cut`を使用して列を抽出します。
   ```bash
   cut -f 1 popular-names.txt > col1.txt
   cut -f 2 popular-names.txt > col2.txt
   ```

### 実装上の注意点
- Pythonでファイルを書き込む際は、`with`文を使用することで、ファイルを確実に閉じることができます。
- 列の区切り文字がタブ以外の場合は、`split`メソッドの引数を変更する必要があります。

## 問題13: col1.txtとcol2.txtをマージ
### 問題の概要
この問題では、col1.txtとcol2.txtを結合し、元のファイルのように1列目と2列目をタブ区切りで並べたテキストファイルを作成するプログラムを実装します。

### 解法のポイント
1. **ファイルの読み込みと結合**：
   Pythonでcol1.txtとcol2.txtを読み込み、対応する行を結合します。
   ```python
   # col1.txtを読み込む
   with open('col1.txt', 'r') as f:
       col1 = [line.strip() for line in f]
   
   # col2.txtを読み込む
   with open('col2.txt', 'r') as f:
       col2 = [line.strip() for line in f]
   
   # 対応する行を結合
   merged = [f"{c1}\t{c2}" for c1, c2 in zip(col1, col2)]
   
   # 結果をファイルに保存
   with open('merged.txt', 'w') as f:
       f.write('\n'.join(merged))
   ```

2. **UNIXコマンドとの比較**：
   UNIXコマンドでは、`paste`を使用して列を結合します。
   ```bash
   paste col1.txt col2.txt > merged.txt
   ```

### 実装上の注意点
- Pythonの`zip`関数は、複数のイテラブルオブジェクトから要素を1つずつ取り出してタプルにまとめます。
- col1.txtとcol2.txtの行数が異なる場合、`zip`関数は短い方に合わせて処理を終了します。行数が同じであることを確認するか、`itertools.zip_longest`を使用して対処する必要があります。

## 問題14: 先頭からN行を出力
### 問題の概要
この問題では、自然数Nをコマンドライン引数などの手段で受け取り、入力のうち先頭のN行だけを表示するプログラムを実装します。

### 解法のポイント
1. **コマンドライン引数の受け取り**：
   Pythonでコマンドライン引数を受け取り、先頭のN行を表示します。
   ```python
   import sys
   
   # コマンドライン引数からNを取得
   N = int(sys.argv[1])
   
   # ファイルの先頭N行を表示
   with open('popular-names.txt', 'r') as f:
       for i, line in enumerate(f):
           if i < N:
               print(line.strip())
           else:
               break
   ```

2. **UNIXコマンドとの比較**：
   UNIXコマンドでは、`head`を使用して先頭のN行を表示します。
   ```bash
   head -n N popular-names.txt
   ```

### 実装上の注意点
- Pythonでコマンドライン引数を受け取る際は、`sys.argv`を使用します。`sys.argv[0]`はプログラム名、`sys.argv[1]`以降が引数となります。
- 大きなファイルの場合でも、1行ずつ読み込んで処理することで、メモリ効率を維持できます。

## 問題15: 末尾のN行を出力
### 問題の概要
この問題では、自然数Nをコマンドライン引数などの手段で受け取り、入力のうち末尾のN行だけを表示するプログラムを実装します。

### 解法のポイント
1. **末尾のN行の取得**：
   Pythonで末尾のN行を取得するには、いくつかの方法があります。
   
   **方法1: 全行を読み込んでからスライス**
   ```python
   import sys
   
   # コマンドライン引数からNを取得
   N = int(sys.argv[1])
   
   # ファイルの全行を読み込む
   with open('popular-names.txt', 'r') as f:
       lines = f.readlines()
   
   # 末尾のN行を表示
   for line in lines[-N:]:
       print(line.strip())
   ```
   
   **方法2: collections.dequeを使用**
   ```python
   import sys
   from collections import deque
   
   # コマンドライン引数からNを取得
   N = int(sys.argv[1])
   
   # 末尾のN行を保持するdequeを作成
   last_n_lines = deque(maxlen=N)
   
   # ファイルを1行ずつ読み込み、dequeに追加
   with open('popular-names.txt', 'r') as f:
       for line in f:
           last_n_lines.append(line.strip())
   
   # 末尾のN行を表示
   for line in last_n_lines:
       print(line)
   ```

2. **UNIXコマンドとの比較**：
   UNIXコマンドでは、`tail`を使用して末尾のN行を表示します。
   ```bash
   tail -n N popular-names.txt
   ```

### 実装上の注意点
- 方法1は、ファイル全体をメモリに読み込むため、大きなファイルの場合はメモリ効率が悪くなります。
- 方法2は、常に最新のN行だけをメモリに保持するため、メモリ効率が良くなります。

## 問題16: ファイルをN分割する
### 問題の概要
この問題では、自然数Nをコマンドライン引数などの手段で受け取り、入力のファイルを行単位でN分割するプログラムを実装します。

### 解法のポイント
1. **ファイルの分割**：
   Pythonでファイルを行単位でN分割するには、以下の手順を実行します。
   1. ファイルの総行数を取得
   2. 各分割ファイルの行数を計算
   3. ファイルを読み込みながら、適切な分割ファイルに書き込む
   
   ```python
   import sys
   import math
   
   # コマンドライン引数からNを取得
   N = int(sys.argv[1])
   
   # ファイルの総行数を取得
   with open('popular-names.txt', 'r') as f:
       total_lines = sum(1 for _ in f)
   
   # 各分割ファイルの行数を計算
   lines_per_file = math.ceil(total_lines / N)
   
   # ファイルを分割
   with open('popular-names.txt', 'r') as f:
       for i in range(N):
           with open(f'split_{i+1}.txt', 'w') as out_f:
               for j in range(lines_per_file):
                   line = f.readline()
                   if not line:  # ファイルの終わりに達した場合
                       break
                   out_f.write(line)
   ```

2. **UNIXコマンドとの比較**：
   UNIXコマンドでは、`split`を使用してファイルを分割します。
   ```bash
   split -l $(( $(wc -l < popular-names.txt) / N + 1 )) popular-names.txt split_
   ```

### 実装上の注意点
- `math.ceil`関数を使用して、各分割ファイルの行数を切り上げることで、すべての行が確実に分割されるようにしています。
- 最後の分割ファイルは、他の分割ファイルよりも行数が少なくなる可能性があります。

## 問題17: １列目の文字列の異なり
### 問題の概要
この問題では、1列目の文字列の種類（異なる文字列の集合）を求めるプログラムを実装します。

### 解法のポイント
1. **1列目の文字列の抽出と重複の除去**：
   Pythonで1列目の文字列を抽出し、重複を除去するには、集合（set）を使用します。
   ```python
   # 1列目の文字列を格納するための集合
   col1_set = set()
   
   # ファイルを読み込み、1列目の文字列を抽出
   with open('popular-names.txt', 'r') as f:
       for line in f:
           fields = line.strip().split('\t')
           if fields:  # 空行でない場合
               col1_set.add(fields[0])
   
   # 結果を表示
   for item in sorted(col1_set):
       print(item)
   ```

2. **UNIXコマンドとの比較**：
   UNIXコマンドでは、`cut`、`sort`、`uniq`を組み合わせて使用します。
   ```bash
   cut -f 1 popular-names.txt | sort | uniq
   ```

### 実装上の注意点
- Pythonの集合（set）は、重複する要素を自動的に除外します。
- 結果を特定の順序で表示したい場合は、`sorted`関数を使用して並べ替えることができます。

## 問題18: 各行を3コラム目の数値の降順にソート
### 問題の概要
この問題では、各行を3コラム目の数値の降順で整列するプログラムを実装します。

### 解法のポイント
1. **3コラム目の数値による降順ソート**：
   Pythonで各行を3コラム目の数値の降順でソートするには、`sorted`関数と`key`パラメータを使用します。
   ```python
   # ファイルを読み込み、各行をリストに格納
   lines = []
   with open('popular-names.txt', 'r') as f:
       for line in f:
           lines.append(line.strip())
   
   # 3コラム目の数値の降順でソート
   sorted_lines = sorted(lines, key=lambda x: int(x.split('\t')[2]), reverse=True)
   
   # 結果を表示
   for line in sorted_lines:
       print(line)
   ```

2. **UNIXコマンドとの比較**：
   UNIXコマンドでは、`sort`コマンドを使用します。
   ```bash
   sort -t $'\t' -k 3,3nr popular-names.txt
   ```

### 実装上の注意点
- `sorted`関数の`key`パラメータには、各要素をどのように比較するかを指定する関数を渡します。ここでは、各行をタブで分割し、3番目の要素（インデックスは2）を整数に変換して比較しています。
- `reverse=True`を指定することで、降順にソートします。

## 問題19: 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
### 問題の概要
この問題では、各行の1コラム目の文字列の出現頻度を求め、出現頻度の高い順に並べるプログラムを実装します。

### 解法のポイント
1. **1コラム目の文字列の出現頻度のカウント**：
   Pythonで1コラム目の文字列の出現頻度をカウントするには、`collections.Counter`を使用します。
   ```python
   from collections import Counter
   
   # 1コラム目の文字列を格納するためのリスト
   col1 = []
   
   # ファイルを読み込み、1コラム目の文字列を抽出
   with open('popular-names.txt', 'r') as f:
       for line in f:
           fields = line.strip().split('\t')
           if fields:  # 空行でない場合
               col1.append(fields[0])
   
   # 出現頻度をカウント
   counter = Counter(col1)
   
   # 出現頻度の高い順に並べて表示
   for item, count in counter.most_common():
       print(f"{item}\t{count}")
   ```

2. **UNIXコマンドとの比較**：
   UNIXコマンドでは、`cut`、`sort`、`uniq`を組み合わせて使用します。
   ```bash
   cut -f 1 popular-names.txt | sort | uniq -c | sort -nr | awk '{print $2 "\t" $1}'
   ```

### 実装上の注意点
- `collections.Counter`は、要素の出現回数をカウントするための便利なクラスです。
- `counter.most_common()`メソッドは、出現回数の多い順に要素と出現回数のペアを返します。
- 出力形式を調整するために、f文字列を使用して整形しています。
