# TranslatorSpider

## 使用指南

本项目依赖了`pyhk`模块实现全局快捷键，该模块需要在本地安装，pypi上未发布，见借助项目列表。
由于`pyhk`模块很久无人维护(本项目使用时已经修改了一些bug，建议下载本项目带的`pyhk`模块)，如果自己直接到`pyhk`项目中下载模块的话请自行修改pahk.py中的open()函数中的encoding为'utf-8',
不然会报错，想更新autohotkey.dll的话可到[ahkdll-v1-release项目](https://github.com/HotKeyIt/ahkdll-v1-release)下载更新。

想要解除字数限制，请自行下载本项目支持的proxy池,放置在`TranslatorSpider`目录下，见目录结构。

**注意**：
    开启proxy池得先开启项目支持的数据库

## 安装指南

clone本项目或者手动下载:

```bash
git clone https://github.com/hhaoao/TranslatorSpider
```

解压项目中的pahk_Win32w-0.1.0.7z,在pahk目录下执行命令进行安装：

```bash
python setup.py install
```

`cd`命令到`requirements.txt`目录下安装本项目所有依赖包：

```bash
pip install -r requirements.txt
```

至此，本项目就可以运行了，开始执行`main.py`开始你的愉快翻译之旅吧。

## 主要功能
- 在输出框右键复制翻译内容。
- 窗口默认不前置。
- 鼠标停在语种按钮上会显示常用语种列表。


## 快捷键

`<Shift-Ctrl-q>`: 最小化/还原窗口(全局)

## 更新日志

1.新增语种选择; 2018.07.07

2.新增实时翻译; 2018.07.09

3.新增多线程工作模式，添加右键复制输出框内容，优化了UI细节；2018.07.10

~~4.解除字数限制，优化翻译请求逻辑，更改翻译快捷键为<shift-enter>; 2018.07.11~~

5.取消翻译快捷键，优化翻译请求逻辑，添加翻译中提示；2018.07.12

6.添加<ctr-q>最小化快捷键，优化翻译逻辑，修复按键BUG；2018.07.14

~~7.完善<ctr-q>快捷键，可还原窗口跟最小化窗口；2018.07.15~~

8.修改快捷键为<shift-ctr-q>,增加图标；2018.07.17

9.优化多线程逻辑，更新了翻译模块，添加错误提示，改菜单栏为表格式，优化了UI细节；2018.08.04

10.优化UI体验，添加常用语种列表选择；2018.08.11

## 目录结构
```cmd
TranslatorSpider       
    ├─proxy_pool-master   
    └─translate           
        ├─bin             
           ├─icon         
           └─scripts      
                └─hotkey.ahk
                          
```

## 借助项目

- [proxy_pool-master](https://github.com/jhao104/proxy_pool)
- [pyhk](https://github.com/MrSimonC/pahk)