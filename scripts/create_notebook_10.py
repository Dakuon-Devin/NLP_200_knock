import nbformat as nbf
import os
from pathlib import Path

def create_notebook_10():
    """Create notebook for problem 10 (Line count)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 10. 行数のカウント\n\n行数をカウントせよ．確認にはwcコマンドを用いよ．'),
        nbf.v4.new_code_cell('# 問題10: 行数のカウント\n\n# Pythonで行数をカウント\ndef count_lines(file_path):\n    """ファイルの行数をカウントする関数\n    \n    Args:\n        file_path: 対象ファイルのパス\n        \n    Returns:\n        行数\n    """\n    with open(file_path, \'r\', encoding=\'utf-8\') as f:\n        return sum(1 for _ in f)\n\n# サンプルファイルのパス（実際の環境に合わせて変更してください）\nfile_path = \'../data/popular-names.txt\'\n\n# 行数をカウント\ntry:\n    line_count = count_lines(file_path)\n    print(f"Pythonでカウント: {line_count}行")\nexcept FileNotFoundError:\n    print(f"ファイル {file_path} が見つかりません。")\n    print("このノートブックを実行する前に、必要なデータファイルをダウンロードしてください。")\n    print("データファイルは https://nlp100.github.io/data/popular-names.txt からダウンロードできます。")'),
        nbf.v4.new_code_cell('# UNIXコマンドでの確認（Jupyter上で実行）\n!wc -l ../data/popular-names.txt 2>/dev/null || echo "ファイルが見つかりません。"'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、ファイルの行数をカウントする方法を学びます。\n\n### Pythonでの実装\n\nPythonでファイルの行数をカウントするには、ファイルを開いて各行を読み込み、カウントする方法があります。上記の実装では、ファイルを開いてジェネレータ式を使用して効率的に行数をカウントしています。\n\n### UNIXコマンドでの確認\n\nUNIXコマンドの`wc`（word count）を使用して行数を確認できます。`-l`オプションを指定すると、行数のみをカウントします。\n\n```bash\nwc -l ファイル名\n```\n\n### 注意点\n\n- ファイルが存在しない場合のエラー処理を行っています。\n- 大きなファイルでも効率的に処理できるように、ファイルを一度に全て読み込むのではなく、1行ずつ処理しています。\n- 文字エンコーディングを指定して、異なる言語や文字セットのファイルも正しく処理できるようにしています。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter02', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter02/10_line_count.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_10()
