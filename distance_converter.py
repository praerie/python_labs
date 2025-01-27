# Write a program that converts distances measured in kilometers to miles. 
# One kilometer is approximately 0.62 miles.

def km_to_mi_converter(km):
    conversion_factor = 0.62
    mi = km * conversion_factor
    return mi 

def main():
    print("[Kilometers to Miles Converter]")
    try:
        distance_to_convert = float(input("Enter a distance in kilometers: "))
        converted_distance = km_to_mi_converter(distance_to_convert)
        print(f"{distance_to_convert:.2f} km = {converted_distance:.2f} mi")
    except:
        print("Invalid distance entered.")

if __name__ == "__main__":
    main()
