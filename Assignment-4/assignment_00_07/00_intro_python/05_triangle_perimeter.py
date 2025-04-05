def main():

    side1 = float(input("\033[1;3m Enter the first side of the triangle: \033[0m"))
    side2 = float(input("\033[1;3m Enter the second side of the triangle: \033[0m"))
    side3 = float(input("\033[1;3m Enter the third side of the triangle: \033[0m"))

    perimeter = side1 + side2 + side3
    print(f"\033[1;3m The perimeter of the triangle is: {perimeter} \033[0m")


if __name__ == "__main__":
    main()