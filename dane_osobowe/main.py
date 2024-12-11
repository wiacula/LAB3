from dataclasses import dataclass, asdict
import json

@dataclass
class PersonalData:
    first_name: str
    last_name: str
    address: str
    postal_code: str
    pesel: str

    def to_json(self, file_path: str) -> None:
        """Zapisuje dane obiektu do pliku JSON."""
        with open(file_path, 'w', encoding='utf-8') as f:
            # Konwersja obiektu do słownika i zapis w formacie JSON
            json.dump(asdict(self), f, ensure_ascii=False, indent=4)

    @classmethod
    def from_json(cls, file_path: str):
        """Tworzy nowy obiekt PersonalData z pliku JSON."""
        with open(file_path, 'r', encoding='utf-8') as f:
            # Odczyt danych z pliku JSON
            data = json.load(f)
            # Tworzenie nowej instancji klasy z użyciem odczytanych danych
            return cls(**data)

    def __repr__(self) -> str:
        """Reprezentacja tekstowa obiektu."""
        return (f"PersonalData(Imie: {self.first_name}, Nazwisko: {self.last_name}, "
                f"Adres: {self.address}, Kod Pocztowy: {self.postal_code}, Pesel: {self.pesel})")


# Przykład użycia:
if __name__ == "__main__":
    # Tworzenie obiektu z danymi osobowymi
    person = PersonalData(
        first_name="Jan",
        last_name="Kowalski",
        address="Krakow, ul. Reymonta 1",
        postal_code="31-216",
        pesel="12345678901"
    )

    # Zapis obiektu do pliku JSON
    person.to_json("person.json")

    # Odczyt danych z pliku JSON i tworzenie nowego obiektu
    loaded_person = PersonalData.from_json("person.json")

    # Wyświetlenie załadowanego obiektu
    print(loaded_person)
