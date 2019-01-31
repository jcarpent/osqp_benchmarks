from __future__ import print_function
import numpy as np
import osqp
import os
import time

from problem_classes.maros_meszaros import MarosMeszaros

problems_dir = "./problem_classes/maros_meszaros_data"
problem_name = "QBORE3D.mat"

full_path = os.path.join(problems_dir,problem_name) 
pb = MarosMeszaros(full_path)

prob = osqp.OSQP()
prob.setup(pb.P, pb.q, pb.A, pb.l, pb.u,eps_rel=1e-6,max_iter=1000000)

tic = time.time()
res = prob.solve()
toc = time.time()

print("Run time:",toc-tic,"s")
