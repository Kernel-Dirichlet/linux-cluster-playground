LINUX_DISTRO=$(cat /etc/os-release | grep -o "ID=[a-z].*" | cut -c 4-)
VERSION_ID=$(cat /etc/os-release | grep VERSION_ID=.* | cut -c 12-)
ID=$(sed -e 's/^"//' -e 's/"$//' <<<"$VERSION_ID") 
echo "#============================================#"
echo "Welcome to ${LINUX_DISTRO^} Version: ${ID}!"
echo "#============================================#"
