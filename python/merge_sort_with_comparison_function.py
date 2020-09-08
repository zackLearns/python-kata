def merge(left_array, right_array, comparison_function):
    merged_array = []
    left_index = 0
    right_index = 0

    while left_array and right_array and left_index < len(left_array) and right_index < len(right_array):

        if comparison_function(left_array[left_index], right_array[right_index]):
            merged_array.append(left_array[left_index])
            left_index += 1
        else:
            merged_array.append(right_array[right_index])
            right_index += 1

    while left_index < len(left_array):
        merged_array.append(left_array[left_index])
        left_index += 1

    while right_index < len(right_array):
        merged_array.append(right_array[right_index])
        right_index += 1
    return merged_array


def merge_sort(array, comparison_function):
    if not array or len(array) <= 1:
        return array

    left_index = 0
    right_index = len(array)
    middle_index = (left_index + right_index)//2

    left_array = merge_sort(array[left_index:middle_index], comparison_function)
    right_array = merge_sort(array[middle_index:right_index], comparison_function)
    return merge(left_array, right_array, comparison_function)


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"


if __name__ == '__main__':
    car1 = Car("Alfa Romeo", "33 SportWagon", 1988)
    car2 = Car("Chevrolet", "Cruze Hatchback", 2011)
    car3 = Car("Corvette", "C6 Couple", 2004)
    car4 = Car("Cadillac", "Seville Sedan", 1995)

    array = [car1, car2, car3, car4]

    cars_sorted_by_year = merge_sort(array, lambda carA, carB: carA.year < carB.year)

    print("Cars sorted by year:")
    for car in cars_sorted_by_year:
        print(car)

    print()
    cars_sorted_by_make = merge_sort(array, lambda carA, carB: carA.make < carB.make)
    print("Cars sorted by make:")
    for car in cars_sorted_by_make:
        print(car)
