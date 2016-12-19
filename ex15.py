from sys import argv  # 传递给python脚本的命令行参数 [字符串]列表

script,filename = argv # 把 argv这个参数变量解包，将所有参数依次赋值给左边的变量
#前三行就是获取文件名的
txt = open (filename ) # 这是一个新命令

print "Here's your file %r:" % filename #打印了一小行
print txt.read() 
# 我们在txt上调用了一个函数，上面已经从open获得了一个file，
#它本身就会支持一些命令。它接收的命令的方式是一个句点（.），紧跟着你的命令。

print "Type the filename again:"
file_again = raw_input (">") # 在过程中需要输入的话，用raw_input（）。 >是简单的提示符。

txt_again = open (file_again ) #这是一个新命令。

print txt_again.read() #已经是上面读数的循环。