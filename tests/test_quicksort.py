def test_should_sorted_elements_after_used_method_quick_sort():
     from functionality.zadania import quick_sort_method
     assert quick_sort_method([8, 7, 6, 1, 0, 9, 2]) == [0, 1, 2, 6, 7, 8, 9]