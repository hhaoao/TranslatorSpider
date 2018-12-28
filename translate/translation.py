import os
import linecache
import queue
import sys

# sys.path.append('proxy_pool_master')
from re import split
import threading
from time import sleep
from tkinter import Tk, ttk, END, DISABLED, N, S, E, W, StringVar, Text, Toplevel, Canvas
# 先测试快捷键在弄UI
from tkinter.font import Font, NORMAL

# from win32api import ShellExecute, SendMessage
# from win32gui import FindWindow
# from win32con import WM_CLOSE

import pahk
from math import ceil
from pyperclip import copy
from pypinyin import lazy_pinyin

# from proxy_pool_master.Run import proxy_main
# from startup_script import startup_script

from translate.google_api import google_tran


def print_exception():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    line_no = tb.tb_lineno
    filename = f.f_code.co_filename
    module_name = f.f_code.co_name
    linecache.checkcache(filename)
    line = linecache.getline(filename, line_no, f.f_globals)
    return 'Traceback (most recent call last):\n{}File "{}", line {}, in {}:\n{}\n\n{}:{}'.format('   ', filename,
                                                                                                  line_no, module_name,
                                                                                                  line.strip(),
                                                                                                  exc_type,
                                                                                                  exc_obj)


class Thread_0(threading.Thread):  # 线程模块
    def __init__(self, queue_1):
        threading.Thread.__init__(self, daemon=True)
        self.queue = queue_1
        self.start()

    def run(self):  # 这里放要运行的函数
        list_queue = self.queue.get(block=False)
        # list_queue[0](list_queue[1])
        # self.queue.task_done()
        # print(threading.activeCount(),
        #       threading.enumerate())
        try:
            if not list_queue[1]:
                # print(list_queue)
                list_queue[0]()
            else:
                list_queue[0](list_queue[1])
            self.queue.task_done()
        except Exception as e:
            list_queue[2](print_exception(), 0.0, END, ('GROOVE', 'font_error'))
        # T_GUI.root.destroy()
        # T_GUI.root.destroy()


class MyTread_0:  # 创建新线程
    def __init__(self, queue_0):
        self.queue = queue_0
        try:
            Thread_0(self.queue)
        except Exception as e:
            self.queue[2](print_exception(), 0.0, END, ('GROOVE', 'font_error'))


