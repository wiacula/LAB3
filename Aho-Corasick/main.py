from collections import defaultdict, deque

class AhoCorasick:
    def __init__(self):
        """Inicjalizacja podstawowych struktur danych."""
        self.num_states = 1  # Liczba stanów, początkowo mamy tylko stan 0 (stan początkowy)
        self.transitions = defaultdict(lambda: defaultdict(lambda: 0))  # Przejścia między stanami
        self.fail = defaultdict(lambda: 0)  # Funkcja porażki
        self.outputs = defaultdict(list)  # Listy wyjść dla stanów

    def add_pattern(self, pattern):
        """Dodaje wzorzec do automatu."""
        current_state = 0
        for char in pattern:
            if char not in self.transitions[current_state]:
                self.transitions[current_state][char] = self.num_states
                self.num_states += 1
            current_state = self.transitions[current_state][char]
        self.outputs[current_state].append(pattern)

    def build_automaton(self):
        """Buduje funkcję porażki dla automatu."""
        queue = deque()

        # Ustawienia funkcji porażki dla dzieci stanu początkowego
        for char, state in self.transitions[0].items():
            if state != 0:  # Dzieci korzenia mają porażkę do korzenia
                self.fail[state] = 0
                queue.append(state)

        while queue:
            state = queue.popleft()

            for char, next_state in self.transitions[state].items():
                queue.append(next_state)
                fail_state = self.fail[state]

                while char not in self.transitions[fail_state] and fail_state != 0:
                    fail_state = self.fail[fail_state]

                if char in self.transitions[fail_state]:
                    self.fail[next_state] = self.transitions[fail_state][char]
                else:
                    self.fail[next_state] = 0

                self.outputs[next_state].extend(self.outputs[self.fail[next_state]])

    def search(self, text):
        """Wyszukiwanie wszystkich wystąpień wzorców w tekście."""
        state = 0
        results = []

        for i, char in enumerate(text):
            while char not in self.transitions[state] and state != 0:
                state = self.fail[state]

            if char in self.transitions[state]:
                state = self.transitions[state][char]
            else:
                state = 0

            for pattern in self.outputs[state]:
                results.append((i - len(pattern) + 1, pattern))

        return results


if __name__ == "__main__":
    # Przykładowe użycie algorytmu Aho-Corasick
    patterns = ["niebieski", "nalesnik", "lina", "kielce"]
    text = "niebieskielcelinalesnik"

    # Tworzenie i budowanie automatu
    automaton = AhoCorasick()
    for pattern in patterns:
        automaton.add_pattern(pattern)
    automaton.build_automaton()

    # Wyszukiwanie wzorców w tekście
    matches = automaton.search(text)
    print("Znalezione wzorce w tekście:", matches)
