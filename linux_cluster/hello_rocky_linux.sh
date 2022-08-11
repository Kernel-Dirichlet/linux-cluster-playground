LINUX_DISTRO=$(cat /etc/os-release | grep PRETTY_NAME | cut -c 13-)
VERSION=$(sed -e 's/^"//' -e 's/"$//' <<<"$LINUX_DISTRO") 
echo "#============================================#"
echo "Welcome to ${VERSION}!"
echo "#============================================#"
