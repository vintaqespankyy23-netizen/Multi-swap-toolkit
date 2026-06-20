from setuptools import setup, find_packages

setup(
    name="cryptoswap-toolkit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests[socks]",
        "stem",
        "ccxt",
        "web3",
        "python-dotenv",
        "click",
    ],
    entry_points={
        'console_scripts': [
            'cryptoswap=tor_swap.cli:main',
        ],
    },
    author="Your Name",
    description="Private crypto swap toolkit with Tor anonymity",
    python_requires=">=3.8",
)
