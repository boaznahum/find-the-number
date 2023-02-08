#
# The problem, find a number
#  compose of 10 digits
# each digit in place I species how many times digit I repeat itself
#
# History
# attempt is checking if number is ok
# without _sum_by_count # attempts = 12457
# with _sum_by_count # attempts = 1210  5156 when starting from right
# Find all - #1428 attempts, find single solution


class Number:

    def __init__(self) -> None:
        super().__init__()
        self._digits: list[int] = [0] * 10

        # for each digit Di in place I _hist[I] is number of this Di
        self._hist: list[int] = [0] * 10  # all digits are 0
        self._hist[0] = 10
        self._sum: int = 0  # number of digits

        # d0 + d1 + d2 ... d9 = count(0)*0 + count(1)*1 + ... count(9) * 9 =
        #  = d0 * 0 + d1 * 1 ... + d9 * 9
        self._sum_by_count = 0

    def solved(self):
        """
        Check that each digit Di in place i, number of i is Di
        :return:
        """

        if not (self._sum == self._sum_by_count == 10):  # sum of digits must be 10
            return False

        for (i, d) in enumerate(self._digits):
            if self._hist[i] != d:
                return False

        return True

    def __str__(self) -> str:
        s = str(self._sum) + " " + str(self._sum_by_count) + "   "

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

        #  = d0 * 0 + d1 * 1 ... + d9 * 9
        self._sum_by_count -= prev * d_index

        # set it
        digits[d_index] = d
        hist[d] += 1
        self._sum += d

        #  = d0 * 0 + d1 * 1 ... + d9 * 9
        self._sum_by_count += d * d_index

        return prev

    def exceed(self) -> bool:
        """
        :return: True if accumulated number of digits > 10
        """
        return self._sum > 10 or self._sum_by_count > 10


class Solver:

    def __init__(self) -> None:
        super().__init__()
        self._n: Number = Number()
        self.attempts = 0
        self._solutions: list[str] = []

        self._find_all = False
        self._start_from_right = True

    def _rec_solve(self, d_index: int) -> bool:
        """

        :param d_index: index of digit to start with, 0..9
        :return:
        """

        n: Number = self._n

        self.attempts += 1
        print(f"{self.attempts}] Checking @ {d_index} / {n}")
        if n.solved():
            self._solutions.append(n.pure_str())
            print(f" *** Found {n}")
            if self._find_all:
                return False # continue search
            else:
                return True # stop search

        if self._start_from_right:
            if d_index == 0:
                return False  # can't try anymore
            d_index -= 1
        else:
            if d_index == 9:
                return False  # can't try anymore
            d_index += 1

        prev = n.get_digit(d_index)
        for d in range(0, 10):

            n.set_digit(d_index, d)

            if n.exceed():
                # can't continue
                n.set_digit(d_index, prev)
                return False

            if self._rec_solve(d_index):
                return not self._find_all # stop search in not find all

        n.set_digit(d_index, prev)
        return False

    def solve(self) -> bool:
        self._n: Number = Number()

        self._rec_solve( 10 if self._start_from_right else -1)
        return bool(self._solutions)

    @property
    def solutions(self):
        return self._solutions


def solve():
    s: Solver = Solver()

    solved = s.solve()

    if solved:
        n = '\n'
        print(f"Solved: {solved} in {s.attempts} attempts:\n {n.join(s.solutions)}")
    else:
        raise RuntimeError("Unable to solve")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solve()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
