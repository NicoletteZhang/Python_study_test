# 定义装饰器，实现不同颜色显示执行结果的功能

# 1. 向装饰器传递参数，通过传递的参数获取到输出的颜色
# 2. 被装饰函数的print( )输出根据装饰器得到的颜色进行输出
import sys


def make_color(code):
    def decorator(func):
        def color_func(s):
            if not sys.stdout.isatty():
                return func(s)
            tpl = '\x1b[{}m{}\x1b[0m'
            return tpl.format(code, func(s))
        return color_func
    return decorator


@make_color(33)
def fmta(s):
    return '{:^7}'.format(str(float(s) * 1000)[:5] + 'ms')