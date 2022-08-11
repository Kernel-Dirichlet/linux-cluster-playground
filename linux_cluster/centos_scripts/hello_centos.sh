
LINUX_VERSION=$(cat /etc/os-release | grep PRETTY_NAME | cut -c 13-)
LINUX_PRINT=$(sed -e 's/^"//' -e 's/"$//' <<<"$LINUX_VERSION")
echo "#============================================#"
echo "Welcome to ${LINUX_PRINT}!"
echo "#============================================#"


