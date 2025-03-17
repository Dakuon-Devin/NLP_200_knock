import nbformat as nbf
import os
from pathlib import Path

def create_notebook_02():
    """Create notebook for problem 02 (alternating characters from two strings)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 02. 「パトカー」+「タクシー」=「パタトクカシーー」\n\n「パトカー」+「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．'),
        nbf.v4.new_code_cell('# 問題02: 「パトカー」+「タクシー」=「パタトクカシーー」\n\n# 与えられた文字列\ns1 = "パトカー"\ns2 = "タクシー"\n\n# 方法1: ループを使用して交互に連結\nresult1 = ""\nfor i in range(len(s1)):\n    result1 += s1[i] + s2[i]\n\n# 方法2: zip関数とリスト内包表記を使用\nresult2 = "".join(c1 + c2 for c1, c2 in zip(s1, s2))\n\n# 結果を表示\nprint(f"文字列1: {s1}")\nprint(f"文字列2: {s2}")\nprint(f"方法1の結果: {result1}")\nprint(f"方法2の結果: {result2}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、2つの文字列の文字を交互に連結する方法を示しています。\n\n### 方法1: ループを使用\n\n最初の方法では、単純なループを使用して各文字列から同じインデックスの文字を交互に取り出し、新しい文字列に連結しています。\n\n### 方法2: zip関数とリスト内包表記\n\n2つ目の方法では、Pythonの`zip`関数を使用して2つの文字列を要素ごとにペアにし、リスト内包表記で各ペアを連結しています。最後に`join`メソッドを使用して、すべての連結されたペアを1つの文字列にまとめています。\n\nどちらの方法でも、「パトカー」と「タクシー」から「パタトクカシーー」という文字列が得られます。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter01', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter01/02_patoka_taxi.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_02()
