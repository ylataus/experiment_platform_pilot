import re
import json
import logging
from channels import Group
from channels.sessions import channel_session
from .models import Room
from experiment.models import ExpUser, TaskUser, Crowd
from channels.auth import http_session, http_session_user, channel_session_user, channel_session_user_from_http

log = logging.getLogger(__name__)

@channel_session_user_from_http
@channel_session
def ws_chat_connect(message):
    # Extract the room from the message. This expects message.path to be of the
    # form /chat/{label}/, and finds a Room if the message path is applicable,
    # and if the Room exists. Otherwise, bails (meaning this is a some othersort
    # of websocket). So, this is effectively a version of _get_object_or_404.
    try:
	log.debug('In the try block of ws_connect')#added by me
        prefix, label = message['path'].decode('ascii').strip('/').split('/')
	#log.debug('the prefix is: %s',prefix)#added by me
        if prefix != 'chat':
            log.debug('invalid ws path=%s', message['path'])
	    
            return
        room = Room.objects.get(label=label)
    except ValueError:
        log.debug('invalid ws path=%s', message['path'])
        return
    except Room.DoesNotExist:
        log.debug('ws room does not exist label=%s', label)
        return

    log.debug('chat connect room=%s client=%s:%s', 
        room.label, message['client'][0], message['client'][1])
    t = TaskUser(user=message.user,crowd=label,time_type='start')
    t.save()
    # Need to be explicit about the channel layer so that testability works
    # This may be a FIXME?
    Group('chat-'+label, channel_layer=message.channel_layer).add(message.reply_channel)

    message.channel_session['room'] = room.label

@channel_session_user
@channel_session
def ws_chat_receive(message):
    # Look up the room from the channel session, bailing if it doesn't exist
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
    except KeyError:
        log.debug('no room in channel_session')
        return
    except Room.DoesNotExist:
        log.debug('recieved message, but room does not exist label=%s', label)
        return

    try:
        expuser = ExpUser.objects.get(user=message.user)
    except KeyError:
        log.debug('problem getting username')
        return
    except ExpUser.DoesNotExist:
        log.debug('recieved message, but user does not exist label=%s', label)
        return

    # Parse out a chat message from the content text, bailing if it doesn't
    # conform to the expected message format.
    try:
        data = json.loads(message['text'])
    except ValueError:
        log.debug("ws message isn't json text=%s", text)
        return
    
    #if set(data.keys()) != set(('message')):
    #    log.debug("ws message unexpected format data=%s", data)
    #    return

    if data:
        log.debug('chat message room=%s handle=%s message=%s', 
            room.label, message.user.username, data['message'])
        m = room.messages.create(user=message.user,room=room,handle=expuser.nickname,message=data['message'])

        # See above for the note about Group
        Group('chat-'+label, channel_layer=message.channel_layer).send({'text': json.dumps(m.as_dict())})

@channel_session_user
@channel_session
def ws_chat_disconnect(message):
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
	t = TaskUser(user=message.user,crowd=label,time_type='end')
	t.save()
        Group('chat-'+label, channel_layer=message.channel_layer).discard(message.reply_channel)
    except (KeyError, Room.DoesNotExist):
        pass
