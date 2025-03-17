import nbformat as nbf
import os
from pathlib import Path

def create_notebook_04():
    """Create notebook for problem 04 (Chemical elements)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 04. 元素記号\n\n"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．'),
        nbf.v4.new_code_cell('# 問題04: 元素記号\n\n# 与えられた文\ntext = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."\n\n# 句読点を除去し、単語に分割\nimport re\nwords = re.sub(r"[,.]", "", text).split()\n\n# 1文字を取り出す単語の位置（1から始まるインデックス）\none_char_positions = [1, 5, 6, 7, 8, 9, 15, 16, 19]\n\n# 単語の位置（1始まり）から元素記号への連想配列を作成\nelement_dict = {}\n\nfor i, word in enumerate(words, 1):  # 1始まりのインデックス\n    if i in one_char_positions:\n        element_dict[word[:1]] = i  # 先頭1文字を取得\n    else:\n        element_dict[word[:2]] = i  # 先頭2文字を取得\n\n# 結果を表示\nprint(f"元の文: {text}")\nprint(f"単語リスト: {words}")\nprint(f"元素記号と単語位置の対応: {element_dict}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、与えられた文を単語に分解し、特定の位置の単語からは先頭1文字、それ以外の単語からは先頭2文字を取り出して、それらの文字と単語の位置を対応付ける辞書を作成します。\n\n1. まず、正規表現を使用してカンマとピリオドを除去し、文を単語に分割します。\n2. 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字を取り出します。\n3. それ以外の単語は先頭の2文字を取り出します。\n4. 取り出した文字と単語の位置（1始まり）を対応付ける辞書を作成します。\n\n結果として得られる辞書には、元素記号とその位置が格納されます。例えば、"H"（水素）は1番目の単語"Hi"から、"He"（ヘリウム）は2番目の単語"He"から取り出されます。\n\n実際に、この文から抽出される文字列は周期表の元素記号と対応しており、その位置は元素の原子番号と一致します。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter01', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter01/04_chemical_elements.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_04()
