import nbformat as nbf
import os
from pathlib import Path

def create_notebook_11():
    """Create notebook for problem 11 (Tab to Space)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 11. タブをスペースに置換\n\nタブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．'),
        nbf.v4.new_code_cell('# 問題11: タブをスペースに置換\n\n# Pythonでタブをスペースに置換\ndef tab_to_space(file_path, output_path):\n    """タブをスペースに置換する関数\n    \n    Args:\n        file_path: 入力ファイルのパス\n        output_path: 出力ファイルのパス\n        \n    Returns:\n        置換した行数\n    """\n    count = 0\n    with open(file_path, \'r\', encoding=\'utf-8\') as f_in, \\\n         open(output_path, \'w\', encoding=\'utf-8\') as f_out:\n        for line in f_in:\n            if \'\\t\' in line:\n                count += 1\n            # タブをスペースに置換\n            new_line = line.replace(\'\\t\', \' \')\n            f_out.write(new_line)\n    return count\n\n# サンプルファイルのパス（実際の環境に合わせて変更してください）\nfile_path = \'../data/popular-names.txt\'\noutput_path = \'../data/popular-names-space.txt\'\n\n# タブをスペースに置換\ntry:\n    replaced_lines = tab_to_space(file_path, output_path)\n    print(f"Pythonで置換: {replaced_lines}行でタブが置換されました")\nexcept FileNotFoundError:\n    print(f"ファイル {file_path} が見つかりません。")\n    print("このノートブックを実行する前に、必要なデータファイルをダウンロードしてください。")\n    print("データファイルは https://nlp100.github.io/data/popular-names.txt からダウンロードできます。")'),
        nbf.v4.new_code_cell('# UNIXコマンドでの確認（Jupyter上で実行）\n# sedコマンドを使用\n!sed "s/\\t/ /g" ../data/popular-names.txt > /tmp/sed_result.txt 2>/dev/null && echo "sedコマンドで置換完了" || echo "sedコマンドでの置換に失敗しました"'),
        nbf.v4.new_code_cell('# trコマンドを使用\n!tr "\\t" " " < ../data/popular-names.txt > /tmp/tr_result.txt 2>/dev/null && echo "trコマンドで置換完了" || echo "trコマンドでの置換に失敗しました"'),
        nbf.v4.new_code_cell('# expandコマンドを使用\n!expand -t 1 ../data/popular-names.txt > /tmp/expand_result.txt 2>/dev/null && echo "expandコマンドで置換完了" || echo "expandコマンドでの置換に失敗しました"'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、ファイル内のタブ文字をスペース文字に置換する方法を学びます。\n\n### Pythonでの実装\n\nPythonでタブをスペースに置換するには、`replace()`メソッドを使用します。この実装では、入力ファイルを1行ずつ読み込み、タブ文字（`\\t`）をスペース文字（` `）に置換して、新しいファイルに書き込んでいます。\n\n### UNIXコマンドでの確認\n\nUNIXコマンドでは、以下の方法でタブをスペースに置換できます：\n\n1. **sedコマンド**：\n   ```bash\n   sed "s/\\t/ /g" input.txt > output.txt\n   ```\n   `s/\\t/ /g`は、タブ文字をスペースに置換するための置換パターンです。\n\n2. **trコマンド**：\n   ```bash\n   tr "\\t" " " < input.txt > output.txt\n   ```\n   `tr`コマンドは、文字の変換（translate）を行います。\n\n3. **expandコマンド**：\n   ```bash\n   expand -t 1 input.txt > output.txt\n   ```\n   `expand`コマンドは、タブをスペースに展開するためのコマンドです。`-t 1`オプションは、タブ1文字をスペース1文字に展開することを指定します。\n\n### 注意点\n\n- ファイルが存在しない場合のエラー処理を行っています。\n- 大きなファイルでも効率的に処理できるように、ファイルを一度に全て読み込むのではなく、1行ずつ処理しています。\n- 文字エンコーディングを指定して、異なる言語や文字セットのファイルも正しく処理できるようにしています。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter02', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter02/11_tab_to_space.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_11()
