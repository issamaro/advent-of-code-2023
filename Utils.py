def parse(i: str, sym: str) -> list:
    return i.split(sym)

if __name__ == "__main__":
    print(parse("hey\nBrother", "\n"))