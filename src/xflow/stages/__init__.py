STAGES = {}


def register(cls):
    print(f"register {cls} to {cls.name}")
    STAGES[cls.name] = cls()
    return cls
