from typing import List
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, conexoes: List[List[int]]) -> List[List[int]]:
        # Grafo como lista de adjacência
        grafo = defaultdict(list)
        for u, v in conexoes:
            grafo[u].append(v)
            grafo[v].append(u)
        
        tempo = 0
        tempo_entrada = [-1] * n
        menor_tempo = [-1] * n
        pontes = []

        def dfs(no: int, pai: int):
            nonlocal tempo
            tempo_entrada[no] = menor_tempo[no] = tempo
            tempo += 1

            for vizinho in grafo[no]:
                if vizinho == pai:
                    continue
                if tempo_entrada[vizinho] == -1:
                    dfs(vizinho, no)
                    menor_tempo[no] = min(menor_tempo[no], menor_tempo[vizinho])

                    # Verifica se a aresta é uma ponte
                    if menor_tempo[vizinho] > tempo_entrada[no]:
                        pontes.append([no, vizinho])
                else:
                    menor_tempo[no] = min(menor_tempo[no], tempo_entrada[vizinho])

        dfs(0, -1)
        return pontes
