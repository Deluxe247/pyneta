Value INTERFACE (\S+)
Value LINE_STATUS ((up|down))
Value ADMIN_STATUS ((up|down))
Value MAC_ADDRESS (\S+)
Value MTU (\d+)
Value DUPLEX ((full|half)-duplex)
Value SPEED (\d+)

Start
  ^Ethernet${INTERFACE} is ${LINE_STATUS}$$
  ^admin state is ${ADMIN_STATUS} 
  ^.*address: ${MAC_ADDRESS}
  ^.*MTU ${MTU} bytes
  ^.*${DUPLEX}, ${SPEED} Mb/s -> Record
