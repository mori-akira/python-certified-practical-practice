# ログ設定
import logging

format = '%(process)s:%(thread)s %(asctime)s %(levelname)6s %(filename)12s:%(lineno)4d %(message)s'
logging.basicConfig(filename='log.log', filemode='a', format=format, level=logging.INFO)

logging.debug('debug log')
logging.info('info log')
logging.warning('warning log')
