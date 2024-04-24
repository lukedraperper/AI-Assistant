from multiprocessing import Process
from SpeechRecognition import listener
def Run():
    if __name__ == "__main__":
        try:
            new = Process(target=listener.Listener())
            new.start()
            # new2 = Process(target=Listener2)
            # new2.start()
        except KeyboardInterrupt:
            pass
