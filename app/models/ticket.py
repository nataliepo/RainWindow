import sys
import sqlite3 
import threading

import settings



class TicketSemaphore:
    def __init__(self, limit):
        sys.stderr.write("[ticketSemaphore::init]\n")
        self.semaphore = threading.BoundedSemaphore(limit)

    def acquire():
        return self.semaphore.acquire()

    def release():
        return self.semaphore.release()
        
    def destroy():
        self.semaphore = False
        


def startSemaphore(semaphore, limit):
	if (semaphore):
		# release it
		semaphore.destroy()
		semaphore = False
		
	semaphore = TicketSemaphore(1)
		
	

def get_active_ticket(semaphore):

    sys.stderr.write("[get_active_ticket] Need to find out how to get the count in the semaphore...\n")

    semaphore.acquire()
    
    #con = sqlite3.connect(settings.SQLITE_DB)
    # 
    #with con:	
    #    cur = con.cursor()    
    #    cur.execute('select active_ticket from ticket;')
    #
    #    original_ticket_number = int(cur.fetchone()[0])
    #    
    #    return original_ticket_number
    #
    #return -1

## CALLED WHEN A USER LEAVES
def move_window_forward(semaphore):
    semaphore.release()

    #original_active_ticket = get_active_ticket()

    #con = sqlite3.connect(settings.SQLITE_DB)
    #with con:
    #    cur = con.cursor()
    #    cur.execute("update ticket set active_ticket=%d where active_ticket=%d;" % (original_active_ticket + 1, original_active_ticket))
        
        
    #return

## Lists how many people have been to the room.
def get_max_waiting_ticket():
    con = sqlite3.connect(settings.SQLITE_DB)
    original_ticket_number = -1
    with con:	
        cur = con.cursor()    
        cur.execute('select max_waiting_ticket from ticket;')
    
        original_ticket_number = int(cur.fetchone()[0])
        

    
    return original_ticket_number
    

# CALLED ON A FRESH PAGE REQUEST, 
#   adds user to the end of the line; returns new max_ticket_number.
def get_new_ticket():
    original_ticket_number = get_max_waiting_ticket()

    con = sqlite3.connect(settings.SQLITE_DB)
    with con:	
        cur = con.cursor()    
        cur.execute("update ticket set max_waiting_ticket=%d where max_waiting_ticket=%d;" % (original_ticket_number + 1, original_ticket_number))
   
        

        return (original_ticket_number + 1)

    return 0
    

####
# UTILITY
# clears max_waiting and active_tickets.
#####
def clear_tickets():
    con = sqlite3.connect(settings.SQLITE_DB)
     
    with con:	
        cur = con.cursor()    
        cur.execute("update ticket set max_waiting_ticket=0;")
        cur.execute("update ticket set active_ticket=1;")
        

