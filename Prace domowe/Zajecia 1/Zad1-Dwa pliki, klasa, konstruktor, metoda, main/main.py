import sys

sys.path.append(".")
from Konst import myClass


def main():
    newClass = myClass(5, 10,"Suma podanych liczb wynosi")
    val = newClass.getVal()


if __name__ == "__main__":
    main()
