from setuptools import setup

setup(
    name='UniversalScraper',
    version='1.0',
    description='Universal Scraper Application',
    author='Tanmay Sarkar',
    author_email='tanmaysarkar959@gmail.com',
    packages=['Major_Project'],  # Replace 'Major_Project' with the actual folder name
    install_requires=[
        'pyttsx3',  # Add any additional dependencies here
        'tkinter',
        'newspaper',
        'pdfplumber',
        'pytesseract',
        'piimagesearch',
    ],
    entry_points={
        'console_scripts': [
            'universalscraper=Major_Project.main:main',  # Replace 'Major_Project' with the actual module and function
        ],
    },
)
