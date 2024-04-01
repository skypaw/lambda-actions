import argparse


def handler(context: argparse.Namespace):
    # lambda writing to the file
    with open('./output.json', 'w') as file:
        print(f"{context} in file")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("save json to outputs")
    parser.add_argument("string-input", dest="string-input", type=str, help="String will be written to output")

    args = parser.parse_args()
    handler(args)
