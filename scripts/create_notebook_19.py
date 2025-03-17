import nbformat as nbf
import os
from pathlib import Path

def create_notebook_19():
    """Create notebook for problem 19 (Frequency of first column)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる\n\n各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．'),
        nbf.v4.new_code_cell('# 問題19: 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる\n\nfrom collections import Counter\n\n# Pythonで1列目の文字列の出現頻度を求める関数\ndef count_column_frequency(file_path, column_index=0, delimiter=\'\\t\'):\n    """ファイルの特定の列の値の出現頻度を求める関数\n    \n    Args:\n        file_path: 入力ファイルのパス\n        column_index: 列のインデックス（0始まり）\n        delimiter: 列の区切り文字\n        \n    Returns:\n        (値, 出現回数)のタプルのリスト（出現回数の降順）\n    """\n    values = []\n    \n    with open(file_path, \'r\', encoding=\'utf-8\') as f:\n        for line in f:\n            columns = line.strip().split(delimiter)\n            if len(columns) > column_index:\n                values.append(columns[column_index])\n    \n    # Counterを使用して出現頻度をカウント\n    counter = Counter(values)\n    \n    # 出現頻度の降順でソート\n    sorted_items = counter.most_common()\n    \n    return sorted_items\n\n# サンプルファイルのパス（実際の環境に合わせて変更してください）\nfile_path = \'../data/popular-names.txt\'\n\n# 1列目の文字列の出現頻度を求める\ntry:\n    frequency = count_column_frequency(file_path)\n    print(f"1列目の文字列の出現頻度（上位10件）:")\n    for i, (value, count) in enumerate(frequency):\n        if i < 10:\n            print(f"{value}: {count}回")\n        else:\n            break\n    print(f"\\n合計: {len(frequency)}種類の異なる値")\nexcept FileNotFoundError:\n    print(f"ファイル {file_path} が見つかりません。")\n    print("このノートブックを実行する前に、必要なデータファイルをダウンロードしてください。")\n    print("データファイルは https://nlp100.github.io/data/popular-names.txt からダウンロードできます。")'),
        nbf.v4.new_code_cell('# UNIXコマンドでの確認（Jupyter上で実行）\n# cut, sort, uniqコマンドを使用して1列目の文字列の出現頻度を求める\n!cut -f 1 ../data/popular-names.txt | sort | uniq -c | sort -nr | head -n 10 2>/dev/null || echo "コマンドの実行に失敗しました"'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、ファイルの1列目に含まれる文字列の出現頻度を求め、その頻度の高い順に並べる方法を学びます。\n\n### Pythonでの実装\n\nPythonで1列目の文字列の出現頻度を求めるには、以下の手順を実行します：\n\n1. ファイルを開いて1行ずつ読み込みます。\n2. 各行をタブ文字で分割して列のリストを取得します。\n3. 1列目（インデックス0）の値をリストに追加します。\n4. `collections.Counter`を使用して、リスト内の各値の出現回数をカウントします。\n5. `most_common()`メソッドを使用して、出現頻度の降順でソートされた(値, 出現回数)のタプルのリストを取得します。\n\n### UNIXコマンドでの確認\n\nUNIXコマンドを組み合わせて、1列目の文字列の出現頻度を求めることができます：\n\n```bash\ncut -f 1 input.txt | sort | uniq -c | sort -nr\n```\n\n- `cut -f 1`：1列目を抽出します。\n- `sort`：抽出した値をソートします。\n- `uniq -c`：ソートされた値の出現回数をカウントします。\n- `sort -nr`：出現回数の降順でソートします（`n`は数値として、`r`は降順）。\n\n### 注意点\n\n- ファイルが存在しない場合のエラー処理を行っています。\n- 列数が不足している行に対する処理を考慮しています。\n- 文字エンコーディングを指定して、異なる言語や文字セットのファイルも正しく処理できるようにしています。\n- 大きなファイルでも効率的に処理できるように、ファイルを一度に全て読み込むのではなく、1行ずつ処理しています。\n- `collections.Counter`は、Pythonの標準ライブラリで提供されている便利なデータ構造で、要素の出現回数を効率的にカウントできます。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter02', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter02/19_frequency.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_19()
