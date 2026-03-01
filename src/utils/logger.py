import logging
from colorlog import ColoredFormatter

# 自定义日志格式并添加颜色
formatter = ColoredFormatter(
    "%(asctime)s.%(msecs)03d %(log_color)s%(levelname):s%(reset)s %(name)s:%(lineno)d: %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': "green",
        'WARNING': "yellow",
        "ERROR": "red",
        'CRITICAL': 'bold_red',
    }
)

# 配置根日志
handler = logging.StreamHandler()
handler.setFormatter(formatter)

# 获取根日志记录器并添加处理器
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
root_logger.addHandler(handler)


def get_logger(name: str):
    return logging.getLogger(name)
