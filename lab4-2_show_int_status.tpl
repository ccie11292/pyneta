Value PORT (\S+)
Value STATUS (\S+)
Value VLAN (\S+)
Value DUPLEX (\S+)
Value SPEED (\S+)
Value TYPE (\S+)

Start
  ^Port.*Type\s*$$ -> ShIntStatus

ShIntStatus
  ^${PORT}\s+${STATUS}\s+${VLAN}\s+${DUPLEX}\s+${SPEED}\s+${TYPE}\s*$$ -> Record

EOF

#Port      Name  Status       Vlan  Duplex Speed Type 
#Gi0/1/0         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/1         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/2         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/3         notconnect   1     auto   auto  10/100/1000BaseTX
