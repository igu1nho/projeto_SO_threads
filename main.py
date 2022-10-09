import time
import threading

print("Operações Realizadas ")
print("Tarefa 1 - Ligar irrigadores da horta!")
print("Tarefa 2 - Ligar água para encher a caixa d'água!")
print("Tarefa 3 - Ligando irrigadores do campo!\n")

def t1():
    print("Thread 1 em execução: Horta sendo regada! ")
    time.sleep(18)   # representando por 3 minutos
    print("Thread 1 finalizada com sucesso!")

def t2():
    print("Thread 2 em execução: Enchendo a caixa d'água! ")
    time.sleep(30)   # representando por 5 minutos
    print("Thread 2 finalizada com sucesso!")

def t3():
    print("Thread 3 em execução: Campo sendo regada! ")
    time.sleep(30)   # representando por 5 minutos
    print("Thread 3 finalizada com sucesso!")

threading.Thread(target=t1).start()
t3()

op = int(input("Deseja encher a caixa d'água também, se sim digite 1! : "))  # opção extra para caso deseja realizar outra thread

if op == 1:
    threading.Thread(target=t2).start()

elif op != 1:
    print("Sistema será desligado!")