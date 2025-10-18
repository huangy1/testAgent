def isLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("yes")
        return True
    else :
        print("no")

if __name__ == "__main__":
    isLeap(1900)
