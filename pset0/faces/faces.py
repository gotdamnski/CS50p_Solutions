def convert(string):
    string = string.replace(':)', '🙂')
    string = string.replace(':(', '🙁')
    return string


def main():
    sentence = input('')
    print(convert(sentence))

main()

