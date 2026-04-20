from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3

class SimpleQoS(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        dp = ev.msg.datapath
        ofp = dp.ofproto
        parser = dp.ofproto_parser

        actions = [parser.OFPActionOutput(ofp.OFPP_FLOOD)]

        # High Priority ICMP
        match = parser.OFPMatch(
            eth_type=0x0800,
            ip_proto=1
        )
        self.add_flow(dp, 200, match, actions)

        # Low Priority UDP
        match = parser.OFPMatch(
            eth_type=0x0800,
            ip_proto=17
        )
        self.add_flow(dp, 10, match, actions)

        # Default Rule
        match = parser.OFPMatch()
        self.add_flow(dp, 1, match, actions)

    def add_flow(self, dp, priority, match, actions):
        parser = dp.ofproto_parser
        ofp = dp.ofproto

        inst = [
            parser.OFPInstructionActions(
                ofp.OFPIT_APPLY_ACTIONS,
                actions
            )
        ]

        mod = parser.OFPFlowMod(
            datapath=dp,
            priority=priority,
            match=match,
            instructions=inst
        )

        dp.send_msg(mod)
