import dxpy


def max_duffel_bag_value(cake_tuples, weight_capacity):

    # we make a list to hold the maximum possible value at every
    # duffel bag weight capacity from 0 to weight_capacity
    # starting each index with value 0
    max_values_at_capacities = [0] * (weight_capacity + 1)

    for current_capacity in xrange(weight_capacity + 1):

        # set a variable to hold the max monetary value so far for current_capacity
        current_max_value = 0

        for cake_weight, cake_value in cake_tuples:

            # if a cake weighs 0 and has a positive value the value of our duffle bag is infinite!
            if cake_weight == 0 and cake_value != 0:
                return float('inf')

            # if the current cake weighs as much or less than the current weight capacity
            # it's possible taking the cake would give get a better value
            if cake_weight <= current_capacity:

                # so we check: should we use the cake or not?
                # if we use the cake, the most kilograms we can include in addition to the cake
                # we're adding is the current capacity minus the cake's weight. we find the max
                # value at that integer capacity in our list max_values_at_capacities
                max_value_using_cake = cake_value + max_values_at_capacities[current_capacity - cake_weight]

                # now we see if it's worth taking the cake. how does the
                # value with the cake compare to the current_max_value?
                current_max_value = max(max_value_using_cake, current_max_value)

        # add each capacity's max value to our list so we can use them
        # when calculating all the remaining capacities
        max_values_at_capacities[current_capacity] = current_max_value

    return max_values_at_capacities[weight_capacity]


@dxpy.entry_point("main")
def main(cakes, capacity):
    # cake_tuples = [(7, 160), (3, 90), (2, 15)]
    # capacity    = 20
    max_value = max_duffel_bag_value(cakes, capacity)

    return {"max_value": max_value}


if __name__ == "__main__":
    import sys
    sys.exit(int(main() or 0))
