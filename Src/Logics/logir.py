from Src.errors import error_proxy
from Src.Storage import storage
from Src.Logics.storage_observer import storage_observer
from Src.Models.event_type import event_type
from pathlib import Path
class logir:
    __storage=None
    __log=None
    __save_path=Path(__file__).parent.parent/"storage"/"saved_models"/"logs.txt"
    __save_path_json=Path(__file__).parent.parent/"storage"/"saved_models"/"logs.json"

    def __init__(self) -> None:
        self.__storage=storage()
        storage_observer.observers.append(self)

    def _create_log(self,type:str,text:str,source:str):

            self.__log=error_proxy(text,source)
            self.__log.log_type=type
            print(list(self.__storage.data.keys()))
            self.__storage.data[storage.logs_key()].append(self.__log)
    def handle_event(self,event:str):
        splitted=event.split(" ")
        if splitted[0]==event_type.make_log_key():
            self._create_log(splitted[1],splitted[2],splitted[3])
            self._save_log()

    
    