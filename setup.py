Version = "0.1.1"
Description = "A guide for using Heisler charts\n\
               and approximation for transient heat transfer."


def main():
    #from setuptools import setup, find_packages
    import setuptools

    with open("README.md", "r") as fh:
        long_description = fh.read()

    # with


    classifiers = [
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Visualization",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ]

    setup_parameteres = dict(
        name="Heisler",
        version=Version,
        description=Description,
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Reza Sadeghi",
        maintainer="Reza Sadeghi",
        author_email="lambertmech@gmail.com",
        classifiers=classifiers,
        keywords=["Heisler", "Heat transfer"],
        python_requires='>=3.6, <4',
        license="Apache-2.0",
        py_modules=["HeislerChartsGuide"],
        url="https://github.com/MRezaSadeghi/Heisler",
        install_requires=["numpy", "matplotlib"],
        packages=setuptools.find_packages(),
        include_package_data=True,
        package_data={'': ['data/*.png']}
        )
    print(setup_parameteres)
    setuptools.setup(**setup_parameteres)

if __name__=="__main__":
    main()
    #print(setuptools.find_packages())
