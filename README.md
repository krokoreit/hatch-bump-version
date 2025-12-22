# hatch-bump-version

[![PyPI - Version](https://img.shields.io/pypi/v/hatch-bump-version.svg)](https://pypi.org/project/hatch-bump-version)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hatch-bump-version.svg)](https://pypi.org/project/hatch-bump-version)


This package provides the bump version build hook for hatch.

It purpose is to check the project version number and to automatically increment it in case the current version has already been published. This avoids the annoying 'already published' message when trying to publish a project to PyPI.

Use the pre-index-publisher to track the version published and provide the information for this build hook.

Add "hatch-bump-version" to the build-system requirements in your project's pyproject.toml
```py
  [build-system]
  requires = ["hatchling", "hatch-bump-version"]
```
Also include a settings section for [tool.hatch.build.hooks.bump_version] (with 'bump_version' being the name of the plugin). No entries for the plugin are required, but the section must be included for the plugin to be activated.
```py
  [tool.hatch.build.hooks.bump_version]
  #nothing for this plugin 
```

The pluging will then run as a hook before the build process.


</br>

Notes for Development:  
For the time being uses 'git bump-version' to retrieve the version and bump patch if needed.


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


## Usage
When your project's pyproject.toml contains "hatch-bump-version" in the build-system requirements and a [tool.hatch.build.hooks.bump_version] section, the plugin is automatically started before the actual build process triggered by
```py
  hatch build
```
It will then display in the console either
```py
  [BumpVersionBuildHook] No version bump needed.
```
or
```py
  [BumpVersionBuildHook] Version already published → bumping version...
```
followed by the information given by the bump version script.


</br>

## License
MIT license  
Copyright &copy; 2025 by krokoreit
