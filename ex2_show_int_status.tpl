#Value VAR_NAME (regex_pattern)
Value PORT (\S+)
Value STATUS (\S+)
Value VLAN (\S+)
Value DUPLEX (\S+)
Value SPEED (\S+)
Value TYPE (\S+)

 #$$ regex end of line
Start
  ^Port.*Type\s*$$ -> Port


#   {VAR_NAME}
Port
  ^${PORT}\s+${STATUS}\s+${VLAN}\s+${DUPLEX}\s+${SPEED}\s+${TYPE}\s+ -> Record

EOF

#Port      Name  Status       Vlan  Duplex Speed Type 
#Gi0/1/0         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/1         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/2         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/3         notconnect   1     auto   auto  10/100/1000BaseTX

#4,8s/^/#
