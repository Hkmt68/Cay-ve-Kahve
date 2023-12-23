from colorama import Fore, Style

# Çay çizimi
cay_cizimi = f"""
{Fore.WHITE}    ( ( (   {Fore.RESET}
{Fore.WHITE}   ) ) )    {Fore.RESET}
{Fore.RED}  ........... {Fore.RESET}
{Fore.RED}   \       /  {Fore.RESET}
{Fore.RED}    )     (   {Fore.RESET}
{Fore.RED}   (       )  {Fore.RESET}
{Fore.RED}    '-----'   {Fore.RESET}
"""
bir_soz = f"{Fore.YELLOW}Benim sana verebileceğim çok bir şey yok aslında.\n{Fore.YELLOW}Çay var içersen, ben var seversen, yol var gidersen…\n\n{Fore.RED}Aşık Veysel{Fore.RESET}"

print(cay_cizimi)
print(bir_soz.center(25, '*'))