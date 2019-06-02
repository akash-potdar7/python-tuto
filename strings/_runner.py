import slice1 as str_slicer
import substr_in_string

mutated_str = str_slicer.mutate_string_by_slice('name', 0, 'l')
print('str_slicer.mutate_string_by_slice', mutated_str)

mutated_str = str_slicer.mutate_string_by_list_conversion('sky', 1, 'l')
print('str_slicer.mutate_string_by_list_conversion', mutated_str)

mutated_str = substr_in_string.count_substring('ABCDCBACDC', 'CDC')
print(mutated_str)

mutated_str = substr_in_string.substring_occurances('ABCDCBACDC', 'CDC')
print(mutated_str)