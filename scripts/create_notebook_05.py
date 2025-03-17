import nbformat as nbf
import os
from pathlib import Path

def create_notebook_05():
    """Create notebook for problem 05 (n-gram)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 05. n-gram\n\n与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．'),
        nbf.v4.new_code_cell('# 問題05: n-gram\n\n# n-gramを作成する関数\ndef n_gram(sequence, n):\n    """シーケンスからn-gramを作成する関数\n    \n    Args:\n        sequence: 文字列またはリスト\n        n: n-gramのn\n        \n    Returns:\n        n-gramのリスト\n    """\n    return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]\n\n# 与えられた文\ntext = "I am an NLPer"\n\n# 単語bi-gram\nwords = text.split()\nword_bigrams = n_gram(words, 2)\n\n# 文字bi-gram\nchar_bigrams = n_gram(text, 2)\n\n# 結果を表示\nprint(f"元の文: {text}")\nprint(f"単語リスト: {words}")\nprint(f"単語bi-gram: {word_bigrams}")\nprint(f"文字bi-gram: {char_bigrams}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、n-gramを作成する関数を実装し、それを使用して単語bi-gramと文字bi-gramを生成します。\n\nn-gramとは、与えられたシーケンス（文字列やリストなど）から連続するn個の要素を取り出したものです。例えば、文字列"hello"の文字bi-gram（n=2）は["he", "el", "ll", "lo"]となります。\n\n実装した関数では、リスト内包表記を使用して、シーケンスの各位置からn個の連続する要素を取り出しています。\n\n単語bi-gramの場合、まず文を単語に分割し、その単語リストに対してn-gram関数を適用します。結果として、連続する2つの単語のリストが得られます。\n\n文字bi-gramの場合、文字列全体に対してn-gram関数を適用します。結果として、連続する2つの文字のリストが得られます。\n\nn-gramは自然言語処理において、テキストの特徴抽出や類似度計算などに広く使用されています。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter01', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter01/05_n_gram.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_05()
