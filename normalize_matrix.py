import numpy as np

def normalize_matrix(matrix, options):
    min_range = options["min_range"]
    max_range = options["max_range"]
    matrix = np.array(matrix)
    min_val = np.min(matrix)
    max_val = np.max(matrix)
    normalized_matrix = (matrix - min_val) / (max_val - min_val) * (max_range - min_range) + min_range
    return normalized_matrix
