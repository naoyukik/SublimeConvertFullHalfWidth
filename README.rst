********************
ConvertFullHalfWidth
********************

About
-----
ConvertFullHalfWidth supported for sublime text 3.

It convert Full-width to Half-width or Half-width to Full-width.
It Supported Katakana(kana), Alphabet(acii) and Number(digit).


Installation
------------
It's simple. Use Package Control.

Search ConvertFullHalfWidth


key Binding
-----------
This package exclude Default.sublime-keymap.

Key map example.

.. code-block:: javascript

    [
        // All Word convert to full-width.
        { "keys": ["ctrl+shift+a, ctrl+shift+"], "command": "convert_full_half_width", "args": {"to": "full", "kana": true, "ascii": true, "digit": true}},

        // Katakana convert to half-width.
        { "keys": ["ctrl+shift+k, ctrl+shift+f"], "command": "convert_full_half_width", "args": {"to": "half", "kana": true}},
    ]
