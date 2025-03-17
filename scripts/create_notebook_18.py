import nbformat as nbf
import os
from pathlib import Path

def create_notebook_18():
    """Create notebook for problem 18 (Sort by third column)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 18. 各行を3コラム目の数値の降順にソート\n\n各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ．'),
        nbf.v4.new_code_cell('# 問題18: 各行を3コラム目の数値の降順にソート\n\n# Pythonで3コラム目の数値の降順でソートする関数\ndef sort_by_column(file_path, column_index=2, reverse=True, delimiter=\'\\t\'):\n    """ファイルの行を特定の列の値でソートする関数\n    \n    Args:\n        file_path: 入力ファイルのパス\n        column_index: ソートする列のインデックス（0始まり）\n        reverse: 降順にする場合はTrue、昇順にする場合はFalse\n        delimiter: 列の区切り文字\n        \n    Returns:\n        ソートされた行のリスト\n    """\n    lines = []\n    \n    with open(file_path, \'r\', encoding=\'utf-8\') as f:\n        for line in f:\n            lines.append(line.rstrip(\'\\n\'))\n    \n    # 3コラム目（インデックス2）の数値でソート\n    # keyにはラムダ関数を使用して、各行を分割し、指定された列の値を数値に変換\n    sorted_lines = sorted(lines, \n                          key=lambda line: float(line.split(delimiter)[column_index]) if len(line.split(delimiter)) > column_index else 0, \n                          reverse=reverse)\n    \n    return sorted_lines\n\n# サンプルファイルのパス（実際の環境に合わせて変更してください）\nfile_path = \'../data/popular-names.txt\'\n\n# 3コラム目の数値の降順でソート\ntry:\n    sorted_lines = sort_by_column(file_path)\n    print(f"3コラム目の数値の降順でソートした結果（最初の5行）:")\n    for i, line in enumerate(sorted_lines):\n        if i < 5:\n            print(line)\n        else:\n            break\n    print("...")\nexcept FileNotFoundError:\n    print(f"ファイル {file_path} が見つかりません。")\n    print("このノートブックを実行する前に、必要なデータファイルをダウンロードしてください。")\n    print("データファイルは https://nlp100.github.io/data/popular-names.txt からダウンロードできます。")\nexcept IndexError:\n    print("ファイルの形式が想定と異なります。3列目が存在するか確認してください。")'),
        nbf.v4.new_code_cell('# UNIXコマンドでの確認（Jupyter上で実行）\n# sortコマンドを使用して3コラム目の数値の降順でソート\n!sort -t $\'\\t\' -k 3,3nr ../data/popular-names.txt | head -n 5 2>/dev/null || echo "コマンドの実行に失敗しました"'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、ファイルの各行を3コラム目（3列目）の数値の降順でソートする方法を学びます。\n\n### Pythonでの実装\n\nPythonで3コラム目の数値の降順でソートするには、以下の手順を実行します：\n\n1. ファイルを開いて全行を読み込みます。\n2. `sorted`関数を使用して、3コラム目（インデックス2）の数値に基づいて行をソートします。\n3. `key`パラメータにラムダ関数を指定して、各行を分割し、3コラム目の値を数値に変換してソートの基準とします。\n4. `reverse=True`を指定して、降順にソートします。\n\n### UNIXコマンドでの確認\n\nUNIXの`sort`コマンドを使用して、3コラム目の数値の降順でソートできます：\n\n```bash\nsort -t $\'\\t\' -k 3,3nr input.txt\n```\n\n- `-t $\'\\t\'`：タブ文字を区切り文字として指定します。\n- `-k 3,3`：3列目をソートのキーとして使用します。\n- `n`：数値としてソートします。\n- `r`：降順（逆順）でソートします。\n\n### 注意点\n\n- ファイルが存在しない場合のエラー処理を行っています。\n- 列数が不足している行に対する処理を考慮しています。\n- 文字エンコーディングを指定して、異なる言語や文字セットのファイルも正しく処理できるようにしています。\n- ソート時に元の行の内容は変更せず、行全体の順序のみを変更しています。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter02', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter02/18_sort_by_column.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_18()
