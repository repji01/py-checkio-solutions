#!/home/mattie/.local/bin/checkio --domain=py run inside-block

# When it comes to city planning it's important to understand the borders of various city structures.    Parks, lakes or living blocks can be represented as closed polygon and can be described using    cartesian coordinates on a map. We need a functionality to determine if a point (a building or a    tree) lies inside the structure.
# 
# For the purpose of this mission, a city structure may be considered a polygon represented as a    sequence of vertex coordinates on a plane or map. The vertices are connected sequentially with    the last vertex in the list connecting to the first. We are given the coordinates of the point    which we need to check. If the point of impact lies on the edge of the polygon then it should be    considered inside of it. For this mission, you need to determine whether the given point lies    inside the polygon.
# 
# 
# END_DESC

from typing import Tuple

def is_inside(polygon: Tuple[Tuple[int, int]], point: Tuple[int, int]) -> bool:
    n = len(polygon)
    inside =False
    x = point[0]
    y = point[1]
    p1x,p1y = polygon[0]
    for i in range(n+1):
        p2x,p2y = polygon[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y
    for i in range(n+1):
        if (x==polygon[i % n][0]) and  (y==polygon[i % n][1]):
            inside = True
    return inside
        



if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) == True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) == False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) == True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)),
                     (3, 3)) == False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) == True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) == False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) == True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) == False, "Eighth"
    print("All done! Let's check now")