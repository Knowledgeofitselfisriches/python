# python  
  ##  >life is short,i use python  """"-->gim
  ## 写作业时，先实现再优化
  ## 注意在一些问题可以自己解决请勿请教他人
  ## 注意请教其他人时，要谦虚
### 语言分类
    * 编译型语言
    会将源代码一次性翻译成机器码的可执行文件 c/c++
    1、执行快 
    2、平台限制
    * 解释型语言
    会将源代码每解释一句源代码就执行一句机器码 python/java
  
      1.跨平台
      2.执行慢
### 设计目标 
    * 简单直观 功能强大
    * 开源
    * 直观 易读 易懂
    * 适宜快速开发   
### 哲学
       * 优雅 工整
       * 明确 一个语句只做一件事
       * 简单 减少繁杂的语法  
          做一件事情，只用一种方法
### 优势
      * 代码少
      * 易读
      * 易学
      * 开源
      * 可移植性
      * 完全面向对象
      * 强大的标准库
         系统管理、网络通信、文本处理、数据库接口、图形系统、
         XML处理等
      * 丰富的第三方模块
         web开发、
         自动化运维
         网络爬虫
         数据分析、
         科学计算、
         人工智能、
         机器学习、
      * 可扩展性
         如果关键代码需要运行更快或需要保密可用c/c++写
### 缺点
       运行速度慢
       市场小
       缺乏中文资料
### [python官网](www.python.org)   
### error
       * SyntaxError invalid
       * NameError   name is not defined 标识符拼错 或 为 None
       * IndentationError upecpected indent 
       * IndexError   索引
       * TypeError 参数不对
       * AttributeError : 属性错误
       * AssertionError : 断言失败
       * UnBoundLocalError 为绑定的本地错误
### 版本
    Python 2.0 默认不支持中文
       解决办法 开头加上 # -*- coding:utf-8 -*-  
    Python 3.0 支持中文
    命令 python2 的解释器执行命令 python
         pyhton3 的解释器执行命令 python3
    最后的2.x 2.7
### 解释器版本
       1、CPython 官方c语言
       2、JYthon      java平台
       3、IronPython  .net 和 Mono平台
       4、PyPy        Python  Jit即时编译
### 执行方式
       1. python file.py
       2. 交互式 cmd 中 python  >>> print('hello')
           小代码，验证某些事情 打开快 但不能保存代码  
           退出 ctrl c 或 exit()
   ** IPython 相比默认的Python shell **
      版本 ipyhton  2.0
           ipython3 3.0 
           * 自动补全
           * 自动缩进
           * 支持 bash shell
           * 内置许多功能和函数
           * 基于BSD开源
   3.pycharm   .idea 文件 会保存项目的相关信息 版本
## 正式学习python
### ptint(parameter1""parameterN )函数     
###  注释 标注说明 屏蔽不需要执行的代码
   
       * 单行注释 使用“#”
       * 块注释  实际是长字符串，只是无法输出
         '''
           注释内容
           
         '''
       * 注释要精简，到位
### 代码规范
      * 一句 80个字符
      * 一句 执行一个功能
      * space
### 算数运算符 + - * / // ** %
      注意 ** 是 有结合原理
           数字 * 字符串 = 重复n次字符串
### 比较运算符
         == 
            == 比较两个对象的value
            is 比较两个对象的 id(CPtython)
         >= 
         <= 
         > 
         < 
         !=
         比较字符串时，会逐个比较字母的unicode编码，
         第一个字母可排出大小则不会比较其它
        python 2 中 不等于可使用 <>        
#### 逻辑运算符 
        and 找 False 短路 优先级高于or 两个非布尔运算会返回原值   0 and 2 == 0  1 and 2 == 2
        or  找 True  短路                                         0 or  2 == 2  1 or  2 == 1
        not  
## 常量
        True
        False
        None
        NotImplemented未实现大额
        Pass 占位语句
        Ellipsis 省略
                
## 变量 
       python中的变量必须赋值 赋值才会创建
       如果不确定变量的值 可用Non来初始化
       python是动态类型语言 不需要指定类型
#### 变量的类型 
          ** 数字型
       1、整形（int） python 3 int 没有大小限制
          python 2 中 有int 和 long
          int 
          long 有L后缀
