import nbformat as nbf
import os
from pathlib import Path

def create_notebook_09():
    """Create notebook for problem 09 (Typoglycemia)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 09. Typoglycemia\n\nスペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが4以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．'),
        nbf.v4.new_code_cell('# 問題09: Typoglycemia\n\nimport random\n\n# Typoglycemiaを実装する関数\ndef typoglycemia(text):\n    """単語の先頭と末尾の文字は残し、それ以外の文字の順序をランダムに並び替える関数\n    \n    ただし、長さが4以下の単語は並び替えない\n    \n    Args:\n        text: 入力文字列\n        \n    Returns:\n        変換後の文字列\n    """\n    words = text.split()\n    result = []\n    \n    for word in words:\n        # 句読点を分離\n        if word[-1] in [\'.\', \',\', \':\', \';\', \'!\', \'?\']:\n            punct = word[-1]\n            word = word[:-1]\n        else:\n            punct = \'\'\n        \n        # 長さが4以下の単語は並び替えない\n        if len(word) <= 4:\n            result.append(word + punct)\n        else:\n            # 先頭と末尾の文字を保持し、それ以外の文字をランダムに並び替え\n            middle_chars = list(word[1:-1])\n            random.shuffle(middle_chars)\n            shuffled_word = word[0] + \'\'.join(middle_chars) + word[-1] + punct\n            result.append(shuffled_word)\n    \n    return \' \'.join(result)\n\n# テスト用の文\ntext = "I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."\n\n# シード値を固定して再現性を確保\nrandom.seed(42)\n\n# Typoglycemiaを適用\nshuffled_text = typoglycemia(text)\n\n# 結果を表示\nprint(f"元の文: {text}")\nprint(f"変換後: {shuffled_text}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、「Typoglycemia」と呼ばれる現象を模倣するプログラムを実装します。Typoglycemiaとは、単語の先頭と末尾の文字が正しい位置にあれば、中間の文字の順序が入れ替わっていても人間は読むことができるという現象です。\n\n実装した関数では、以下の処理を行っています：\n\n1. 入力文字列をスペースで区切って単語のリストに分割します。\n2. 各単語に対して：\n   - 句読点（.,:;!?）が末尾にある場合、一時的に分離します。\n   - 単語の長さが4以下の場合、そのまま出力します。\n   - 単語の長さが5以上の場合、先頭と末尾の文字を保持し、中間の文字をランダムに並び替えます。\n3. 処理した単語を再びスペースで連結して返します。\n\nランダムな結果を再現可能にするために、`random.seed()`を使用して乱数生成器のシード値を固定しています。\n\nこのプログラムを実行すると、長い単語の中間部分がランダムに並び替えられますが、先頭と末尾の文字は変わらないため、文章全体の意味は理解できる状態を保ちます。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter01', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter01/09_typoglycemia.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_09()
