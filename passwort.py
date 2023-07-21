# Importieren der benötigten Module
import tkinter as tk  # Modul für die GUI
import random  # Modul für Zufallsfunktionen
import string  # Modul für Zeichenkettenoperationen
import pyperclip  # Modul zum Kopieren in die Zwischenablage

# Funktion zum Generieren des Passworts
def generate_password():
    # Die eingegebene Passwortlänge aus dem Textfeld "password_length" erhalten
    length = int(password_length.get())

    # Zeichen, die für das generierte Passwort verwendet werden sollen (Buchstaben, Zahlen und Sonderzeichen)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Zufällige Auswahl der Zeichen, um das Passwort zu erstellen
    password = ''.join(random.choice(characters) for i in range(length))

    # Das generierte Passwort im Label "result_label" anzeigen
    result_label.config(text="Generiertes Passwort: " + password)

# Funktion zum Kopieren des generierten Passworts in die Zwischenablage
def copy_to_clipboard():
    # Das generierte Passwort aus dem Text des Labels "result_label" erhalten
    generated_password = result_label.cget("text")

    # Wenn der Text mit "Generiertes Passwort: " beginnt, wird das Passwort extrahiert und in die Zwischenablage kopiert
    if generated_password.startswith("Generiertes Passwort: "):
        password = generated_password[len("Generiertes Passwort: "):]
        pyperclip.copy(password)

# Funktion, die aufgerufen wird, wenn die Eingabetaste gedrückt wird
def on_enter_press(event):
    generate_password()

# GUI erstellen
root = tk.Tk()  # Erzeugung des Hauptfensters (Root)

# Fenstertitel festlegen
root.title("Passwort-Generator")

# Ein Rahmen (Frame) innerhalb des Hauptfensters erstellen
frame = tk.Frame(root)
frame.pack(pady=10)  # Füge einen Innenabstand zum Rahmen hinzu

# Label und Eingabefeld für die Passwortlänge im Rahmen platzieren
password_length_label = tk.Label(frame, text="Passwortlänge:")
password_length_label.grid(row=0, column=0)

password_length = tk.Entry(frame)  # Eingabefeld für die Passwortlänge
password_length.grid(row=0, column=1)
password_length.bind('<Return>', on_enter_press)  # Die Eingabetaste wird mit der Funktion "on_enter_press" verknüpft

# Schaltfläche zum Generieren des Passworts
generate_button = tk.Button(frame, text="Generieren", command=generate_password)
generate_button.grid(row=0, column=2, padx=10)

# Schaltfläche zum Kopieren des Passworts in die Zwischenablage
copy_button = tk.Button(frame, text="Kopieren", command=copy_to_clipboard)
copy_button.grid(row=0, column=3, padx=10)

# Label für die Anzeige des generierten Passworts erstellen
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Hauptereignisschleife starten, um die GUI anzuzeigen
root.mainloop()
