### opencourse-python-web项目学习总结

#### MySQL数据库的安装

##### MySQL的安装

[MySQL官网下载地址](https://dev.mysql.com/downloads/file/?id=471631)

需要注册一个oracle的账号才能下载。

**安装完以后会有一个弹窗，上面有数据库的访问密码，这个要记下来，可以在设置数据库的时候换成自己的密码。**


##### 设置环境变量 

安装完以后用命令行还跑不起来，因为找不到可执行文件，这个时候需要设置一下mysql的环境变量，设置方法如下：

```
1. 进入/usr/local/mysql/bin,查看此目录下是否有mysql

2. 执行vim ~/.bash_profile 将下面这个代码放到最后
	PATH=$PATH:/usr/local/mysql/bin
	然后esc退出编辑模式，然后输入 :wq（保存并退出）回车。
3. source ~/.bash_profile

```

##### 安装MySQL驱动

目前有两个驱动：

* mysql-connector-python：是MySQL官方的纯Python驱动

安装方式：pip install mysql-connector==2.1.4 如果不带版本号在mac上会有问题

* MySQL-python：是封装了MySQL C驱动的Python驱动

安装方式：pip MySQL-python

##### 运行MySQL

在命令行执行下面的命令：

```
mysql -uroot -p

```

需要输入密码，就是安装的时候的弹出框上面的密码。

登录成功后可以修改自定义的密码：

```
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('newpass');

```
[MySQL常用命令汇总](http://www.cnblogs.com/bluecobra/archive/2012/01/11/2318922.html)

