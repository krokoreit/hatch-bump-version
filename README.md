# hatch-bump-version

[![PyPI - Version](https://img.shields.io/pypi/v/hatch-bump-version.svg)](https://pypi.org/project/hatch-bump-version)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hatch-bump-version.svg)](https://pypi.org/project/hatch-bump-version)


This package provides the PreIndebump version build hook for hatch.

It purpose is to check the project version and automatically increment it when the current version has already be published.
This avoids the annoying 'already published' message after having tried to publish a project to PyPI.

Use it by adding "hatch-bump-version" to the build-system requiremets:
```py
  [build-system]
  requires = ["hatchling", "hatch-bump-version"]
```

It will then run as a hook before the build process.

For the time being use 'git bump-version' to retrieve the version and bump patch if needed.


Using 'hatch version' ??
Consider for future versions, as 'hatch version' brings alreay the required functionality to bump or set to version string.
However, it requires an pyproject.toml entry of
```py
  [tool.hatch.version]
  path = "./src/spNewProj1Py/__about__.py"
```
and the file, e.g. '__about__.py' existing with a string variable of __version__ or VERSION defined
```py
  __version__ = "2.0.0"
```
Maybe possible to check and add if missing. Alternatively catch the exception when running 'hatch version' and inform the use to set them up manually.




Enjoy

&emsp;krokoreit  
&emsp;&emsp;&emsp;<img src="https://github.com/krokoreit/hatch-bump-version/blob/main/assets/krokoreit-01.svg?raw=true" width="140"/>


## Installation

```console
pip install hatch-bump-version
```


## Usage & API

### hatch_pre_index Class
Import module:
```py
  hatch publish -p pre_index
```


</br>

### API

#### Methods
* [aaa()](#aaa-method)  
* [bbb()](#bbb-method)  


#### aaa() Method
```py
  sss
```

<div style="text-align: right"><a href="#methods">&#8679; back up to list of methods</a></div>


</br>

## License
MIT license  
Copyright &copy; 2025 by krokoreit
