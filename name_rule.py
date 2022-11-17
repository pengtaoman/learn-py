_observers = []
__observers = []


def add_observer(observer):
    _observers.append(observer)


def get_observers():
    """Makes sure _observers cannot be modified."""
    return tuple(_observers)


if __name__ == "__main__":
    _observers = [1,2323]
    print(_observers)
    print(get_observers())