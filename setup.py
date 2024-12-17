from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='characterai',
    version='1.0.0',
    description='An unofficial API for Character AI for Python',
    keywords='ai wrapper api library',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/Neear7771/CharacterAI',
    author='kramcat',
    license='MIT',
    install_requires=['pydantic', 'curl_cffi', 'websockets'],
    packages=find_packages(include=['characterai*']),
    project_urls={
        'Community': 'https://discord.gg/ZHJe3tXQkf',
        'Source': 'https://github.com/kramcat/characterai',
        'Documentation': 'https://docs.kram.cat',
    },
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
    ],
)
