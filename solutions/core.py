# -*- coding: utf-8 -*-

import util.initialization as init
import warmup
import arrays


def main():
   print(init.random_int_list()) 
   warmup.fizz_buzz(19)
   warmup.fizz_buzz()
   print(warmup.find_longest_single_char_substring("Hello world! Hi Julia!"))
   to_remove_duplicates_from = init.random_int_list(size = 10, upper_bound = 5, to_sort=True)
   print(to_remove_duplicates_from)
   print(arrays.delete_duplicates(to_remove_duplicates_from, version = 1))

if __name__ == "__main__":
    main()
