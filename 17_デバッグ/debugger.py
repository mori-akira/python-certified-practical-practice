# デバッガを挿入
import sys
import pdb

def get_system_implementation():
    result = sys.implementation
    pdb.set_trace()
    return result

def main():
    get_system_implementation()

if __name__ == '__main__':
    main()
