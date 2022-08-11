# linux-cluster-playground
A place for users to learn and experiment with Linux distros

![Alt text](/linux_cluster/repo_logo.png?raw=true "Title")

# OVERVIEW

This repo provides users a "sandbox" to explore various Linux distros in any version supported by Docker. This is especially useful for 

1) WSL users who only have access to distros provided on the Windows store, but have Docker installed. 
2) Users who want to experiment with different Linux supported file systems like EXT3 and XFS with distros like Arch Linux before commiting to one on personal or production server(s). 
3) Users who want a central location to quickly setup and experiment with a new distro they haven't used before. 

## Upcoming Features

1) **Docker Swarm support** - This feature will spin up containers across different servers with Docker running. Inside the containers will be Linux VMs that have SSH access to other containers running in the swarm. **Expected completion: 9/1/2022**

2) **Shell script collection** - Directories for each distro will include shell scripts that users can run and experiment with. Here, users can learn about the different Linux shells. **Expected completion: ongoing effort**

3) **Improved VM versioning** - Currently, this repo supports an arbitrary number of VMs (limited only by hardware resources), but *one* version per distro. For example, users can run one, five, or twenty Alpine VMs, but they must all be the same version. **Expected completion: 9/15/2022** 

4) **Improved repository organization** - Depending on web traffic and general interest, future updates to this repo will be better organized under the "Projects" section. A guide for submitting PRs will also be provided. Oh, and more a comprehensive install / setup guide **Expected completion: ongoing effort**

5) **Enabling systemctl and/or service** - this is a current major limitation, as starting and configuring applications like Redis, postgres, and Docker (yes, you can run Docker inside a Docker container) is not currently supported. Once this is configured, it is possible to make more sophisticated DevOps sandboxes with Docker compose which can be experimented with before an architecture is chosen for production/deployment. 
    **Expected completion: 10/15/2022**
    
6) **Add all Docker supported Linux images** - this is an easy enough task, just slightly tedious. **Expected completion: 9/1/2022**

## How-to-run 

This repo assumes Python is installed (obviously 3+) and Docker. Code was written on a Windows 11 laptop and tested with Docker installed on WSL Ubuntu 20.04 LTS, but should work as long as Python and Docker work correctly on host machine (submit an issue if it doesn't). Setup here will assume you are in a Linux terminal. Docker volumes are mounted to each container, containing shell scripts appropriate for each distro. This structure may be reworked in future updates. 

There is a JSON-based configuration file, which allows users to switch which version of the Linux distro they want (make sure it matches a tag supported on Docker Hub EXACTLY) and the number of containers (which run a VM of that particular distro + version). Then, a Python file auto-generates a Docker compose YAML file which is used to spin up the containers. Default is one container for each of the supported distros (ten as of 8/10/2022)

And now, for a step-by-step guide
1) <code> git clone https://github.com/Kernel-Dirichlet/linux-cluster-playground.git </code> - clone this repository 

2) <code> cd linux-cluster-playground/linux_cluster </code> - navigate into the directory 

3) <code> vim default-config.json </code> OR
   <code> nano default-config.json </code> - open the default-config.json file. Here, you can simply change the number of containers you want for each distro       and the specific version. 

4) <code> python3 make_cluster.py </code> - runs the python script which auto-generates the Docker compose YAML file. 

5) <code> bash local-config.sh </code> - This spins up the cluster. Sit back and watch the magic. Bash script sets up and congifures cluster.

6) Now, you can just shell your way into any of the containers. Because we spin the containers up with Docker Compose, the containers always have a lovely
consistent naming format - <code> linux_cluster-*(distro)*-container-*(index)* </code>. Below is the full command for each of the distros

     I) **ALPINE** - <code> sudo docker exec -it linux_cluster-alpine-container-1 sh </code> 
     
     II) **ARCH LINUX** - <code> sudo docker exec -it linux_cluster-archlinux-container-1 bash </code> 
     
     III) **CENTOS** - <code> sudo docker exec -it linux_cluster-centos-container-1 bash </code> 
     
     IV) **CLEAR LINUX** - <code> sudo docker exec -it linux_cluster-clearlinux-container-1 bash </code>
     
     V) **DEBIAN** - <code> sudo docker exec -it linux_cluster-debian-container-1 bash </code> 
     
     VI)  **FEDORA** - <code> sudo docker exec -it linux_cluster-fedora-container-1 bash </code>
     
     VII) **ORACLE** - <code> sudo docker exec -it linux_cluster-oracle-container-1 bash </code>
     
     VIII) **ROCKY LINUX** - <code> sudo docker exec -it linux_cluster-rockylinux-container-1 bash </code> 
     
     IX) **SUSE LINUX** - <code> sudo docker exec -it linux_cluster-suse-container-1 bash </code> 
     
     X) **UBUNTU** - <code> sudo docker exec -it linux_cluster-ubuntu-container-1 bash </code> 
 
 
 ### Getting started 
 
 Now that we know how to actually get inside the containers, we can now run commands, and ultimately, shell scripts. Below are some commands to install
 basic packages and begin exploring each distro. There is an asterisk * next to some of the update/upgrade commands because there are nuances between 
 how different distros and package managers implement this. This will be documented in future updates to this repo. 

