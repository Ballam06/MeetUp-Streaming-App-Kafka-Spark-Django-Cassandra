from multiprocessing import Process


def one(): from MeetupP import Consumer
def two(): from MeetupP import Producer

Process(target=one).start()
Process(target=two).start()