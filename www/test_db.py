#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import User,Blog,Comment

from transwarp import db

db.create_engine(user = 'root',password = 'lly880620',database = 'awesome')

# u0 = User(name = 'Test',email = 'test@163.com',password = '123456',image = 'about:blank')

# u0.insert()

u1 = User(name = 'Test001',email = 'test001@163.com',password = '123456',image = 'about:blank')

u1.insert()

u2 = User(name = 'Test002',email = 'test002@163.com',password = '123456',image = 'about:blank')

u2.insert()

u3 = User(name = 'Test003',email = 'test003@163.com',password = '123456',image = 'about:blank')

u3.insert()


# print 'new user id',u.id