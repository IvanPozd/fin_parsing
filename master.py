from earning import main_earning
from fs_stock import main_fs_stock
from most_recommended import main_most_recommended
from wall import additional_wall, main_wall
import time


def master():
    start = time.time()
    main_earning()
    main_fs_stock()
    main_most_recommended()
    main_wall()
    additional_wall()
    print("Script time ", time.time() - start, " seconds")


if __name__ == "__main__":
    master()
