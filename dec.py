import functools
import copy

def pass_by_value(func):
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
  
        new_args = copy.deepcopy(list(args))
        return (
            func( *new_args, **kwargs)
        )
    return wrapper_func

@pass_by_value
def reverse(list_of_values):
    list_of_values.sort(reverse=True)
    return list_of_values

values_list = [1,2,3,4,5,6,7,8,9]

print(values_list)
new_values_list = reverse(values_list)
print(new_values_list)
print(values_list)

# print(reverse(values_list))

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [9, 8, 7, 6, 5, 4, 3, 2, 1]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]