import africastalking
from django.conf import settings
import queue, threading


africastalking.initialize(username=settings.AFRICASTALKING_USERNAME, api_key=settings.AFRICASTALKING_API_KEY)
sms = africastalking.SMS

sms_queue = queue.Queue()

def send_sms_alert(customer_phone, message):
    response = sms.send(message, [str(customer_phone)])
    return response


def worker():
    while True:
        customer_phone, message = sms_queue.get()
        try:
            send_sms_alert(customer_phone, message)
        finally:
            sms_queue.task_done()


num_worker_threads = 4
threads = []
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)


def queue_sms(customer_phone, message):
    sms_queue.put((customer_phone, message))