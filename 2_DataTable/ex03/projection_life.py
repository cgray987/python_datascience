from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    loads life expectancy and gdp and plots in scatter plot
    """

    life_expectancy = load("life_expectancy_years.csv")
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    year = '1900'
    gdp_1900 = gdp[year]
    life_1900 = life_expectancy[year]

    plt.scatter(gdp_1900, life_1900)
    plt.title(f"Life expectancy vs GDP in year {year}")
    plt.xscale("log")
    plt.xlabel("gross domestic product (per person)")
    plt.ylabel("life expectancy")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    # countries = life_expectancy['country'].values
    # for i, country in enumerate(countries):
    #     plt.annotate(country, (gdp_1900[i], life_1900[i]), fontsize=6)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
