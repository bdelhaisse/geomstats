"""
Plot geodesics of the following Riemannian manifolds:
    - SE(3) with its left-invariant canonical metric: a Lie group
"""

import numpy as np

from geomstats.special_euclidean_space import SpecialEuclideanGroup
import geomstats.visualization

se3_group = SpecialEuclideanGroup(n=3)

metric = se3_group.left_canonical_metric

initial_point = se3_group.identity
initial_tangent_vec = np.array([0.1, 0.2, 0.3, 1., 0., 0])

geodesic = metric.geodesic(initial_point=initial_point,
                           initial_tangent_vec=initial_tangent_vec)
