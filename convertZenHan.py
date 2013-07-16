import sublime
import sublime_plugin
from . import zenhan


class ConvertZenHanCommand(sublime_plugin.TextCommand):
    def run(self, edit, to, target):
        option = 0
        sels = self.view.sel()
        for target_str in target:
            target_int = getattr(zenhan, target_str.upper())
            if target_int >= 7:
                option = option | target_int
                break
            option = option | target_int

        for sel in sels:
            selection_word = self.view.substr(sel)
            if to == 'zen':
                result = zenhan.h2z(selection_word, option)
            else:
                result = zenhan.z2h(selection_word, option)

            self.view.replace(edit, sel, result)
