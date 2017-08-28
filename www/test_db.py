#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import User,Blog,Comment

from transwarp import db

db.create_engine(user = 'root',password = 'lly880620',database = 'awesome')

u = User(name = 'Test',email = 'test@163.com',password = '123456',image = 'about:blank')

u.insert()

print 'new user id',u.id