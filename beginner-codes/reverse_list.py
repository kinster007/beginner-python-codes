"""
the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.
"""
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  new_list=list2
  r=list(reversed(list1))
  new_list+=r
  return new_list

  
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
