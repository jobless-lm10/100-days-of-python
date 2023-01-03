def kWeakestRows(mat: list[list[int]], k: int) -> list[int]:
    strength = {sum(mat[i]): i for i in range(len(mat))}
    least_strength = sorted(strength.keys())[:k]
    return [strength[x] for x in least_strength]


print(kWeakestRows(mat=[[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], k=2))
