import nbformat as nbf
import os
from pathlib import Path

def create_notebook_01():
    """Create notebook for problem 01 (extract characters at specific positions)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 01. 「パタトクカシーー」\n\n「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．'),
        nbf.v4.new_code_cell('# 問題01: 「パタトクカシーー」\n\n# 与えられた文字列\ns = "パタトクカシーー"\n\n# 1,3,5,7文字目を取り出して連結\n# 注意: Pythonのインデックスは0から始まるため、1,3,5,7文字目は実際にはインデックス0,2,4,6\nresult = s[0] + s[2] + s[4] + s[6]\n\n# 結果を表示\nprint(f"元の文字列: {s}")\nprint(f"抽出結果: {result}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nPythonでは、文字列の各文字にインデックスを使ってアクセスできます。インデックスは0から始まるため、1文字目はインデックス0、3文字目はインデックス2、というように対応します。\n\n- 1文字目（インデックス0）: パ\n- 3文字目（インデックス2）: ト\n- 5文字目（インデックス4）: カ\n- 7文字目（インデックス6）: ー\n\nこれらを連結すると「パトカー」という文字列が得られます。\n\n別の解法として、スライシングを使用することもできます：\n```python\nresult = s[::2]  # 開始位置から終了位置まで、2文字ごとに取得\n```\nこの方法でも同じ結果が得られます。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter01', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter01/01_patatokukashi.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_01()
