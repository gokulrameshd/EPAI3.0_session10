from math import *
from objective1 import *


class polygons_sequence:
    def __init__(self,n,r):
        self.n = n
        if n < 3:
            raise ValueError("n must be greater then 3")
        self.r = r
        self._polygons = list([polygon((i), r )  for (i) in range(3,self.n+1)])
        self.maximum_efficient_polygon = self.max_efficiency_polygons()
    def __repr__(self):
        return f'Polygon sequence of {len(self._polygons)} polygons'

    def __len__(self):
        return len(self._polygons)

    def __getitem__(self,s):
        return self._polygons[s] #next(self._polygons[s])

    def max_efficiency_polygons(self):
        seq = sorted(self._polygons,
                    key = lambda p:p.area/p.perimeter,
                    reverse = True)
        # print(seq)
        return seq[0]
    