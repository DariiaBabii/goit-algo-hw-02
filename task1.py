import queue 
import time

def generate_request(q, request_id):
    print(f"Генерується нова заявка з ID: {request_id}")
    q.put(request_id)

def process_request(q):
    if not q.empty():
        request_id = q.get()
        print(f"Обробляється заявка з ID: {request_id}")
    else:
        print("Черга пуста")

# Створюємо чергу
request_queue = queue.Queue()

request_counter = 0

try:
    while True:
            # Генерувати нові заявки
            generate_request(request_queue, request_counter)
            request_counter += 1

            # Обробляти заявки
            process_request(request_queue)

            # Імітувати паузу
            time.sleep(1)
    
except KeyboardInterrupt:
    print("Програма завершена користувачем")