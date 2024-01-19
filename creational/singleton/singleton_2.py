def singleton(the_class):
    instances = {}

    def get_class():
        if the_class not in instances:
            instances[the_class] = the_class()
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self) -> None:
        self.tema = 'O tema escuro'
        self.font = '18px'


@singleton
class Teste:
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    as0 = AppSettings()
    print(as0.tema)
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema)

    t1 = Teste()
    t2 = Teste()
    print(t1 == t2)
    print(as0 == as1)
