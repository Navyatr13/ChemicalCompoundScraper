from setuptools import setup, find_packages

setup(
    name="ChemicalCompoundScraper",
    version="1.0.0",
    description="Unified pipeline for scraping, semantic search, and NLP for chemical compounds",
             # Root directory for packages is src/
    install_requires=[
        "requests",
        "lxml",
        "biopython",
        "scispacy",
        "spacy",
        "sentence-transformers==3.3.1",
    ],
    python_requires=">=3.8",
)
