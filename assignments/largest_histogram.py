# Python3 program to find maximum
# rectangular area in linear time

def max_area_histogram(arr):
    stack = list()

    max_area = 0  # Initialize max area

    index = 0
    while index < len(arr):
        if (not stack) or (arr[stack[-1]] <= arr[index]):
            stack.append(index)
            index += 1

        else:
            top_of_stack = stack.pop()

            area = (arr[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))

            max_area = max(max_area, area)

    while stack:
        # pop the top
        top_of_stack = stack.pop()

        area = (arr[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index))

        # update max area, if needed
        max_area = max(max_area, area)

    # Return maximum area under
    # the given histogram
    return max_area


# Driver Code
hist = [6, 3, 1, 4, 12, 4]
print("Maximum area is",
      max_area_histogram(hist))

# This code is contributed
# by Jinay Shah
