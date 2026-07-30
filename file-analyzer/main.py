try:
    filename = input("Enter a file name ")
    with open(filename,"r") as file:
        data = file.read()
        lines_of = data.splitlines()
        word = data.split()
        empty_file = len(data)
        if empty_file == 0:
            raise ValueError("File is empty")
        print(len(lines_of))
        print(len(word))
except ValueError as e:
    print(e)
except FileNotFoundError:
    print("File not Founded")
