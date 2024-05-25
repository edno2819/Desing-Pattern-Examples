from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


class QuickSortStrategy(SortStrategy):
    def sort(self, data):
        return sorted(data)

class ReverseSortStrategy(SortStrategy):
    def sort(self, data):
        return sorted(data, reverse=True)

class LengthSortStrategy(SortStrategy):
    def sort(self, data):
        return sorted(data, key=len)


class SortContext:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort_data(self, data):
        return self._strategy.sort(data)


if __name__ == "__main__":
    data = ["pear", "apple", "orange", "banana"]

    context = SortContext(QuickSortStrategy())
    print("QuickSortStrategy:", context.sort_data(data))

    context.set_strategy(ReverseSortStrategy())
    print("ReverseSortStrategy:", context.sort_data(data))

    context.set_strategy(LengthSortStrategy())
    print("LengthSortStrategy:", context.sort_data(data))
