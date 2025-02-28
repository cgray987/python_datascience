import time  # for clock
import shutil  # to get terminal size (width)


def f_time(time) -> str:
    """takes time in seconds, returns formatted string MM:SS"""
    min, sec = divmod(time, 60)
    return f"{int(min):02d}:{int(sec):02d}"


def ft_tqdm(lst: range) -> None:  # type: ignore
    """A function to generate a progress bar based on the given
    iterable (lst). Displays various percentage, bar, total size and timings

    Does not work well when terminal is smaller than 15 columns
    (but it doesn't crash ;)"""

    print_info = True
    total_items = len(lst)
    info_len = (len(str(total_items)) * 2) + 5
    start_time = time.time()
    terminal_buffer = 30
    terminal_width = shutil.get_terminal_size().columns - terminal_buffer
    progress_bar_width = terminal_width - info_len
    if terminal_width <= 15:
        print_info = False
        terminal_width = 1
        progress_bar_width = terminal_width

    for i, item in enumerate(lst, 1):
        iteration_size = int(i / total_items * progress_bar_width)
        time_since = time.time() - start_time
        speed = i / time_since
        finish_time = (total_items - i) / speed
        progress_percent = i * 100 // total_items

        if i % 10 == 0 or i == total_items:
            bar = "█" * iteration_size
            progress_bar = f"|{bar:<{progress_bar_width}}|"
            time_formated = f"{f_time(time_since)}<{f_time(finish_time)},"
            full_line = f"{progress_percent:3}%{progress_bar}"
            info = f" {i}/{total_items} [{time_formated} {speed:.2f}it/s]"
            if print_info:
                full_line += info
            print(f"\r{full_line:<{terminal_width - 1}}", end="", flush=True)
        yield item
