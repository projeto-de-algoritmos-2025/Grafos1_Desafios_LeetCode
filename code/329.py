from collections import defaultdict
from typing import List, Tuple

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        linhas, colunas = len(matrix), len(matrix[0])
        direcoes = [(-1,0), (1,0), (0,-1), (0,1)]

        grafo = defaultdict(list)

        for i in range(linhas):
            for j in range(colunas):
                for dx, dy in direcoes:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < linhas and 0 <= nj < colunas:
                        if matrix[ni][nj] > matrix[i][j]:
                            grafo[(i, j)].append((ni, nj))

        memo = {}

        def dfs(no: Tuple[int, int]) -> int:
            if no in memo:
                return memo[no]
            
            max_caminho = 1
            for vizinho in grafo[no]:
                max_caminho = max(max_caminho, 1 + dfs(vizinho))
            
            memo[no] = max_caminho
            return max_caminho

        maior_resultado = 0
        for i in range(linhas):
            for j in range(colunas):
                maior_resultado = max(maior_resultado, dfs((i, j)))

        return maior_resultado
