from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def main():
    for _ in tqdm(range(333)):
        sleep(0.005)
    print()

    for _ in ft_tqdm(range(333)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    main()
