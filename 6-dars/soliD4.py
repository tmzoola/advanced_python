

import time

class TerminalPrinter():
    def write(self, msg):
        print(f"{msg}")

class FilePrinter():
    def write(self, msg):
        with open('log.txt', 'a+', encoding="UTF-8") as file:
            file.write(f"{msg}")
            

class Logger:
    
    def __init__(self) -> None:
        self.prefix = time.strftime('%Y-%B-%d %H:%M:%S', time.localtime())
    
    def log(self, message, object_class):
        object_class().write(f"{self.prefix} --> {message}")

        
        
logger = Logger()
logger.log("Hello World", FilePrinter)
logger.log("Hello World", TerminalPrinter)