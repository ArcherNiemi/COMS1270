def choose_cell_plan(number_of_messages,base_price_A,price_per_message_A,extra_charge_message_threshold_A,extra_charge_price_A,
                     base_price_B,price_per_message_B,extra_charge_message_threshold_B,extra_charge_price_B):
    
    final_price_A = calculatePlanPrice(number_of_messages,base_price_A,price_per_message_A,extra_charge_message_threshold_A,extra_charge_price_A)
    final_price_B = calculatePlanPrice(number_of_messages,base_price_B,price_per_message_B,extra_charge_message_threshold_B,extra_charge_price_B)

    if(final_price_A <= final_price_B):
        return "Plan A", final_price_A
    else:
        return "Plan B", final_price_B

def calculatePlanPrice(number_of_messages, base_price, price_per_message, extra_charge_message_threshold, extra_charge_price):
    final_price = base_price + price_per_message * number_of_messages

    if number_of_messages > extra_charge_message_threshold:
        final_price += extra_charge_price

    return final_price


def main():
    number_of_messages = 1200

    price_A = 30.00
    message_A = 0.08
    threshold_A = -1
    extra_charge_A = 0.00

    price_B = 45
    message_B = 0.03
    threshold_B = 1000
    extra_charge_B = 10.00

    plan_name, plan_cost = choose_cell_plan(number_of_messages,price_A,message_A,threshold_A,extra_charge_A,price_B,message_B,threshold_B,extra_charge_B)

    print(f"Number of messages: {number_of_messages}")
    print(f"Cheapest plan: {plan_name}")
    print(f"Cost: ${plan_cost:.2f}")

if __name__ == "__main__":
    main()