# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 18:19:47 2022

@author: ezw19
"""
import json 
import os 
import re 

def linux_cfg_parser(cfg_file='./default-config.json',compose_version=3.7):
    
    f = open(cfg_file)
    json_dict = json.load(f)
    compose_file = open('./user_config.yml','w')
    compose_file.write('version: "{}"\n'.format(compose_version))
    compose_file.write('services:\n')
    
    #=============== ALPINE =====================================#
    ""
    compose_file.write('  alpine-container:\n')
    compose_file.write('    image: alpine:{}\n'.format(json_dict['Alpine']['version']))
    compose_file.write('    tty: true\n')
    compose_file.write('    stdin_open: true\n')
    compose_file.write('    restart: on-failure\n')
    compose_file.write('    volumes:\n')
    compose_file.write('      - ./alpine_scripts:/shell_scripts/\n')
    compose_file.write('    networks:\n      - linux_swarm\n')
    compose_file.write('    deploy:\n      replicas: {}\n\n'.format(json_dict['Alpine']['containers']))
    
    #================ ARCHLINUX =================================#
    "Chuck Norris certified - Chuck Norris"
    "It put hair on my chest - "
    compose_file.write('  archlinux-container:\n')
    compose_file.write('    image: archlinux:{}\n'.format(json_dict['ArchLinux']['version']))
    compose_file.write('    tty: true\n')
    compose_file.write('    stdin_open: true\n')
    compose_file.write('    restart: on-failure\n')
    compose_file.write('    volumes:\n')
    compose_file.write('      - ./arch_linux_scripts:/shell_scripts/\n')
    compose_file.write('    networks:\n      - linux_swarm\n')
    compose_file.write('    deploy:\n      replicas: {}\n\n'.format(json_dict['ArchLinux']['containers']))
    
    #================ CENTOS ===================================#
    "Not bad, just my two CENTOS - author unknown"
    
    compose_file.write('  centos-container:\n')
    compose_file.write('    image: centos:{}\n'.format(json_dict['CentOS']['version']))
    compose_file.write('    tty: true\n')
    compose_file.write('    stdin_open: true\n')
    compose_file.write('    restart: on-failure\n')
    compose_file.write('    volumes:\n')
    compose_file.write('      - ./centos_scripts:/shell_scripts/\n')
    compose_file.write('    networks:\n      - linux_swarm\n')
    compose_file.write('    deploy:\n      replicas: {}\n\n'.format(json_dict['CentOS']['containers']))
    
    #=============== CLEARLINUX =================================#
    compose_file.write('  clearlinux-container:\n')
    compose_file.write('    image: clearlinux:{}\n'.format(json_dict['ClearLinux']['version']))
    compose_file.write('    tty: true\n')
    compose_file.write('    stdin_open: true\n')
    compose_file.write('    restart: on-failure\n')
    compose_file.write('    volumes:\n')
    compose_file.write('      - ./clear_linux_scripts:/shell_scripts/\n')
    compose_file.write('    networks:\n      - linux_swarm\n')
    compose_file.write('    deploy:\n      replicas: {}\n\n'.format(json_dict['ClearLinux']['containers']))
    
    #================ DEBIAN ====================================#
    "Guys, it just works - Abraham Lincoln"
    "Debian good - caveman"
    
    compose_file.write('  debian-container:\n')
    compose_file.write('    image: debian:{}\n'.format(json_dict['Debian']['version']))
    compose_file.write('    tty: true\n')
    compose_file.write('    stdin_open: true\n')
    compose_file.write('    restart: on-failure\n')
    compose_file.write('    volumes:\n')
    compose_file.write('      - ./debian_scripts:/shell_scripts/\n')
    compose_file.write('    networks:\n      - linux_swarm\n')
    compose_file.write('    deploy:\n      replicas: {}\n\n'.format(json_dict['Debian']['containers']))
    
    #================ Fedora ====================================#
    "Dude, I'm talking about Linux, not the hat!" 
    
    compose_file.write('  fedora-container:\n')
    compose_file.write('    image: fedora:{}\n'.format(json_dict['Fedora']['version']))
    compose_file.write('    tty: true\n')
    compose_file.write('    stdin_open: true\n')
    compose_file.write('    restart: on-failure\n')
    compose_file.write('    volumes:\n')
    compose_file.write('      - ./fedora_scripts:/shell_scripts/\n')
    compose_file.write('    networks:\n      - linux_swarm\n')
    compose_file.write('    deploy:\n      replicas: {}\n\n'.format(json_dict['Fedora']['containers']))
    
    #=============== ORACLE LINUX ===============================#
    "The Matrix was actually written in Oracle - Neo, you know, from the Matrix."
    
    compose_file.write('  oracle-container:\n')
    compose_file.write('    image: oraclelinux:{}\n'.format(json_dict['OracleLinux']['version'])) #might need to do type conversion
    compose_file.write('    tty: true\n')
    compose_file.write('    stdin_open: true\n')
    compose_file.write('    restart: on-failure\n')
    compose_file.write('    volumes:\n')
    compose_file.write('      - ./oracle_linux_scripts:/shell_scripts/\n')
    compose_file.write('    networks:\n      - linux_swarm\n')
    compose_file.write('    deploy:\n      replicas: {}\n\n'.format(json_dict['OracleLinux']['containers']))
    
    #=============== ROCKY LINUX =================================#
    '''
    "gross" - everyone 
    "friends don't let their friends use Rocky Linux" - everyone everywhere
    "Rocky Linux is just trying too hard to be edgy" - everyone 
    "No really, what is this? - everyone and their grandma"
    
    '''
    
    compose_file.write('  rockylinux-container:\n')
    compose_file.write('    image: rockylinux:{}\n'.format(json_dict['RockyLinux']['version']))
    compose_file.write('    tty: true\n')
    compose_file.write('    stdin_open: true\n')
    compose_file.write('    restart: on-failure\n')
    compose_file.write('    volumes:\n')
    compose_file.write('      - ./rocky_linux_scripts:/shell_scripts/\n')
    compose_file.write('    networks:\n      - linux_swarm\n')
    compose_file.write('    deploy:\n      replicas: {}\n\n'.format(json_dict['RockyLinux']['containers']))
    
    #================= SUSE LINUX =================================#
    "Idk man, this distro seems kinda SUSE to me. Might be the imposter - FluffyLlamas in some Among Us lobby circa 2020"
    
    
    compose_file.write('  suse-container:\n')
    compose_file.write('    image: opensuse/{}\n'.format(json_dict['SUSELinux']['version']))
    compose_file.write('    tty: true\n')
    compose_file.write('    stdin_open: true\n')
    compose_file.write('    restart: on-failure\n')
    compose_file.write('    volumes:\n')
    compose_file.write('      - ./suse_linux_scripts:/shell_scripts/\n')
    compose_file.write('    networks:\n      - linux_swarm\n')
    compose_file.write('    deploy:\n      replicas: {}\n\n'.format(json_dict['SUSELinux']['containers']))
    
    #================ UBUNTU ======================================#
    "Everyone's friend - Definitely everyone"
    "10/10 would recommend - some dude on Reddit"
    
    compose_file.write('  ubuntu-container:\n')
    compose_file.write('    image: ubuntu:{}\n'.format(json_dict['Ubuntu']['version']))
    compose_file.write('    tty: true\n')
    compose_file.write('    stdin_open: true\n')
    compose_file.write('    restart: on-failure\n')
    compose_file.write('    volumes:\n')
    compose_file.write('      - ./ubuntu_scripts:/shell_scripts/\n')
    compose_file.write('    networks:\n      - linux_swarm\n')
    compose_file.write('    deploy:\n      replicas: {}\n\n'.format(json_dict['Ubuntu']['containers']))
    
    compose_file.write('networks:\n  linux_swarm:\n    external: true\n')
    compose_file.close() 
    
if __name__ == '__main__':
    linux_cfg_parser()
    
