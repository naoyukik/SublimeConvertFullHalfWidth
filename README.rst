*************
ConvertZenHan
*************

About
-----
CovertZenHan supported for sublime text 3.

It convert Full-width to Half-width or Half-width to Full-width.
It Supported Katakana, Alphabet and Number.


Installation
------------
It's simple. Use Package Control.

Search ConvertZenHan


key Binding
-----------
This package exclude Default.sublime-keymap.

Key map example.

.. code-block:: javascript

    [
        // All Word convert to full-width.
        { "keys": ["ctrl+shift+a, ctrl+shift+"], "command": "convert_zen_han", "args": {"to": "zen", "kana": true, "ascii": true, "digit": true}},

        // Katakana convert to half-width.
        { "keys": ["ctrl+shift+k, ctrl+shift+f"], "command": "convert_zen_han", "args": {"to": "han", "kana": true}},
    ]
