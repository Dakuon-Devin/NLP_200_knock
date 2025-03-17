import nbformat as nbf
import os
from pathlib import Path

def create_notebook_08():
    """Create notebook for problem 08 (Cipher)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 08. 暗号文\n\n与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．\n\n- 英小文字ならば(219 - 文字コード)の文字に置換\n- その他の文字はそのまま出力\n\nこの関数を用い，英語のメッセージを暗号化・復号化せよ．'),
        nbf.v4.new_code_cell('# 問題08: 暗号文\n\n# 暗号化・復号化関数\ndef cipher(text):\n    """文字列を暗号化・復号化する関数\n    \n    英小文字ならば(219 - 文字コード)の文字に置換し、\n    その他の文字はそのまま出力する\n    \n    Args:\n        text: 入力文字列\n        \n    Returns:\n        暗号化・復号化された文字列\n    """\n    result = ""\n    for char in text:\n        if char.islower():  # 英小文字かどうかを判定\n            # 文字コードを取得し、変換式を適用\n            code = ord(char)\n            converted_code = 219 - code\n            result += chr(converted_code)\n        else:\n            # その他の文字はそのまま\n            result += char\n    return result\n\n# テスト用の文字列\noriginal_text = "Hello, World! This is a test message."\n\n# 暗号化\nencrypted_text = cipher(original_text)\n\n# 復号化（同じ関数を適用）\ndecrypted_text = cipher(encrypted_text)\n\n# 結果を表示\nprint(f"元の文字列: {original_text}")\nprint(f"暗号化後: {encrypted_text}")\nprint(f"復号化後: {decrypted_text}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、特定のルールに従って文字列を変換する暗号化・復号化関数を実装します。\n\n変換ルールは以下の通りです：\n- 英小文字（a-z）の場合、(219 - 文字コード)の文字に置換します。\n- その他の文字（大文字、数字、記号、空白など）はそのまま出力します。\n\nPythonでは、`ord()`関数を使用して文字のUnicode文字コードを取得し、`chr()`関数を使用して文字コードから文字を取得できます。また、`islower()`メソッドを使用して、文字が英小文字かどうかを判定できます。\n\n例えば、\'a\'の文字コードは97なので、変換後は219 - 97 = 122となり、これは\'z\'の文字コードです。同様に、\'z\'の文字コードは122なので、変換後は219 - 122 = 97となり、これは\'a\'の文字コードです。\n\n興味深いことに、この暗号化方式は対称的であり、同じ関数を2回適用すると元の文字列に戻ります。これは、(219 - (219 - x)) = xとなるためです。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter01', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter01/08_cipher.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_08()
