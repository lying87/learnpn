# learnpn
####入学小任务思考过程

敲完17个.py文件之后，它们留在电脑的文件夹里，我怎么推送到远程仓库？

我早就注册了github账户，需要新库的时候，就直接在自己的github页面点击了 new repository,以为这样就完事了。结果发现这个新库和我本地存放17个py.文件的文件夹A联系不到一块。应该说我怎么把17个文件上传到网页上去呢？有点傻Q。继而我开始略微漫长的纠结之路。

那时候我有了第一个问题：我是不是应该把py.文件都放到本地仓库去，想办法把本地仓库和github仓库关联起来？

那么，本地仓库是啥？装着17个py.文件的A只是个普通文件夹而已。

至此，我明白得先创建版本库。也就是在本地建一个目录作为可以被git管理的仓库。

######建版本库
我先建一个空目录，名为learnpn。（learn python new）名字是随意取的。之前学习的命令行没有忘，就可以用起来：
> mkdir   learnpn
> cd  learnpn
> pwd  learnpn  (这样就会出现learnpn的位置)

######通过 git init 命令让learnpn变成可以让git 管理的仓库
> git init
Initialized empty Git repository in /Users/lying87/learnpn/.git/

你说对了git能懂的语言，它马上就帮你建好仓库了。learnpn由普通文件夹成了本地版本库。

######添加文件+提交文件
现在我就可以把文件夹A里的文件放进learnpn里。两步:git add 和 git commit -m
（git commit是命令，后面的-m 是用来注释的。）
> git add ex1.py ex2.py ex3.py ex4.py
> git commit -m ex1.py ex2.py ex3.py ex4.py
4 files changes,95 insertions(+)
create mode 100644 ex1.py
create mode 100644 ex2.py
create mode 100644 ex3.py
create mode 100644 ex4.py

######本地库关联远程库，推送
到这里我有点兴奋了。好像感觉已经看到作业上传完的曙光。
> git remote add origin git@github.com:lying87/learngit.git
> git push -u origin master

在这里遇到我的第二个问题：

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1565564-632b5cc2b8e51bf0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
我push了文件，在网页上没有如数出现，被吞了几个。等我弄清楚再补充。

我临时的解决方法是，看缺哪几个，就重推哪几个。：）

######从远程库克隆
以上法子是先有本地库，再关联远程库。
但其实，我已经建好了远程库。
一是刚开始先建的远程库，我可以直接克隆到本地。
二是我已经上传部分py.文件的远程库，也可以再克隆到本地。

我首先把本地库的文件，放回A中，然后把本地库删掉。重新从远程库（已有部分文件）克隆到本地。
> git clone git@github.com:lying87/gitskills.git

克隆成功之后，我就把远程仓库上缺的几个文件找出来，复制到本地，再推上去。

这里我有第三个问题：我文件在A夹（一个普通文件夹），克隆的本地库是learnpn(嘻我又用了同个名字：）)，是否一定要把文件从A复制到learnpn再推到远程库？还是能不能直接又把A改名为learnpn，再推到远程库？

#####完成作业
虽然只是涉及到敲打17个代码文件，和建仓库上传而已，但学习的过程已经过几次反复和困顿。最开心还是每一次解决问题，就能从电脑上得到快速而正面的反馈，真是太爽的体验了。
