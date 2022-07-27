import argparse
import importlib

from typing import List

DAYS = [x for x in range(1, 26)]
UNSOLVED = [18, 19, 22, 24]


def parser_arguments():
    parser = argparse.ArgumentParser(description='AOC 2015 solutions')
    parser.add_argument('-d', '--day', type=int, help='Problem day')
    parser.add_argument('-i', '--input_file', type=argparse.FileType('r'), help='Problem input file')
    parser.add_argument('-a', '--all', action='store_true')
    parser.add_argument('-md', '--mark_down', action='store_true')
    return parser.parse_args()


def get_input_file(args):
    if not args.input_file:
        return open('data/day' + str(args.day))
    else:
        return args.input_file


def get_input_data(day):
    with open('data/day' + str(day)) as f:
        return read_puzzle_input(f)


def read_puzzle_input(file_descriptor) -> List[str]:
    return file_descriptor.read().splitlines()


def execute_problem(day, input_lines):
    if day in UNSOLVED:
        raise NotImplementedError('Solution is not yet implemented')
    if day in DAYS:
        obj = str_to_class(day)
        print_answer(day, obj(input_lines).solve())
    else:
        raise RuntimeError('Invalid Date Entered')


def print_answer(day: int, answer: (str, str)):
    print(f'Solutions for day {day} is {answer}')


def str_to_class(day):
    module_name = 'solutions.day' + str(day)
    class_name = 'Day' + str(day)
    return getattr(importlib.import_module(module_name), class_name)


def execute_all():
    for day in set(DAYS).difference(UNSOLVED):
        obj = str_to_class(day)
        print_answer(day, obj(get_input_data(day)).solve())


def print_all_markdown():
    print("| Day | Part 1 | Part 2 |")
    print("| --- | ------ | ------ |")
    for day in set(DAYS).difference(UNSOLVED):
        obj = str_to_class(day)
        answers = obj(get_input_data(day)).solve()
        print(f'| {day} | {answers[0]} | {answers[1]} |')


if __name__ == '__main__':
    args = parser_arguments()
    if args.all:
        execute_all()
    elif args.mark_down:
        print_all_markdown()
    else:
        execute_problem(args.day, read_puzzle_input(get_input_file(args)))
