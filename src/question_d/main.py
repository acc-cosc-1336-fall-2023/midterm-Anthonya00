#add import
import question_d

print("Celsius \t Fahrenheit ")

for Celsius  in range (0,21):
    Fahrenheit  = question_d.Celsius_to_Fahrenheit(Celsius)
    print (f"{Celsius} \t {Fahrenheit}")