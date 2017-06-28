import numpy as np
import time
N = 6000
M = 10000

k_list = [64, 80, 96, 104, 112, 120, 128, 144, 160, 176, 192, 200, 208, 224, 240, 256, 384]

def get_gflops(M, N, K):
    return M*N*(2.0*K-1.0) / 1000**3

np.show_config()

for K in k_list:
    a = np.random.randn(M, N)
    b = np.random.randn(N, K)

    start = time.time()
    C = np.dot(a,b)
    C = np.dot(a,b)
    C = np.dot(a,b)
    C = np.dot(a,b)
    C = np.dot(a,b)
    end = time.time()

    tm = (end-start) / 5.0

    print ('{}, {}, {}'.format("K", "time", get_gflops(M, N, K) / tm))
    print ('{0:4}, {1:9.7}, {2:9.7}'.format(K, tm, get_gflops(M, N, K) / tm))
