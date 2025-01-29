# The National Weather Service computes the windchill index using the formula:
# 35.74 + 0.6215T - 35.75(V^0.16) + 0.4275T(V^0.16)
# T — temperature in degrees F
# V — wind speed in mph

# Write a program that prints a formatted table of windchill values,
# with rows representing wind speed for 0 to 50 in 5-mph increments,
# and columns representing temperatures from -20 to +60 in 10-degree increments.
# The formula only applies for wind speeds in excess of 3 mph.

# calculate windchill
def windchill(T, V):
    return 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)

def main():
    # define temperature range (-20 to 60 in 10-degree increments)
    temperatures = list(range(-20, 61, 10))

    # define wind speed range (0 to 50 in 5-mph increments)
    windspeeds = list(range(0, 51, 5))

    # print header row
    print(f"{' ':<7}", end="") 
    for temp in temperatures:
        print(f"{temp:>7}", end="")
    print() # move to the next line

    # print table values
    for windspeed in windspeeds:
        print(f"{windspeed:<7}", end="") # print wind speed at start of row
        for temp in temperatures:
            if windspeed > 3: # formula only applies for wind speeds in excess of 3 mph
                wc = windchill(temp, windspeed)
                print(f"{wc:>7.2f}", end="") # windchill rounded to 2 decimals
            else:
                print(f"{'N/A':>7}", end="") # placeholder for wind speeds ≤ 3 mph
        print() # move to the next line

if __name__ == "__main__":
    main()
