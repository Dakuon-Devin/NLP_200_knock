import nbformat as nbf
import os
from pathlib import Path

def create_notebook_06():
    """Create notebook for problem 06 (Set operations)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 06. 集合\n\n"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，\'se\'というbi-gramがXおよびYに含まれるかどうかを調べよ．'),
        nbf.v4.new_code_cell('# 問題06: 集合\n\n# n-gramを作成する関数（問題05で作成した関数を再利用）\ndef n_gram(sequence, n):\n    """シーケンスからn-gramを作成する関数\n    \n    Args:\n        sequence: 文字列またはリスト\n        n: n-gramのn\n        \n    Returns:\n        n-gramのリスト\n    """\n    return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]\n\n# 与えられた文字列\nstr1 = "paraparaparadise"\nstr2 = "paragraph"\n\n# 文字bi-gramの集合を作成\nX = set(n_gram(str1, 2))\nY = set(n_gram(str2, 2))\n\n# 和集合、積集合、差集合を計算\nunion_set = X | Y  # または X.union(Y)\nintersection_set = X & Y  # または X.intersection(Y)\ndifference_set_X_Y = X - Y  # または X.difference(Y)\ndifference_set_Y_X = Y - X  # または Y.difference(X)\n\n# \'se\'がXおよびYに含まれるかどうかを調べる\nse_in_X = "se" in X\nse_in_Y = "se" in Y\n\n# 結果を表示\nprint(f"文字列1: {str1}")\nprint(f"文字列2: {str2}")\nprint(f"X: {X}")\nprint(f"Y: {Y}")\nprint(f"和集合 (X | Y): {union_set}")\nprint(f"積集合 (X & Y): {intersection_set}")\nprint(f"差集合 (X - Y): {difference_set_X_Y}")\nprint(f"差集合 (Y - X): {difference_set_Y_X}")\nprint(f"\'se\' in X: {se_in_X}")\nprint(f"\'se\' in Y: {se_in_Y}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、2つの文字列から文字bi-gramの集合を作成し、集合演算を行います。\n\n1. まず、問題05で作成したn-gram関数を使用して、各文字列の文字bi-gramを生成します。\n2. 次に、これらのbi-gramをセット（集合）に変換します。\n3. 集合演算（和集合、積集合、差集合）を行います。\n4. 最後に、特定のbi-gram（\'se\'）が各集合に含まれるかどうかを確認します。\n\nPythonでは、集合演算を行うための演算子が用意されています：\n- 和集合（Union）: `|` または `union()`メソッド\n- 積集合（Intersection）: `&` または `intersection()`メソッド\n- 差集合（Difference）: `-` または `difference()`メソッド\n\n集合は重複を許さないため、同じbi-gramが複数回出現しても、集合内では1つとしてカウントされます。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter01', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter01/06_set_operations.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_06()
