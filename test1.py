# 第一种是 将生成器对象生成的匿名函数转化成列表 ，匿名函数使用的是相同的内存空间。
# 转换成列表后，循环结束，命名空间里的i都为3
def multipliters():
    return [lambda x:i * x for i in range(4)]

print([m(2) for m in multipliters()])
