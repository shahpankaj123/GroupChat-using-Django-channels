from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
import json
from asgiref.sync import async_to_sync
class MysyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("connected...",event) 
        async_to_sync(self.channel_layer.group_add)(
            'programmer',
            self.channel_name
         )
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        print("recieved...",event) 
        data=json.loads(event['text'])
        print(data['msg'])
        rply=data['msg']
        async_to_sync(self.channel_layer.group_send)(
            'programmer',
            {
                'type':'chat.message',
                'message':rply
            }
         )
        

    def chat_message(self,event): 
        self.send(
            {
                'type':'websocket.send',
                'text':json.dumps({ 'msg' :event['message']})
            }
        )

    def websocket_disconnect(self, event):    
        print("disconnect")
        async_to_sync(self.channel_layer.group_discard)(
            'programmer',
            self.channel_name
         )
        raise StopConsumer()


     

        