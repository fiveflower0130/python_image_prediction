import os
import logging
import datetime


class LoggerSingleton():
    __instance = None

    # Singleton的另一個寫法
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    # def __init__(self):
    #     if LoggerSingleton.__instance is not None:
    #         raise Exception('instance is exist')
    #     else:
    #         LoggerSingleton.__instance = Logger()

    # @staticmethod
    # def get_instance():
    #     if LoggerSingleton.__instance is None:
    #         LoggerSingleton()
    #     return LoggerSingleton.__instance


class Logger(LoggerSingleton):
    # class Logger():
    __logger = None
    __execution_path = os.getcwd()

    def __init__(self):
        self.__logger = logging.getLogger("logger")
        self.__logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s \t [%(levelname)s | %(filename)s | %(funcName)s:%(lineno)s ] -> %(message)s'
        )

        # %Y-%m-%d_%H_%M_%S
        logname = datetime.datetime.now().strftime("%Y-%m-%d.log")
        dirname = os.path.join(self.__execution_path, "log")

        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        fileHandler = logging.FileHandler(dirname + "/log_" + logname,
                                          encoding="utf-8",
                                          mode="a")

        streamHandler = logging.StreamHandler()

        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        self.__logger.addHandler(fileHandler)
        self.__logger.addHandler(streamHandler)

    def get_logger(self):
        return self.__logger


# s1 = Logger().get_logger()
# s1.info("test")
