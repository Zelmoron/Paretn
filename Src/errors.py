import json
from datetime import datetime
#
# Класс для обработки и хранения текстовой информации об ошибке
#
class error_proxy:
    __period=None
    __type=""
    """
    Текст с описанием ошибки"""
    __error_text=""
    __error_source=""
    __if_error=False


    def __init__ (self, error_text: str="", error_source:str=""):
        self.__period=datetime.now()
        self.source=error_source
        self.text=error_text

    @property
    def text(self):
        return self.__error_text


    
    @text.setter
    def text(self,value:str):
        if not isinstance(value,str):
            raise Exception("Error")

        
        if value.strip()==" ":
            self.__if_error=False
            return 0
    @property
    
    def source(self):
        return self.__error_source

    
    @source.setter
    def source(self,value:str):
        if not isinstance(value,str):
            raise Exception("Error")

        if value.strip()==" ":
            self.__if_error=False
            return 0
        
    
    @property
    def error(self):
        """
            Получить текстовое описание ошибки
        Returns:
            str: _description_
        """
        return self._error_text
    
    @error.setter
    def error(self, value: str):
        if value == "":
            raise Exception("Некорректно переданы параметры!")
            
        self._error_text = value
        
    @classmethod
    def set_error(self, exception: Exception):
        """
            Сохранить текстовое описание ошибки из исключения
        Args:
            exception (Exception): входящее исключение
        """
        
        if exception  is None:
            self._error_text = ""
            return
            
        self._error_text = "Ошибка! " + str(exception)    
            
    @property        
    def is_empty(self) -> bool:
        """
            Флаг. Есть ошибка
        Returns:
            bool: _description_
        """
        if len(self._error_text) != 0:
            return False
        else:
            return True       
        
    def clear(self):
        """
            Очистить
        """
        self._error_text = "" 
        
    @staticmethod    
    def create_error_response( app,  message: str, http_code: int = 0):
        """
            Сформировать структуру response_class для описания ошибки
        Args:
            app (_type_): Flask
            message (str): Сообщение
            http_code(int): Код возврата

        Returns:
            response_class: _description_
        """
        
        if app is None:
            raise Exception("Некорректно переданы параметры!")
        
        if http_code == 0:
            code = 500
        else:
            code = http_code
        
        # Формируем описание        
        json_text = json.dumps({"details" : message}, sort_keys = True, indent = 4,  ensure_ascii = False)  
        
        # Формируем результат
        result = app.response_class(
            response =   f"{json_text}",
            status = code,
            mimetype = "application/json; charset=utf-8"
        )    
        
        return result
    
    @property
    def period(self):
        return self.__period


    @property 
    def log_type(self):
        return self.__type


    @log_type.setter
    def log_type(self,value:str):
        if not isinstance(value,str):
            raise Exception("Error")
        self.__type=value
            