class T_GUI:
    def __init__(self, root):
        self.language = {'阿尔巴尼亚语': 'sq', '阿拉伯语': 'ar', '阿姆哈拉语': 'am', '阿塞拜疆语': 'az',
                         '爱尔兰语': 'ga', '爱沙尼亚语': 'et', '巴斯克语': 'eu', '白俄罗斯语': 'be', '保加利亚语': 'bg',
                         '冰岛语': 'is', '波兰语': 'pl', '波斯尼亚语': 'bs', '波斯语': 'fa', '布尔语南非荷兰语': 'af',
                         '丹麦语': 'da', '德语': 'de', '俄语': 'ru', '法语': 'fr', '菲律宾语': 'tl',
                         '弗里西语': 'fy', '高棉语': 'km', '格鲁吉亚语': 'ka', '古吉拉特语': 'gu', '哈萨克语': 'kk',
                         '海地克里奥尔语': 'ht', '韩语': 'ko', '豪萨语': 'ha', '荷兰语': 'nl', '吉尔吉斯语': 'ky',
                         '加利西亚语': 'gl', '加泰罗尼亚语': 'ca', '捷克语': 'cs', '卡纳达语': 'kn', '科西嘉语': 'co',
                         '克罗地亚语': 'hr', '库尔德语': 'ku', '拉丁语': 'la', '拉脱维亚语': 'lv', '老挝语': 'lo',
                         '立陶宛语': 'lt', '卢森堡语': 'lb', '罗马尼亚语': 'ro', '马尔加什语': 'mg', '马耳他语': 'mt',
                         '马拉地语': 'mr', '马拉雅拉姆语': 'ml', '马来语': 'ms', '马其顿语': 'mk', '毛利语': 'mi',
                         '蒙古语': 'mn', '孟加拉语': 'bn', '缅甸语': 'my', '苗语': 'hmn', '南非科萨语': 'xh',
                         '南非祖鲁语': 'zu', '尼泊尔语': 'ne', '挪威语': 'no', '旁遮普语': 'pa', '葡萄牙语': 'pt',
                         '普什图语': 'ps', '齐切瓦语': 'ny', '日语': 'ja', '瑞典语': 'sv', '萨摩亚语': 'sm',
                         '塞尔维亚语': 'sr', '塞索托语': 'st', '僧伽罗语': 'si', '世界语': 'eo', '斯洛伐克语': 'sk',
                         '斯洛文尼亚语': 'sl', '斯瓦希里语': 'sw', '苏格兰盖尔语': 'gd', '宿务语': 'ceb', '索马里语': 'so',
                         '塔吉克语': 'tg', '泰卢固语': 'te', '泰米尔语': 'ta', '泰语': 'th', '土耳其语': 'tr',
                         '威尔士语': 'cy', '乌尔都语': 'ur', '乌克兰语': 'uk', '乌兹别克语': 'uz', '希伯来语': 'iw',
                         '希腊语': 'el', '西班牙语': 'es', '夏威夷语': 'haw', '信德语': 'sd', '匈牙利语': 'hu',
                         '修纳语': 'sn', '亚美尼亚语': 'hy', '伊博语': 'ig', '意大利语': 'it', '意第绪语': 'yi',
                         '印地语': 'hi', '印尼巽他语': 'su', '印尼语': 'id', '印尼爪哇语': 'jw', '英语': 'en',
                         '约鲁巴语': 'yo', '越南语': 'vi', '中文繁体': 'zh-TW', '中文简体': 'zh-CN'}

        self.common_list = [['英语'], ['西班牙语'], ['中文简体'], ['日语']]
        lan_sort_1 = sorted(self.language.keys(), key=lambda char: lazy_pinyin(char)[0][0])  # 排好序的语种list
        table_len, lan_sort = len(self.language), []
        # 按扭最大宽度，表格横竖比
        button_max_width, table = len(max(lan_sort_1, key=len)) + 2, (ceil(table_len / 7), 7)
        for i in range(0, len(lan_sort_1), table[0]):  # 格式化成二维数组,
            lan_sort.append(lan_sort_1[i:i + table[0]])  # 由于后面会进行行纵交换操作，这里取最大值为列数
        # print(button_max_width)

        var, var_1 = StringVar(), StringVar()
        var.set('自动检测')
        var_1.set(lan_sort_1[-1])

        self.root = root
        self.root.title('书香年华的专用翻译小工具')
        self.font = Font()
        self.frame = ttk.Frame(self.root)
        self.text = Text(self.frame, width=20, height=10)
        self.text_out = Text(self.frame)

        self.button_1 = ttk.Button(self.frame, text='自动检测')
        self.button_2 = ttk.Button(self.frame, text='<=>')
        self.button_3 = ttk.Button(self.frame, text='中文简体')
        self.button_4 = ttk.Button(self.frame, text='翻译')
        self.top_1 = Toplevel(self.button_1)
        self.top_2 = Toplevel(self.button_3)
        self.foc_button = None
        self.top_3 = Toplevel(self.button_1)

        self.tree_1 = ttk.Treeview(self.top_1)
        self.tree_2 = ttk.Treeview(self.top_2)
        self.tree_3 = ttk.Treeview(self.top_3)

        self.canvas_1 = Canvas(self.tree_1)
        self.canvas_2 = Canvas(self.tree_2)
        self.canvas_3 = Canvas(self.tree_3)
        self.canvas_1_text = self.canvas_1.create_text(0, 0)
        self.canvas_2_text = self.canvas_2.create_text(0, 0)
        self.canvas_3_text = self.canvas_3.create_text(0, 0)

        self.sizegrip = ttk.Sizegrip(self.frame)  # 方便调整窗口大小的部件
        # 菜单按钮没写，已完成2018.07.30
        # 位置布局
        self.frame.grid(row=0, column=0, columnspan=4, sticky=(N, S, E, W))
        self.text_out.grid(row=0, column=0, columnspan=4, sticky=(N, S, E, W))
        self.button_1.grid(row=1, column=0, sticky=E)
        self.button_2.grid(row=1, column=1)
        self.button_3.grid(row=1, column=2, sticky=W)
        self.button_4.grid(row=1, column=3)
        self.text.grid(row=2, column=0, columnspan=4, sticky=(N, S, E, W))
        self.top_1.grid()
        self.top_2.grid()
        self.top_3.grid()
        self.tree_1.grid()
        self.tree_2.grid()
        self.tree_3.grid()
        self.sizegrip.grid(row=2, column=3, sticky=(S, E))

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=2)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=4)
        self.frame.rowconfigure(0, weight=3)
        self.frame.rowconfigure(2, weight=1)

        # 字体设置
        self.text_out.tag_configure('font', foreground='#476042',
                                    font=('Tempus Sans ITC', 35, 'bold'))
        self.text_out.tag_configure('font_normal', font=20)
        self.text_out.tag_configure('font_error', foreground='red', font=('Segoe Print', 16, 'bold'))

        self.text.insert(END, '输入框', 'SUNKEN')
        self.text.focus_set()
        self.text.tag_add('sel', 1.0, END)  # 全选文本
        # self.frame.tk_focusFollowsMouse()
        self.text_out.insert(END, '输出框', ('GROOVE', 'font_normal'))
        self.all_var = [self.text.get(0.0, END), var, var_1, True]
        self.text_out.configure(state=DISABLED)

        # 忽略并隐藏窗口
        self.top_1.wm_overrideredirect(True)
        self.top_2.wm_overrideredirect(True)
        self.top_3.wm_overrideredirect(True)
        self.top_1.withdraw()
        self.top_2.withdraw()
        self.top_3.withdraw()

        #  事件0
        self.text_out.bind('<Button-3>', self._right_click)  # 右键复制文本
        self.button_1.bind('<Enter>', self._button_menu)
        self.button_1.bind('<Leave>', self._button_leave)
        self.button_3.bind('<Enter>', self._button_menu)
        self.button_3.bind('<Leave>', self._button_leave)
        # self.top_3.bind('Leave', lambda e: self.top_3.withdraw())
        self.top_1.bind('<FocusOut>', self._lose_focus)  # 失去焦点隐藏窗口
        self.top_2.bind('<FocusOut>', self._lose_focus)
        self.top_3.bind('<FocusOut>', self._lose_focus)
        # 在同一个位置，第一次按是tree部件，第二次是canvas部件
        self.canvas_1.bind('<ButtonPress-1>', lambda evt: self.top_1.withdraw())  # 画布按下时，隐藏窗口
        self.tree_1.bind('<Configure>', lambda evt: self.canvas_1.grid_forget())  # place_forget()取消选中状态
        self.tree_1.bind('<ButtonPress-1>', self._tree_pressed)
        self.tree_1.bind('<Leave>', lambda e: self.top_1.withdraw())  # 离开某组件，隐藏窗口
        self.canvas_2.bind('<ButtonPress-1>', lambda evt: self.top_2.withdraw())  # 画布按下时，隐藏窗口
        self.tree_2.bind('<Configure>', lambda evt: self.canvas_2.grid_forget())  # place_forget()取消选中状态
        self.tree_2.bind('<ButtonPress-1>', self._tree_pressed)
        self.tree_2.bind('<Leave>', lambda e: self.top_2.withdraw())  # 离开某组件，隐藏窗口
        self.canvas_3.bind('<ButtonPress-1>', lambda evt: self.top_3.withdraw())
        self.tree_3.bind('<Configure>', lambda evt: self.canvas_3.grid_forget())
        self.tree_3.bind('<ButtonPress-1>', self._tree_pressed)
        self.tree_3.bind('<Leave>', lambda e: self.top_3.withdraw())
        # 表格设置
        # print(table, lan_sort)      # 7列 15行
        self.tree_1.configure(show='', selectmode='none', height=table[0])
        self.tree_2.configure(show='', selectmode='none', height=table[0])
        self.tree_3.configure(show='', selectmode='none', height=4)
        self.tree_1['columns'] = tuple([lan_sort[i] for i in range(table[1])])  # 7行，循环7次
        self.tree_2['columns'] = tuple([lan_sort[i] for i in range(table[1])])
        self.tree_3['columns'] = ('',)  # 列数
        self.items_1 = [self.tree_1.insert('', 'end', values='') for _ in range(table[0])]
        self.items_2 = [self.tree_2.insert('', 'end', values='') for _ in range(table[0])]
        self.items_3 = [self.tree_3.insert('', 'end', values='') for _ in range(4)]
        for i in range(1 + 1):  # 由于后面会进行行列交换，所以这里添的是列数
            self.tree_3.column('#%d' % i, width=button_max_width * 10 + 4)
        for i in range(table[1] + 1):  # 列头不像行头（不纳入计数），默认保留列头（#0），所以得加一，才能显示正确，不然最后一列无法配置width
            self.tree_1.column('#%d' % i, width=button_max_width * 10 + 4)
            self.tree_2.column('#%d' % i, width=button_max_width * 10 + 4)

        if lan_sort[-2] != lan_sort[-1]:  # 填补空白数据，使表格在后续处理中不会丢失数据
            lan_sort[-1].extend([' '] * (len(lan_sort[-2]) - len(lan_sort[-1])))
        table_list = tuple(map(list, zip(*lan_sort)))  # 行列交换
        # common_table_list = tuple(map(list, zip(*self.common_list)))
        # print(self.items_2, self.items_3)
        # table_list = [[row[i] for row in lan_sort] for i in range(len(lan_sort[0]))]
        for index, item in enumerate(self.items_3):
            self.tree_3.item(item, values=self.common_list[index])
            # print(self.common_list[index])
        for index, (item_1, item_2) in enumerate(zip(self.items_1, self.items_2)):
            self.tree_1.item(item_1, values=table_list[index])
            self.tree_2.item(item_2, values=table_list[index])
            # print(item_2, table_list[index])
        table_list[-2][-1] = '自动检测'  # 补充数据
        self.tree_1.item('I00E', values=table_list[-2])

        self.button_1.config(width=(button_max_width - 3) * 2)
        self.button_3.config(width=(button_max_width - 3) * 2)
        self.button_1.configure(command=self._button_menu_1)
        self.button_3.configure(command=self._button_menu_2)
        self.button_2.configure(command=self._swap_key)
        self.button_4.configure(command=self._button_translation)
        # self.root.attributes('-alpha')
        # self.root.attributes('-alpha', 0.8)   # 设置窗口属性，这里是设置透明度
        # 队列
        self.q = queue.LifoQueue(9)
        # self.q.put(list([proxy_main.run, None]))
        # Thread_0(self.q)

        # 这里开线程运行附加程序
        # list_script = (startup_script, '', self._text_1_show)
        # self.q.put(list_script)
        # Thread_0(self.q)
        self._real_translation()

    # def _thread_update(self, e):  # 创建线程
    #     Thread_0(e)

    def _real_update(self, src_text):  # 加入数据到队列
        fun_list = (self._translator_word, src_text, self._text_1_show)
        self.q.put(fun_list)
        # print(threading.activeCount()) 获取线程数
        MyTread_0(self.q)

    def _swap_key(self):  # 交换语种
        a_var, b_var = self.all_var[1].get(), self.all_var[2].get()
        if a_var == '自动检测':
            a_var = '中文简体'
        if a_var == b_var:
            return
        a_var, b_var = b_var, a_var
        # 这里添加判断语种，根据情况是否put数据到队列
        self.button_1.config(text=a_var)
        self.button_3.config(text=b_var)
        self._real_update(self.text.get(0.0, END))
        sleep(0.1)

    def _real_translation(self):
        """实时翻译"""
        src_text = self.text.get(0.0, END)

        if not self._is_change(src_text):
            # print('产生变化')
            self._real_update(src_text)
        # print('dd%s无变化' % src_text)

        self.root.after(2500, self._real_translation)

    def _right_click(self, _):
        """右键事件,可能会添加激活控件再操作,已添加聚焦"""
        self.text_out.focus_set()
        text_txt = self.text_out.get(0.0, END)
        copy(text_txt)

    def _translator_word(self, string_var):  # 翻译
        """翻译"""
        # print('数据来了')
        if self._is_change(string_var) or string_var.strip() == '':  # 交换语种后与显示语种相同直接返回,字符为空也返回
            return

        # print('有谁', len(string_var.strip()), bool(string_var.strip() == ''))
        # return
        self.all_var[1].set(self.button_1['text'])
        self.all_var[2].set(self.button_3['text'])
        self.all_var[0] = string_var
        self._text_1_show('   \n IN translation...\n', 3.5, 3.5, ('GROOVE', 'font'))
        des_language, src_language = self.all_var[2].get(), self.all_var[1].get()
        src_1 = 'auto' if src_language == '自动检测' else self.language[src_language]
        # try:
        # print(string_var, '开始翻译了')
        des_string = google_tran(string_var,
                                 des_1=self.language[des_language],
                                 src_1=src_1).text
        self._text_1_show(des_string, style=('GROOVE', 'font_normal'))
        # except Exception as e:      # 异常处理
        #     self._text_1_show(e)

    def _is_change(self, src_text):
        """判断文本是否变化,判断语种是否改变, 无变化则返回真"""
        if src_text.strip() == self.all_var[0].strip() and self.all_var[1].get() == self.button_1['text']:
            if self.all_var[2].get() == self.button_3['text']:
                return True
        else:
            return False

    def _button_translation(self):
        """翻译按钮"""
        sleep(0.1)
        src_text = self.text.get(0.0, END)
        # print(src_text)
        if not self._is_change(src_text):
            self._real_update(src_text)
            # self.all_var[0] = src_text

    def _button_menu(self, event):
        button = event.widget
        sleep(0.6)
        in_button = button.winfo_pointerxy()
        sleep(0.2)
        out_button = button.winfo_pointerxy()
        if in_button != out_button:  # 在button中停留太短时间不展示菜单
            return
        self.foc_button = button
        menu_3_geometry = button.winfo_geometry()
        # print(menu_3_geometry, '在里面')
        if self.top_1.state() == 'withdrawn' and self.top_2.state() == 'withdrawn':
            x3, y3 = self._position(menu_3_geometry, self.top_3)
            self._set_top_windows(self.top_3, x3, y3)
            # sleep(2000)
            # self.top_3.withdraw()
            # print('正常', self.top_1.state(), self.top_2.state())

    def _button_menu_1(self):
        """按键菜单"""
        self.foc_button = self.button_1
        menu_1_geometry = self.button_1.winfo_geometry()
        x1, y1 = self._position(menu_1_geometry)
        self._set_top_windows(self.top_1, x1, y1)
        # root x + button x
        # print(self.top_1.winfo_geometry())

    def _button_menu_2(self):
        self.foc_button = self.button_3
        menu_2_geometry = self.button_3.winfo_geometry()
        x1, y1 = self._position(menu_2_geometry)
        self._set_top_windows(self.top_2, x1, y1)
        # print(x1, y1)
        # root x + button x

    def _set_top_windows(self, top, x1, y1):  # 设置窗口状态
        if top is self.top_1:
            self.button_1.state(['!pressed'])
        elif top is self.top_2:
            self.button_3.state(['!pressed'])
        top.geometry('+%i+%i' % (x1, y1))
        top.focus_force()
        top.deiconify()

    def _text_1_show(self, snap_string, x=0.0, y=END, style=tuple('GROOVE')):  # 刷新输出框
        self.text_out.configure(state=NORMAL)
        self.text_out.delete(x, y)
        self.text_out.grid(row=0, column=0, columnspan=4)
        self.text_out.insert(y, snap_string, style)
        self.text_out.configure(state=DISABLED)

    def _set_font(self, snap_string='   \n IN translation...\n'):  # 字体设置
        self._text_1_show(snap_string, x=3.5, y=3.5, style=('GROOVE', 'font'))

    def _lose_focus(self, event):  # 表格失去焦点
        if event.widget == self.top_1:
            self.top_1.withdraw()
            self.tree_1.state(['!pressed'])
        else:
            self.top_2.withdraw()
            self.tree_2.state(['!pressed'])

    def _position(self, widget_geometry, top_3=None):
        """计算语种表格位置"""
        menu_geometry = widget_geometry  # 按扭geometry
        root_geometry, top_geometry = self.root.winfo_geometry(), self.top_1.winfo_geometry()
        menu_position = [int(i) for i in split('[+x]', menu_geometry)]

        root_position, top_position = [int(i) for i in split('[+x]', root_geometry)], \
                                      [int(i) for i in split('[+x]', top_geometry)]
        child_window_x = root_position[2] + menu_position[2] + 9
        child_window_y = root_position[3] + menu_position[3] - top_position[1] + 31
        if top_3:
            top_3_geometry = top_3.winfo_geometry()
            top_position = [int(i) for i in split('[+x]', top_3_geometry)]
            # print(top_position)
            child_window_y = root_position[3] + menu_position[3] - top_position[1] + 31
            return child_window_x, child_window_y
        return child_window_x, child_window_y

    def _button_leave(self, e):
        x, y, widget_geometry = e.x, e.y, e.widget.winfo_geometry()
        widget_geometry = [int(i) for i in split('[+x]', widget_geometry)]
        if not 0 < x < widget_geometry[1] and not y < 0:
            if self.top_3.state() == 'withdraw':
                sleep(1)
            self.top_3.withdraw()
        # print(x, y, widget_geometry)

    def _tree_pressed(self, event):
        # self.top_3.withdraw()
        x, y, widget = event.x, event.y, event.widget
        item = widget.identify('item', 0, y)
        column = widget.identify('column', x, 0)
        tree_widget = widget.winfo_toplevel()
        item_values = widget.item(item)['values']

        tree_widget.withdraw()
        if not len(item_values):  # 点击到空白表格（行），返回
            return
        text = item_values[int(column[1]) - 1]  # 默认tkinter保留列头（#0），所以列数得减一
        if not text:  # 数据为空，返回
            return
        # button_widget = tree_widget.winfo_toplevel()
        # print(tree_widget, item_values, text)
        self.foc_button.config(text=text)
        bbox = widget.bbox(item, column)
        self._reveal_selection(text, bbox, widget)

    def _reveal_selection(self, text, bbox, tree):
        x, y, width, height = bbox
        # print(bbox)
        if tree == self.tree_1:
            canvas_ = self.canvas_1
            canvas_text = self.canvas_1_text
        elif tree == self.tree_2:
            canvas_ = self.canvas_2
            canvas_text = self.canvas_2_text
        else:
            canvas_ = self.canvas_3
            canvas_text = self.canvas_3_text
        self.font.measure(text)
        canvas_['background'] = 'SystemHighlight'
        canvas_.configure(width=width, height=height)
        canvas_.coords(canvas_text, width / 2 - 1, height / 2 - 1)  # 居中显示
        canvas_.itemconfigure(canvas_text, text=text)
        canvas_.place(in_=tree, x=x, y=y)


