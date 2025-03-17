import nbformat as nbf
import os
from pathlib import Path

def create_notebook_17():
    """Create notebook for problem 17 (Unique values in first column)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 17. １列目の文字列の異なり\n\n1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．'),
        nbf.v4.new_code_cell('# 問題17: １列目の文字列の異なり\n\n# Pythonで1列目の文字列の異なりを求める関数\ndef get_unique_values_in_column(file_path, column_index=0, delimiter=\'\\t\'):\n    """ファイルの特定の列の異なる値（ユニークな値）を取得する関数\n    \n    Args:\n        file_path: 入力ファイルのパス\n        column_index: 列のインデックス（0始まり）\n        delimiter: 列の区切り文字\n        \n    Returns:\n        ユニークな値のセット\n    """\n    unique_values = set()\n    \n    with open(file_path, \'r\', encoding=\'utf-8\') as f:\n        for line in f:\n            columns = line.strip().split(delimiter)\n            if len(columns) > column_index:\n                unique_values.add(columns[column_index])\n    \n    return unique_values\n\n# サンプルファイルのパス（実際の環境に合わせて変更してください）\nfile_path = \'../data/popular-names.txt\'\n\n# 1列目の文字列の異なりを求める\ntry:\n    unique_values = get_unique_values_in_column(file_path)\n    print(f"1列目の異なる文字列の数: {len(unique_values)}")\n    print("\\n1列目の異なる文字列の一部（最初の10個）:")\n    for i, value in enumerate(sorted(unique_values)):\n        if i < 10:\n            print(f"- {value}")\n        else:\n            break\n    print("...")\nexcept FileNotFoundError:\n    print(f"ファイル {file_path} が見つかりません。")\n    print("このノートブックを実行する前に、必要なデータファイルをダウンロードしてください。")\n    print("データファイルは https://nlp100.github.io/data/popular-names.txt からダウンロードできます。")'),
        nbf.v4.new_code_cell('# UNIXコマンドでの確認（Jupyter上で実行）\n# cut, sort, uniqコマンドを使用して1列目の文字列の異なりを求める\n!cut -f 1 ../data/popular-names.txt | sort | uniq | wc -l 2>/dev/null || echo "コマンドの実行に失敗しました"'),
        nbf.v4.new_code_cell('# 1列目の異なる文字列の一部を表示\n!cut -f 1 ../data/popular-names.txt | sort | uniq | head -n 10 2>/dev/null || echo "コマンドの実行に失敗しました"'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、ファイルの1列目に含まれる文字列の種類（異なる文字列の集合）を求める方法を学びます。\n\n### Pythonでの実装\n\nPythonで1列目の文字列の異なりを求めるには、以下の手順を実行します：\n\n1. ファイルを開いて1行ずつ読み込みます。\n2. 各行をタブ文字で分割して列のリストを取得します。\n3. 1列目（インデックス0）の値をセット（`set`）に追加します。セットは重複を許さないデータ構造なので、自動的に異なる値のみが保持されます。\n4. 最終的に得られたセットの要素数が、1列目の異なる文字列の数となります。\n\n### UNIXコマンドでの確認\n\nUNIXコマンドを組み合わせて、1列目の文字列の異なりを求めることができます：\n\n```bash\ncut -f 1 input.txt | sort | uniq | wc -l\n```\n\n- `cut -f 1`：1列目を抽出します。\n- `sort`：抽出した値をソートします。\n- `uniq`：ソートされた値から重複を除去します。\n- `wc -l`：行数（異なる値の数）をカウントします。\n\n### 注意点\n\n- ファイルが存在しない場合のエラー処理を行っています。\n- 列数が不足している行に対する処理を考慮しています。\n- 文字エンコーディングを指定して、異なる言語や文字セットのファイルも正しく処理できるようにしています。\n- 大きなファイルでも効率的に処理できるように、ファイルを一度に全て読み込むのではなく、1行ずつ処理しています。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter02', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter02/17_unique_values.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_17()
