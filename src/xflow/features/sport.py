from xflow.base import BaseFeature


class Sport(BaseFeature):
    name = "sport"

    def check(self):
        return True

    def run(self):
        print(f"{self.name} running")
