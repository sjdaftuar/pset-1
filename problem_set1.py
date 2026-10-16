def main():
    blue()
    blastoff()

def blue():
    red = 3
    purple = red * 12
    print(purple)

def blastoff():
    count = int(input("can i have a number pretty please? "))
    for i in range (0, count):
        print(count-i)
    print("blastoff")

if __name__ == "__main__" :
    main()