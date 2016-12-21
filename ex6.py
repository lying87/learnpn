x = "There are %d types of people." % 10 # 10 这个数字刚好插入 %d 
binary = "binary" # 成了字符串 become string
do_not = "don't" # 简写也可以写成 string
y = "Those who know %s and those who %s." % (binary ,do_not) #插入两项

print x  #直接输出
print y  #直接输出已经套好的字符串

print "I said: %r." % x   #字符串中再套字符串
print "I also said: '%s'." % y #字符串中再套字符串

hilarious = False #这里可以改成yes
joke_evaluation = "Isn't that joke so funny?! %r" #字符串中再套字符串

print joke_evaluation % hilarious #这里算不算套进

w = "This is the left side of ..."
e = "a string with a right side."

print w + e   #未解释中间为什么是+
