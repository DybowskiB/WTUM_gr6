from arima_model import prepare_data, train, calculate_mse_plot
import warnings


warnings.filterwarnings("ignore")

# Store_nbr in [1; 54]
# Product family in [0; 32]
print("ARIMA model store sales prediction")
store_nbr = family = iterations = -1
while (store_nbr < 1) | (store_nbr > 54):
    store_nbr = int(input("Enter store number ([1; 54]): "))
while (family < 0) | (family > 32):
    family = int(input("Enter family product number ([0; 32]): "))
while (iterations != 1) & (iterations != 2) & (iterations != 3) & (iterations != 4) & (iterations != 5):
    print("Level 1: 1 iteration [~5s]")
    print("Level 2: 10 iterations [~2min]")
    print("Level 3: 100 iterations [~25min]")
    print("Level 4: 200 iterations [~1h]")
    print("Level 5: 1000 iterations [~80h]")
    iterations = int(input("Enter number of iterations level (choose number [1-5]): "))
data = prepare_data(store_nbr, family)
result = train(data, iterations)
print("Chosen p, d and q values:", result[2], result[3], result[4])
calculate_mse_plot(result[0], result[1], True, store_nbr, family)
