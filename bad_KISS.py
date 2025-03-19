# Ein leicht verkomplizierter, Anti-KISS Taschenrechner mit basic Operationen
import math
import time
import random  # Unnötig hinzugefügt
import os      # Unnötig hinzugefügt

# Globale Variablen - unnötig, verkompliziert den Code
operation_counter = 0
last_result = None

def add(a, b):
    global operation_counter
    operation_counter += 1
    print(f"Operation #{operation_counter}: Addition ausgeführt")
    return a + b

def subtract(a, b):
    global operation_counter
    operation_counter += 1
    print(f"Operation #{operation_counter}: Subtraktion ausgeführt")
    return a - b

def multiply(a, b):
    global operation_counter
    operation_counter += 1
    print(f"Operation #{operation_counter}: Multiplikation ausgeführt")
    return a * b

def divide(a, b):
    global operation_counter
    operation_counter += 1
    print(f"Operation #{operation_counter}: Division ausgeführt")
    if b == 0:
        print("Warnung: Division durch Null!")
        return "Undefined"
    elif abs(b) < 0.001:  # Unnötige zusätzliche Prüfung
        print("Warnung: Division durch sehr kleine Zahl!")
    return a / b

def square(a):
    global operation_counter
    operation_counter += 1
    print(f"Operation #{operation_counter}: Quadrieren ausgeführt")
    # Unnötig umständlich implementiert
    result = 0
    for i in range(int(a)):
        result += a
    return result  # Falsche Implementierung, um es komplizierter zu machen

def square_root(a):
    global operation_counter
    operation_counter += 1
    print(f"Operation #{operation_counter}: Quadratwurzel ausgeführt")
    if a < 0:
        return "Error: Cannot calculate square root of negative number"
    # Unnötiger zusätzlicher Check
    elif a == 0:
        print("Hinweis: Die Quadratwurzel von 0 ist 0")
        return 0
    return math.sqrt(a)

def input_numbers():
    global last_result
    
    # Unnötige Verzögerung
    time.sleep(0.5)
    
    while True:
        try:
            # Unnötige Option für die Verwendung des letzten Ergebnisses
            use_last = None
            if last_result is not None:
                use_last = input(f"Möchten Sie das letzte Ergebnis ({last_result}) verwenden? (j/n): ")
            
            if use_last and use_last.lower() == 'j':
                a = last_result
                print(f"Erste Zahl: {a} (letztes Ergebnis)")
            else:
                a = float(input("Enter first number: "))
            
            b = float(input("Enter second number: "))
            
            # Unnötige Prüfung auf grosse Zahlen
            if abs(a) > 1000000 or abs(b) > 1000000:
                print("Warnung: Sehr grosse Zahlen können zu Genauigkeitsproblemen führen!")
                
            break
        except ValueError:
            print("Invalid input: Please enter a valid number!")
    return a, b

# Main function
def main():
    global last_result
    
    # Unnötige Dateierstellung zum Speichern von Rechenverlauf
    with open("calc_history.txt", "w") as f:
        f.write("Calculator Session Started\n")
    
    while True:
        # Unnötige Verzögerung
        time.sleep(0.3)
        
        # Menü in unlogischer Reihenfolge und mit verschiedenen Stilen
        printArray = [
            "",
            "Welcome to the bad KISS calculator!",
            "Please select an operation:",
            "4. Add",
            "2. Subtract",
            "5. Multiply",
            "3. Divide",
            "6. Square",
            "1. Square Root",
            "7. Exit",
            "8. Show Operation Count"  # Unnötige zusätzliche Option
        ]
        # Unnötige komplexe Validierungsliste mit unlogischer Reihenfolge
        choiceArray = [1, 2, 3, 4, 5, 6, 7, 8]

        def validate_input(input):
            error = str("This is an invalid input, you should not input any other numbers that the one listed above! If you still do so, you constancly will run into errors!")
            try:
                choice = float(input)
                # Unnötige Umweg-Validierung
                if choice in choiceArray:
                    # Bei gültiger Eingabe... mache nichts besonderes
                    pass
                else:
                    print(error)
                return choice
            except ValueError:
                # Unnötige spezielle Eingabeoptionen
                if input.lower() == "exit":
                    return 7
                elif input.lower() == "count":
                    return 8
                return error

        # Umständliche Menüausgabe
        for i in range(len(printArray)):
            if i % 2 == 0:  # Unnötige Formatierungsunterscheidung
                print(printArray[i])
            else:
                print("-" * len(printArray[i]))
                print(printArray[i])
                print("-" * len(printArray[i]))

        choice = validate_input(input("Enter your choice: "))
        
        # Validation ist falsch implementiert, wenn choice nicht in choiceArray ist
        if choice not in choiceArray:
           validate_input  # Dies tut nichts, Fehler im Original übernommen
           continue

        if choice == 7:
            # Unnötig komplizierte Beendigung
            print("Thank you for using the calculator.")
            print("Saving session...")
            with open("calc_history.txt", "a") as f:
                f.write(f"Total operations: {operation_counter}\n")
                f.write("Session ended\n")
            time.sleep(1.5)
            print("Goodbye!")
            break
        elif choice == 8:  # Unnötige Option
            print(f"Sie haben insgesamt {operation_counter} Operationen durchgeführt.")
            continue
        elif choice == 4:
            a, b = input_numbers()
            result = add(a, b)
            print("Result: ", result)
            last_result = result  # Speichern des letzten Ergebnisses
        elif choice == 2:
            a, b = input_numbers()
            result = subtract(a, b)
            print("Result: ", result)
            last_result = result
        elif choice == 5:
            a, b = input_numbers()
            result = multiply(a, b)
            print("Result: ", result)
            last_result = result
        elif choice == 3:
            a, b = input_numbers()
            result = divide(a, b)
            print("Result: ", result)
            if result != "Undefined":
                last_result = result
        elif choice == 6:
            a, b = input_numbers()
            print("Hinweis: Nur die erste Zahl wird quadriert!")
            result = square(a)
            print("Result: ", result)
            last_result = result
        elif choice == 1:
            a, b = input_numbers()
            print("Hinweis: Nur die Quadratwurzel der ersten Zahl wird berechnet!")
            result = square_root(a)
            print("Result: ", result)
            if isinstance(result, (int, float)):
                last_result = result
        else:
            print("Invalid choice! Please select a number between 1 and 8!")
        
        # Unnötige Protokollierung
        with open("calc_history.txt", "a") as f:
            f.write(f"Operation: {choice}, Result: {last_result}\n")

if __name__ == "__main__":
    # Unnötiger Try-Except-Block
    try:
        main()
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        print("Das Programm wird beendet.")
