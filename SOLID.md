
[SOLID Principles Python](https://realpython.com/solid-principles-python/)

# Single Responsibility Principle
- [ ] provide a code example
[Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin)
*A class should have only one reason to change.*

# Dependency Inversion Principle
*Abstractions should not depend upon details. Details should depend upon abstractions.*
### Bad Example
```
# app_dip.py

class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_csv()
        print("Display data:", data)

class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"
```
### Good Example
```
# app_dip.py

from abc import ABC, abstractmethod

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"

class CSV(DataSource):
    def get_data(self):
        return "Data from the CSV"
```
