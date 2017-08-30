#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import User,Blog,Comment

from transwarp import db

db.create_engine(user = 'root',password = 'lly880620',database = 'awesome')

# u0 = User(name = 'Test',email = 'test@163.com',password = '123456',image = 'about:blank')

# u0.insert()

# u1 = User(name = 'Test001',email = 'test001@163.com',password = '123456',image = 'about:blank')

# u1.insert()

# u2 = User(name = 'Test002',email = 'test002@163.com',password = '123456',image = 'about:blank')

# u2.insert()

# u3 = User(name = 'Test003',email = 'test003@163.com',password = '123456',image = 'about:blank')

# u3.insert()

# b1 = Blog(user_id = '001',user_name = 'lly001',user_image = '',name = '这是一条博客',sunmary = '总结的话',content = '这条博客是一条测试博客，为了测试web是否能正常显示数据库的内容啦啦啦啦啦啦啦啦啦啦啊啊',create_at = 'beijing')
# b1.insert()

# b2 = Blog(user_id = '002',user_name = 'lly002',user_image = '',name = '这是一条博客',sunmary = '总结的话',content = '这条博客是一条测试博客，为了测试web是否能正常显示数据库的内容啦啦啦啦啦啦啦啦啦啦啊啊',create_at = 'beijing')
# b2.insert()

# b3 = Blog(user_id = '003',user_name = 'lly003',user_image = '',name = '这是一条博客',sunmary = '总结的话',content = '这条博客是一条测试博客，为了测试web是否能正常显示数据库的内容啦啦啦啦啦啦啦啦啦啦啊啊',create_at = 'beijing')
# b3.insert()

# b4 = Blog(user_id = '004',user_name = 'lly004',user_image = '',name = '这是一条博客',sunmary = 'This is a goooooood blog content you know that why because i am a very good men hahahahaha',content = '这条博客是一条测试博客，为了测试web是否能正常显示数据库的内容啦啦啦啦啦啦啦啦啦啦啊啊',create_at = 'beijing')
# b4.insert()

# b5 = Blog(user_id = '005',user_name = 'lly005',user_image = '',name = '这是一条博客',sunmary = 'This is a goooooood blog content you know that why because i am a very good men hahahahaha',content = '这条博客是一条测试博客，为了测试web是否能正常显示数据库的内容啦啦啦啦啦啦啦啦啦啦啊啊',create_at = 'beijing')
# b5.insert()

# b6 = Blog(user_id = '006',user_name = 'lly006',user_image = '',name = '这是一条博客',sunmary = 'This is a goooooood blog content you know that why because i am a very good men hahahahaha',content = '这条博客是一条测试博客，为了测试web是否能正常显示数据库的内容啦啦啦啦啦啦啦啦啦啦啊啊',create_at = 'beijing')
# b6.insert()


c1 = Comment(blog_id = '001504063573197b263e28573bf409a99a5b71246c99fe9000',user_id = '008',user_name = 'curry',user_image = '',content = '这是我的评论哈哈哈哈哈哈',create_at = 'beijing')
c1.insert()

c2 = Comment(blog_id = '001504064273196941351df2882454eb490ea483c435dff000',user_id = '30',user_name = '勇士库里',user_image = '',content = '这是我的评论哈哈哈哈哈哈',create_at = 'beijing')
c2.insert()
c3 = Comment(blog_id = '001504064273196941351df2882454eb490ea483c435dff000',user_id = '11',user_name = '勇士克莱',user_image = '',content = '这是我的评论哈哈哈哈哈哈',create_at = 'beijing')
c3.insert()
c4 = Comment(blog_id = '001504064273196941351df2882454eb490ea483c435dff000',user_id = '35',user_name = '勇士杜兰特',user_image = '',content = '这是我的评论哈哈哈哈哈哈',create_at = 'beijing')
c4.insert()


# print 'new user id',u.id