def start_gui():
    root = Tk()
    T_GUI(root)
    # print(d.tree_1.winfo_parent())
    # exit()
    root.mainloop()


if __name__ == '__main__':
    # pass
    # ahk_code = 'MsgBox Hello World!'
    # ahk_interpreter = pahk.Interpreter()
    # ahk_interpreter.execute_script(ahk_code)
    # import time
    # sleep(10)
#     # 启动数据库
#     server_lnk = os.path.abspath('.') + '/ssdb-bin-master/ssdb-server-1.9.4.lnk'
#     server_hinstance_0 = FindWindow(0, 'SSDB-SERVER-1.9.4')
#     if server_hinstance_0:
#         close_server = SendMessage(server_hinstance_0, WM_CLOSE, 0, 0)
#     server = ShellExecute(0, 'open', server_lnk, '', '', 1)  # 后台启动
#
#     # 启动脚本
    ahk_code = os.path.abspath('.') + '/bin/scripts/hotkey.ahk'
    ahk_interpreter = pahk.Interpreter()
    ahk_interpreter.execute_file(ahk_code)
    start_gui()
#
#     # 启动代理服务器
#     # proxy_main.run()
#     # 绘制UI
#     start_gui()
#     # 终止数据库
#     server_hinstance = FindWindow(0, 'SSDB-SERVER-1.9.4')  # 查找窗口并结束
#     r = SendMessage(server_hinstance, WM_CLOSE, 0, 0)  # 返回0，表明系统处理过这个消息，是不是你想要的结果就不一定了
#     # print(server_hinstance, close_server, 'dd')
