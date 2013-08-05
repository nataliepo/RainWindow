import sys

import models.ticket


sys.stderr.write("Clearing ticket count....\n")



models.ticket.clear_tickets()


sys.stderr.write("Complete.\n")