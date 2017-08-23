#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading functools

# 数据库引擎对象:
class _Engin(object):
	"""docstring for _Engin"""
	def __init__(self, connect):
		super(_Engin, self).__init__()
		self._connect = connect

	def connect(self):
		return self._connect()
		
engine = None

# 持有数据库连接的上下文对象

class _DbCtx(threading.local):
	"""docstring for _DbCtx"""
	def __init__(self):
		super(_DbCtx, self).__init__()
		self.connection = None
		self.transactions = 0

	def is_init(self):
		return not self.connection is None

	def init(self):
		self.connection = _LasyConnection()
		self.transactions = 0

	def cleanup(self):
		self.connection.cleanup()
		self.connection = None

	def cursor(self):
		return self.connection.cursor()

_db_ctx = _DbCtx()

class _ConnectionCtx(object):
	"""docstring for _ConnectionCtx"""
	def __enter__(self):
		global _db_ctx
		self.should_cleanup = False

		if not _db_ctx.is_init():
			_db_ctx.init()
			self.should_cleanup = True

		return self

	def __exit__(self,exctype,excvalue,traceback):
		global _db_ctx
		if self.should_cleanup:
			_db_ctx.cleanup()


def connection():
	return _ConnectionCtx()

def with_connection(func):
	@functools.wraps(func)
	def _wrapper(*args,**kw):
		with _ConnectionCtx():
			return func(*args,**kw)
		return _wrapper

class _TransactionCtx(object):
    '''
    _TransactionCtx object that can handle transactions.

    with _TransactionCtx():
        pass
    '''

    def __enter__(self):
        global _db_ctx
        self.should_close_conn = False
        if not _db_ctx.is_init():
            # needs open a connection first:
            _db_ctx.init()
            self.should_close_conn = True
        _db_ctx.transactions = _db_ctx.transactions + 1
        logging.info('begin transaction...' if _db_ctx.transactions==1 else 'join current transaction...')
        return self

    def __exit__(self, exctype, excvalue, traceback):
        global _db_ctx
        _db_ctx.transactions = _db_ctx.transactions - 1
        try:
            if _db_ctx.transactions==0:
                if exctype is None:
                    self.commit()
                else:
                    self.rollback()
        finally:
            if self.should_close_conn:
                _db_ctx.cleanup()

    def commit(self):
        global _db_ctx
        logging.info('commit transaction...')
        try:
            _db_ctx.connection.commit()
            logging.info('commit ok.')
        except:
            logging.warning('commit failed. try rollback...')
            _db_ctx.connection.rollback()
            logging.warning('rollback ok.')
            raise

    def rollback(self):
        global _db_ctx
        logging.warning('rollback transaction...')
        _db_ctx.connection.rollback()
        logging.info('rollback ok.')
		




