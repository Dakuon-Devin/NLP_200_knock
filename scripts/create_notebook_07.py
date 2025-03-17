import nbformat as nbf
import os
from pathlib import Path

def create_notebook_07():
    """Create notebook for problem 07 (Template)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 07. テンプレートによる文生成\n\n引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．'),
        nbf.v4.new_code_cell('# 問題07: テンプレートによる文生成\n\n# テンプレート文を生成する関数\ndef generate_template(x, y, z):\n    """「x時のyはz」という文字列を返す関数\n    \n    Args:\n        x: 時間\n        y: 主語\n        z: 値\n        \n    Returns:\n        テンプレート文字列\n    """\n    return f"{x}時の{y}は{z}"\n\n# 関数を実行\nx, y, z = 12, "気温", 22.4\nresult = generate_template(x, y, z)\n\n# 結果を表示\nprint(f"x = {x}, y = {y}, z = {z}")\nprint(f"生成された文: {result}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、引数を受け取り、それらを組み合わせて特定のテンプレートに従った文字列を生成する関数を実装します。\n\nPythonでは、文字列フォーマットにいくつかの方法があります：\n\n1. f-string（Python 3.6以降）: `f"{x}時の{y}は{z}"`\n2. format()メソッド: `"{}時の{}は{}".format(x, y, z)`\n3. %演算子: `"%s時の%sは%s" % (x, y, z)`\n\nこの実装では、最も読みやすく簡潔なf-stringを使用しています。\n\n関数は、与えられた引数x, y, zを受け取り、それらを「x時のyはz」というテンプレートに当てはめた文字列を返します。\n\n例として、x=12, y="気温", z=22.4を与えると、「12時の気温は22.4」という文字列が生成されます。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter01', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter01/07_template.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_07()
