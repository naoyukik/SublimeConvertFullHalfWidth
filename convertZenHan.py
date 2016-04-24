import sublime_plugin
from .jaconv.jaconv import h2z, z2h


class ConvertZenHanCommand(sublime_plugin.TextCommand):
    def run(self, edit, to, target):
        # option = 0
        sels = self.view.sel()
        for sel in sels:
            selection_word = self.view.substr(sel)
            if to == 'zen':
                result = h2z(selection_word, target[0])
            else:
                result = z2h(selection_word, target[0])

            self.view.replace(edit, sel, result)
