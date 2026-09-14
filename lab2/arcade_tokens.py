def calculate_tokens(small_token_value,large_token_value,total_number_of_tokens,total_token_value):
    number_of_large_tokens = (total_token_value - small_token_value*total_number_of_tokens)/(large_token_value-small_token_value)
    number_of_small_tokens = total_number_of_tokens - number_of_large_tokens
    return number_of_small_tokens,number_of_large_tokens

def main():
    small_token_value = 5
    large_token_value = 25
    total_number_of_tokens = 30
    total_token_value = 510

    small_tokens, large_tokens = calculate_tokens(small_token_value,large_token_value,total_number_of_tokens,total_token_value)
    
    print(f"There are {small_tokens} small tokens, and {large_tokens} large tokens!")

if __name__ == "__main__":
    main()