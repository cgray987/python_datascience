from load_csv import load
import sys
import matplotlib.pyplot as plt


def main():
    """
    loads life_expectancy_years.csv and
    plots graph of given country or of
    Czech Republic if none is given
    """
    df = load("life_expectancy_years.csv")
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        target = 'Czech Republic'
    country_row = df[df['country'] == target]
    if country_row.empty:
        print(f"Country '{target}' not found in the dataset.")
        return

    years = country_row.columns[1:]
    data = country_row.iloc[0, 1:]

    plt.plot(years, data, label=target)
    plt.title(target + " life expectancy projections")
    plt.xlabel("year")
    plt.ylabel("life expectancy")
    plt.xticks(years[::40], rotation=45)
    plt.yticks(range(30, 90, 10))
    plt.tight_layout()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
