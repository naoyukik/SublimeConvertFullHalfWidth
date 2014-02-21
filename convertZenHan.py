import sublime
import sublime_plugin
from . import jctconv

class ConvertZenHanCommand(sublime_plugin.TextCommand):
    def run(self, edit, to, target):
        option = 0
        sels = self.view.sel()
        print(target[0])
        for sel in sels:
            selection_word = self.view.substr(sel)
            if to == 'zen':
                result = jctconv.h2z(selection_word, target[0])
            else:
                result = jctconv.z2h(selection_word, target[0])

            self.view.replace(edit, sel, result)
