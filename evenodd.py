def evenandodd(num):
    if num%2 == 0:
        return "Even number"
    else:
        return "Odd number"

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Even and Odd result is: ", evenandodd(num))