# AdaptiveRestoreInMLC

Abstract—For the sake of higher cell density while achieving near-zero standby power, recent research progress in Magnetic
Tunneling Junction (MTJ) devices has leveraged Multi-Level Cell (MLC) configurations of Spin-Transfer Torque Random Access
Memory (STT-RAM). However, in order to mitigate the write disturbance in an MLC strategy, data stored in the soft bit must be restored
back immediately after the hard bit switching is completed. Furthermore, as the result of MTJ feature size scaling, the soft bit can be
expected to become disturbed by the read sensing current, thus requiring an immediate restore operation to ensure the data reliability.
In this paper, we design and analyze a novel Adaptive Restore Scheme for Write Disturbance (ARS-WD) and Read Disturbance
(ARS-RD), respectively. ARS-WD alleviates restoration overhead by intentionally overwriting soft bit lines which are less likely to be
read. ARS-RD, on the other hand, aggregates the potential writes and restore the soft bit line at the time of its eviction from higher level
cache. Both of these two schemes are based on a lightweight forecasting approach for the future read behavior of the cache block. Our
experimental results show substantial reduction in soft bit line restore operations, delivering 17.9% decrease in overall energy
consumption and 9.4% increase in IPC, while incurring negligible capacity overhead. Moreover, ARS promotes advantages of MLC to
provide a preferable L2 design alternative in terms of energy, area and latency product compared to SLC STT-RAM alternatives.
