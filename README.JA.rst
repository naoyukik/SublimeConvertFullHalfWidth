*************
ConvertZenHan
*************

プラグインについて
------------------
| Sublime Text 3向けの全角文字を半角に、半角文字を全角へ変換するのをサポートするパッケージです。
| カタカナ(Kana)・アルファベット(Ascii)・数字(Digit)を全角半角へ変換するコマンドを用意しています。

また、このプラグインは全角半角変換に `jaconv <https://pypi.python.org/pypi/jaconv/>` 使用しています。

インストール
------------
Package Contorolに登録しています。下記の名前で検索できます。

ConvertZenHan

使用方法
--------
コンテキストメニュー
  コンテキストメニューにconvertZenHanのメニューを追加してあります。
  変換したい文字列を選択し、メニューから変換方法を選んでください。

コマンドパレット
	コマンドパレットからコマンドを呼び出すことが出来ます。
	ConvertZenHan: で登録してあります。
	変換したい文字列を選択し、コマンドパレットから変換方法を選んでください。


キーバインド例
--------------
このプラグインの初期設定のキーバインドは、設定していません。

もし設定を行いたい場合、下記のcommandを参考に "Preference -> Key Bindings - User" へ登録を行ってください。

.. code-block:: javascript

    [
        // 全ての文字列を全角へ
        { "keys": ["ctrl+shift+a, ctrl+shift+"], "command": "convert_zen_han", "args": {"to": "zen", "kana": true, "ascii": true, "digit": true}},

        // カタカナを半角へ
        { "keys": ["ctrl+shift+k, ctrl+shift+f"], "command": "convert_zen_han", "args": {"to": "han", "kana": true}},
    ]
