"""
获取鼠标拖拽选中的文本
Author: hhaoao
date:   2018/12/30

"""

from pahk import Interpreter
from time import sleep

# def get_clipboard():
#     ahk_interpreter = Interpreter()
#     ahk_script = 'D:\\PycharmProjects\\imtranslator\\test.ahk'
#     # Create a variable "x" which hold the clipboard data.
#     ahk_interpreter.execute_file(ahk_script)
#
#     sleep(1.5)  # Let the thread warms up
#
#     while 1:
#         print(get_clipboard(), '打印剪切板内容')
#         quit_text = input('输入quit退出')
#         if quit_text == 'quit':
#             break
#         clipboard = ahk_interpreter.var_get('ha')
#     # Get the value of the variable x in the current running script
#     # clipboard = ahk_interpreter.var_assign()
#     # ahk_interpreter.terminate()  # Terminate the running script
#     # del ahk_interpreter
#
#     return clipboard
from translate.google_api import google_tran
from translate.imtranslator import CreateToolTip


class GetAhkText(object):
    def __init__(self):
        self.ahk_interpreter = Interpreter()
        self.ahk_script = r'D:\PycharmProjects\TranslatorSpider\translate\bin\scripts\get_text.ahk'

        self.ahk_tt = self.ahk_interpreter.execute_file(self.ahk_script)

    def get_ready(self):
        while 1:
            sleep(0.1)
            if self.ahk_interpreter.ready():
                break
            # print('等待0.1秒')

    def get_clipboard(self):
        board = self.ahk_interpreter.var_get('clipboard_text')
        # print(board, "board")
        return board


# def get_text():
#     clipboard = autohotkey.get_clipboard()
#     if clipboard != clipboard_old:
#     clipboard_old = clipboard
#     tip.set_text(clipboard)
#     print(clipboard, '内容')
#     sleep(500)
#     quit_text = input('输入quit退出')

class ToolText(object):
    def __init__(self):
        self.tooltip = CreateToolTip()
        self.autohotkey = GetAhkText()
        self.autohotkey.get_ready()
        self.text_old = ""

    def get_text(self):
        clipboard = self.autohotkey.get_clipboard()
        # print(clipboard, "剪切板")
        if (clipboard != self.text_old) and clipboard:
            self.text_old = clipboard
            self.tooltip.set_text("翻译中。。。")
            # sleep(3)
            des_string_translated = google_tran(clipboard,
                                                des_1='zh-cn',
                                                src_1='auto')
            if des_string_translated.src == 'zh-CN':
                des_string = google_tran(clipboard, des_1='en', src_1='zh-cn').text
            else:
                des_string = des_string_translated.text
            # des_string = clipboard
            # print('翻译：', des_string, "内容：\n", clipboard)
            self.tooltip.set_text(des_string)
        self.tooltip.root.after(100, self.get_text)


if __name__ == '__main__':
    # ui中定时更新内容，试着将autohotkey弄进UI
    tooltip = ToolText()
    tooltip.get_text()
    tooltip.tooltip.mainloop()
