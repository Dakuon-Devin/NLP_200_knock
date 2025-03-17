import nbformat as nbf
import os
from pathlib import Path

def create_notebook_00():
    """Create notebook for problem 00 (string reversal)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 00. 文字列の逆順\n\n文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．'),
        nbf.v4.new_code_cell('# 問題00: 文字列の逆順\n\n# 与えられた文字列\ns = "stressed"\n\n# 文字列を逆順にする\nreversed_s = s[::-1]\n\n# 結果を表示\nprint(f"元の文字列: {s}")\nprint(f"逆順の文字列: {reversed_s}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nPythonでは、文字列のスライシング構文 `s[::-1]` を使用して文字列を逆順にすることができます。\n\n- `s[start:end:step]` の形式で、`start`から`end`までの範囲を`step`間隔で取得します。\n- `start`と`end`を省略すると、文字列全体が対象になります。\n- `step`に`-1`を指定すると、文字列を逆順に走査します。\n\n結果として、"stressed"の逆順である"desserts"が得られました。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter01', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter01/00_reverse_string.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_00()
