import nbformat as nbf
import os
from pathlib import Path

def create_notebook_14():
    """Create notebook for problem 14 (First N lines)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 14. 先頭からN行を出力\n\n自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．'),
        nbf.v4.new_code_cell('# 問題14: 先頭からN行を出力\n\n# Pythonで先頭N行を出力する関数\ndef head(file_path, n):\n    """ファイルの先頭N行を出力する関数\n    \n    Args:\n        file_path: 入力ファイルのパス\n        n: 出力する行数\n        \n    Returns:\n        先頭N行の文字列のリスト\n    """\n    lines = []\n    with open(file_path, \'r\', encoding=\'utf-8\') as f:\n        for i, line in enumerate(f):\n            if i < n:\n                lines.append(line.rstrip(\'\\n\'))\n            else:\n                break\n    return lines\n\n# サンプルファイルのパス（実際の環境に合わせて変更してください）\nfile_path = \'../data/popular-names.txt\'\n\n# 行数を指定（コマンドライン引数の代わりに直接指定）\nn = 5\n\n# 先頭N行を出力\ntry:\n    result = head(file_path, n)\n    print(f"先頭{n}行:")\n    for line in result:\n        print(line)\nexcept FileNotFoundError:\n    print(f"ファイル {file_path} が見つかりません。")\n    print("このノートブックを実行する前に、必要なデータファイルをダウンロードしてください。")\n    print("データファイルは https://nlp100.github.io/data/popular-names.txt からダウンロードできます。")'),
        nbf.v4.new_code_cell('# コマンドライン引数を受け取る場合の実装例\nimport sys\n\ndef head_with_args(file_path, n):\n    """ファイルの先頭N行を出力する関数\n    \n    Args:\n        file_path: 入力ファイルのパス\n        n: 出力する行数\n    """\n    try:\n        with open(file_path, \'r\', encoding=\'utf-8\') as f:\n            for i, line in enumerate(f):\n                if i < n:\n                    print(line.rstrip(\'\\n\'))\n                else:\n                    break\n    except FileNotFoundError:\n        print(f"ファイル {file_path} が見つかりません。")\n\n# この関数をコマンドラインから実行する場合の例\n# python head.py popular-names.txt 5\nif __name__ == \'__main__\' and len(sys.argv) > 2:\n    file_path = sys.argv[1]\n    n = int(sys.argv[2])\n    head_with_args(file_path, n)\n\n# Jupyter上では実行しない（デモンストレーションのみ）\nprint("これはコマンドライン引数を受け取る実装例です。")\nprint("実際にコマンドラインから実行する場合は、以下のようにします：")\nprint("python head.py popular-names.txt 5")'),
        nbf.v4.new_code_cell('# UNIXコマンドでの確認（Jupyter上で実行）\n# headコマンドを使用して先頭N行を出力\n!head -n 5 ../data/popular-names.txt 2>/dev/null || echo "ファイルが見つかりません"'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、ファイルの先頭から指定された行数だけを出力する方法を学びます。\n\n### Pythonでの実装\n\nPythonでファイルの先頭N行を出力するには、以下の手順を実行します：\n\n1. ファイルを開いて1行ずつ読み込みます。\n2. カウンタを使用して、指定された行数に達するまで各行を処理します。\n3. 指定された行数に達したら、ループを終了します。\n\n### コマンドライン引数を受け取る実装\n\nPythonスクリプトをコマンドラインから実行する場合、`sys.argv`を使用してコマンドライン引数を受け取ることができます。\n\n```python\nimport sys\n\nfile_path = sys.argv[1]  # 1番目の引数（ファイルパス）\nn = int(sys.argv[2])     # 2番目の引数（行数）\n```\n\n### UNIXコマンドでの確認\n\nUNIXの`head`コマンドを使用して、ファイルの先頭N行を表示できます：\n\n```bash\nhead -n N input.txt\n```\n\n`-n`オプションは、表示する行数を指定します。\n\n### 注意点\n\n- ファイルが存在しない場合のエラー処理を行っています。\n- 大きなファイルでも効率的に処理できるように、ファイルを一度に全て読み込むのではなく、1行ずつ処理しています。\n- 文字エンコーディングを指定して、異なる言語や文字セットのファイルも正しく処理できるようにしています。\n- 実際のアプリケーションでは、コマンドライン引数やGUIなどを通じて、ユーザーから行数を受け取ることができます。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter02', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter02/14_head.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_14()
