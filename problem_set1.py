def main():
    blue()
    blastoff()
    candy_shop()

def blue():
    red = 3
    purple = red * 12
    print(purple)

def blastoff():
    count = int(input("can i have a number pretty please? "))
    for i in range (0, count):
        print(count-i)
    print("blastoff")

def candy_shop():
    candies = ["sour patch kids", "hershey's", "M&Ms"]
    candies.append("kitkat")
    candies.insert(1, "milky ways")
    candies.sort()

    for i in range (0, len(candies)):
        index_to_remove = 0
        if candies[i] == "kitkat":
            index_to_remove=i
    
    candies.pop(index_to_remove)
    print(candies)

    user_candies = []
    for i in range (0, 3):
        to_add = input("add a candy, please: ")
        user_candies.append(to_add)
    
    all_candies = candies
    for i in range (0, len(user_candies)):
        all_candies.append(user_candies[i])
    print(len(all_candies))
    
    for i in range (0, len(all_candies)):
        print(all_candies[i])

    return(1.25*len(all_candies))


if __name__ == "__main__" :
    main()