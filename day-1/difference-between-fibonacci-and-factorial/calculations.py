class FactorialCalculation:
    def get_factorial_item(self, item_index: int) -> int:
        return 1 if item_index == 0 else item_index * self.get_factorial_item(item_index - 1)


class FibonacciCalculation:
    def get_fibonacci_item(self, item_index: int) -> int:
        is_except_initial_case = item_index == 0 or item_index == 1 or item_index == 2

        return 1 if is_except_initial_case else \
            self.get_fibonacci_item(item_index - 1) + self.get_fibonacci_item(item_index - 2)


class CoreCalculation:
    __factorial = FactorialCalculation()
    __fibonacci = FibonacciCalculation()

    def get_core_elements_difference(self, item_index: int) -> int:
        return self.__factorial.get_factorial_item(item_index) - self.__fibonacci.get_fibonacci_item(item_index)
