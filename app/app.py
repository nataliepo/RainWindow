#!/usr/bin/env python

import logging
import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import uuid
import tornado.httpserver

from tornado.options import define, options

import settings as app_settings
import models.ticket

define("port", default=app_settings.PORT, help="run on the given port", type=int)

import views.web

import sys


class Application(tornado.web.Application):
    def __init__(self, limit=1):
        #semaphore = models.ticket.startSemaphore(limit)
        self.semaphore = models.ticket.TicketSemaphore(limit)
		
        handlers = [
            (r"^/api/leave.(js|json)$", views.web.LeaveRainRoomAPI, dict(semaphore=self.semaphore)),
            (r"^/api/check_line.(js|json)$", views.web.CheckLineForRainRoom, dict(semaphore=self.semaphore)),

            (r"^/?$", views.web.RainNoRainHandler, dict(semaphore=self.semaphore)),
            
        ]
        settings = dict(
            cookie_secret="5Qd4RuwcQ0ChU+dpT6x0o7QL91Zlk0/Hjg2toz0pITM=",
            login_url="/auth/login",
            template_path=os.path.join(os.path.dirname(__file__), "media/tmpl"),
            static_path=os.path.join(os.path.dirname(__file__), "media"),
            
            xsrf_cookies=False,
            autoescape=None
        )
        
        
        tornado.web.Application.__init__(self, handlers, **settings)
        


def main():
    tornado.options.parse_command_line()

    # start the app with the semaphore.
    app = Application(1)

    # app.listen(options.port)
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(options.port)    
    tornado.ioloop.IOLoop.instance().start()
    

    


if __name__ == "__main__":
    main()        
    
