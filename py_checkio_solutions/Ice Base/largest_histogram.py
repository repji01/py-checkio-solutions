#!/home/mattie/.local/bin/checkio --domain=py run largest-histogram

# "Your power to choose can never be taken from you.
# It can be neglected and it can be ignored.
# But if used, it can make all the difference."
# ― Steve Goodier
# 
# You have a histogram. Try to find the size of the biggest rectangle you can build out of the histogram bars.
# 
# Input:A list of all rectangles’ heights on the histogram.
# 
# Output:Area of the biggest rectangle.
# 
# Example:
# 
# largest_histogram([5]) == 5
# largest_histogram([5, 3]) == 6
# largest_histogram([1, 1, 4, 1]) == 4
# largest_histogram([1, 1, 3, 1]) == 4
# largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8
# How it is used:There is no way the solution you come up with will be of any use in real life. So, just have fun here!
# 
# Precondition:
# 0 < len(data) < 1000
# 
# 
# 
# END_DESC

def largest_histogram(histogram):
    increasing, area, i = [], 0, 0
    while i <= len(histogram):
            if not increasing or (i < len(histogram) and histogram[i] > histogram[increasing[-1]]):
                increasing.append(i)
                i += 1
            else:
                last = increasing.pop()
                if not increasing:
                    area = max(area, histogram[last] * i)
                else:
                    area = max(area, histogram[last] * (i - increasing[-1] - 1 ))
    
    return area


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")