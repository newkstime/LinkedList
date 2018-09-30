import sys
from broker import Broker

def main():
    rounds = 1000
    broker = Broker(rounds)
    broker.setup()
    broker.play()
    broker.display_results()
   
main()
