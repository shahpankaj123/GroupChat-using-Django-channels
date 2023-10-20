from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
import json
from asgiref.sync import async_to_sync
from .models import *

class MysyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("connected...",event) 
        self.group_name=self.scope['url_route']['kwargs']['gname']
        print(self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
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
        group=Group.objects.filter(g_name=self.group_name).first()

        chat_obj=chat(content=rply,group=group)
        chat_obj.save()

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
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
            self.group_name,
            self.channel_name
         )
        raise StopConsumer()


     

        