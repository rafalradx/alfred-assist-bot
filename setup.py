from setuptools import setup, find_namespace_packages

setup(
    name='Alfred',
    version='1.0.0',
    description='CLI Bot assistant. Package for adding data to'
                'address book, read/update/delete it, adding notes etc.',
    url='https://github.com/rafalradx/alfred-assist-bot',
    author='Gotham Devs', #czy podać imiona i nazwiska?
    #czy dodać adres e-mail?
    readme="README.md",
    license="MIT",
    packages=find_namespace_packages(),
    #install_requires=[], #tą sekcję możemy zostawić pustą lub ją usunąć - do decyzji
    entry_points={'console_scripts': ["Alfred=classes.run_alfred:main"]}
    ) 
