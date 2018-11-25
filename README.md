# Docker
## Comparison to VMs
A virtual machine sits on top of hardware and has its own "copy" of CPU, memory, storage, and network. Even if the VM is idling, these resources are bound.
This leads to under utilization of hardware.

Docker is a virtualization ontop of operating system, not the physical resources! Has its own PID, network stack and root file system.

More dynamic than VMs. If you have 4 containers and 3 are idle, the last one can utilize more resources.

## Comparison to conda or python environments

Conda envs isolate well too but Docker is more portable. Reproducability of environment leads to reproducability of output.