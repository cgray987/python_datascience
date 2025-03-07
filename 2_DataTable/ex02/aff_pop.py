from load_csv import load
import sys
import matplotlib.pyplot as plt


def to_number(pop: str) -> float:
    """
    changes number ending in 'K', 'M' or 'B' to
    their appropriate numerical form
    """
    if pop.endswith('k'):
        return float(pop[:-1]) * 1e3
    elif pop.endswith('M'):
        return float(pop[:-1]) * 1e6
    elif pop.endswith('B'):
        return float(pop[:-1]) * 1e9
    else:
        return float(pop)


def main():
    """
    loads population_total.csv and
    plots graph of given countries or of
    Czech Republic vs United States
    if none are given
    """
    df = load("population_total.csv")
    if len(sys.argv) == 3:
        target = sys.argv[1].title()
        comparison = sys.argv[2].title()
    else:
        target = 'Czech Republic'
        comparison = 'United States'
    country_row = df[df['country'] == target]
    comparison_row = df[df['country'] == comparison]
    if country_row.empty or comparison_row.empty:
        print(f"Country '{target}' or {comparison} not found in the dataset.")
        return

    data = country_row.iloc[0, 1:]
    data_comp = comparison_row.iloc[0, 1:]
    years = country_row.columns[1:].astype(int)

    data_pop = data.values.flatten()
    comp_pop = data_comp.values.flatten()

    data_num = [to_number(x) for x in data_pop]
    comp_num = [to_number(x) for x in comp_pop]

    plt.plot(years, data_num, label=target)
    plt.plot(years, comp_num, label=comparison)

    plt.title(f"Population in {target} vs {comparison}")
    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.tight_layout()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

"""
    I added all of this before realizing I could let pyplot handle scaling
    max_num = max(max(data_num), max(comp_num))
    min_num = min(min(data_num), min(comp_num))
    scale = int(np.log10(max_num)) - 1
    print(scale)
    y_ticks = [i * 10 ** scale for i in
               range(int(min_num / 10 ** scale),
                     int(max_num / 10 ** scale), 3)]

    if scale >= 9:
        y_labels = ["{:,.0f}B".format(pop / 1e9) for pop in y_ticks]
    elif scale >= 6:
        y_labels = ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks]
    else:
        y_labels = ["{:,.0f}K".format(pop / 1e3) for pop in y_ticks]
    plt.yticks(y_ticks, y_labels)
"""
