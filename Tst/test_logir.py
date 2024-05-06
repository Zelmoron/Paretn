from pathlib import Path
import os
import sys
sys.path.append(Path(__file__).parent.parent)
from Src.settings_manager import settings_manager
from Src.Models.event_type import event_type
from Src.Logics.storage_observer import storage_observer
from Src.Models.log_models import log_type
from Src.Logics.start_factory import start_factory
from Src.Storage.storage import storage

import unittest


class test_logs(unittest.TestCase):

    def create_log(self):  
        #Подготовка
        unit=settings_manager()
        address=os.path.join(Path(__file__).parent.parent,'Jsons')
        unit.open('Test.json',address)
        item=start_factory(unit.settings)
        item.create()
        #действие 
        storage_observer.raise_event(event_type.make_log(log_type.log_type_debug(),"Проверяем","Тест"))
        #проверка
        assert len(item.storage.data[storage.logs_key()])!=0