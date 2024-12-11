import heapq


def dijkstra(graph, start):
    """Znajduje najkrótszą ścieżkę w grafie od wierzchołka start do wszystkich innych wierzchołków."""
    distances = {vertex: float('inf') for vertex in
                 graph}  # Inicjalizacja odległości do wszystkich wierzchołków na nieskończoność
    distances[start] = 0  # Odległość do siebie samego wynosi 0
    priority_queue = [(0, start)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(
            priority_queue)  # Pobranie wierzchołka o najkrótszej odległości

        if current_distance > distances[current_vertex]:
            continue  # Jeśli obecna odległość jest większa niż aktualnie zapisana, przejdź dalej

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight  # Oblicz odległość do sąsiada

            if distance < distances[neighbor]:  # Jeśli nowa odległość jest mniejsza, zaktualizuj ją
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))  # Dodaj sąsiada do kolejki priorytetowej

    return distances


if __name__ == "__main__":
    # Przykładowy graf do testów
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_vertex = 'A'
    distances = dijkstra(graph, start_vertex)

    print(f"Najkrótsze odległości od wierzchołka {start_vertex} do innych wierzchołków: {distances}")
