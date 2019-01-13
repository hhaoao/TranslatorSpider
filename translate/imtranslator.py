"""
一个翻译提示窗
Author: hhaoao
date:   2019/1/5

"""

import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class CreateToolTip(object):
    """
    创建翻译提示框
    """

    def __init__(self, text='imtranslator info'):
        self.root = tk.Tk()
        # self.root.attributes("-toolwindow", 1)
        # self.root.wm_overrideredirect(True)
        self.root.title("书香年华")
        self.root.wm_geometry("+820+304")
        self.text = ScrolledText(self.root,
                                 background='#FFC66D',
                                 font=("楷体", "14", "normal"), height=10, width=50)
        self.text.insert(0.0, text)
        # self.root.bind("<FocusOut>", self.focusout)
        # self.root.bind("<FocusIn>", self.focusin)
        self.text.grid()
        # self.root.mainloop()

    def mainloop(self):
        self.root.mainloop()

    def set_text(self, text=None):
        self.text.delete(0.0, tk.END)
        # self.text.grid()
        self.text.insert(0.0, text)
        self.text.update_idletasks()

        # self.focusin()

    def focusin(self, event=None):
        # print("haha")
        self.root.deiconify()

    def focusout(self, event=None):
        pass
        # self.root.iconify()  # 最小化窗口
        # self.root.withdraw()  # 隐藏窗口
        # x = y = 0
        # x, y, cx, cy = self.widget.bbox("insert")
        #
        # x += self.widget.maxsize()[0] / 2
        #
        # y += self.tw.maxsize()[1] + 20


if __name__ == '__main__':
    tt = CreateToolTip()
    tt.mainloop()
