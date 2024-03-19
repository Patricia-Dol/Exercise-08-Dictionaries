alphabet: str = "abcedfghijklmnopqrstuvwxyz"
keys: str = "22233344455566677778889999"

"""Convert a mnemonic into a phone number"""
# test

converter: dict[str, int] = {}

for i in range(len(alphabet)):
    converter[alphabet[i]] = int(keys[i])


def to_keys(mnemonic: str) -> str:
    newStr: str = ''
    for element in mnemonic:
        if element.isalpha():
            newStr += str(converter[element])
        else:
            newStr += element
    return newStr


def from_keys(key_sequence: str) -> str:
    """Convert a sequence of digits and pauses (represented by spaces) into text."""
    pass


if __name__ == "__main__":

    print("'(foo) bar-quuz' is: " + to_keys("(foo) bar-quuz"))
    print("'3 444 222 8 444 666 66 2 777 444 33 7777 2 777 33 2 9 33 7777 666 6 33' is: " + from_keys(
        "3 444 222 8 444 666 66 2 777 444 33 7777 2 777 33 2 9 33 7777 666 6 33"))
