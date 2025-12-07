import argparse


def greet(name: str) -> str:
    """Return a greeting addressed to the provided name.

    Raises:
        ValueError: If the given name is empty.
    """
    if not name:
        raise ValueError("Name must not be empty.")
    return f"Hello, {name}!"


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Greet someone by name.")
    parser.add_argument("name", help="Name to greet")
    return parser.parse_args(argv)


def main(argv=None) -> None:
    args = parse_args(argv)
    print(greet(args.name))


if __name__ == "__main__":
    main()
