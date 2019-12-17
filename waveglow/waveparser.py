import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--check', action='store_true')
parser.add_argument('--data', action='store_true')

parser.add_argument('--file', type=str, default=None)
parser.add_argument('--outf', type=str, default='test_files.txt')
args = parser.parse_args()

if (args.check):
    print("Checking...")
    assert(args.file is not None)

    file = open(args.file, 'r', encoding='utf-8-sig')
    data = file.readlines()
    file.close()

    for i in range(len(data)):
        if not os.path.exists(data[i]): print(data[i])

if (args.data):
    print("Splitting data...")
    assert(args.file is not None)

    file = open(args.file, 'r', encoding='utf-8-sig')
    data = file.readlines()
    file.close()

    file = open(args.outf, 'w', encoding='utf-8-sig')
    for i in range(len(data)):
        dir = data[i].split('|')[0]
        file.write(dir+'\n')
    file.close()
