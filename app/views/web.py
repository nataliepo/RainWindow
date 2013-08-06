import logging
import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import uuid
import tornado.httpserver
import sys

import simplejson

import models.ticket


from Cheetah.Template import Template
from tornado.options import define, options

import settings as settings

class DefaultHandler(tornado.web.RequestHandler):
    
    def __init__(self, **kwargs):
    	self.semaphore = self.get('semaphore', False)
    	return self
    	
    def render_cheetah_template(self, type, json, config_arg={}, **kwargs):
        json.update({
			# constants
        })

        json.update(config_arg)
        compiler_settings = { }
        
        template = Template(
            #file=file, 
            file="cheetah/%s.py" % type,
            searchList=[json],  #[data], # Attach data
            compilerSettings = compiler_settings)
        result = str(template)
                
        self.write(result)
        
        
        result = ''
        return
        
class DefaultAPI(tornado.web.RequestHandler):
    def render(self, json_obj={}, is_json=1, **kwargs):         
        if (is_json == 1):
            self.write(simplejson.dumps(json_obj))
            self.set_header('Content-Type', 'application/json')
        
            return
            
        # otherwise, it's javascript.
        c = self.get_arguments('callback', '')
        if (c):
            c = c[0]
        
        self.write("%s(%s)" % (c, simplejson.dumps(json_obj)))
        self.set_header('Content-Type', 'application/javascript')
        
        return

class RainNoRainHandler(DefaultHandler):
    def get(self, semaphore):
    	# this needs to be a string
    	# new_ticket = ("%s" % models.ticket.get_new_ticket())
    	
    	sys.stderr.write("About to acquire semaphore...\n")
    	semaphore.acquire()
    	sys.stderr.write("Acquired!!!\n")
    	
    	# set this as a cookie.
    	# self.set_cookie('ticket', new_ticket)
    	
    	self.render_cheetah_template('rain', {
         	'ticket_number': new_ticket
         })
        
        return

class CheckLineForRainRoom(DefaultAPI):
    def get(self, ending):
        # this_ticket = int(self.get_cookie('ticket'))
        this_ticket = self.get_arguments('ticket_number', [])
        if (len(this_ticket) > 0):
            this_ticket = int(this_ticket[0])
        else:
            this_ticket = 0

        
        num_waiting_before_this_ticket = this_ticket - (models.ticket.get_active_ticket() + (settings.WINDOW_SIZE - 1))

        sys.stderr.write("There are %s waiting before this ticket.\n" % num_waiting_before_this_ticket)
        
        # is this the active ticket number?
        if (num_waiting_before_this_ticket <= 0):
            self.render({
                'access': True
            }, (ending == 'json'))
        else:
            self.render({
                'access': False,
                'num_waiting': num_waiting_before_this_ticket
            }, (ending == 'json'))

        return

class LeaveRainRoomAPI(DefaultAPI):
    def get(self, ending, semaphore):
    
        sys.stderr.write("Release called...\n")

        semaphore.release()
        sys.stderr.write("Release done!\n")
    
        #this_ticket = self.get_arguments('ticket_number', [])
        #
        #if (len(this_ticket) > 0):
        #    this_ticket = int(this_ticket[0])
        #else:
        #    this_ticket = 0
        #sys.stderr.write("This ticket = %d and the active ticket = %d.\n" % 
        #    (this_ticket, models.ticket.get_active_ticket()))
            
        # if this ticket was in the waiting room, then move them forward.
        
        if ((this_ticket - 1) <= models.ticket.get_active_ticket()):
            models.ticket.move_window_forward()
            sys.stderr.write("*** Somebody left! ***\n")
        else:
            sys.stderr.write("Someone got out of line.\n")

        self.render({}, (ending == 'json'))

        
        
        