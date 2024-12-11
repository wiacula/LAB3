import json


class PersonalData:

    def __init__(self, first_name, last_name, address, postal_code, pesel):

        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.postal_code = postal_code
        self.pesel = pesel

    def to_json(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            # Konwersja obiektu do słownika i zapis w formacie JSON
            json.dump(self.__dict__, f, ensure_ascii=False, indent=4)

    @classmethod
    def from_json(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            # Odczyt danych z pliku JSON
            data = json.load(f)
            # Tworzenie nowej instancji klasy z użyciem odczytanych danych
            return cls(**data)

    def __repr__(self):
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
