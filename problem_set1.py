def main(): # main method yay
    blue()
    blastoff()
    candy_shop()
    fruit_pricing()

def blue(): # testing multiplication of int variables with color names
    red = 3
    purple = red * 12
    print(purple)

def blastoff(): # creating a countdown until blastoff starting at from an inputted value
    count = int(input("can i have a number pretty please? "))
    for i in range (0, count):
        print(count-i)
    print("blastoff")

def candy_shop(): # creating a list of candies in a candy shop
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

def fruit_pricing(): # creating a dictionary with different fruits and their corresponding costs
    fruits = {"apple":0.75, "banana":1.25, "orange":0.80, "peach":2.25, "coconut":2.80}
    fruits["pear"] = 1.15
    print(fruits.get("peach"))

    for fruit in fruits:
        if fruits.get(fruit) >= 1.25:
            print(fruit)

    print(3*fruits["apple"]+2*fruits["banana"]+fruits["coconut"])

if __name__ == "__main__" : # so we can run main method
    main()