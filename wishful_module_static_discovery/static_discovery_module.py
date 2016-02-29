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
class StaticDiscoveryModule(wishful_module.AgentUpiModule):
    def __init__(self, agentPort=None):
        super(StaticDiscoveryModule, self).__init__(agentPort)
        self.log = logging.getLogger('static_discovery_module.main')
        self.running = False
        self.controller_dl = None
        self.controller_ul = None


    @wishful_module.loop()
    @wishful_module.on_start()
    @wishful_module.on_disconnected()
    def start_discovery(self):
        self.log.debug("Start static discovery procedure".format())
        self.running = True
        self.controller_dl = None
        self.controller_ul = None

        while self.running:
            self.controller_dl = "tcp://127.0.0.1:8989"
            self.controller_ul = "tcp://127.0.0.1:8990"
            time.sleep(1)


    @wishful_module.on_exit()
    @wishful_module.on_connected()
    def stop_discovery(self):
        self.log.debug("Stop static discovery procedure".format())
        self.running = False


    @wishful_module.discover_controller()
    def get_controller(self):
        self.log.debug("Get Controller addresses: DL:{}, UL:{}".format(self.controller_dl, self.controller_ul))
        return [self.controller_dl, self.controller_ul]