import nbformat as nbf
import os
from pathlib import Path

def create_notebook_03():
    """Create notebook for problem 03 (Pi)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 03. 円周率\n\n"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．'),
        nbf.v4.new_code_cell('# 問題03: 円周率\n\n# 与えられた文\ntext = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."\n\n# 句読点を除去し、単語に分割\nimport re\nwords = re.sub(r"[,.]", "", text).split()\n\n# 各単語の文字数をリストに格納\nword_lengths = [len(word) for word in words]\n\n# 結果を表示\nprint(f"元の文: {text}")\nprint(f"単語リスト: {words}")\nprint(f"各単語の文字数: {word_lengths}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、与えられた文を単語に分解し、各単語の文字数を順番に並べたリストを作成します。\n\n1. まず、正規表現を使用してカンマとピリオドを除去します。\n2. 次に、`split()`メソッドを使用して文を単語に分割します。\n3. リスト内包表記を使用して、各単語の長さを計算し、新しいリストに格納します。\n\n結果として得られるリストは `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]` となります。\n\n興味深いことに、これは円周率（π）の最初の数桁（3.14159265358979）に対応しています。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter01', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter01/03_pi.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_03()
