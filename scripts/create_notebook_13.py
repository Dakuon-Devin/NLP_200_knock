import nbformat as nbf
import os
from pathlib import Path

def create_notebook_13():
    """Create notebook for problem 13 (Merge columns)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 13. col1.txtとcol2.txtをマージ\n\ncol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．'),
        nbf.v4.new_code_cell('# 問題13: col1.txtとcol2.txtをマージ\n\n# Pythonで列をマージ\ndef merge_columns(col1_path, col2_path, output_path):\n    """2つのファイルの内容をマージしてタブ区切りのファイルを作成する関数\n    \n    Args:\n        col1_path: 1列目のファイルのパス\n        col2_path: 2列目のファイルのパス\n        output_path: 出力ファイルのパス\n        \n    Returns:\n        処理した行数\n    """\n    count = 0\n    with open(col1_path, \'r\', encoding=\'utf-8\') as f_col1, \\\n         open(col2_path, \'r\', encoding=\'utf-8\') as f_col2, \\\n         open(output_path, \'w\', encoding=\'utf-8\') as f_out:\n        for line1, line2 in zip(f_col1, f_col2):\n            count += 1\n            # 改行文字を削除して結合\n            merged_line = line1.strip() + \'\\t\' + line2.strip() + \'\\n\'\n            f_out.write(merged_line)\n    return count\n\n# サンプルファイルのパス（実際の環境に合わせて変更してください）\ncol1_path = \'../data/col1.txt\'\ncol2_path = \'../data/col2.txt\'\noutput_path = \'../data/merged.txt\'\n\n# 列をマージ\ntry:\n    processed_lines = merge_columns(col1_path, col2_path, output_path)\n    print(f"Pythonで処理: {processed_lines}行をマージしました")\n    print(f"マージ結果を {output_path} に保存しました")\nexcept FileNotFoundError as e:\n    print(f"ファイルが見つかりません: {e}")\n    print("このノートブックを実行する前に、問題12を実行して必要なファイルを作成してください。")'),
        nbf.v4.new_code_cell('# UNIXコマンドでの確認（Jupyter上で実行）\n# pasteコマンドを使用して列をマージ\n!paste ../data/col1.txt ../data/col2.txt > /tmp/unix_merged.txt 2>/dev/null && echo "pasteコマンドでマージ完了" || echo "pasteコマンドでのマージに失敗しました"'),
        nbf.v4.new_code_cell('# 結果の確認（最初の5行を表示）\nprint("Pythonでマージした結果（最初の5行）:")\n!head -n 5 ../data/merged.txt 2>/dev/null || echo "ファイルが見つかりません"\n\nprint("\\nUNIXコマンドでマージした結果（最初の5行）:")\n!head -n 5 /tmp/unix_merged.txt 2>/dev/null || echo "ファイルが見つかりません"'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、2つのファイルの内容を1行ずつ読み込み、それらをタブ区切りで結合して新しいファイルに書き込む方法を学びます。\n\n### Pythonでの実装\n\nPythonで2つのファイルをマージするには、以下の手順を実行します：\n\n1. 2つの入力ファイルと1つの出力ファイルを開きます。\n2. `zip`関数を使用して、2つのファイルから1行ずつ同時に読み込みます。\n3. 各行の末尾の改行文字を削除し、タブ文字で結合して新しい行を作成します。\n4. 結合した行を出力ファイルに書き込みます。\n\n### UNIXコマンドでの確認\n\nUNIXの`paste`コマンドを使用して、複数のファイルを列方向に結合できます：\n\n```bash\npaste col1.txt col2.txt > merged.txt\n```\n\n`paste`コマンドは、デフォルトでタブ区切りを使用して、指定された複数のファイルの各行を結合します。\n\n### 注意点\n\n- ファイルが存在しない場合のエラー処理を行っています。\n- `zip`関数は、最も短いイテラブルが終了した時点で停止するため、2つのファイルの行数が異なる場合は、短い方に合わせて処理されます。\n- 文字エンコーディングを指定して、異なる言語や文字セットのファイルも正しく処理できるようにしています。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter02', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter02/13_merge_columns.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_13()
