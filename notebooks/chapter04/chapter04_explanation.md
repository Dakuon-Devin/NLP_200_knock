# 第4章: 形態素解析 - 解説

## 問題30: 形態素解析結果の読み込み
### 問題の概要
この問題では、夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し、その結果（neko.txt.mecab）を読み込むプログラムを実装します。各形態素は表層形（surface）、基本形（base）、品詞（pos）、品詞細分類1（pos1）をキーとするマッピング型に格納します。

### 解法のポイント
1. **MeCabの出力形式の理解**：
   MeCabの出力は「表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音」という形式になっています。
   
2. **ファイル読み込みと形態素情報の抽出**：
   ```python
   def load_mecab_result(file_path):
       """MeCabの解析結果ファイルを読み込み、各形態素を辞書のリストとして返す関数"""
       morphemes = []
       with open(file_path, 'r', encoding='utf-8') as f:
           for line in f:
               # 空行とEOSを飛ばす
               if line == '\n' or line == 'EOS\n':
                   continue
               
               # タブで分割して表層形とそれ以外の情報に分ける
               surface, info = line.split('\t')
               
               # カンマで分割して品詞情報などを取得
               info_items = info.split(',')
               
               # 形態素情報を辞書として格納
               morpheme = {
                   'surface': surface,
                   'base': info_items[6],
                   'pos': info_items[0],
                   'pos1': info_items[1]
               }
               
               morphemes.append(morpheme)
       
       return morphemes
   ```

### 実装上の注意点
- MeCabの出力形式は、使用する辞書やオプションによって異なる場合があります。実際の出力を確認して、適切にインデックスを設定する必要があります。
- 「原形」（基本形）が存在しない場合、「*」が格納されることがあります。
- 文の区切りを認識するために、EOSマーカーの処理方法を考慮する必要があります。

## 問題31: 動詞
### 問題の概要
この問題では、形態素解析結果から動詞の表層形をすべて抽出します。

### 解法のポイント
問題30で作成した関数を使用して形態素解析結果を読み込み、品詞が「動詞」である形態素の表層形を抽出します。

```python
def extract_verbs(morphemes):
    """形態素リストから動詞の表層形を抽出する関数"""
    return [m['surface'] for m in morphemes if m['pos'] == '動詞']

# 形態素解析結果の読み込み
morphemes = load_mecab_result('neko.txt.mecab')

# 動詞の表層形を抽出
verbs = extract_verbs(morphemes)
```

### 実装上の注意点
- 日本語の動詞には、「する」「なる」などの頻出動詞が多く含まれるため、結果が大量になる可能性があります。
- 重複する動詞を除去したい場合は、集合（set）を使用することができます。

## 問題32: 動詞の基本形
### 問題の概要
この問題では、形態素解析結果から動詞の基本形をすべて抽出します。

### 解法のポイント
問題30で作成した関数を使用して形態素解析結果を読み込み、品詞が「動詞」である形態素の基本形を抽出します。

```python
def extract_verb_base_forms(morphemes):
    """形態素リストから動詞の基本形を抽出する関数"""
    return [m['base'] for m in morphemes if m['pos'] == '動詞']

# 形態素解析結果の読み込み
morphemes = load_mecab_result('neko.txt.mecab')

# 動詞の基本形を抽出
verb_base_forms = extract_verb_base_forms(morphemes)
```

### 実装上の注意点
- 動詞の基本形は、辞書形（終止形）で表されます。例えば、「走った」の基本形は「走る」です。
- 基本形が「*」となっている場合は、原形が存在しないか、解析できなかった可能性があります。

## 問題33: 「AのB」
### 問題の概要
この問題では、形態素解析結果から「AのB」という表現を抽出します。ここでの「の」は助詞、AとBは名詞とします。

### 解法のポイント
連続する3つの形態素を調べ、「名詞+助詞「の」+名詞」というパターンを抽出します。

```python
def extract_a_no_b(morphemes):
    """形態素リストから「AのB」表現を抽出する関数"""
    result = []
    for i in range(len(morphemes) - 2):
        if (morphemes[i]['pos'] == '名詞' and
            morphemes[i+1]['surface'] == 'の' and morphemes[i+1]['pos'] == '助詞' and
            morphemes[i+2]['pos'] == '名詞'):
            
            a_no_b = morphemes[i]['surface'] + morphemes[i+1]['surface'] + morphemes[i+2]['surface']
            result.append(a_no_b)
    
    return result

# 形態素解析結果の読み込み
morphemes = load_mecab_result('neko.txt.mecab')

# 「AのB」表現を抽出
a_no_b_expressions = extract_a_no_b(morphemes)
```

