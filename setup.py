from setuptools import setup

DESCRIPTION = """
minio like python Local File System based Object Storage (FSOS)
""".strip()

DEPENDENCIES = [

]

TEST_DEPENDENCIES = [

]

VERSION = '0.0.1'
URL = "https://github.com/davinnovation/fsos"

setup(
    name="fsos",
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    
    packages=['fsos', 'fsos.utils'],
    
    install_requires=DEPENDENCIES,
    test_requires=TEST_DEPENDENCIES
)