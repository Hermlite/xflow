from xflow.base import BaseFeature


class Cook(BaseFeature):
    name = "cook"

    def check(self):
        return True

    def run(self):
        print(f"{self.name} running")
