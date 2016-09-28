import logging
import time
import wishful_framework
import wishful_upis as upis

__author__ = "Piotr Gawlowicz"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz}@tkn.tu-berlin.de"


@wishful_framework.build_module
class StaticDiscoveryModule(wishful_framework.WishfulModule):
    def __init__(self, downlink, uplink):
        super(StaticDiscoveryModule, self).__init__()
        self.log = logging.getLogger('static_discovery_module.main')
        self.running = False
        self.controller_dl = downlink
        self.controller_ul = uplink

    @wishful_framework.run_in_thread()
    @wishful_framework.on_start()
    @wishful_framework.on_disconnected()
    def start_discovery(self):
        self.log.debug("Start static discovery procedure".format())
        self.running = True
        while self.running:
            time.sleep(2)
            self.log.debug("Discovered Controller DL-{}, UL-{}"
                           .format(self.controller_dl,
                                   self.controller_ul))
            self.send_event(
                upis.mgmt.BrokerDiscoveredEvent(
                    self.controller_dl, self.controller_ul)
            )

    @wishful_framework.on_exit()
    @wishful_framework.on_connected()
    def stop_discovery(self):
        self.log.debug("Stop static discovery procedure".format())
        self.running = False
