import time

def findFactors(number):
    factors = set()
    for i in range(1,number+1):
        if(number % i == 0):
            factors.add(i)
    return factors

def findFactorsFaster(number):
    factors = set() 
    for i in range(1,round(number**(1/2)+0.5)):
        if(number % i == 0):
            factors.add(i)
            factors.add(int(number/i))
    return factors

def main():
    start_time = time.perf_counter()
    print(sorted(findFactorsFaster(1_000_000_000_000_000_000)))
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(execution_time)


if __name__ == "__main__":
    main()