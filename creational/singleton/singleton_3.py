from typing import Any


class Singleton(type):
    _intances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._intances:
            cls._intances[cls] = super().__call__(*args, **kwds)
        return cls._intances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        self.tema = 'Escuro'


if __name__ == '__main__':
    as1 = AppSettings()

    as1.tema = 'Qualquer outra coisa'

    as2 = AppSettings()
    as3 = AppSettings()

    print(as3.tema)
    print(as1 == as2)
    print(as1 == as3)
    print(as2 == as3)
