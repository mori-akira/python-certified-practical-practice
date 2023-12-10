# コマンドラインオプションを扱う
import argparse

parser = argparse.ArgumentParser(description='Example Command')
parser.add_argument('-s', '--string', type=str, help='string to display', required=True)
parser.add_argument('-n', '--num', type=int, help='number of times repeat', required=False, default=2)
args = parser.parse_args()

print(args.string * args.num)
