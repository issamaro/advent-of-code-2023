import requests

SESSION_ID = "53616c7465645f5f32b8e7a7838ac83f734938c707a456e938e9dd4b9d981b30081f56c0c5e6d41e0451c4ca79401dea25c7192c55c6d79f9a06987e870bf9d8"
AOC_URL = "https://adventofcode.com/2023/day/1/input"


def main():
    input = requests.get(
        AOC_URL, cookies={"session": SESSION_ID}
    )
    print(input.text)
    
    
if __name__ == "__main__":
    main()