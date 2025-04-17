from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        grafo = defaultdict(list)
        for u, v in connections:
            grafo[u].append(v)
            grafo[v].append(u)

        ordem = [-1] * n  # tempo de descoberta
        baixo = [-1] * n  # menor tempo alcançável
        tempo = [0]
        resultado = []

        def dfs(no, pai):
            ordem[no] = baixo[no] = tempo[0]
            tempo[0] += 1

            for vizinho in grafo[no]:
                if vizinho == pai:
                    continue
                if ordem[vizinho] == -1:  # ainda não visitado
                    dfs(vizinho, no)
                    baixo[no] = min(baixo[no], baixo[vizinho])
                    if baixo[vizinho] > ordem[no]:
                        resultado.append([no, vizinho])
                else:
                    baixo[no] = min(baixo[no], ordem[vizinho])

        dfs(0, -1)
        return resultado
