import os
import json
from constants import INTERVAL_OPTS
from data_fetchers.coin_data_fetcher import COINS_DATA_PATH
from strategies.examples import ThreeEmaStochRsi
from use_local_data import use_local_data
from strategy_tester import StrategyTester


RESULTS_FOLDER = ".\\test_results"

def main():
    strategy = ThreeEmaStochRsi
    new_dir_path = RESULTS_FOLDER + "\\" + strategy.__name__

    if not os.path.isdir(new_dir_path):
        os.mkdir(new_dir_path)

    for interval in INTERVAL_OPTS:
        coins_data = use_local_data(interval, COINS_DATA_PATH)
        strat_tester = StrategyTester(strategy, coins_data, interval=interval)
        analysis = strat_tester.get_analysis()
        print(interval, analysis["daily_increase_percentage"], analysis["total_amount"], analysis["starting_amount"])

        with open(new_dir_path + f"\\{interval}.json", "w") as f:
            json.dump(analysis, f, indent=4)

        strat_tester.save_plot(new_dir_path + f"\\{interval}.png")


if __name__ == '__main__':
    main()

