class State:
    """Reprezentuje stan w automacie Moore'a."""
    def __init__(self, name, output):
        self.name = name  # Nazwa stanu
        self.output = output  # Wyjście dla tego stanu
        self.transitions = {}  # Przejścia do innych stanów

    def add_transition(self, input_signal, next_state):
        """Dodaje przejście do innego stanu."""
        self.transitions[input_signal] = next_state

    def get_next_state(self, input_signal):
        """Zwraca następny stan na podstawie sygnału wejściowego."""
        return self.transitions.get(input_signal)

    def get_output(self):
        """Zwraca wyjście przypisane do stanu."""
        return self.output


class MooreMachine:
    """Automat Moore'a."""
    def __init__(self, initial_state):
        self.current_state = initial_state  # Ustawienie początkowego stanu

    def transition(self, input_signal):
        """Przejście do następnego stanu na podstawie sygnału wejściowego."""
        next_state = self.current_state.get_next_state(input_signal)
        if next_state:
            self.current_state = next_state

    def get_output(self):
        """Zwraca wyjście obecnego stanu."""
        return self.current_state.get_output()


if __name__ == "__main__":
    # Definiowanie stanów automatu
    state_A = State("A", "0")
    state_B = State("B", "1")
    state_C = State("C", "0")
    state_D = State("D", "1")

    # Definiowanie przejść między stanami
    state_A.add_transition("0", state_B)
    state_A.add_transition("1", state_C)
    state_B.add_transition("0", state_A)
    state_B.add_transition("1", state_D)
    state_C.add_transition("0", state_D)
    state_C.add_transition("1", state_A)
    state_D.add_transition("0", state_C)
    state_D.add_transition("1", state_B)

    # Tworzenie automatu Moore'a
    moore_machine = MooreMachine(state_A)

    # Przykładowe wejścia do automatu
    inputs = ["0", "1", "0", "1", "1", "0", "0"]

    print("Symulacja automatu Moore'a")
    for i, signal in enumerate(inputs):
        output = moore_machine.get_output()
        print(f"Krok {i}: Stan = {moore_machine.current_state.name}, Wyjście = {output}")
        moore_machine.transition(signal)

    # Ostatni stan i wyjście
    final_output = moore_machine.get_output()
    print(f"Końcowy stan = {moore_machine.current_state.name}, Końcowe wyjście = {final_output}")