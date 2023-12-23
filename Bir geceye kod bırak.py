from colorama import Fore, Style

# Kahve çizimi
kahve_cizimi = f"""
{Fore.YELLOW}  ( ({Fore.RESET}
{Fore.YELLOW}   ) ){Fore.RESET}
{Fore.RED}.........{Fore.RESET}
{Fore.RED}|       |]{Fore.RESET}
{Fore.RED}\\       /{Fore.RESET}
{Fore.RED} `-----'{Fore.RESET}
"""

# Yazı ve süsleme
bir_geceye_kod_birak = f"{Fore.CYAN}Bir kahve (☕) ile geceye (🌃) kod (👩‍💻👨‍💻) bırak{Fore.RESET}"

# Alt alta yazdırma
print(kahve_cizimi)
print(bir_geceye_kod_birak.center(25, '*'))