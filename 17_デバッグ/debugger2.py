# breakpoint()関数でブレークポイントを挿入
import sys

def get_system_implementation():
    ret = sys.implementation
    breakpoint()
    return ret

def main():
    get_system_implementation()

if __name__ == '__main__':
    main()
