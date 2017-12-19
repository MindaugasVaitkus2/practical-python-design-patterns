from singleton_logger import Logger

myLogger = Logger("/var/log/singleton_logger.log")

myLogger.warn("This is your first warning!")