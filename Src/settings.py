from Src.exceptions import exception_proxy, argument_exception
from Src.Logics.storage_observer import storage_observer
from Src.Models.event_type import event_type
from Src.Models.log_models import log_type
from datetime import datetime

#
# Класс для описания настроек
#
class settings():
    _inn = 0
    _short_name = ""
    _first_start = True
    _mode = "csv"
    _block_period = datetime.now
    __INN=""
    __account=""
    __BIK=""
    __name=""
    __property_type=""
    __report_type=""

    @property
    def inn(self):
        """
            ИНН
        Returns:
            int: 
        """
        return self._inn
    
    @inn.setter
    def inn(self, value: int):
        exception_proxy.validate(value, int)
        self._inn = value
         
    @property     
    def short_name(self):
        """
            Короткое наименование организации
        Returns:
            str:
        """
        return self._short_name
    
    @short_name.setter
    def short_name(self, value:str):
        exception_proxy.validate(value, str)
        self._short_name = value
        
        
    @property    
    def is_first_start(self):
        """
           Флаг Первый старт
        """
        return self._first_start    
            
    @is_first_start.setter        
    def is_first_start(self, value: bool):
        self._first_start = value
        
    @property
    def report_mode(self):
        """
            Режим построения отчетности
        Returns:
            _type_: _description_
        """
        return self._mode
    
    
    @report_mode.setter
    def report_mode(self, value: str):
        exception_proxy.validate(value, str)
        
        self._mode = value
    

    @property
    def block_period(self):
        """
            Дата блокировки периода
        """
        return self._block_period
    @property
    def INN(self):
        return self.__INN
    
    @property
    def account(self):
        return self.__account
    
    @property
    def BIK(self):
        return self.__BIK
    
    @property
    def name(self):
        return self.__name
    
    @property 
    def property_type(self):
        return self.__property_type
    
    @block_period.setter
    def block_period(self, value):
        legacy_period = self._block_period
        
        if isinstance(value, datetime):
            self._block_period = value
            
            if legacy_period != self._block_period:
                storage_observer.raise_event(  event_type.changed_block_period()  )    

            return

        if isinstance(value, str):
            try:
               self._block_period = datetime.strptime(value, "%Y-%m-%d")    
               if legacy_period != self._block_period:
                    storage_observer.raise_event(  event_type.changed_block_period()  )    
            except Exception as ex:
                raise argument_exception(f"Невозможно сконвертировать сроку в дату! {ex}")
        else:
            raise argument_exception("Некорректно переданы параметры!")
            
    @INN.setter
    def INN(self,value: str):
      
        value_stripped=value.strip().replace(' ','')

        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  argument_exception("Некорректный аргумент")
        
        #проверка на длинну
        if len(value_stripped)!=12:
            raise argument_exception("Некорректная длинна")
            
        storage_observer.raise_event(event_type.make_log(log_type.log_type_debug(),"изменение INN", "settings.py/INN"))
        self.__INN=value_stripped

    @account.setter
    def account(self,value:str):

        value_stripped=value.strip().replace(' ','')
   
        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  argument_exception("Некорректный аргумент")
        #проверка на длинну
        if len(value_stripped)!=11:
            raise argument_exception("Некорректная длинна")
            
        storage_observer.raise_event(event_type.make_log(log_type.log_type_debug(),"изменение account", "settings.py/account"))
        self.__account=value_stripped



        #проверка на длинну
        if len(value_stripped)!=11:
            raise argument_exception("Некорректная длинна")
            
        storage_observer.raise_event(event_type.make_log(log_type.log_type_debug(),"изменение correspond_account", "settings.py/correspond_account"))
        self.__correspond_account=value_stripped

    @BIK.setter
    def BIK(self,value:str):
        value_stripped=value.strip().replace(' ','')

        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  argument_exception("Некорректный аргумент")

        if len(value_stripped)!=9:
            raise argument_exception("Некорректная длинна")
            
        storage_observer.raise_event(event_type.make_log(log_type.log_type_debug(),"изменение BIK", "settings.py/BIK"))
        self.__BIK=value_stripped

    @name.setter
    def name(self,value:str):

        if not isinstance(value, str):
            raise argument_exception("Некорректный аргумент!")

        storage_observer.raise_event(event_type.make_log(log_type.log_type_debug(),"изменение name", "settings.py/name"))
        self.__name = value.strip()

    @property_type.setter
    def property_type(self,value:str):
        value_stripped=value.strip()
        if not isinstance(value,str):
            raise  argument_exception("Некорректный аргумент")
        
        #проверка на длинну
        if len(value_stripped)!=5:
            raise argument_exception("Некорректная длинна")
            
        storage_observer.raise_event(event_type.make_log(log_type.log_type_debug(),"изменение property_type", "settings.py/property_type"))
        self.__property_type=value_stripped

    @block_period.setter
    def block_period(self,value:str):
        if not isinstance(value,str):
            raise  argument_exception("Некорректный аргумент")
        
        #проверка на указание даты со временем
        try:
            value=value.split(' ')[0]
            legacy=self.__block_period
            self.__block_period=datetime.strptime(value, "%Y-%m-%d")

            if legacy!=self.__block_period:
                storage_observer.raise_event(event_type.changed_block_period())
                storage_observer.raise_event(event_type.make_log(log_type.log_type_debug(),"изменение block_period", "settings.py/block_period"))

        except:
            storage_observer.raise_event(event_type.make_log(log_type.log_type_debug(),"изменение is_first_start", "settings.py/is_first_start"))
            self.__first_start=(str(value).lower()=='true')