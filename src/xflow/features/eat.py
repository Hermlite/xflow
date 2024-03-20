from xflow.base import BaseFeature


class Eat(BaseFeature):
    name = "eat"

    def check(self):
        return True

    def run(self):
        print(f"{self.name} running")
