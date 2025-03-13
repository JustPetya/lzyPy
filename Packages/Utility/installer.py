import sys

class Installer:
    def __init__(self):
        if not self.in_venv():
            print("Not running inside virtual environment!")

    @staticmethod
    def in_venv(self) -> bool:
        return sys.prefix != sys.base_prefix

if __name__ == "__main__":
    print("Not able to run by itself at this point!")