I) **ALPINE** - https://www.alpinelinux.org/ 
      
  - install bash: <code> apk add bash </code> - adds bash shell capabilities, since Alpine does not come with bash. Once installed, run 
  
        bash /shell_scripts/hello_alpine.sh 
        
   This will display a welcome message with the Alpine version defined in the JSON config file! 
        
  - upgrade: <code> apk upgrade </code>
  - update:  <code> apk update </code>
  - search packages: <code> apk search *package-name* </code>
  - installing package: <code> apk add *package-name* </code> 

  
II) **ARCH LINUX** - https://archlinux.org/ 

  - upgrade: <code> pacman -Syu </code> 
  - update: *N/A
  - search packages: *<code> pacman -Sy </code>
  - installing packages: <code> pacman -S *package-name* </code> 
  - run "hello linux" - <code> bash /shell_scripts/hello_arch_linux.sh </code> 

III) **CENTOS** - https://www.centos.org/
  - upgrade: *N/A
  - update: <code> yum update </code> 
  - search packages: <code> yum search *package-name* </code>
  - installing packages: <code> yum install *package-name* </code> 
  - run "hello linux" - <code> bash /shell_scripts/hello_centos.sh </code> 
  
IV) **CLEAR LINUX** - https://clearlinux.org/
  - upgrade: *there is a command for auto-updating - <code> swupd autoupdate </code>
  - update: <code> swupd update </code>
  - search packages: We need to first run <code> swupd bundle-add os-core-search </code>, then we run <code> swupd-search *package-name* </code>
  - installing packages: <code> swupd bundle-add *package-name* </code>
  - run "hello linux" - <code> bash /shell_scripts/hello_clear_linux.sh </code>
  
V) **DEBIAN** - https://www.debian.org/ 
  - upgrade: <code> apt upgrade </code>
  - update: <code> apt update </code>
  - search packages: <code> apt search *package-name* </code>
  - installing packages: <code> apt install *package-name* </code>
  - run "hello linux": <code> bash /shell_scripts/hello_debian.sh </code>
  
VI) **FEDORA** - https://getfedora.org/
  - upgrade: <code> dnf upgrade </code>
  - update: <code> dnf update </code>
  - search packages: <code> dnf search *package-name* </code>
  - installing packages: <code> dnf install *package-name* </code> 
  - run "hello linux": <code> bash /shell_scripts/hello_fedora.sh </code>

VII) **ORACLE** - https://www.oracle.com/linux/
  - upgrade: <code> dnf upgrade </code>
  - update: <code> dnf update </code>
  - search packages: <code> dnf search *package-name* </code>
  - installing packages: <code> dnf install *package-name* </code> 
  - run "hello linux": <code> bash /shell_scripts/hello_oracle.sh </code> 
  
VIII) **ROCKY LINUX** - https://rockylinux.org/
  - upgrade: <code> dnf upgrade </code>
  - update: <code> dnf update </code>
  - search packages: <code> dnf search *package-name* </code>
  - installing packages: <code> dnf install *package-name* </code> 
  - run "hello linux": <code> bash /shell_scripts/hello_rocky_linux.sh </code> 
  
IX) **SUSE LINUX** - https://www.suse.com/
  - upgrade: <code> zypper dist-upgrade </code> 
  - update: <code> zypper update </code> 
  - search packages: <code> zypper search *package-name* </code>
  - installing packages: <code> zypper install *package-name* </code>
  - run "hello linux": <code> bash /shell_scripts/hello_suse_linux.sh </code>
  
X) **UBUNTU** - https://ubuntu.com/
  - upgrade: <code> apt updrade </code>
  - update: <code> apt update </code>
  - search packages: <code> apt search *package-name* </code>
  - installing packages: <code> apt install *package-name* </code> 
  - run "hello linux": <code> bash /shell_scripts/hello_ubuntu.sh </code> 
  
  

  
  
    
