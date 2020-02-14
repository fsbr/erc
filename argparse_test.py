import argparse

# here would be my convert funciton
def task_a(alpha):
    print("task a", alpha)

# here woudl be my options functions
def task_b(beta, gamma):
    print("task b", beta, gamma)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser")

    parser_a = subparsers.add_parser("task_a")
    parser_a.add_argument(
        "-a", "--alpha", dest="alpha", help="Alpha Description")

    parser_b = subparsers.add_parser("task_b")
    parser_b.add_argument(
        "-b", "--beta", dest="beta", help="Beta Description")

    parser_b.add_argument(
        "-g", "--gamma", dest="gamma", default=42, help="Gamma Description")

    # this puts all the arguments into a stack and then calls the functions
    # vars puts these as global variables i think
    kwargs = vars(parser.parse_args())

    # then pops the lits of kwargs and rus them
    globals()[kwargs.pop('subparser')](**kwargs)

