"""

import threading

counter = 0
lock = threading.Lock()

def increment(name):
    global counter
    lock.acquire()
    with lock:
        for i in range(1000):
            counter += 1
            print(name, counter, lock.locked())


def dicrement(name):
    global counter
    lock.acquire()
    with lock:
        for i in range(1000):
            counter -= 1
            print(name, counter, lock.locked())

thread1 = threading.Thread(target=increment, args=(thread1,))
thread2 = threading.Thread(target=dicrement, args=(thread2,))
thread3 = threading.Thread(target=increment, args=(thread3,))
thread4 = threading.Thread(target=dicrement, args=(thread4,))
thread1.start()
thread3.start()
thread2.start()
thread4.start()


"""

import threading
import random
import time

counter = 0
lock = threading.Lock

class Bank:
    def __innit__(self, balance, lock):
        threading.Thread.__init__(self)
        self.balance = balance
        # self.lock = lock

    def deposit(self):
        for i in range(100):
            summ = random.randint(50,500)
            self.balance += summ
            if self.balance >= 500 and lock.locked():
                lock.release()
            print(f"Пополнение: {i}. Баланс: {self.balance}")
        time.sleep(0.001)

    def take(self):
        for i in range(100):
            summ = random.randint(50, 500)
            print(f"Запрос на {summ}")
            if summ <= self.balance:
                self.balance -= summ
                print(f"Снятие: {summ}. Баланс: {self.balance}")
            if summ > self.balance:
                print("Запрос отклонён, недостаточно средств")
                lock.acquire()
        time.sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')