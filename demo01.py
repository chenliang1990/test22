"""
元祖的作用是用来装数据的，我们可以把数据装在元祖里面。
因为每个变量都是存在内存中的。所以放在元祖中取值比较快
元祖的方法：index()获取元素下标,count()统计元素个数
"""

"""
元祖不可以修改，数组可以修改
数组的方法:index()获取元素下标；count()统计元素个数；append()追加元素(只能追加一个值)；
extend()追加数组，实现数组的合并；insert()通过下标追加值；pop()取走数组里面的元素；
clear()清空数组里面的值；sort()对数组的排序，如果想对数组倒叙，使用sort(reverse=True)；
remove()删除数组里面的元素；del a[0]通过下标去删除数组里面的元素；

字典的方法：
get()取值；pop()取走字典里面的元素；keys()获取所有的key,并生成进数组中;
values()获取所有的value,并生成进数组中;
items()获取所有的(key,value),并生成进数组中;
a.update(name="李四"),可以把字典中的name的value值改为李四,name不用加引号,
因为里面的key充当变量，如果key存在就修改，如果不存在就新增
del a["name"],删除
"""


a = {"name" : "你好","sex" : [],"a" : 1}