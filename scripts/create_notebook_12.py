import nbformat as nbf
import os
from pathlib import Path

def create_notebook_12():
    """Create notebook for problem 12 (Split columns)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存\n\n各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．'),
        nbf.v4.new_code_cell('# 問題12: 1列目をcol1.txtに，2列目をcol2.txtに保存\n\n# Pythonで列を抽出して保存\ndef extract_columns(file_path, col1_path, col2_path):\n    """ファイルから1列目と2列目を抽出して別々のファイルに保存する関数\n    \n    Args:\n        file_path: 入力ファイルのパス\n        col1_path: 1列目を保存するファイルのパス\n        col2_path: 2列目を保存するファイルのパス\n        \n    Returns:\n        処理した行数\n    """\n    count = 0\n    with open(file_path, \'r\', encoding=\'utf-8\') as f_in, \\\n         open(col1_path, \'w\', encoding=\'utf-8\') as f_col1, \\\n         open(col2_path, \'w\', encoding=\'utf-8\') as f_col2:\n        for line in f_in:\n            if line.strip():  # 空行でない場合\n                count += 1\n                columns = line.strip().split(\'\\t\')\n                if len(columns) >= 2:\n                    f_col1.write(columns[0] + \'\\n\')\n                    f_col2.write(columns[1] + \'\\n\')\n    return count\n\n# サンプルファイルのパス（実際の環境に合わせて変更してください）\nfile_path = \'../data/popular-names.txt\'\ncol1_path = \'../data/col1.txt\'\ncol2_path = \'../data/col2.txt\'\n\n# 列を抽出して保存\ntry:\n    processed_lines = extract_columns(file_path, col1_path, col2_path)\n    print(f"Pythonで処理: {processed_lines}行を処理しました")\n    print(f"1列目を {col1_path} に保存しました")\n    print(f"2列目を {col2_path} に保存しました")\nexcept FileNotFoundError:\n    print(f"ファイル {file_path} が見つかりません。")\n    print("このノートブックを実行する前に、必要なデータファイルをダウンロードしてください。")\n    print("データファイルは https://nlp100.github.io/data/popular-names.txt からダウンロードできます。")'),
        nbf.v4.new_code_cell('# UNIXコマンドでの確認（Jupyter上で実行）\n# cutコマンドを使用して1列目を抽出\n!cut -f 1 ../data/popular-names.txt > /tmp/unix_col1.txt 2>/dev/null && echo "1列目を抽出しました" || echo "1列目の抽出に失敗しました"'),
        nbf.v4.new_code_cell('# cutコマンドを使用して2列目を抽出\n!cut -f 2 ../data/popular-names.txt > /tmp/unix_col2.txt 2>/dev/null && echo "2列目を抽出しました" || echo "2列目の抽出に失敗しました"'),
        nbf.v4.new_code_cell('# 結果の確認（最初の5行を表示）\nprint("Pythonで抽出した1列目（最初の5行）:")\n!head -n 5 ../data/col1.txt 2>/dev/null || echo "ファイルが見つかりません"\n\nprint("\\nPythonで抽出した2列目（最初の5行）:")\n!head -n 5 ../data/col2.txt 2>/dev/null || echo "ファイルが見つかりません"\n\nprint("\\nUNIXコマンドで抽出した1列目（最初の5行）:")\n!head -n 5 /tmp/unix_col1.txt 2>/dev/null || echo "ファイルが見つかりません"\n\nprint("\\nUNIXコマンドで抽出した2列目（最初の5行）:")\n!head -n 5 /tmp/unix_col2.txt 2>/dev/null || echo "ファイルが見つかりません"'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、タブ区切りのテキストファイルから特定の列を抽出し、別々のファイルに保存する方法を学びます。\n\n### Pythonでの実装\n\nPythonで列を抽出するには、以下の手順を実行します：\n\n1. 入力ファイルを開き、1行ずつ読み込みます。\n2. 各行をタブ文字（`\\t`）で分割して列のリストを取得します。\n3. 1列目（インデックス0）と2列目（インデックス1）を別々のファイルに書き込みます。\n\n### UNIXコマンドでの確認\n\nUNIXの`cut`コマンドを使用して、特定の列を抽出できます：\n\n```bash\ncut -f 1 input.txt > col1.txt  # 1列目を抽出\ncut -f 2 input.txt > col2.txt  # 2列目を抽出\n```\n\n`-f`オプションは、抽出するフィールド（列）を指定します。デフォルトのフィールド区切り文字はタブです。\n\n### 注意点\n\n- ファイルが存在しない場合のエラー処理を行っています。\n- 空行や列数が不足している行に対する処理を考慮しています。\n- 文字エンコーディングを指定して、異なる言語や文字セットのファイルも正しく処理できるようにしています。\n- 大きなファイルでも効率的に処理できるように、ファイルを一度に全て読み込むのではなく、1行ずつ処理しています。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter02', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter02/12_split_columns.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_12()
