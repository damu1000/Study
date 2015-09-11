terminal 1:
sudo mn -c
sudo mn --topo single,3 --mac --switch ovsk --controller remote


h1 python -m SimpleHTTPServer 80 &
h2 wget -O - h1



terminal2:
cd pox
 ./pox.py log.level --DEBUG forwarding.ipmute




log.debug("ip on : %s, dmau",packet.payload.protosrc)
protosrc


  msg = of.ofp_flow_mod()
  msg.priority = 42
  msg.match.dl_type = 0x800
  msg.match.nw_dst = IPAddr("10.0.0.5")
  #msg.match.tp_dst = 80
  msg.actions.append(of.ofp_action_output(port = 3))
  event.connection.send(msg)



  #event.connection.send( of.ofp_flow_mod(action=of.ofp_action_output(port=1), priority=42, match=of.ofp_match(dl_type=0x800,nw_proto=6, nw_dst="10.0.0.1",tp_dst=80)))
  #event.connection.send( of.ofp_flow_mod(action=of.ofp_action_output(port=2), priority=42, match=of.ofp_match(dl_type=0x800,nw_proto=6, nw_dst="10.0.0.2",tp_dst=80)))
  #event.connection.send( of.ofp_flow_mod(action=of.ofp_action_output(port=3), priority=42, match=of.ofp_match(dl_type=0x800,nw_proto=6, nw_dst="10.0.0.3",tp_dst=80)))
