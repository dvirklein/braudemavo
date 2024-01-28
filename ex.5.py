def main():
    firstchar = ord(input("Please enter a char:"))
    charafterchange = (((firstchar - ord('a')) + 1) % 26) + ord('a')
    print("Next letter is", chr(charafterchange))

main()