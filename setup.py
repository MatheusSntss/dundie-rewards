from setuptools import setup, find_packages

setup(
    name="dundie",
    version="0.1.0",
    description = "Rewards point system for Dundie Mifflin",
    author = "Matheus Santos",
    packages = find_packages(),
<<<<<<< HEAD
=======
    entry_points = {
        "console_scripts":[
            "dundie = dundie.__main__:main"
        ]
    }
>>>>>>> e2a5a7f (turned to installable binary)
)
