import logging
import time
import random
import wishful_upis as upis
import wishful_agent as wishful_module

__author__ = "Piotr Gawlowicz"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz}@tkn.tu-berlin.de"


@wishful_module.build_module
class StaticDiscoveryControllerModule(wishful_module.AgentUpiModule):
    def __init__(self, agentPort=None):
        super(StaticDiscoveryControllerModule, self).__init__(agentPort)
        self.log = logging.getLogger('static_discovery_module.main')
        self.running = False
        self.controller_dl = "tcp://127.0.0.1:8989"
        self.controller_ul = "tcp://127.0.0.1:8990"


    @wishful_module.loop()
    @wishful_module.on_start()
    def start_discovery_announcements(self):
        self.log.debug("Start discovery announcements".format())
        self.running = True
        while self.running:
            self.log.debug("Controller Discovery Announcements, Donwlink={}, Uplink={}".format(self.controller_dl, self.controller_ul))
            time.sleep(5)


    @wishful_module.on_exit()
    def stop_discovery_announcements(self):
        self.log.debug("Stop discovery announcements".format())
        self.running = False