#### 进制表示  进制转换函数  
       十六进制   0x hex()
       八进制     0o oct()
       十进制     int(num,radix)
       二进制     0b bin() 
       
       2、浮点（float） 
       3、布尔型（bool） 底层实际是数字 
          True  真  1    
          False 假  0 
       4、复数型（complex） 
          主要用于科学计算
       数字性的变量之间可以直接计算 （隐式转换 bool-->int-->float-->conplex）     
      ------------------------------    ** 非数字型 ** ----------------------------------------
        公共方法
        len()
        dle()
        max()
        min()
        cmp(item1,item2)
        切片
        算数运算符
          1、+          字符串 元组 列表
          2、*           字符串 元组 列表
          3、in          字符串 元组 列表 字典
          4、not in      字符串 元组 列表 字典
          5、> < <= >= == != 字符串 元组 列表 
       5、字符串 (str)
          字符串变量之间使用+拼接字符串 （操作符重载）
          特殊使用 string * number = sting1""stringN
          *  长字符串  
          def f(a:int,b:str) -> str:
              '''
                 string
                 
              '''
          使用help函数会打印出相应的说明文档
          *  文档字符串
             '''
                
             '''
          *  原始字符串
          r"str " 它会忽略 \ 即将\变成\\ 但注意\不能出现\ 常用来保存路劲
          *   格式化字符串
             1、f"str { var }" ,
             2、'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
          * 占位符
          * 字节序列
            b"str" 生成字节序列对象bytearray  
          * utf-8码
            u"中文"   
            字符串的方法
            'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
             'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
             'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 
             'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
              'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
          
          1、str.format() 返回格式化的字符串
            new_str = 'hello {}'.format(str)
            fmt = '-{0}- -{1}- {0}- -{1}'.format(str1,str2) 可重复使用
            fmt = '{name},{age},{gender}'.format(name='rose',age=20,gender=male) 
            fmt = '{num:10}'.format(num=3)限制内容的宽度 设置打印的对齐 空格+内容 = 10
            fmt = '{num:.3f}'.format(num=3.141596)限制内容的宽度 输出小数后3位四舍五入
            fmt = '{:.3}'.format(‘3.141596’)限制内容的宽度 取字符串的3个 
            fmt = '{:.3}'.format(‘3.141596’)限制内容的宽度 取字符串的3个 
            fmt = '{:010.2f}'.format(‘3.141596’)限制内容的宽度为10位不足补零，取小数位2位
            fmt = '{:<10.2f}'.format(‘3.141596’)相对10个字符左对齐
            fmt = '{:>10.2f}'.format(‘3.141596’)右对齐
            fmt = '{:^10.2f}'.format(‘3.141596’)居中对齐
            fmt = '{:=^10.2f}'.format(‘3.141596’)居中对齐,=填充
            检查一个字符串是否是数字，是返回True
            isdecimal()  True : Unicode 只检查阿拉伯数字   
                         False 罗马数字,汉字数字 ① 
                         Error byte数字
            isdigit() True  Unicode数字 byte数字（单字节）,全角数字（双字节），罗马数字  ①
                      False 汉字数字 
            isnumeric()  True : nicode数字 ,全角数字（双字节），罗马数字  ①
                         False: 无
                         Error: byte数字（单字节）
            检查字符串的组成
            isspace() 是否只右空格 space \r \t \n
            isalnum（）是否只有数字或字母
            isalpha() 是否只由数字组成
            islower() 检查小写
            istitle() 检查标题
            isUpper() 检查大写
            
            
             
            查找
            startwith()
            endwith()
            index(sub,start,end) 返回sub出现的位置，没找到Error
            rindex（）
            find(sub,start,end) 返回sub出现的位置,没找到不报错返回-1
            rfind()
            
            
            分割
            spilt() 如不传参数 默认根据空格 缩进 换行拆分
            resplit('*',2)从右往左放
            连接
            join(iterable) 可迭代对象必须是字符串列表合并为一个字符串
            对齐方式
            center(widtn,[fillchar])
            ljust(widtn,[fillchar])
            rjust(widtn,[fillchar])
            去除空格
            strip（[char]）默认去除前后空格或前后指定的字符 可去除字符的组合
            rstrip()去除左边字符
            lstrip()去除右边字符
            大小写 用于比较两个字符串是否相同
            lower()
            upper()
            capitalize（）首字母大写
            swrapcase() 切换大小写
            title() 将每个单词首字母大写
            替换
            relace(old new count)
            other
            zfill(width) 指定宽度并填充0
            
            
            
       6、序列 sequence 
          * 可变序列 list set dict
          * 不可变序列 str tuple
   #### 列表类似数组 ,可存任意类型。也可用index操作
        index可以是负数 从-1开始
   #### 通用方法
         len（）  长度函数 len(list) = n 
         切片技术 [0:k]+[k:n] = [0:n] [开始，结束） 返回新列表
         [:n] 从0从到n
         [:]  复制原列表
         [k:] 从k取到n
          [:-1]  从0到-1
         如果index超过范围则只切到n  
         只能 从左往右走
         [::-1]反转
         [i:j:k]从 i 到 j  step = k
         max/min() 最大最小函数
         count(substr,start end) 计算子串出现的次数
         index(substr,str,end)   查找字串在str中第一次出现的位置 没有会报错
         find(substr,str,end)   查找字串在str中第一次出现的位置 没有不会报错
   ### 对于可变序列 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
        None   = list.append(elem) 在list 末尾追加elem
        None   = list.insert(index,elem) 在index位置插入elem
                 list.extend(otherList ) 用otherList向尾部来插入一组数据 效果与 list += otherl_list 且不改变原list的id值 
                 list *= n 将list重复n次， 不改变原有的list的id
        ps : 对于+= / *=中 技术叫增强赋值 是去改变对象而不是去赋值          
        target = pop(index)删除index位置的元素 如果没有 index 则删除尾部 并返回被删除的elem
                 remove(elem) 移除指定数据
                 clear () 清空列表
          **     del var 将变量从内存中删除
        统计
        len(list)
        list.count('str')
        排序
        sort() 升序 改变原有对象的顺序
        new_list = sorted() 会返回一个新的排序后的列表
        sort(reverse = True)
        reverse() 反转
        new_list = list.copy() 返回一组新的浅克隆list 
            
        替换  list[index] = "other"
   ### 对于tuple 一旦初始化就不能修改即只读
       7、元组 
            创建元组
            t = 1,2,3 ()可省略
            t = 1,
            t = (1,)
            index(elem )去元素的下标  count（） 统计计数
            原组很少遍历，因为其中存储的是不同的数据类型
            格式化字符串的（） 本质是一个tuple
            让列表不可修改，来保护数据
            zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组
            for k,v in zip(list1,list2)
   #### 相互转换  
            tuple() 与 list() 在tuple 于 list之间互转
   #### 序列的解构的封装
            t = 1,2
            a,b = t
            list = 1,2,3,4
            a,*b,c = list   同一个解构中，只能使用一个星号
            *a,b,c = list
            a,b,*c = list
            经常用于交换变量的位置
            a,b = b,a         
       8、字典 （dict）类似 键值对集合 字典是映射 mapping的具体实现
       注意定义字典，可分行，不用理会缩进
          key是唯一的 是任意的不可变对象
          创建方式
          1.dic = {'name': "John","age":20}
          2.dict(name='john',age = 28.gender= 'male')
          3.dict([('one',1),('two',2)])
          4.dict(zip([key],[value])) 
          检查用in key
          删除
          del d['name']
          pop('name',default) 当删除的吗，目标是不存在的，会右default显示
          popitem（） 删除最后一项，返回一元组
          添加
          setdefault('adress','花果山'):向字典中添加数据，如果键存在则返回值，否则插入key返回default 默认为None
          update('adress','花果山')
           len(dict) 计算长度
           update() 合并字典
           clear() 清空字典
          遍历的方法
          keys（） 
          values（） 
          items（） 
          iter（） 返回一个itertor
          clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
          1.用in 判断是否有key "name" in dict
          2.通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
            dict.get("undefined",-1) 返回-1
          与list相比 以空间换取时间
          1、查找和插入的速度极快，不会随着key的增加而变慢；
          2、需要占用大量的内存，内存浪费多。
           
       set 无序且无重复元素的集合 与添加顺序无关
        'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update',
         'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
          创建方式
          s = {1，2，3，4，5，6，2，3}  
          s = set([1,2,3,2,4,2,3]) = {1,2,3,4}
           set.add(elem)
           删除
           set.remove(elem)   如果元素不存在，会保错
           set.discard(elem)  如果元素不存在，则不会报错
           set.clear(elem)  
           set.pop(elem) 
         可进行数学意义上的取交集并集
           a | b  并集   
           a & b  交集
           a - b  差集
           b - a 
           a ^ b 获取 a - b | b - a
                 
         
       每个Object都有 id type value print(object.value)  
   ### 作用域 global 
        注意 python 中没有块级作用域 
        搜索顺序 规则 LEGB
        1、局部作用域 locals
            locals()查看局部变量，返回一个 dict 叫局部命名空间  dict = { 'var': value  }
        2、enclosing 
            num = 1
            def outer():
                num = 10
                def inner():
                    num = 100
        3、全局作用域 globals
        4、内部命名作用域    builtins
        如果需要修改不在自己作用定义变量的值，如在函数中进行 var += 1 操作会报错 
        global var  声明使用全局的定义变量
        var += 1
        nonlocals var 声明使用上一层函数的定义的变量
   ### 格式化字符串
   ### 编码 string.encode('utf-8')    
   ### 类型转换 
       int(numStr,radix) 将合法的数值字符串或其它数字型转为整形
       对于非数字类型，转换时将会报错
       float()
       str() 对用户友好 与 repr()对python 解释器友好 且 可以使用eval（）函数重新得到对象  object = eval(repr(object))
             ascii 与 repr()相似 返回一个表示对象的字符串,   ascii/repr('hello') = "'hello'"  
             str("hello") = 'hello' 

       bool() 可接受任意类型 可将任意空性类型转为False
   ### 格式化字符串
       d = 10 f = 3.0 s = 'abc'
       '%d,%f,%s,%%'%(d,f,s) 输出 10 3，0 abc %
       %d 整形  %06d 显示6位 不足补零
       %f 浮点型 %.3f 取小数点后3位
       %s 字符串
       %% %   
   ### 标识符命名
   ####规则
        * 由 数字、下划线、数字组成            
        * 不能以数字开头            
        * 不使用关键字
          查看keyword
           import keyword
           print(keyword.kwlist)
           判断是不是关键字iskeyword
        * 尽量避开函数名
        * 使用变量单词都小写字母用下划线隔开
        * 类名的每个单词首字母都大写
        * 等号左右应保持一个space
        * 区分大小写
   ## 条件判断
   ### if 结构 
       if express: statement
       if express:           
          statement1      
          statement2
       if express:
          statement1   
          statement2
       else:
          statement1   
          statement2           
       if express:
          statement1   
          statement2
       elif express:
          statement1   
          statement2           
       else:
        一个分支只执行一次，注意死代码 条件范围小的写再前面
   ### 代码块
       以: 开头 以空格表示{ }
       缩进恢复之前的状态，表示代码块结束 
   ###  pass
			- pass可以用来占位 是空语句，是为了保持程序结构的完整性。  
            
   ### 随机数 random
       random.randint(a,b) 包含[a,b]
   ### 流程控制
           1、顺序
           2、分支
           3、循环  循环的初始值 循环的条件 执行步进 
              while 条件表达式 :
				语句""
			  else :
				语句""  
			  - break
			    - 用来退出当前循环

              - continue	
                - 用来跳过当次循环	
              for var in sequence :
                  语句
              else:        
              
   ## ps: #!/usr/bin/env python 会去调用path目录下寻找解释器     
   ### 编码问题
      ascii 只支持 128位字符 1个字节
      unicode 为支持ascii以外的字符而诞生 2个字节，但如果传英文也使用 unicode 太占空间
      uyf-8  可变长编码     
      获取单个字符的编码 ord("a") 获取字符 chr()   
      Unicode表示的str通过encode()方法可以编码为指定的bytes
   ## 函数 封装了完成某个功能的代码块
   ### 定义函数
        def my_abs(x):
            if not isinstance(x, (int, float)):
                raise TypeError('bad operand type')
            if x >= 0:
                return x
            else:
                return -x   
   ##### 数据类型检查 isinstance(x, (int, float)) 检查是不是（int float）元组的类型 不是返回 TypeError       
   ### 函数的参数 调用函数时，不会检查实参类型，注意检查类型
        1、必选参数，
        2、默认参数 必须是不可变对象 str tuple int float complex  bool None  可变 list  dict set 在形参中直接赋值 reverse = False
                    注意如果默认值是可变对象，函数每次调用都会共用一个默认值 
                            def f(l=[]) 改进 def f(l) : if not l : l = []
            def printrect(height,width=None,reverse = False):
        3、可变参数 只能写一个*arg
            在形参中 *argu 会将传入的arg1,arg2,arg3,arg4打包成tuple
            在是实参中 * argument 解构 *list = list[0]..list[N]  
            def foo(x,*args,y=1): foo(1,2,3,4,5) x=1 arg=(2,3,4,5) y=1
            def foo(x,y=1,*args): foo(1,2,3,4,5) x=1 y=2 arg=(3,4,5)
            def foo(x，*arg，y) : 注意 y 必须在传实参命名y=1 
            总结可变参数不是最后一个参数，其他参数必须是命名参数或默认参数
        4.命名关键字参数 d defined 在传实参时，给要传递的实参命名，可以无视形参命名的顺序而传递正确的参数比如print("",end="")
        5、关键字参数 
          实参:**kw  如果agruments为dict（） *dict 解构为键 ， **dict（） 解构为value
          形参: **argu 会将命名实参，打包为一个字典 注意**argu必须写在最后
           特殊用法
             def f(*,a,b) ==> f(a=1,b=2) 第一个形参为* ，那么之后的形参必须使用命名关键字实参
        传递不是参数的值，而是参数的地址
   ### 函数的返回值    
   ### 函数的分类
       递归函数 
          定义出口
          出口靠近     
   ## 迭代
      d = {'a': 1, 'b': 2, 'c': 3}
      for key in d      
      for value in d.values()      
      for k,v in d.items()      
      for ch in str
   ### 判断是否可迭代
       from collections import Iterable
       isinstance('abc', Iterable) # str是否可迭代   
       给切片赋值的必须是个序列
       list[:]="123456"   
       普通index迭代   
       for i, value in enumerate(['A', 'B', 'C']):
       print(i, value)
   ### 迭代对象iterable
        * 一类是集合数据类型，如list、tuple、dict、set、str等；
        * 一类是generator，包括生成器和带yield的generator function。    
   ## 模块 即.py文件
      import 模块名 as 别名
      from 模块 import function as 别名
       
   ## 列表生成式
      [x * x for x in range(1, 11)  if x % 2 == 0]]  [4,16,"",x^2]
      
      [m + n for m in 'ABC' for n in 'XYZ']
      
      import os # 导入os模块，模块的概念后面讲到
      [d for d in os.listdir('C:')] # os.listdir可以列出文件和目录
      
      d = {'x': 'A', 'y': 'B', 'z': 'C' }
      for k, v in d.items():
      print(k, '=', v)
      
      d = {'x': 'A', 'y': 'B', 'z': 'C' }
      [k + '=' + v for k, v in d.items()]
      ['y=B', 'x=A', 'z=C']     
      
      [s.lower() for s in L]
   ##  生成器 减少列表生成式的内存空间白白浪费   不懂
     1、 g =（x*x for x in range(1,11)）
       寻找下一个 next(g)
       循环for n in g :
             print(n)  
      
     2、定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：  
     yeild关键字类似于contiue 观察下列程序
       def odd():
            print('step 1')
            yield 1
            print('step 2')
            yield(3)
            print('step 3')
            yield(5)
        o = odd()
        next(o)
        next(o)
        next(o)   
        每次调用next 都会打断下面的执行 ，下次调用就会接着打断之后的执行
       def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            a, b = b, a + b
            n = n + 1
        return 'done'   
        g = fib(6)
        while True:
         try:
             x = next(g)
             print('g:', x)
         except StopIteration as e:
             print('Generator return value:', e.value)
             break    
   ## 迭代器 itertor   不懂
        from collections import Iterator 
        isinstance((x for x in range(10)), Iterator) == True
     注意:生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
        iter() 将list、dict、str 转为Itertor
        Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
     直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
     只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
     Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
   ## 内建函数
        import builtins 
        dir(builtins)
        help（） 查看函数类的使用说明
        数学运算
        abs()
        sum()
        min()
        pow(x,y) == x ** y
        max()
        round(num,n)保留num四舍五入小数后n位
        
        setattr() setattr(x, 'foobar', 123) = x.foobar = 123
        getattr() 
        hasattr()
        delattr()
        
        any() 检查elem 是否不为空 
        all() 检查所有elem 中是否有为空
        dir() 列出所有的属性和方法
        类型转换
        hex() 转换为16进制
        oct()
        bin()
        int()
        str()
        list()
        tuple()
        iter()
        bool()
        float()
        
        next() 取回下一个item
        slice() 可复用的切片模式
             list[slice(start stop step)] = list[start stop step]  
        divmod(m,n) 返回 m//n m % n     
        id()
        type()
        
        complex() 创建复数
        object() 返回一个新的无特征对象
        dict()
        set() 创建一个集合 set无序排序且不重复，是可变的 不存在哈希值 基本功能包括关系测试和消除重复元素 有add remove方法
        frozenset() frozenset是冻结的集合，它是不可变的，存在哈希值 作为key 一旦创建就不可变 ，没有add 等操作方法
        
        sorted()
        
        ascii() 返回一个可打印的对象字符串方式表示，如果是非ascii字符就会输出\x，\u或\U等字符来表示
        repr() 生成适合解释器阅读的字符串，可被eval()执行 
        str() 生成适合打印的字符串，可能无法被eval执行
        
        enumerate(iterable, start=0) 默认从0开始遍历iterable
            def enumerate(sequence, start=0):
                n = start
                for elem in sequence:
                    yield n, elem
                    n += 1
        input()
        classmethod()
        staticmethod() 将一个方法转为静态方法
        eval(expression) 执行字符串表达式 eval('1+1')
        exec(expression) 执行字符串代码  exec('print("hello")')
        open() 打开文件流
        isinstance()
        
        ord(char)  返回char的unicode编码
        chr(ord)   返回ord代表的unicode的字符         
        
        bytearray('str',encoding) mttable sequence 可变序列[0-255] 根据字符编码str生成字节数组
        bytes() 返回值为一个新的不可修改字节数组，每个数字元素都必须在0 - 255范围内，是bytearray函数的具有相同的行为，
                    差别仅仅是返回的字节数组不可修改
        compile() 函数将一个字符串编译为字节代码
                str = "for i in range(0,10): print(i)" 
                c = compile(str,'','exec')
                exec(c)
        高级函数
        filter() 
        map() map（None,list） 返回原有的list
        list(map(lambda x:x*x,range(1,11)))
        list(map(lambda x:x+5 if x <20))
        issubclass()
        print() 打印
        callable()
        format()
        len()
        property()
        range()
        zip() 打包
        vars()
        命名空间是一个字典用来记录变量的轨迹 key= 变量名 value = 变量值
        每个函数都有自己的命名空间，叫局部命名空间
        每个模块的全局命名空间
        locals()
        globals()
        
        supper()
        reversed() 返回一个新的反向的序列
        hash() 获取hash值
        memoryview()
        
        
        
   ## 高阶函数 一个函数可以接收另一个函数作为参数，这种函数就称之为高阶函数。
       我们可以给函数起别名以方便调用
       判断一个对象是否是函数 
       hasattr(func,'__call__')
       callable
       内置高阶函数 
        sort(iterable,reverse=False,key=function) list,str
        sorted()
        max()
        min()
        map()
        reduce()
        filter(function,iterable)
        
   ### map(fun args)/reduce
        map 接收传入两个参数 第一个参数为要调用的function ，第二个参数为需计算的数，注意接收的结果为Iterator是惰性序列，
            因此通过list()函数让它把整个序列都计算出来并返回一个list。
        def f(n):
        return n*n
        r = map(f,[1,2,3])
        print(list(r))
           这种做法比循坏去计算更加的直观 如：将数字列表转为字符数组list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])) 
        reduce： reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
           将函数作用于x1,x2 返回 result  再f（f(result x3),x4）
        如果执行求和 
           '''
            def add(a,b):
                return a+b
            r = reduce(add,[x for x in range(1,11)])
            print(r)
           '''
   ###   filter()函数用于过滤序列
        filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。  
        过滤列表保留奇数
        '''
            def is_odd(n):
                return n & 1 == 1
            print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))) 
            list(filter(lambda x :x & 1,[1,2,2,3,5,4,2,56,7]))
        '''
   ### sorted()  接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
        sorted([36, 5, -12, 9, -21], key=abs,reverse=True) 
                
   ### 返回值函数
    '''
        def lazy_sum(*args):
            def sum():
                ax = 0
                for n in args:
                    ax = ax + n
            return ax
        return sum   
        f = lazy_sum(1, 3, 5, 7, 9)
        f()
    '''
       当我们需要的，只是将参数传入，而不必立即得出结果，只在需要时执行，可使用类是js中colsure的技术
    在   函数内部嵌套函数，内部函数引用了局部变量。当外部函数接收参数，并返回内部函数的引用。此时内部函数
    保存着相关参数和变量，这里也被称之为closuer
       def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

    f1, f2, f3 = count()
 ### 匿名函数 lambda 表达式 
       f = lambda argument : expression
       f = lambda n : n & 1 ==1
       L = list(filter(f, range(1, 20)))   
 ### 闭包
     def out():
        a = 1
        def in():
            print(a)
        return in
     特点
      1、函数内嵌函数
      2、内部函数引用外部函数的变量
      3、返回内部函数成为全局变量   
     1.可访问局部变量 局部变量存于__closure__ 变量中             
     2.延迟调用
     3.外部函数执行返回内部函数到更高层次中，外部函数不会被回收 
 ### 装饰器 需强化练习
     在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）    
     1.不改动原函数
     2.动态的增加功能，需要包装的就装饰
     
     def now():
        print('now')   
     def log(func):
        print('1')
        def wrapper(*args, **kw):
             print('3')
            print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper
         print('2')
     1、原始实现   
     now = log(now) = @log()
     now()   
     2、@语法
     @log
     def now():
         print('2015-3-25')
     now()   
     多个装饰器会按顺序执行 谁离函数最近谁先执行
     3、选择执行
     flag = True
    def log(f):
        if flag:
            def wrap():
                print('call %s():' % f.__name__)
                return  f()
            return wrap
        else:
            return f
    @log
    def now():
        print('%d'%time.time())
    
    4.类装饰器
    5.多个装饰器执行顺序 
      Decorator2,Decorator1,wrqp1,wrqp2,def
    6.装饰器带有参数
      # 装饰器本身有参数
        # def outer(name):  # name="胡歌"
        # 	def decoration(func):
        # 		def packing(*args,**kwargs):
        # 			func(*args,**kwargs)
        # 		return packing
        # 	return decoration
        # # 1. decoration = outer("胡歌")  打印：  2.say = decoration(say)
        # @outer("胡歌")
        # def say():
        # 	print("say hello")
        # say()          
 ### 偏函数
       需求 在int(x,base) 函数中将大量的str 按二进制数据转换时，十分的不方便
       我们可定义def int2(x,base = 2): return int(x,base) int2 = lambda x base=2: int(x,base) int2即是偏函数       
       导入functools 定义int2 = functools.partial(int, base=2)  即可
 ## 模块 module
 ### package 包
        每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，
    而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompan        
 ###  Python 模拟的程序入口
     一个 Python 源码文件除了可以被直接运行外，还可以作为模块（也就是库）被导入。不管是导入还是直接运行，最顶层的代码都会被运行           
     if __name__ == '__main__'：
        test()               
 ### 可被直接应用的private 变量 _ _ Xxx _ _习惯性写法    
 ## 对象和类 封装 继承 多态
 ### 类
        --。class ClassName(extend):
            class Student()
                def __init__(self, name, score):
                    self.name = name
                    self.score = score
                def print_score(self):
                    print('%s: %s' % (self.name, self.score)) 
                def get_grade(self):
                    if self.score >= 90:
                        return 'A'
                    elif self.score >= 60:
                        return 'B'
                    else:
                        return 'C'      
        使用class 关键字+类名（首字母大写）+（父类（默认object））
       --。 创建实例      
            me = Student('jhon',20)
       --. 类方法 
           第一个参数永远是self,如同其它语言中的this，代表的是调用者或者创建者，其它参数类似普通函数
       --。访问限制
           给属性加上 _ _ Xxx,再通过get_xxx 和set_xxx方法进行访问，这样可对参数做出修改。如判断类型，范围
                set_grade(grade) if grade >100 : return -1
           注意 _ _ xxx 是private 变量 
                _ _ xxx _ _    ，特殊变量是可以直接访问的\
  ### 继承
       baseclass  object
       superclass class Animate(object)
       subclass   class Dog(Animal) 
       class Animal(object):
            def run(self):
                print('animal is running')
       class Dog(Animal):
            def run(self):
                print('dog is running')
       class Cat(Animal):
            def run(self):
                print('cat is running') 
  ### 多态  注意鸭子问题
       def ex(ani):
            ani.run()
       ex(cat)
       ex(dog)
       注意 鸭子问题  当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”
       class Duck(object):
            def run(self):
                print('like a duck')
       ex(duck)  
       不关注类型的继承，只关注行为
       让一个类表现像一个list，让len() 函数作用于自定义类，类必须提供__len__()的实现
       
  ### 判断类型
       isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。优先使用isinstance()
       检查指定类型及其子类 效率高于type，用于判断某个已知类型
       type 不可以判断某个类是否继承与另一个 用于打印未知类型     
       总结 
           type主要用于获取未知变量的类型 
           isinstance主要用于判断A类是否继承于B类
  ## 面向对象
       pyhton是动态语言，所以类方法不必直接定义在类中，python允许我们动态绑定给class 加上类方法
     1、  Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
       使用方式：
              class ClassName():
                   __slots__ = (*arguments)  
       注意该属性不会限制其子类对象对子类的修改
     2、 封装，为了不让类属性的被随便更改，使用私有变量，同时提供getter,setter 方法供外界访问
     也可以对私有变量进行值类型和范围的判断
         为了简便的使用getter与setter 方法 使用@property 装饰器
            给getter方法加上@property  get_xxx 改为 xxx
            给setter方法加上@xxx.setter  set_xxx 改为 xxx
         就让该属性向普通的公有属性一样访问了
            object . xxx = y;
  ### 多重继承 Mixin设计
     思想 单继承，多实现 主线是单一继承的，功能通过多继承实现额外添加 如果方法重名则先继承覆盖后面的
     Runable(){}
     Flyable(){}
     Eatable(){}
     Dog(Animal,Runable,Eatable)
     Bird(Animal,Flyable,Eatable)
  ### 高度定制类  不懂   
     总结:
        特殊方法 描述对象的行为
        基本定制型
        C.__init__(self[, arg1, ...]) 初始化对象
        C.__new__(cls,*args,**kwargs) 构造器 新建一个对象时第一个执行开辟内存
          return superClass/object.__new__(cls,*args,**kwargs) python 2.x
          return superClass/object.__new__(cls) python 3.x
          没有正确返回当前类cls的实例，那__init__()将不会被调用，即使是父类的实例也不行 
          class Singleton(object):
              def __new__(cls, *args, **kwargs):
                  if not hasattr(cls, '_instance'):
                      cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instanc
        C.__del__(self) 解构器
        C.__str__(self) 可打印的字符输出；内建str()及print 语句输出
          
          return [x for x in object.__dict__]
        C.(self) 交互式模式运行时的 输出对象 默认使用repr；内建repr() 和‘‘ 操作符
        C.__unicode__(self)b Unicode 字符串输出；内建unicode()
        
        C.__call__(self, *args) 表示可调用的实例 让对象像函数一样执行
          class Base():
            def __call__(self,path):
                print(path)
          base = Base()
          base('http://www.baidu.com')      
        C.__nonzero__(self) 为object 定义False 值；内建bool() （从2.2 版开始）
        C.__len__(self) “长度”（可用于类）；内建len()
        
        特殊方法 描述
        对象（值）比较c
        C.__cmp__(self, obj) 对象比较；内建cmp()
        C.__lt__(self, obj) and 小于/小于或等于；对应<及<=操作符
        C.__gt__(self, obj) and 大于/大于或等于；对应>及>=操作符
        C.__eq__(self, obj) and 等于/不等于；对应==,!=及<>操作符
        属性
        C.__getattr__(self, attr) 获取属性；内建getattr()；仅当属性没有找到时调用
          obj[attr] 
        C.__setattr__(self, attr, val) 设置属性
          obj['attr'] = val 触发
        C.__delattr__(self, attr) 删除属性
        C.__getattribute__(self, attr) 获取属性；内建getattr()；总是被调用
        C.__get__(self, attr) （描述符）获取属性
        C.__set__(self, attr, val)  （描述符）设置属性
        C.__delete__(self, attr)  （描述符）删除属性
        c.__dict__() 属性字典
        c.__class__
        定制类/模拟类型
        数值类型：二进制操作符
        C.__*add__(self, obj) 加；+操作符
        C.__*sub__(self, obj) 减；-操作符
        C.__*mul__(self, obj) 乘；*操作符
        C.__*div__(self, obj) 除；/操作符
        C.__*truediv__(self, obj)  True 除；/操作符
        C.__*floordiv__(self, obj)  Floor 除；//操作符
        C.__*mod__(self, obj) 取模/取余；%操作符
        C.__*divmod__(self, obj) 除和取模；内建divmod()
        C.__*pow__(self, obj[, mod]) 乘幂；内建pow();**操作符
        C.__*lshift__(self, obj) 左移位；<<操作符
        特殊方法 描述
        定制类/模拟类型
        数值类型：二进制操作符
        
        C.__*rshift__(self, obj) 右移；>>操作符
        C.__*and__(self, obj) 按位与；&操作符
        C.__*or__(self, obj) 按位或；|操作符
        C.__*xor__(self, obj) 按位与或；^操作符
        数值类型：一元操作符
        C.__neg__(self) 一元负
        C.__pos__(self) 一元正
        C.__abs__(self) 绝对值；内建abs()
        C.__invert__(self) 按位求反；~操作符
        数值类型：数值转换
        C.__complex__(self, com) 转为complex(复数);内建complex()
        C.__int__(self) 转为int;内建int()
        C.__long__(self) 转为long；内建long()
        C.__float__(self) 转为float；内建float()
        数值类型：基本表示法（String）
        C.__oct__(self) 八进制表示；内建oct()
        C.__hex__(self) 十六进制表示；内建hex()
        数值类型：数值压缩
        C.__coerce__(self, num) 压缩成同样的数值类型；内建coerce()
        C.__index__(self)g 在有必要时,压缩可选的数值类型为整型（比如：用于切片
        索引等等
        
        序列类型
        C.__len__(self) 序列中项的数目
        C.__getitem__(self, ind) 得到单个序列元素
        C.__setitem__(self, ind,val) 设置单个序列元素
        C.__delitem__(self, ind) 删除单个序列元素
        特殊方法 描述
        序列类型
        C.__getslice__(self, ind1,ind2) 得到序列片断
        C.__setslice__(self, i1, i2,val) 设置序列片断
        C.__delslice__(self, ind1,ind2) 删除序列片断
        C.__contains__(self, val) f 测试序列成员；内建in 关键字
        C.__*add__(self,obj) 串连；+操作符
        C.__*mul__(self,obj) 重复；*操作符
        C.__iter__(self)  创建迭代类；内建iter() 让其可用于for循环
        
        映射类型
        C.__len__(self) mapping 中的项的数目
        C.__hash__(self) 散列(hash)函数值
        C.__getitem__(self,key) 得到给定键(key)的值
        C.__setitem__(self,key,val) 设置给定键(key)的值
        C.__delitem__(self,key) 删除给定键(key)的值
        C.__missing__(self,key) 给定键如果不存在字典中，则提供一个默认值
        
         
        
        可以使用with关键字的类型，需要实现：
        
        __enter__ 和 __exit__

        iterator迭代器对象必须实现：
        
        __iter__ 和 next()
        
  ### 枚举类
     from enum import Enum
     Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))  
     for name, member in Month.__members__.items():
         print(name, '=>', member, ',', member.value)       value默认从1开始
     如果需要更加精细的控制value    需要自定义派生类
     from enum import Enum, unique
     @unique
     class Weekday(Enum):
        Sun = 0 # Sun的value被设定为0
        Mon = 1
        Tue = 2
        Wed = 3
        Thu = 4
        Fri = 5
        Sat = 6             
     uniquez装饰器可让我们保证值的唯一性
 ###  元类   
    type() 函数可查看类型或变量的类型，type(Animal) = 'type' type(ani) = 'Animal'
    定义类的方式
    1、class Animal(object): def run(self): print('Animal is running')
    2、type()函数除了可返回一个对象的类型外，还可以创建一个新类型
    def fn(self):
        print('Animal is running')
    Animal = type('Animal',(object,),dict(run=fn))
    我们先定义类，再创建对象
    ani = Animal()
    ani.run()
    高级定制 如果我们需要控制类的创建行为，使用metaclass控制 
        class ListMetaclass(type):
            def __new__(cls,name,bases,attrs):
                attrs['add'] = lambda self,value:self.append(value)
                return  type.__new__(cls,name,bases,attrs)
        class MyList(list,metaclass=ListMetaclass):
            pass
        l = MyList()
        l.add(1)
        print(l)
    使用metaclass ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，
    也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。 
 ## 异常处理
    try:
        print('语句')
    except ErrorType1 as e:
        print('except:', e)
    except ErrorType2 as e:
        print('except:', e)
    else:
        print('no error!')    
    finally:
        print('finally...')
    print('END')  
    错误类型都继承自BaseException，所以在使用except时需要注意的是，它捕获该类型及其子类的错误。如果error没被正确捕获
     会一层层的上报 直到python解释器捕获
 >>>     出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。
     还可以使用logging模块 打印error信息  再异常处理块中 logging.exception(e) 可让程序再打印完错误信息后，程序继续执行
 ### 自定义异常类
    class FooError(ValueError):
         pass       
    在需要抛出错误的位置   raise FooError('invalid value: %s' % s)使用raise 抛出该类的一个实例
    raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，
    还可以把一种类型的错误转化成另一种类型：
        except ZeroDivisionError:
            raise ValueError('input error!')
 ### 调试
    1、print()
    2、assert断言 assert n !=0 如果断言失败会报 AssertionError ,
        通过关闭断言可让解释器把assert当作pass处理
    3、logging 
       import logging
       logging.basicConfig(level=logging.INFO) 低于warning级别的就不输出了
            
            debug，info，warning，error BASIC_FORMAT CRITICAL FATAL
       logging.info()
    4、ide调试工具    
 ### 测试驱动开发”（TDD：Test-Driven Development）
 ## input or output
    1、通过open方法打开一个文件对象
    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)      
    file : 文件路径对象 
    mode : 操作模式  
        r default
        w
        +
        t default
        b 二进制模式
        a 追加
        |oprator | r    | r+   | w    | w+   | a    | a+   |
        | ---    | ----:| ----:|-----:|-----:|:----:|:-----|
        | read   | +    |   +  |      |   +  |      |  +   |
        | write  |      |   +  |   +  |   +  |   +  |  +   |
        | create |      |      |   +  |   +  |   +  |  +   |
        |Truncate|      |      |   +  |   +  |      |      |
        | head   | +    |   +  |   +  |   +  |      |      |
        | foot   |      |      |      |      |   +  |  +   |
       
    读写都可能出错所以需要异常处理，保证出错时正常关闭那个文件流
     try:
        f = open(url,mode)
        str = f.read()
     finally:
        if f:
            f.close()
     可以有更加简化的写法
        with open(url ,r ) as f:
            f.read()
     2、注意read()方法一次会读取所有内容，注意文件大小不要过大，或者反复调用read(size),或者调用readline()每次读取一行
     调用readlines()一次读取所有内容并按行返回list
        // TODO
     3、调用write(str)写入数据 注意windows的换行是\r\n
     
     调用tell() 返回当前读写指针所在的位置
     调用flush() 刷新文件内部缓冲
     调用 next() 返回文件下一行。
     
     调用seek（offset [,from]） 
            offset:要移动的字节数
            from: 0 开头 1 当前位置 2 结尾
    
 ### StringIO / BytesIO   操作内存数据   
        1、  StringIO 在内存中读写 str
            from io import StringIO
            f = StringIO()
            f.write("hello")
            print(f.getvalue())
            getvalue() 获取写入内存的str
        2、BytesIO 操作内存中的二进制
           f.write('中文'.encode('utf-8'))
          
 ### 操纵文件目录   Python内置的os模块也可以直接调用操作系统提供的接口函数。         
     查看操作系统基本类型 os.name = nt --windows posix -- 类 unix
 ####     导入os 模块执行文件处理       
        import os 
        调用rename(old,new) 重命名                              
        调用remove(file_name) 移除   
        调用mkdir( path ) 创建目录  
        调用chdir( path ) 修改路径
        调用getcwd()方法显示当前的工作目录。
        调用getcwd()方法显示当前的工作目录。
        调用 rmdir()方法删除目录，注意该目录下的文件必须先被清空
 ####  环境变量      
        os.environ 返回一个环境变量的字典 {‘PATH’: 值}
        os.environ.get('PATH')         
 #### 路径相关 os.path   
      如何正确的处理不同系统下的分割符问题
          abs = os.path.abspath('.')      查看当前目录的绝对路径
          new_path = os.path.join(abs, 'testdir')    如果要创建目录先将完整路径表示出来
          os.mkdir(new_path) 再创建相关的目录
      如何正确的拆分路径 os.path.split(path) 会将路径拆为两个部分，最后一个部分为最后一级文件，或目录
          path = '/Users/michael/testdir/file.txt'
          t = os.path.split(path) 
          t[1] 
      如何获得扩展名 os.path.splitext()可以直接让你得到文件扩展名 
          t = os.path.splitext()
          t[1]
       shutil模块提供了copyfile()的函数    可复制文件
 ### 序列化
    变量从内存中变成可存储或传输的过程称之为序列化 pickling
    变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
        import pickle/Json 
        d = {'name':'bob','age':20,'score':80}
        byt = pickle.dumps(d)   
    pickle.dumps(obj) 会将obj转化为二进制字符串存入内存中
    pickle.loads(byt) 会将obj转化为二进制字符串存入内存中
        with open(url,'wb') as f:
            pickle.dump(d,f)  
        with open(url,'rb') as f:
            print(pickle.load(f))      
    pickle.dump(obj,file) 会将  obj存入文件中
    pickle.load(file) 会 读取文件的信息
    
    注意Json.dump(obj)无法序列化自定义对象
    可选参数default就是把任意一个对象变成一个可序列为JSON的对象
    def studentodict(s):
        return {
            'name' : s.name,
            'age'  : s.age,
            'score': s.score
        }
     序列化自定义对象
         1、print(json.dumps(s,default=studentodict))
         2、print(json.dumps(s, default=lambda obj: obj.__dict__))
     反序列化自定义对象
        
        def dictostudent(d):
            return Student(d['name'],d['age'],d['score'])
        print(json.loads(str, object_hook=dictostudent))   
      
 ##  python 之 禅
    import this    
>>> intern 字符串驻留机制
      