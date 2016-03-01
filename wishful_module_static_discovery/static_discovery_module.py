import logging
import time
import random
import wishful_agent
import wishful_upis as upis

__author__ = "Piotr Gawlowicz"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz}@tkn.tu-berlin.de"


@wishful_agent.build_module
class StaticDiscoveryModule(wishful_agent.AgentModule):
    def __init__(self, downlink, uplink):
        super(StaticDiscoveryModule, self).__init__()
        self.log = logging.getLogger('static_discovery_module.main')
        self.running = False
        self.controller_dl = downlink
        self.controller_ul = uplink


    @wishful_agent.loop()
    @wishful_agent.on_start()
    @wishful_agent.on_disconnected()
    def start_discovery(self):
        self.log.debug("Start static discovery procedure".format())
        self.running = True

        while self.running:
            #do nothing
            time.sleep(10)


    @wishful_agent.on_exit()
    @wishful_agent.on_connected()
    def stop_discovery(self):
        self.log.debug("Stop static discovery procedure".format())
        self.running = False


    @wishful_agent.discover_controller()
    def get_controller(self):
        self.log.debug("Get Controller addresses: DL:{}, UL:{}".format(self.controller_dl, self.controller_ul))
        return [self.controller_dl, self.controller_ul]