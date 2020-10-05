import time 

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-26240124-069d-11eb-a4c5-6ea1d8be3fc3'
pnconfig.publish_key = 'pub-c-553985c0-6c92-46d9-8915-9d106402196f'
pubnub = PubNub(pnconfig)

CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK',
}

class Listener(SubscribeCallback):
    def message(self, pubnub,message_object):
        print(f'\n-- Channel:{message_object.channel} | Message: {message_object.message}')

class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between nodes of the blockchain network.
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener())
    
    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self,block):
        """
        Broadcast a block object to all nodes.
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())

def main():
    pubsub = PubSub()

    time.sleep(1)

    pubsub.publish(CHANNELS[''], {'foo': 'bar'})

if __name__ == '__main__':
    main()

