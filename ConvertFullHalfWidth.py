import sublime_plugin
from .jaconv.jaconv import h2z, z2h, hira2kata, kata2hira, hira2hkata


class ConvertFullHalfWidthCommand(sublime_plugin.TextCommand):
    def run(self, edit, to, kana=False, ascii=False, digit=False):
        sels = self.view.sel()
        for sel in sels:
            selection_word = self.view.substr(sel)
            if to == 'full':
                result = h2z(selection_word, '', kana, ascii, digit)
            else:
                result = z2h(selection_word, '', kana, ascii, digit)

            self.view.replace(edit, sel, result)


class ConvertHiraKataCommand(sublime_plugin.TextCommand):
    def run(self, edit, to, half=False):
        sels = self.view.sel()
        for sel in sels:
            selection_word = self.view.substr(sel)
            if to == 'kata':
                if half is False:
                    result = hira2kata(selection_word)
                else:
                    result = hira2hkata(selection_word)
            else:
                result = kata2hira(selection_word)

            self.view.replace(edit, sel, result)
