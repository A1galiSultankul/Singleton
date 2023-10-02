class Singleton:
    instance= None

    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance= super().__new__(cls)
        return Singleton.instance


    def _do_work(self):
        print("do some hard work")
        self.data = 101


if __name__=="__main__":
    first = Singleton()
    first._do_work()
    print(first)
    second = Singleton()
    print(second)
    print(first is second)
    print(first.data)
    first.data = 105
    print(second.data)
