#
# The problem, find a number
#  compose of 10 digits
# each digit in place I species how many times digit I repeat itself
#

class Number:

    def __init__(self) -> None:
        super().__init__()
        self._digits: list[int] = [0] * 10

        # for each digit Di in place I _hist[I] is number of this Di
        self._hist: list[int] = [0] * 10  # all digits are 0
        self._hist[0] = 10
        self._sum: int = 0  # number of digits

    def solved(self):
        """
        Check that each digit Di in place i, number of i is Di
        :return:
        """

        if self._sum != 10:  # sum of digits must be 10
            return False

        for (i, d) in enumerate(self._digits):
            if self._hist[i] != d:
                return False

        return True

    def __str__(self) -> str:
        s = str(self._sum) + "   "

        for (i, d) in enumerate(self._digits):
            s += "[" + str(i) + "]" + str(d) + "/" + str(self._hist[i]) + " "

        return s

    def pure_str(self) -> str:

        s = ""

        for d in self._digits:
            s += str(d)

        return s

    def get_digit(self, d_index) -> int:
        return self._digits[d_index]

    def set_digit(self, d_index: int, d: int) -> int:
        """

        :param d_index:
        :param d:
        :return: the previous one
        """
        digits = self._digits
        hist = self._hist

        # unset it
        prev = digits[d_index]
        hist[prev] -= 1
        self._sum -= prev

        # set it
        digits[d_index] = d
        hist[d] += 1
        self._sum += d

        return prev

    def exceed(self) -> bool:
        """
        :return: True if accumulated number of digits > 10
        """
        return self._sum > 10


def rec_solve(n: Number, d_index: int) -> bool:
    """

    :param n:
    :param d_index: index of digit to start with, 0..9
    :return:
    """

    print(f"Checking @ {d_index} / {n}")
    if n.solved():
        return True

    if d_index == 0:
        return False  # can't try anymore

    d_index = d_index - 1

    prev = n.get_digit(d_index)
    for d in range(0, 10):

        n.set_digit(d_index, d)

        if n.exceed():
            # can't continue
            n.set_digit(d_index, prev)
            return False

        if rec_solve(n, d_index):
            return True

    n.set_digit(d_index, prev)
    return False


def solve():
    n: Number = Number()

    solved = rec_solve(n, 10)

    if solved:
        print(f"Solved: {solved} : {n.pure_str()}")
    else:
        raise RuntimeError("Unable to solve")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solve()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