### 実装上の注意点
- 「AのB」表現は日本語で非常に一般的であり、多くの結果が得られる可能性があります。
- 名詞の連続（例：「東京都の人口」）も考慮する場合は、より複雑なパターンマッチングが必要になります。

## 問題34: 名詞の連接
### 問題の概要
この問題では、形態素解析結果から名詞の連接（連続して出現する名詞）を抽出します。

### 解法のポイント
連続する形態素を調べ、品詞が「名詞」である形態素が連続している部分を抽出します。

```python
def extract_noun_sequences(morphemes):
    """形態素リストから名詞の連接を抽出する関数"""
    result = []
    current_sequence = []
    
    for morpheme in morphemes:
        if morpheme['pos'] == '名詞':
            current_sequence.append(morpheme['surface'])
        else:
            # 名詞の連接が終了した場合、2つ以上の名詞からなる連接のみを結果に追加
            if len(current_sequence) >= 2:
                result.append(''.join(current_sequence))
            current_sequence = []
    
    # 最後の名詞の連接を処理
    if len(current_sequence) >= 2:
        result.append(''.join(current_sequence))
    
    return result

# 形態素解析結果の読み込み
morphemes = load_mecab_result('neko.txt.mecab')

# 名詞の連接を抽出
noun_sequences = extract_noun_sequences(morphemes)
```

### 実装上の注意点
- 名詞の連接の長さに制限を設けない場合、非常に長い連接が抽出される可能性があります。
- 複合名詞（例：「高校生」）は、MeCabの設定によっては1つの名詞として扱われる場合と、複数の名詞として扱われる場合があります。

## 問題35: 単語の出現頻度
### 問題の概要
この問題では、形態素解析結果から単語の出現頻度を求めます。

### 解法のポイント
Pythonの`collections.Counter`を使用して、単語の出現回数を効率的にカウントします。

```python
from collections import Counter

def count_word_frequency(morphemes):
    """形態素リストから単語の出現頻度を計算する関数"""
    # 表層形をキーとしてカウント
    word_counts = Counter(m['surface'] for m in morphemes)
    
    # 出現頻度の降順でソート
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_word_counts

# 形態素解析結果の読み込み
morphemes = load_mecab_result('neko.txt.mecab')

# 単語の出現頻度を計算
word_frequencies = count_word_frequency(morphemes)
```

### 実装上の注意点
- 助詞や助動詞などの機能語は非常に頻繁に出現するため、内容語（名詞、動詞、形容詞など）のみを対象にしたい場合は、フィルタリングが必要です。
- 表層形ではなく基本形でカウントすることで、活用形の違いを無視した頻度を求めることもできます。

## 問題36: 頻度上位10語
### 問題の概要
この問題では、出現頻度が高い10語とその出現頻度をグラフで表示します。

### 解法のポイント
問題35で計算した単語の出現頻度から上位10語を抽出し、matplotlibを使用して棒グラフを描画します。

```python
import matplotlib.pyplot as plt
import japanize_matplotlib  # 日本語表示のため

def plot_top_n_words(word_frequencies, n=10):
    """頻度上位n語とその出現頻度を棒グラフで表示する関数"""
    # 上位n語を抽出
    top_n = word_frequencies[:n]
    
    # 単語と頻度を分離
    words = [word for word, count in top_n]
    counts = [count for word, count in top_n]
    
    # グラフの描画
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts)
    plt.xlabel('単語')
    plt.ylabel('出現頻度')
    plt.title(f'出現頻度上位{n}語')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 形態素解析結果の読み込み
morphemes = load_mecab_result('neko.txt.mecab')

# 単語の出現頻度を計算
word_frequencies = count_word_frequency(morphemes)

# 頻度上位10語をグラフで表示
plot_top_n_words(word_frequencies, 10)
```

### 実装上の注意点
- 日本語を正しく表示するために、`japanize_matplotlib`などのライブラリを使用するか、適切なフォントを設定する必要があります。
- 機能語（助詞、助動詞など）を除外したい場合は、品詞情報でフィルタリングすることができます。

## 問題37: 「猫」と共起頻度の高い上位10語
### 問題の概要
この問題では、「猫」という単語と共起する単語の頻度を計算し、共起頻度の高い10語を表示します。

### 解法のポイント
「猫」を含む文を特定し、その文に出現する他の単語をカウントします。ここでは、文の区切りとしてEOSマーカーを使用します。

