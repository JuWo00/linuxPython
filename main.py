import subprocess

vpns = []

def takeCommand(command):
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            print("[+] == ")
            print(result.stdout)
            vpns.append(result.stdout)
            return result.stdout
            pass

        else:
            print("[-] == ")
            print(result.stderr)


    except Exception as e:
        print("[EXCEPTİON] == ", e)


while True:

    inputCommand = input("Command: ")
    if inputCommand == "EXİT":
        break

    if inputCommand == "PRİNT":
        for vpn in vpns:
            print("NEW VPN" + vpn)
    else:
        takeCommand(inputCommand)

