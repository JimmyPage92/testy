from datetime import datetime, timezone
from decouple import config
'''
Stwórz funkcję sprawdzającą, czy liczba jest pierwsza. Otestuj ją,
pamiętając równocześnie o otestowaniu każdego edge-case’a (np. 1 nie
jest liczbą pierwszą).
Spróbuj stworzone testy umieścić w klasie.
Uwaga:
Aby uruchomić testy znajdujące się w klasie, np. TestIsPrime, użyj
polecenia:
">>> pytest tests/tests.py::TestIsPrime"
'''

def is_num_prime(num: int)-> None:
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print(is_num_prime(5))

'''Zad 2.
Napisz funkcję, która zwracać będzie “Fizz”, gdy prześlesz do niej
wartość podzielną przez 3, “Buzz”, gdy podzielną przez 5, a “FizzBuzz”,
gdy liczba będzie podzielna przez obie te wartości. Napisz do niej testy
jednostkowe.'''

def fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return ('fizzbuzz')
    if num % 3 == 0:
        return ('FIZZ')
    elif num % 5 == 0:
        return ('BUZZ')




print(fizz_buzz(3))
print(fizz_buzz(10))
print(fizz_buzz(45))

'''Zad 3.
Napisz funkcję sortującą metodą quick sort listę podanych elementów.
Otestuj jej poprawne działanie.'''

lista = [8,7,6,1,0,9,2]

def quick_sort_method(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()
        nums_greater = []
        nums_lower = []

        for num in list:
            if num > pivot:
                nums_greater.append(num)
            else:
                nums_lower.append(num)

        return quick_sort_method(nums_lower) + [pivot] + quick_sort_method(nums_greater)

print(quick_sort_method(lista))

'''Zad 4.
Poniższy kod realizuje funkcjonalność prostego notatnika TODO.
Możemy do niego dodawać dowolne notatki, usuwać niektóre oraz
czyścić całą listę. Umieść go w pliku src.py i otestuj każdą z funkcji.
Zapewnij sprawdzenie przypadków, w których zostanie rzucony wyjątek.
'''


todos = ["Clean my room", "Make my bed", "Go to school", "Do school homework"]
class NoMoreTodos(Exception):
    pass
class NoSuchItemNumber(Exception):
    pass
def check_pos(pos):
    if len(todos) == 0:
        raise NoMoreTodos
    elif pos >= len(todos) or pos < 0:
        raise NoSuchItemNumber

def add_todo(content):
    todos.append(content)

def remove_todo(pos):
    check_pos(pos)
    todos.pop(pos)

def edit_todo(pos, content):
    check_pos(pos)
    todos[pos] = content

def remove_all():
    todos.clear()

add_todo("Go to bed")
print(todos)
remove_todo(0)
print(todos)
edit_todo(0,"Get up from bed")
print(todos)
remove_all()

print(f'Teraz mamy puste notatki: {todos}')

#zad.5

'''
Rozważ poniższy program:
'''

def get_datetimenow():
    return datetime.now(timezone.utc)
def calc_diff(case):
    end_time = case['end_time']
    start_time = case['start_time']
    start_time_obj = datetime.fromisoformat(start_time)
    if end_time is None:
        end_time_obj = get_datetimenow()
    else:
        end_time_obj = datetime.fromisoformat(end_time)
    return (end_time_obj - start_time_obj).total_seconds()


def main():
    case = {
        'start_time' : '2021-11-03T09:22:28+00:00' ,
        'end_time' : None # None means that case is currently going on
    }

    print(calc_diff(case))

if __name__ == "__main__" :
    main()

'''
Odpowiedzialny jest on za wyliczanie różnicy czasowej (podanej w
sekundach) między start_time oraz end_time.
Napisz test, który będzie sprawdzał poprawne działanie funkcji 
calc_diff.
Podpowiedź:
Tylko tyle, albo aż tyle! Zauważ, że konieczne będzie zamockowanie
datetime.now(). Dlaczego? To już zostawiam Twoim dywagacjom
'''

#zad.6
'''
Zad 6.
Wyobraź sobie, że mamy następującą funkcjonalność w programie:
'''
class Config:
    DB_URL: str = config('DB_URL')
    DB_USERNAME: str = config('DB_USERNAME')
    DB_PASSWORD: str = config('DB_PASSWORD')
    OK_MSG: str = config('OK_MSG')
    NOK_MSG: str = config('NOK_MSG')

class DbHandler:
    def connect_to_database(self):
        return f"I am connecting to {Config.DB_URL} as " \
               f"{Config.DB_USERNAME} with pass: {Config.DB_PASSWORD}..."
    def show_msg_when_connected(self):
        return f"{Config.OK_MSG}"
    def show_msg_when_interrputed(self):
        return f"{Config.NOK_MSG}"

x=DbHandler().show_msg_when_connected()

print(x)
'''
W powyższym kodzie użyliśmy biblioteki python-decouple, która
umożliwia odczytywanie wartości do kodu ze specjalnego pliku .env
(Takie rozwiązanie jest często wykorzystywane, gdy nie chcemy
umieszczać bezpośrednio w kodzie pewnych informacji, np. Wrażliwych
danych połączeniowych do DB).
Napisz testy sprawdzające poprawne działanie klasy DbHandler.
Pamiętaj, aby zamockować odpowiednie informacje (w docelowym
środowisku, na którym będą uruchamiane testy, raczej nie będziemy
chcieli tworzyć pliku specjalnego .env).
'''

