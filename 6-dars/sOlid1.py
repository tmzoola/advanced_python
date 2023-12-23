
import time


class Logger:
    
    def __init__(self) -> None:
        self.prefix = time.strftime('%Y-%B-%d %H:%M:%S', time.localtime())
    
    def log(self, message):
        print(f"{self.prefix} -->{message}")
        
class CustomLogger(Logger):
    def __init__(self) -> None:
        super().__init__()
        self.prefix = time.strftime('%Y-%B-%d ', time.localtime())
        
        
logger = CustomLogger()
logger.log("-Soat Minut Sekund kerak emas")