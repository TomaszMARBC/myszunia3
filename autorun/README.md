# Zawartość modułu autorun

## Uwaga ogólna
Funkcje zawarte w tym module wymagają podania jako parametr absolutnej ścieżki do pliku, do którego skrót chcemy utworzyć.

## Funkcje pomocnicze
- receive_user_autostart(): fukcja zwraca sćieżkę do folderu autostart akualnego użytkownika komputera.
- create_shortcut_path(target_path: str): funkcja zwraca ścieżkę do rządanego pliku w folderze Autostart (Startup).

## Funkcje główne do bezpośredniego wykorzystania
- create_starup_shortcut(target_path: str): funkcja tworzy skrót do pliku w folderze autostart.
- delete_shortcut_from_startup(target_path: str): funkcja usuwa skrót do pliku w folderze autostart.

## Skrypt test_example.py
Skrypt umożliwia przetestowanie powyższych funkcji na przykładzie Notatnika.
Po uruchomieniu skryptu w zwykłym trybie zostanie utworzony skrót do notatnika oraz wyświetlony stosowny kompentarz w terminalu.
Jeżeli skrypt zostanie uruchomiony z parametrem 'del':
```bash
$ python test_example.py del
```
to skrót powinien zostać usunięty, a w terminalu wyświetli się stosowny komunikat.