```python
from collections import Counter

def find_cooccurrences(morphemes, target_word):
    """特定の単語と共起する単語の頻度を計算する関数"""
    # 文ごとに形態素をグループ化
    sentences = []
    current_sentence = []
    
    for morpheme in morphemes:
        if morpheme['surface'] == 'EOS':
            if current_sentence:
                sentences.append(current_sentence)
                current_sentence = []
        else:
            current_sentence.append(morpheme)
    
    # 最後の文を追加
    if current_sentence:
        sentences.append(current_sentence)
    
    # 対象単語を含む文を抽出
    target_sentences = []
    for sentence in sentences:
        if any(m['surface'] == target_word for m in sentence):
            target_sentences.append(sentence)
    
    # 共起する単語をカウント
    cooccurrences = Counter()
    for sentence in target_sentences:
        for morpheme in sentence:
            if morpheme['surface'] != target_word:
                cooccurrences[morpheme['surface']] += 1
    
    # 出現頻度の降順でソート
    sorted_cooccurrences = sorted(cooccurrences.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_cooccurrences

# 形態素解析結果の読み込み
morphemes = load_mecab_result('neko.txt.mecab')

# 「猫」と共起する単語の頻度を計算
cat_cooccurrences = find_cooccurrences(morphemes, '猫')

# 共起頻度上位10語をグラフで表示
plot_top_n_words(cat_cooccurrences, 10)
```

### 実装上の注意点
- 共起の定義によって結果が大きく変わります。ここでは同じ文内での共起を考えていますが、より狭い範囲（例：前後3語）や広い範囲（例：前後の文も含む）で定義することもできます。
- 機能語（助詞、助動詞など）を除外することで、より意味のある共起関係を抽出できる場合があります。

## 問題38: ヒストグラム
### 問題の概要
この問題では、単語の出現頻度のヒストグラムを描画します。

### 解法のポイント
問題35で計算した単語の出現頻度を使用して、matplotlibでヒストグラムを描画します。

```python
import matplotlib.pyplot as plt

def plot_frequency_histogram(word_frequencies):
    """単語の出現頻度のヒストグラムを描画する関数"""
    # 頻度のリストを作成
    frequencies = [count for word, count in word_frequencies]
    
    # ヒストグラムの描画
    plt.figure(figsize=(10, 6))
    plt.hist(frequencies, bins=50, range=(1, 50))
    plt.xlabel('出現頻度')
    plt.ylabel('単語の種類数')
    plt.title('単語の出現頻度のヒストグラム')
    plt.grid(True)
    plt.show()

# 形態素解析結果の読み込み
morphemes = load_mecab_result('neko.txt.mecab')

# 単語の出現頻度を計算
word_frequencies = count_word_frequency(morphemes)

# 出現頻度のヒストグラムを描画
plot_frequency_histogram(word_frequencies)
```

### 実装上の注意点
- 出現頻度の分布は一般的に非常に偏っており、少数の高頻度語と多数の低頻度語が存在します。そのため、適切なビンの数と範囲を設定することが重要です。
- 対数スケールを使用することで、分布の特性をより明確に表示できる場合があります。

## 問題39: Zipfの法則
### 問題の概要
この問題では、単語の出現頻度順位を横軸、その出現頻度を縦軸として、両対数グラフをプロットします。これにより、Zipfの法則（単語の出現頻度はその順位に反比例する）を確認します。

### 解法のポイント
問題35で計算した単語の出現頻度を使用して、両対数グラフを描画します。

```python
import matplotlib.pyplot as plt
import numpy as np

def plot_zipf_law(word_frequencies):
    """Zipfの法則を確認するための両対数グラフを描画する関数"""
    # 順位と頻度のリストを作成
    ranks = np.arange(1, len(word_frequencies) + 1)
    frequencies = [count for word, count in word_frequencies]
    
    # 両対数グラフの描画
    plt.figure(figsize=(10, 6))
    plt.loglog(ranks, frequencies, 'o', markersize=2)
    
    # Zipfの法則の理論曲線（f ∝ 1/r）
    k = frequencies[0] * ranks[0]  # 定数（最高頻度 × 1）
    theory = [k / r for r in ranks]
    plt.loglog(ranks, theory, 'r-', linewidth=1, label='Zipfの法則（理論値）')
    
    plt.xlabel('出現頻度順位')
    plt.ylabel('出現頻度')
    plt.title('Zipfの法則')
    plt.legend()
    plt.grid(True)
    plt.show()

# 形態素解析結果の読み込み
morphemes = load_mecab_result('neko.txt.mecab')

# 単語の出現頻度を計算
word_frequencies = count_word_frequency(morphemes)

# Zipfの法則を確認するグラフを描画
plot_zipf_law(word_frequencies)
```

### 実装上の注意点
- Zipfの法則は完全に成り立つわけではなく、特に高頻度語と低頻度語では理論値からのずれが生じることがあります。
- 両対数グラフでは、Zipfの法則が成り立つ場合、プロットは傾き-1の直線に近づきます。
