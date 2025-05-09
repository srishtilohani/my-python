# import pytest
#
#
# class Fruit:
#     def __init__(self, name):
#         self.name = name
#
#     def __eq__(self, other):
#         return self.name == other.name
#
#
# @pytest.fixture
# def my_fruit():
#     return Fruit("apple")
#
#
# @pytest.fixture
# def fruit_basket(my_fruit):
#     return [Fruit("banana"), my_fruit]
#
#
# def test_my_fruit_in_basket(my_fruit, fruit_basket):
#     assert my_fruit in fruit_basket

# a1) range(10)[0] -- 0
# a2) range(10)[-1] -- 9
#print(range(3,8,2))